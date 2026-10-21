#!/usr/bin/env python3
"""Refactor Episode 06 (The Midpoint Capstone) into the Interleaved Cliffhanger Handoff Model."""

from pathlib import Path

KIT_ROOT = Path(__file__).resolve().parent.parent

NARRATIVE_PATH = KIT_ROOT / "portland-desk" / "narrative" / "06-the-portland-flood.md"
DOCS_NARRATIVE_PATH = KIT_ROOT / "docs" / "portland-desk" / "narrative" / "06-the-portland-flood.md"

WORKBENCH_PATH = KIT_ROOT / "portland-desk" / "workbench" / "06-the-portland-flood.md"
DOCS_WORKBENCH_PATH = KIT_ROOT / "docs" / "portland-desk" / "workbench" / "06-the-portland-flood.md"

NEW_NARRATIVE_END = """## The morning stampede

At seven-fifteen, the city electrical utility restored commercial grid power to the district. Outside our basement vault, the diesel generator cycled down with a heavy mechanical shudder. The campus transfer switch transferred the electrical load back to the municipal grid. Overhead fluorescent tubes flickered on throughout Building C, illuminating the wet stairwells and hallways.

Upstairs on the first and second floors, more than one hundred and fifty municipal devices powered on at the exact same moment. Desktop workstations in the water billing bullpen booted into their login screens. Wall-mounted logistics monitors reconnected their displays. Rows of VoIP handsets on dispatch desks initialized their operating firmware.

Within three minutes, my mobile service phone began vibrating continuously in my pocket. Jared opened our network monitoring dashboard on his tablet. A sea of yellow and red warning icons populated the Building C device overview. 

"The billing workstations are throwing network errors," Jared announced as he pointed his tablet screen toward us. "The clerks are arriving early to prepare the monthly billing cycle. None of their machines can resolve the billing server. They are pulling sixteen-nine addresses and displaying disconnected socket errors."

"Did the fiber trunk drop?" Jules asked, her eyes narrowing as she stepped toward my console.

"The trunk interface is up and passing frames," I replied, running `show interfaces trunk` on the console. "The port-channel is green. I will connect to the Windows DHCP server in the central datacenter and check the scope status for VLAN 10."

I opened a remote PowerShell terminal to our primary domain controller. I queried the active DHCP scope servicing the water billing subnet at `10.20.10.0/24`. The output revealed an immediate operational problem.

```console
PS C:\\Users\\emercer> Get-DhcpServerv4Scope -ScopeId 10.20.10.0 | Format-List ScopeId, Free, InUse, State

ScopeId : 10.20.10.0
Free    : 0
InUse   : 200
State   : Active
```

"Look at the address counter on this scope," I called out, tracing the numbers on the display. "The available free address count is zero. The active in-use count is at two hundred. We have hit complete [[dhcp_exhaustion|DHCP scope exhaustion]] on the water billing subnet."

"How can a department with eighty desks exhaust a pool of two hundred addresses?" Jared asked, scratching his beard in frustration. "Did someone plug an unauthorized rogue wireless router into a wall jack upstairs?"

I ran `Get-DhcpServerv4Lease -ScopeId 10.20.10.0` and piped the output into a sorting filter. Long rows of hostnames and physical hardware addresses scrolled rapidly across my monitor alongside lease expiration timestamps. The diagnostic data revealed a clear operational failure. The scope lease duration was configured for eight days, an old legacy setting left behind from a previous office configuration. 

When the power cut during the storm, eighty desktop computers dropped off the network. When commercial power returned, those machines powered back on alongside fifty docking stations, twenty network printers, and fifteen field tablets carried in by arriving logistics drivers. Because the old leases were still active in the database, the DHCP server refused to reassign those addresses to new client requests. The eighty booting workstations broadcasted DHCP Discover packets across VLAN 10. They received zero Offers from the exhausted server and fell back to link-local APIPA assignments.

"The scope ran out of leases because the lease duration is set to eight days," I explained to Jules and Jared, using the binary search method Jules had drilled into me. "Over one hundred offline leases from last week are locking up the pool. When all one hundred and fifty devices booted at once, the server exhausted its remaining twenty addresses in sixty seconds."

Jules set her flashlight down on the rack rail and looked directly at me.

"We have twenty-five minutes before the public service windows unlock upstairs, Ethan," Jules said, her voice cutting through the hum of the cooling fans. "Eighty billing clerks are locked out, twenty printers are dead, and the dispatchers cannot place emergency calls. If this building is not fully online at eight o'clock, the city shuts down public intake. What is your plan of action? How do you flush the stale leases, re-architect the scope duration, expand the dynamic pool without colliding with static equipment, and verify the entire four-layer protocol stack before that bell rings? Call your shot, Ethan."

I looked at the red warning icons multiplying across the monitoring board. Four hours of sweating in rubber boots in an ankle-deep flood came down to the next twenty-five minutes. I needed to execute the DHCP reconciliation, restore address leases to one hundred and fifty endpoints, and run the end-to-end verification checklist before the doors unlocked.

## Desk Translation Table

| Concept / Term | Formal Examination Definition | Help Desk Operational Translation |
| :--- | :--- | :--- |
| **[[vlan_trunking|VLAN Trunking (802.1Q)]]** | A Layer 2 bridging mechanism allowing multiple virtual local area networks to traverse a single physical link by inserting a 4-byte 802.1Q VLAN tag into the Ethernet frame header. | The high-capacity pipe that carries multiple department networks across a single fiber cable without letting their data cross over or mix. |
| **[[dhcp_exhaustion|DHCP Scope Exhaustion]]** | A network denial-of-service condition where a Dynamic Host Configuration Protocol scope has leased all available IP addresses in its allocation pool, preventing new devices from acquiring network configurations. | The digital parking lot being full; when every lease is taken, new computers cannot get an IP address and fall back to useless 169.254 numbers. |
| **[[patch_panel|Patch Panel]]** | A passive, rack-mounted structural interconnect device containing female RJ-45 modular jacks on the front and 110 punchdown blocks on the rear to terminate horizontal structured cabling. | The organized wall organizer where all the permanent building cables end, letting technicians plug patch cords into switches without ripping out wall wires. |
| **[[flea_power|Flea Power]]** | The residual static electrical charge stored in motherboard capacitors, power supply filter stages, and integrated circuits after primary electrical power is disconnected. | The leftover electric charge lingering in capacitors that keeps corrupt chips frozen until you unplug the cord and hold the power button down. |
| **[[spanning_tree|Spanning Tree Protocol (STP)]]** | A Layer 2 network protocol that monitors bridge topology and dynamically places redundant switch ports into blocking state to prevent catastrophic broadcast storms and switching loops. | The network traffic cop that turns off duplicate switch cables so broadcast loops do not circle endlessly and crash the entire building network. |
| **[[link_aggregation|Link Aggregation (LACP)]]** | A networking standard (Link Aggregation Control Protocol) that bundles multiple physical Ethernet interfaces into a single logical channel to provide multiplied bandwidth and active redundancy. | The team-up protocol that binds two or more network cables together to act like one double-speed wire that stays up even if one cable snaps. |

## The Handoff Gate

```bridge-card
title: Portland Desk Lab: The Campus Flood & Disaster Recovery Crucible
target: workbench/06-the-portland-flood.md
domain: CompTIA Network+ N10-008/009 • Disaster Recovery & Layer 1-4 Rebuild
badge: The Hands-On Lab
---
Take over Ethan's console at 07:35 AM in the flooded vault. Execute the PowerShell DHCP reconciliation to clear 84 stale leases, reduce lease durations, expand pool capacity, and run the Layer 1-4 verification checklist before the 08:00 AM municipal opening bell.
```
"""

