#!/usr/bin/env python3
"""Build docs/portland-desk/artifacts/jared-telnet-capture.pcap for Episode 7, Drill 1.

The drill prints frames 101-137 of a capture taken from a span port on the
management VLAN. This script writes that capture as a real .pcap so learners can
open it in Wireshark: 100 frames of ordinary management traffic (frames 1-100),
then Jared's Telnet session exactly as the drill table lists it (frames 101-137).

Needs scapy (not in requirements.txt: `pip install scapy`). The output is
deterministic, so rerunning it gives the same file.

    python3 tools/generate_ep07_telnet_capture.py [out.pcap]
"""
import datetime as dt
import random
import sys

from scapy.all import ARP, DNS, DNSQR, DNSRR, ICMP, IP, NTP, TCP, UDP, Ether, Raw, wrpcap

OUT = sys.argv[1] if len(sys.argv) > 1 else "docs/portland-desk/artifacts/jared-telnet-capture.pcap"

CLIENT, SWITCH = "192.168.10.45", "10.0.4.15"          # from the drill
RESOLVER, NTPSRV, LOGHOST, PINGER, GATEWAY = ("192.168.10.2", "192.168.10.3",
                                              "192.168.10.5", "192.168.10.50", "192.168.10.1")
T0 = dt.datetime(2026, 10, 13, 8, 44, 12, tzinfo=dt.timezone.utc)   # frame 101, per the drill
rng = random.Random(7)


def mac(ip):
    return "02:00:" + ":".join(f"{int(o):02x}" for o in ip.split("."))


def eth(src, dst):
    return Ether(src=mac(src), dst=mac(dst))


def stamp(pkt, when):
    pkt.time = when.timestamp()
    return pkt


# ---- frames 1-100: ordinary traffic before the Telnet session -------------------
groups = []   # each group: (start offset seconds before T0, [(delta, packet), ...])
for _ in range(10):   # ARP request/reply, 20 frames
    a, b = rng.sample([CLIENT, PINGER, GATEWAY, LOGHOST, RESOLVER], 2)
    groups.append((rng.uniform(1, 40), [
        (0, Ether(src=mac(a), dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, psrc=a, pdst=b, hwsrc=mac(a))),
        (0.0004, eth(b, a) / ARP(op=2, psrc=b, pdst=a, hwsrc=mac(b), hwdst=mac(a)))]))
names = ["files.pdx-ops.example.", "ntp.pdx-ops.example.", "syslog.pdx-ops.example.",
         "updates.pdx-ops.example.", "mail.pdx-ops.example."]
for i in range(10):   # DNS query/response, 20 frames
    n, sport, txid = names[i % 5], 40000 + i, 0x1200 + i
    groups.append((rng.uniform(1, 40), [
        (0, eth(CLIENT, RESOLVER) / IP(src=CLIENT, dst=RESOLVER) / UDP(sport=sport, dport=53) /
         DNS(id=txid, rd=1, qd=DNSQR(qname=n))),
        (0.002, eth(RESOLVER, CLIENT) / IP(src=RESOLVER, dst=CLIENT) / UDP(sport=53, dport=sport) /
         DNS(id=txid, qr=1, aa=1, rd=1, ra=1, qd=DNSQR(qname=n),
             an=DNSRR(rrname=n, ttl=300, rdata=f"192.168.10.{10 + i % 5}")))]))
NTP_EPOCH_OFFSET = 2208988800        # seconds between 1900 (NTP) and 1970 (Unix)
for i in range(5):    # NTP client/server, 10 frames
    when = rng.uniform(1, 40)
    ts = (T0 - dt.timedelta(seconds=when)).timestamp() + NTP_EPOCH_OFFSET   # fixed, so reruns match
    groups.append((when, [
        (0, eth(CLIENT, NTPSRV) / IP(src=CLIENT, dst=NTPSRV) / UDP(sport=123, dport=123) /
         NTP(mode=3, version=4, ref=0, orig=0, recv=0, sent=ts)),
        (0.001, eth(NTPSRV, CLIENT) / IP(src=NTPSRV, dst=CLIENT) / UDP(sport=123, dport=123) /
         NTP(mode=4, version=4, stratum=2, ref=ts, orig=ts, recv=ts + 0.0005, sent=ts + 0.0006))]))
