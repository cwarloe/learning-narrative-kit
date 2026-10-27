#!/usr/bin/env python3
"""Apply final Aaron Sorkin storytelling refinements and technical SME fixes.
1. Episode 12: Ensure workbench alignment with expanded narrative.
2. Episode 04: Fix negative cache RFC 2308 SOA MINIMUM TTL, Lena Chen references, and varied ending.
3. Episode 05: Fix TCP teardown terminology, cut Ethan answer-key lecture, and vary ending.
4. Episode 07: Fix Cisco SSH privilege 15 / enable bypass, and vary ending.
5. Episode 11: Clarify deauthentication vs disassociation frames.
Mirrors all changes between docs/portland-desk/ and docs/portland-desk/.
"""

from pathlib import Path
import shutil

ROOT = Path(r"C:\Users\charl\learning-narrative-kit")
PORTLAND = ROOT / "portland-desk"
DOCS = ROOT / "docs" / "portland-desk"

def update_ep12_workbench():
    for base in [PORTLAND, DOCS]:
        w_file = base / "workbench" / "12-when-the-ticket-escalates.md"
        text = w_file.read_text(encoding="utf-8")
        
        # Disambiguate remaining Ken Vance on TODD-SALES-14 to Todd Miller
        text = text.replace(
            "- Hostname: TODD-SALES-14 | IP: 192.168.10.45 | User: Ken Vance (Warehouse Logistics)",
            "- Hostname: TODD-SALES-14 | IP: 192.168.10.45 | User: Todd Miller (Inside Sales Lead)"
        )
        text = text.replace(
            "- UPN: kvance@harrowmere.com (Warehouse Lead — Domain User)",
            "- UPN: tmiller@harrowmere.com (Inside Sales Lead — Domain User)"
        )
        # In Epilogue, Todd Miller's USB instead of Ken
        text = text.replace(
            '"And you didn\'t let Ken plug his stick back in."',
            '"And you didn\'t let Todd plug his stick back in."'
        )
        w_file.write_text(text, encoding="utf-8")
    print("Updated Episode 12 workbench alignment.")

def update_ep04():
    for base in [PORTLAND, DOCS]:
        n_file = base / "narrative" / "04-the-name-is-not-the-number.md"
        text = n_file.read_text(encoding="utf-8")
        
        # Lena Chen fix
        text = text.replace(
            '"Look at the interface binding order and gateway metrics," Maya observed.',
            '"Look at the interface binding order and gateway metrics," Lena observed.'
        )
        
        # RFC 2308 negative cache fix
        old_cache = '"To make matters worse, look at the negative response caching," I added. I checked the record properties. "The local resolver caches those failed lookups according to the zone [[dns_ttl|DNS TTL]]. That means even if the employee restarts their browser or reconnects the tunnel, the operating system keeps feeding them the cached failure for the next fifteen minutes."'
        new_cache = '"To make matters worse, look at the negative response caching," Lena added, pulling up the resolver cache. "Under RFC 2308, Windows caches that NXDOMAIN using the negative TTL defined in the upstream SOA record. So even if the employee restarts their browser or reconnects the tunnel, the operating system keeps serving the failure until the negative cache expires or you flush it."'
        text = text.replace(old_cache, new_cache)
        
        # Varied ending (break 'Call your shot' metronome)
        old_ending = """"You have eighty-two tunnels open, eighteen tickets blinking amber, and seventy remote workers locked out of payroll by their own home routers," Jules said quietly. "Jared is ready to call the ISP, and our users are rebooting cable modems for nothing. How do you re-architect the client resolution priority, eliminate the negative cache trap, and prove the fix across these remote endpoints without dropping their live sessions? Call your shot, Ethan."

I looked at the terminal output and the dual adapter configuration. The tunnel was wide open, but the packets were flying blind. I needed to isolate the DNS leak, calculate the corrected adapter metrics, and draft the infrastructure escalation before the morning payroll deadline expired."""

        new_ending = """Jules picked up her phone to intercept another incoming call from finance. "We have eighty-two tunnels open and seventy remote workers locked out of payroll while Jared is ready to yell at Comcast. The XML profile fix has to push cleanly, the adapter metrics need to prioritize the tunnel, and that negative cache trap has to clear without rebooting eighty laptops in the middle of their shift."

She looked back over her monitor. "You have fifteen minutes before accounting calls the Director, Ethan. Fix the plumbing."

I looked at the terminal output and the dual adapter configuration. The tunnel was wide open, but the packets were flying blind. I needed to isolate the DNS leak, calculate the corrected adapter metrics, and draft the infrastructure escalation before the morning payroll deadline expired."""

        assert old_ending in text, "Old ending not found in Ep 04"
        text = text.replace(old_ending, new_ending)
        n_file.write_text(text, encoding="utf-8")
    print("Updated Episode 04 (RFC 2308 cache, Lena Chen, varied ending).")

