#!/usr/bin/env python3
"""Refactor Episode 04 into the Interleaved Cliffhanger Handoff Model."""

from pathlib import Path

KIT_ROOT = Path(__file__).resolve().parent.parent

NARRATIVE_PATH = KIT_ROOT / "portland-desk" / "narrative" / "04-the-name-is-not-the-number.md"
DOCS_NARRATIVE_PATH = KIT_ROOT / "docs" / "portland-desk" / "narrative" / "04-the-name-is-not-the-number.md"

WORKBENCH_PATH = KIT_ROOT / "portland-desk" / "workbench" / "04-the-name-is-not-the-number.md"
DOCS_WORKBENCH_PATH = KIT_ROOT / "docs" / "portland-desk" / "workbench" / "04-the-name-is-not-the-number.md"

NEW_NARRATIVE_END = """## The leak in the tunnel

The diagnostic output laid the entire breakdown bare:

```console
InterfaceAlias               : Wi-Fi
InterfaceIndex               : 14
IPv4Address                  : 192.168.1.105
IPv4DefaultGateway           : 192.168.1.1
DNSServer                    : 192.168.1.1

InterfaceAlias               : Portland-Corporate-VPN
InterfaceIndex               : 22
IPv4Address                  : 10.200.15.42
IPv4DefaultGateway           : 
DNSServer                    : 10.100.10.2, 10.100.10.3
```

"Look at the interface binding order and gateway metrics," Maya observed. She spotted the configuration discrepancy immediately. "The client VPN profile was updated during last night's maintenance window to enable split-tunneling. That was intended to keep remote employees from pushing video streaming traffic across our corporate circuits. But whoever updated the XML connection profile forgot to configure the domain suffix search list. They also left the virtual adapter metric set higher than the physical Wi-Fi interface."

"A textbook [[dns_leak|DNS leak]]," Jules observed. She took another sip of coffee. "Modern Windows operating systems query all available network interfaces simultaneously under multi-homed resolution. The physical Wi-Fi adapter responds in four milliseconds, while the encrypted tunnel takes twenty. The home router answers first with an authoritative NXDOMAIN failure. The Windows resolver accepts the fastest negative response. The client never even waits for the internal domain controller to answer through the VPN."

"To make matters worse, look at the negative response caching," I added. I checked the record properties. "The local resolver caches those failed lookups according to the zone [[dns_ttl|DNS TTL]]. That means even if the employee restarts their browser or reconnects the tunnel, the operating system keeps feeding them the cached failure for the next fifteen minutes."

Jules set her mug down and leaned over the cubicle partition, her eyes scanning the board where eighteen tickets continued to flash amber.

"You have eighty-two tunnels open, eighteen tickets blinking amber, and seventy remote workers locked out of payroll by their own home routers," Jules said quietly. "Jared is ready to call the ISP, and our users are rebooting cable modems for nothing. How do you re-architect the client resolution priority, eliminate the negative cache trap, and prove the fix across these remote endpoints without dropping their live sessions? Call your shot, Ethan."

I looked at the terminal output and the dual adapter configuration. The tunnel was wide open, but the packets were flying blind. I needed to isolate the DNS leak, calculate the corrected adapter metrics, and draft the infrastructure escalation before the morning payroll deadline expired.

## Vocabulary & Concepts

| Concept / Term | Formal Examination Definition | Help Desk Operational Translation |
| :--- | :--- | :--- |
| **[[split_dns|Split-Horizon DNS]]** | A name resolution configuration where separate authoritative DNS servers or zone views provide different IP addresses for the same hostname based on client network location. | Internal staff on the corporate network resolve private `10.x.x.x` addresses, while external internet users resolve public gateway or CDN IPs for the same domain name. |
| **[[dns_leak|DNS Leak]]** | A networking anomaly where DNS lookups from a VPN-connected client bypass the encrypted tunnel and are sent in cleartext to local or ISP resolvers. | A remote worker's home Wi-Fi router answers corporate queries with failure errors before the corporate domain controller on the other end of the tunnel can respond. |
| **[[hosts_file|Hosts File]]** | A plain-text operating system file that maps hostnames directly to static IP addresses, taking precedence over DNS server queries during resolution. | A legacy manual override file that developers and contractors often forget to clean up, silently redirecting modern traffic to dead or obsolete test servers. |
| **[[recursive_resolver|Recursive Resolver]]** | A DNS server that performs the iterative process of querying root, TLD, and authoritative name servers on behalf of a client stub resolver to return an answer. | The intermediate server (such as an ISP or public DNS provider) that tracks down the final IP address for a computer that does not know where to go. |
| **[[dns_ttl|DNS TTL]]** | A 32-bit integer in a DNS resource record determining the duration in seconds that intermediate resolvers and client caches may retain the record before re-querying. | The expiration timer that tells your laptop how long to remember a good or bad answer; if set too high, it traps users on stale or broken addresses after an outage. |
| **[[cname_record|CNAME Record]]** | A DNS Canonical Name resource record that establishes an alias from one domain name to another fully qualified domain name rather than to an IP address. | An alias pointer that routes a friendly hostname (like `wiki.portland-ops.com`) to an external cloud or vendor URL where the real web application lives. |

## The Handoff Gate

```bridge-card
title: Portland Desk Lab: DNS Plumbing, Name Resolution Triage, & Split-Horizon Analysis
target: workbench/04-the-name-is-not-the-number.md
domain: CompTIA Network+ N10-008 • Domain 1.0 & 4.0
badge: Hands-On Lab
---
Take over Ethan's workstation. Triage the multi-homed VPN DNS leak in interactive terminal drills, correct the interface metrics and domain suffix bindings, wipe the stale negative cache, and draft the Tier 2 Infrastructure Escalation Note.
```
"""