for i in range(10):   # ICMP echo request/reply to the switch, 20 frames
    groups.append((rng.uniform(1, 40), [
        (0, eth(PINGER, SWITCH) / IP(src=PINGER, dst=SWITCH) / ICMP(type=8, id=77, seq=i) / Raw(b"abcdefgh" * 4)),
        (0.0006, eth(SWITCH, PINGER) / IP(src=SWITCH, dst=PINGER) / ICMP(type=0, id=77, seq=i) / Raw(b"abcdefgh" * 4))]))
logs = ["port Gi1/0/12 link up", "port Gi1/0/12 link down", "fan 1 speed normal", "temperature normal",
        "NTP synchronized to 192.168.10.3", "port Gi1/0/7 link up"]
for i in range(30):   # syslog from the switch to the log host, 30 frames
    off = rng.uniform(1, 40)
    stamp_txt = (T0 - dt.timedelta(seconds=off)).strftime("Oct 13 %H:%M:%S")   # matches arrival time
    groups.append((off, [
        (0, eth(SWITCH, LOGHOST) / IP(src=SWITCH, dst=LOGHOST) / UDP(sport=514, dport=514) /
         Raw(f"<189>{stamp_txt} Switch-Closet-C: {logs[i % len(logs)]}\n".encode()))]))

filler = []
for off, pkts in groups:
    start = T0 - dt.timedelta(seconds=off)
    for delta, p in pkts:
        filler.append(stamp(p, start + dt.timedelta(seconds=delta)))
filler.sort(key=lambda p: p.time)
assert len(filler) == 100, len(filler)

# ---- frames 101-137: Jared's Telnet session, exactly as the drill lists it ------
cport, tport = 51240, 23
seq = {"c": 1000, "s": 5000}      # initial sequence numbers (Wireshark shows them relative)
ack = {"c": 0, "s": 0}
session = []


def tcp(frm, flags, data=b"", when=0.0, win=64240):
    src, dst = (CLIENT, SWITCH) if frm == "c" else (SWITCH, CLIENT)
    sp, dp = (cport, tport) if frm == "c" else (tport, cport)
    other = "s" if frm == "c" else "c"
    p = eth(src, dst) / IP(src=src, dst=dst) / TCP(sport=sp, dport=dp, flags=flags, seq=seq[frm],
                                                   ack=ack[frm], window=win) / (Raw(data) if data else b"")
    seq[frm] += len(data) + (1 if "S" in flags else 0)
    ack[other] = seq[frm]
    session.append(stamp(p, T0 + dt.timedelta(seconds=when)))


tcp("c", "S", when=0.00)                                       # 101
tcp("s", "SA", when=0.01)                                      # 102
tcp("c", "A", when=0.02)                                       # 103
tcp("s", "PA", b"User Access Verification\r\n", when=1.0)      # 104
tcp("s", "PA", b"Password: ", when=1.1)                        # 105
for i, ch in enumerate("C1sco_Sw!tch_2026"):                   # 106-122, one key per frame
    tcp("c", "PA", ch.encode(), when=2.0 + i * 0.03)
tcp("c", "PA", b"\r\n", when=2.6)                              # 123
tcp("s", "PA", b"Switch-Closet-C> enable", when=3.0)           # 124
tcp("s", "PA", b"Password: ", when=3.1)                        # 125
for i, ch in enumerate("Enable!247"):                          # 126-135
    tcp("c", "PA", ch.encode(), when=4.0 + i * 0.03)
tcp("c", "PA", b"\r\n", when=4.5)                              # 136
tcp("s", "PA", b"Switch-Closet-C#", when=5.0)                  # 137
assert len(session) == 37, len(session)

wrpcap(OUT, filler + session)
print(f"wrote {OUT}: {len(filler)} + {len(session)} = {len(filler) + len(session)} frames")