def update_ep05():
    for base in [PORTLAND, DOCS]:
        n_file = base / "narrative" / "05-the-wire-has-two-ends.md"
        text = n_file.read_text(encoding="utf-8")
        
        # Prompt teardown fix
        text = text.replace(
            "Flowchart lines illustrate TCP four-way handshake connection termination from FIN-WAIT to TIME-WAIT to CLOSED.",
            "Flowchart lines illustrate TCP four-way FIN connection termination sequence from FIN-WAIT to TIME-WAIT to CLOSED."
        )
        
        # Cut Ethan's answer-key lecture & vary ending
        old_lecture_block = """"Your script opened thousands of rapid-fire transport sessions," I realized, sketching the lifecycle on my pad. "When it called close, the client stack initiated an active close. Under RFC 793, the client must park each closed socket in `TIME_WAIT` for two maximum segment lifetimes—one hundred and twenty seconds in Windows. In ten minutes of rapid retries, you burned through all sixteen thousand ephemeral ports in the dynamic range."

Jules wheeled her chair closer, looking from the fifteen thousand frozen sockets on Jared's screen to the blinking backup SLA alert on the dispatch board.

"You have four hundred switches waiting on configuration backups, and our disaster recovery SLA expired two hours ago," Jules said, her voice quiet and direct. "The server is healthy, but Jared's workstation has consumed every dynamic port in its outbound pool. How do you triage this socket exhaustion, reconfigure the operating system TCP recycling timers, refactor the client transport architecture, and prove the fix without losing a single device backup? Call your shot, Ethan."

I looked at the mountain of frozen TIME_WAIT sockets. The wire had two ends, and right now, our own management station was starving itself to death. I needed to isolate the dynamic port depletion, calculate the socket reuse rates, and implement connection pooling before the next scheduled archive sweep failed."""

        new_lecture_block = """"Every socket is parked in `TIME_WAIT`," I said, pointing at the terminal columns. "Thousands of them, all outbound from your desktop to port 8443, and the process ID is already zero."

Jared leaned in, squinting at the numbers as the color drained from his face. "The active close... The loop doesn't pool connections. Every retry spins up a new client, fires a packet, and slams the door shut."

"And Windows parks each closed socket in `TIME_WAIT` for two minutes," Jules said, tapping her pen against Jared's monitor. "You burned through all sixteen thousand dynamic ephemeral ports on your own box in ten minutes of rapid retries."

Jared slumped into his chair, rubbing his temples. "The disaster recovery audit is at noon. Every switch in the district is waiting."

"Then stop kicking the trash can," Jules said. "Ethan, take his terminal, calculate the TCP recycling timer, and get connection pooling in place before we lose another hour of archives."

I looked at the mountain of frozen TIME_WAIT sockets. The wire had two ends, and right now, our own management station was starving itself to death. I needed to isolate the dynamic port depletion, calculate the socket reuse rates, and implement connection pooling before the next scheduled archive sweep failed."""

        assert old_lecture_block in text, "Old lecture block not found in Ep 05"
        text = text.replace(old_lecture_block, new_lecture_block)
        n_file.write_text(text, encoding="utf-8")
    print("Updated Episode 05 (teardown terminology, dialogue polish, varied ending).")

def update_ep07():
    for base in [PORTLAND, DOCS]:
        n_file = base / "narrative" / "07-the-port-that-is-open.md"
        text = n_file.read_text(encoding="utf-8")
        
        # Cisco SSH privilege 15 fix
        text = text.replace(
            '"Configure [[key_auth|key auth]] while you\'re in there," I added. "Then you never have to type the enable password into a script again."',
            '"Configure [[key_auth|key auth]] and a privilege-fifteen account while you\'re in there," I added. "Then the script won\'t need an enable secret or a cleartext password."'
        )
        
        # Vary ending (break 'Call your shot')
        old_ep07_end = """"You have six different teams asking for convenience shortcuts, and automated port scanners probing our perimeter from the outside right now," Jules said, crossing her arms. "How do you lock down the perimeter, map every insecure legacy protocol to its hardened enterprise replacement, configure the jump host access rules, and draft the Tier 1 Security Escalation before the change window closes? Call your shot, Ethan."

I looked at the stack of port index cards on my desk. Memorizing port numbers was easy; the hard part was standing between busy people and bad habits. I needed to build the protocol defense matrix, lock down the open sockets, and prove the secure paths before someone punched a hole in our firewall."""

        new_ep07_end = """Jules pointed to the queue monitor above our heads. A facilities tech was asking for unauthenticated TFTP across the user VLAN, legal could not bind to LDAP across the guest SSID, and network monitoring was asking to poll edge switches using cleartext SNMP with a community string of `public`.

"Six tickets, six shortcuts," Jules said, her voice dropping into operational focus. "Sam wants RDP to the open street, and five other teams want to send credentials in cleartext. Map every legacy port to its encrypted replacement, configure the jump host rule, and submit the firewall change before someone punches an uninsurable hole in our edge."

I looked at the stack of port index cards on my desk. Memorizing port numbers was easy; the hard part was standing between busy people and bad habits. I needed to build the protocol defense matrix, lock down the open sockets, and prove the secure paths before someone punched a hole in our firewall."""

        assert old_ep07_end in text, "Old Ep 07 ending not found"
        text = text.replace(old_ep07_end, new_ep07_end)
        n_file.write_text(text, encoding="utf-8")
    print("Updated Episode 07 (privilege 15 SSH & varied ending).")

def update_ep11():
    for base in [PORTLAND, DOCS]:
        n_file = base / "narrative" / "11-the-air-is-shared.md"
        text = n_file.read_text(encoding="utf-8")
        
        # Deauthentication vs disassociation nuance
        text = text.replace(
            "bursts of [[disassociation|disassociation / deauthentication]] frames aimed at lobby clients.",
            "bursts of spoofed 802.11 [[deauthentication|deauthentication frames]] aimed at lobby clients, forcibly severing their management associations."
        )
        n_file.write_text(text, encoding="utf-8")
    print("Updated Episode 11 (802.11 deauthentication precision).")

def mirror_all():
    for sub in ["narrative", "workbench"]:
        for f in (PORTLAND / sub).glob("*.md"):
            shutil.copy2(f, DOCS / sub / f.name)
    print("Mirrored all narrative and workbench files to docs/portland-desk/.")

if __name__ == "__main__":
    update_ep12_workbench()
    update_ep04()
    update_ep05()
    update_ep07()
    update_ep11()
    mirror_all()