WORKBENCH_EPILOGUE = """

---

## 6. Shift Resolution Epilogue

```callout-panel
title: "FIGURE 6.2: THE RESTORED CAMPUS VAULT"
badge: "Shift Epilogue"
caption: "Sub-basement vault view: At 07:55 AM, the elevated switch stack hums with unbroken green link lights above the receding water line as the morning opening bell sounds."
prompt: "Clean graphic novel cutaway panel of an industrial server rack inside an elevated telecommunications room. Outside the high clerestory windows, morning winter light reflects over a swollen river. Technicians in rain gear pack toolkits as green status lights glow steadily across mounted switch interfaces. Ligne Claire style, sharp technical precision, no text, no words. 16:9 ratio."
```

Following the PowerShell scope reconciliation, the DHCP server flushed eighty-four stale leases from memory in six seconds. Almost instantly, our monitoring dashboard showed client devices renewing their addresses across the building. 

I consoled into a test workstation on the billing floor and executed `ipconfig /renew`. Within two seconds, the terminal returned a valid network configuration with IP address `10.20.10.74`, a subnet mask of `255.255.255.0`, and a default gateway pointing to `10.20.10.1`. The billing application splash screen loaded cleanly, authenticated against the database cluster, and displayed green status indicators across all transaction ledgers.

By seven-fifty in the morning, the basement vault had quieted down. The sump pump had lowered the standing water to a shallow sheen across the low corners of the concrete floor. The newly mounted switches in the upper rack operated quietly, their link lights blinking in steady green unison across all forty-eight interfaces.

Jules stood beside the rack with her clipboard in hand, verifying our post-restoration punch list. "Run the end-to-end verification across all four layers, Ethan. I want proof before the department director walks through the door."

I opened four simultaneous terminal sessions on my laptop and executed our standard verification checklist:

1. **Layer 1 (Physical):** Link status on both fiber transceivers and all forty-eight copper ports showed full-duplex operation at one gigabit per second, with zero CRC alignment errors on the counter registers.
2. **Layer 2 (Data Link):** The LACP bundle showed both physical member links active in Port-Channel 1. Rapid Spanning Tree Protocol confirmed zero topology changes or blocked ports across all three active virtual networks.
3. **Layer 3 (Network):** Default gateway pings to `10.20.10.1` (Billing), `10.20.20.1` (Telemetry), and `10.20.30.1` (VoIP) responded with consistent sub-millisecond round-trip times.
4. **Layer 4 and Application:** Telemetry loggers on VLAN 20 successfully delivered Modbus sensor packets to the central SCADA database. VoIP phones on VLAN 30 registered with the call manager, and water billing terminals on VLAN 10 completed test database queries without packet loss.

I closed my active terminal windows and reported that all three network segments were fully operational. The trunk was balanced, the DHCP pool had ninety free leases remaining, and the plant telemetry stream had been stable for twenty minutes.

Jared latched his toolcase and slung his cable harness over his shoulder with a weary grin. "Not bad for four hours in rubber boots, kid. You handled that DHCP pool storm faster than our third-shift network admin did last winter."

Outside the high basement windows, the rain had finally tapered off to a gentle Pacific Northwest drizzle. The dark storm clouds were breaking over the Willamette River. Pale winter morning light reflected across the wet asphalt of the loading bay. Upstairs, the faint chime of the municipal elevator signaled the arrival of the morning staff as the eight o'clock bell rang out across the campus.

Jules switched off her halogen lantern and hooked her bicycle helmet to her pack. "You did not panic when the scope exhausted, Ethan," she said, looking at me with a quiet nod of approval. "You followed the protocol stack from the wet concrete up to the transport layer, and you committed your decisions before you typed them. That is the difference between guessing in the dark and doing the work."

We hauled our empty cartons and spent gear up the stairwell to Jared's truck, leaving the basement telecommunications vault secure, elevated, and fully restored.
"""

def update_narrative():
    raw = NARRATIVE_PATH.read_text(encoding="utf-8")
    part1 = raw.split("## The morning stampede")[0].strip()
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