WORKBENCH_EPILOGUE = """

---

## 6. Shift Resolution Epilogue

```callout-panel
title: "FIGURE 4.2: RESOLVED REMOTE ACCESS RESOLUTION"
badge: "Shift Epilogue"
caption: "Operations center bullpen: At 10:15 AM, the remote dispatch queue returns to green. On Greg's remote desktop, the internal payroll timesheet portal renders cleanly over the encrypted tunnel."
prompt: "Clean graphic novel cutaway panel of a municipal IT help desk operations center. Outside the panoramic windows, morning rain clears over the Willamette River. On a large wall-mounted operations monitor, a network traffic graph displays balanced green metrics. A technician types at a dual-monitor workstation. Ligne Claire style, sharp technical lines, no text, no words. 16:9 ratio."
```

With the root cause identified, Maya Chen pulled up the centralized VPN gateway management console on her workstation. She pushed a mandatory client profile revision across the cluster, enforcing an interface metric of 10 on the virtual tunnel adapter, appending `portland-ops.local` to the suffix search list, and disabling multi-homed smart resolution.

"I will handle the queue," I told Maya, opening our mass notification template. I broadcasted the three-step resolution instructions to affected staff: disconnect the client session, reconnect to pull the revised profile from the gateway cluster, and run `ipconfig /flushdns` in an elevated prompt to wipe the negative NXDOMAIN cache.

Within twelve minutes, the gateway logs confirmed that seventy-five remote endpoints had downloaded the corrected configuration. I called Greg back in Hillsboro. I walked him through the reconnection and cache flush, and watched his screen over remote control as he refreshed the browser.

The bright orange GoDaddy parked domain page vanished immediately. It was replaced by the clean green-and-white header of our internal payroll application. Greg let out an audible sigh of relief over the line, murmuring that he could finally submit his department's morning timesheets, and thanked us before hanging up. One by one, the remaining seventeen tickets on the board were updated, verified, and resolved.

Jared walked back past our row with a fresh cup of coffee. He glanced at the green status board, and gave a brief, sheepish shrug before heading back toward the network closet. He did not say another word about CenturyLink backhoes.

Jules smiled faintly and set her empty mug down on the edge of the partition. She unclipped her helmet from the display arm.

"You spent two hours chasing down someone else's bad configuration, Ethan, but you did not spend it guessing," Jules said. "Remember this shift the next time someone tells you an application is broken. The application is almost never broken. Most of the time, the client is just asking the wrong stranger for directions."

I wrote her words down in my technical journal. I saved the ticket escalation notes for Maya's post-incident review, and turned back to the queue as the rain outside softened into a quiet, steady mist.
"""

def update_narrative():
    raw = NARRATIVE_PATH.read_text(encoding="utf-8")
    part1 = raw.split("## The leak in the tunnel")[0].strip()
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
