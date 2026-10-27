#!/usr/bin/env python3
"""Check that Episode 7, Drill 1 and its packet capture still agree.

The drill prints frames 101-137 of a capture as a text table and gives the two
passwords in its answer key. docs/portland-desk/artifacts/jared-telnet-capture.pcap is
the real file behind that table. This script fails if any of these drift apart:

  1. the capture's Telnet session (TCP port 23) is not exactly frames 101-137
  2. a frame's source, destination, clock time or payload differs from the table
  3. the keystrokes in the capture do not spell the passwords in the answer key

No third-party packages and no tshark: it reads the classic .pcap format directly.

    python3 tools/check_ep07_capture.py [repo_root]
"""
import datetime as dt
import pathlib
import re
import struct
import sys

ROOT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parent.parent
PCAP = "docs/portland-desk/artifacts/jared-telnet-capture.pcap"
WORKBENCH = "docs/portland-desk/workbench/07-the-port-that-is-open.md"


def read_pcap(path):
    """Yield (epoch_seconds, frame_bytes) from a classic little-endian .pcap."""
    data = path.read_bytes()
    magic = data[:4]
    if magic == b"\xd4\xc3\xb2\xa1":
        scale = 1e-6
    elif magic == b"\x4d\x3c\xb2\xa1":
        scale = 1e-9
    else:
        raise ValueError(f"{path}: not a little-endian classic pcap (magic {magic.hex()})")
    pos = 24
    while pos + 16 <= len(data):
        sec, frac, caplen, _ = struct.unpack_from("<IIII", data, pos)
        pos += 16
        yield sec + frac * scale, data[pos:pos + caplen]
        pos += caplen


def tcp_port23(frame):
    """Return (src_ip, dst_ip, payload) if the frame is IPv4/TCP touching port 23, else None."""
    if len(frame) < 34 or frame[12:14] != b"\x08\x00":
        return None
    ihl = (frame[14] & 0x0F) * 4
    if frame[23] != 6:
        return None
    t = 14 + ihl
    sport, dport = struct.unpack_from(">HH", frame, t)
    if 23 not in (sport, dport):
        return None
    toff = (frame[t + 12] >> 4) * 4
    total = struct.unpack_from(">H", frame, 16)[0]
    payload = frame[t + toff:14 + total]
    ip = lambda o: ".".join(str(b) for b in frame[o:o + 4])
    return ip(26), ip(30), payload


def drill_table(md):
    block = md[md.index("caption: Wireshark / tcpdump Stream Reassembly"):]
    block = block[:block.index("```")]
    rows = {}
    for line in block.splitlines():
        m = re.match(r"^(\d+)\s+(\d\d:\d\d:\d\d)\s+(\S+)\s+(\S+)\s+(TCP|TELNET)\s+(.*)$", line)
        if m:
            rows[int(m[1])] = {"time": m[2], "src": m[3], "dst": m[4], "proto": m[5], "info": m[6]}
    return rows


def main():
    problems = []
    md = (ROOT / WORKBENCH).read_text(encoding="utf-8")
    table = drill_table(md)
    frames = list(read_pcap(ROOT / PCAP))

    # 1. the Telnet session is exactly the frames the drill lists
    session = {n: tcp_port23(f) for n, (_, f) in enumerate(frames, 1) if tcp_port23(f)}
    if sorted(session) != sorted(table):
        problems.append(f"port-23 frames are {min(session, default=None)}-{max(session, default=None)} "
                        f"({len(session)} frames) but the drill table lists {min(table)}-{max(table)} ({len(table)} rows)")

    # 2. every row agrees: addresses, clock time (UTC), payload
    for n, row in sorted(table.items()):
        if n not in session:
            continue
        src, dst, payload = session[n]
        clock = dt.datetime.fromtimestamp(frames[n - 1][0], dt.timezone.utc).strftime("%H:%M:%S")
        if (src, dst, clock) != (row["src"], row["dst"], row["time"]):
            problems.append(f"frame {n}: capture has {src} -> {dst} at {clock}; drill says "
                            f"{row['src']} -> {row['dst']} at {row['time']}")
        if row["proto"] == "TELNET":
            text = row["info"][6:] if row["info"].startswith("Data: ") else row["info"]
            want = text.replace("\\r\\n", "\r\n").encode()
            got = payload
            same = got == want if row["info"].startswith("Data: ") else got.rstrip() == want.rstrip()
            if not same:
                problems.append(f"frame {n}: payload {got!r} does not match drill text {row['info']!r}")
        elif payload:
            problems.append(f"frame {n}: drill says a bare TCP frame but the capture has {len(payload)} payload bytes")

    # 3. the answer key's passwords are what the keystrokes actually spell
    typed = "".join(chr(session[n][2][0]) for n in sorted(session)
                    if session[n][0] == "192.168.10.45" and len(session[n][2]) == 1)
    for label, key in (("Login Password", "login"), ("Enable Password", "enable")):
        m = re.search(rf"\*\*{label}:\*\*\s*`([^`]+)`", md)
        if not m:
            problems.append(f"answer key has no '{label}' line")
        elif m[1] not in typed:
            problems.append(f"answer key {key} password {m[1]!r} is not spelled by the capture's keystrokes")

    # 4. the published mirror is identical
    if problems:
        print("Episode 7 capture check FAILED:")
        for p in problems:
            print("  -", p)
        return 1
    print(f"Episode 7 capture OK: {len(frames)} frames; Telnet frames {min(session)}-{max(session)} "
          f"match the drill table ({len(table)} rows); answer-key passwords match the keystrokes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
