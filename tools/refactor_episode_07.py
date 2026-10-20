#!/usr/bin/env python3
"""Refactor Episode 07 into the Interleaved Cliffhanger Handoff Model."""

from pathlib import Path

KIT_ROOT = Path(__file__).resolve().parent.parent

NARRATIVE_PATH = KIT_ROOT / "portland-desk" / "narrative" / "07-the-port-that-is-open.md"
DOCS_NARRATIVE_PATH = KIT_ROOT / "docs" / "portland-desk" / "narrative" / "07-the-port-that-is-open.md"

WORKBENCH_PATH = KIT_ROOT / "portland-desk" / "workbench" / "07-the-port-that-is-open.md"
DOCS_WORKBENCH_PATH = KIT_ROOT / "docs" / "portland-desk" / "workbench" / "07-the-port-that-is-open.md"

NEW_NARRATIVE_END = """## The hotel room and the open perimeter

While that worked its way through, a contractor named Sam wanted Remote Desktop from a hotel in Seattle to a finance workstation. He was polite about it, and late on a deliverable.

"I only need the desktop for an hour," Sam said over the phone line. "Hotel Wi-Fi, my laptop, their machine. It's TCP 3389, right? My last client just whitelisted my hotel IP on the edge firewall and called it done."

I caught myself reaching for the firewall change template, starting to draft a temporary thirty-day port forward.

Jules reached over and tapped the edge of my monitor with her pen. "Read that request back to yourself as a decision, Ethan."

"Allow inbound RDP from an unauthenticated public IP to finance-WS-14 on port 3389," I said, feeling the weight of the words.

"Right. Now read the second half of it out loud," Jules said, her voice quiet and direct. "Our cyber insurance renewal questionnaire asks whether port 3389 faces the public internet. That is a policy termination conversation, not a movie plot. Automated ransomware scripts scan that port every second of every day. And Sam is not the only ticket on the board right now."

She pointed to the queue monitor above our heads. A facilities tech was asking for unauthenticated TFTP across the user VLAN, legal could not bind to LDAP across the guest SSID, and network monitoring was asking to poll edge switches using cleartext SNMP with a community string of `public`.

"You have six different teams asking for convenience shortcuts, and automated port scanners probing our perimeter from the outside right now," Jules said, crossing her arms. "How do you lock down the perimeter, map every insecure legacy protocol to its hardened enterprise replacement, configure the jump host access rules, and draft the Tier 1 Security Escalation before the change window closes? Call your shot, Ethan."

I looked at the stack of port index cards on my desk. Memorizing port numbers was easy; the hard part was standing between busy people and bad habits. I needed to build the protocol defense matrix, lock down the open sockets, and prove the secure paths before someone punched a hole in our firewall.

## The Handoff Gate

```bridge-card
title: Portland Desk Lab: Protocol Triage, Port Hardening, & Perimeter Defense
target: workbench/07-the-port-that-is-open.md
domain: CompTIA Security+ SY0-701 • Domain 1.4 & 2.5
badge: The Hands-On Lab
---
Take over Ethan's workstation. Triage cleartext Telnet, FTP, and HTTP traffic in packet capture drills, map insecure legacy services to encrypted replacements (SSH, SFTP, FTPS, LDAPS, SNMPv3), design the jump host firewall rule, and draft the Tier 1 Security Escalation Dossier.
```
"""

WORKBENCH_EPILOGUE = """

---

## 6. Shift Resolution Epilogue

```callout-panel
title: "FIGURE 7.2: HARDENED PROTOCOL ARCHITECTURE"
badge: "Shift Epilogue"
caption: "Operations center: At 05:40 PM, the rain clears over the Willamette River. On Ethan's desk, index cards sit neatly paired in secure couples as external port 3389 and 445 scanners hit zero open sockets."
prompt: "Clean graphic novel cutaway panel of an IT support technician desk at twilight. Rain streaks down the window behind the desk, showing twilight city lights over an industrial river. On the laminate desk, index cards are neatly stacked in pairs beside an empty coffee mug. A dual-monitor display shows green firewall access rule tables. Ligne Claire style, sharp technical ink linework, no text, no words. 16:9 ratio."
```

With the security matrix completed, I called Sam back in Seattle. "We will get you onto the corporate VPN first, and from there you will remote into a dedicated jump host. We do not open raw port 3389 to the public internet, not even for an hour, for the same reason we do not expose SMB on port 445 off the outside of the building."

Sam groaned over the line, then gave in. "I already have the VPN profile from the last gig. A jump box is fine if somebody sends me the hostname. It is honestly nicer than hoping the hotel Wi-Fi is friendly."

The firewall rule we submitted was narrow on purpose: source the VPN client address pool, destination the hardened jump host, port 3389, TCP, allow—with all direct internet access to internal workstations blocked. Jules initialed the ticket on her way past.

Across the rest of the queue, the legacy cleartext protocols fell into line. We moved the legal directory tool from LDAP on 389 to LDAPS on 636, synchronized Lena's skewed clock with internal NTP on UDP 123 to restore Kerberos ticket validation, and rejected unauthenticated SNMP `public` polling in favor of SNMPv3 with SHA authentication and AES encryption. When facilities tech Owen needed printer firmware, we restricted TFTP to a transient staging segment and closed the port behind him.

By 5:40 PM the queue was down to noise. The index cards were still out on my desk, and I had been pairing them off all afternoon without meaning to: Telnet next to SSH, HTTP next to HTTPS, FTP next to SFTP and FTPS, POP and IMAP next to their TLS versions, LDAP next to LDAPS, SNMP next to SNMPv3, syslog next to 6514. None of the port numbers had changed.

Jules stopped at my cube on her way out, raincoat on, bike lights already clipped to her pack strap.

"How many ports did you memorize today, Ethan?"

"None," I answered with a tired grin. "I collected some war stories and made a few swaps."

"Keep the cards if they help you get started," Jules said, giving my desk partition a nod of approval. "Throw them out when the person on the phone already knows the number, and what they actually need from you is the other half."

That was the one I wrote down in my technical notebook. I locked the drawer and went out into the rain to catch the MAX.
"""

def update_narrative():
    raw = NARRATIVE_PATH.read_text(encoding="utf-8")
    part1 = raw.split("While that worked its way through, a contractor named Sam")[0].strip()
    full_new = part1 + "\n\n" + NEW_NARRATIVE_END
    NARRATIVE_PATH.write_text(full_new, encoding="utf-8")
    DOCS_NARRATIVE_PATH.write_text(full_new, encoding="utf-8")
    print(f"Updated narrative in {NARRATIVE_PATH} and {DOCS_NARRATIVE_PATH}")

def update_workbench():
    wb = WORKBENCH_PATH.read_text(encoding="utf-8")
    if "## 6. Shift Resolution Epilogue" not in wb:
        wb = wb.strip() + "\n" + WORKBENCH_EPILOGUE
        WORKBENCH_PATH.write_text(wb, encoding="utf-8")
        DOCS_WORKBENCH_PATH.write_text(wb, encoding="utf-8")
        print(f"Appended Epilogue to {WORKBENCH_PATH} and {DOCS_WORKBENCH_PATH}")

if __name__ == "__main__":
    update_narrative()
    update_workbench()
