#!/usr/bin/env python3
"""Refactor Episode 03 into the Interleaved Cliffhanger Handoff Model."""

from pathlib import Path

KIT_ROOT = Path(__file__).resolve().parent.parent

NARRATIVE_PATH = KIT_ROOT / "portland-desk" / "narrative" / "03-the-default-gateway-doesnt-care.md"
DOCS_NARRATIVE_PATH = KIT_ROOT / "docs" / "portland-desk" / "narrative" / "03-the-default-gateway-doesnt-care.md"

WORKBENCH_PATH = KIT_ROOT / "portland-desk" / "workbench" / "03-the-default-gateway-doesnt-care.md"
DOCS_WORKBENCH_PATH = KIT_ROOT / "docs" / "portland-desk" / "workbench" / "03-the-default-gateway-doesnt-care.md"

NEW_NARRATIVE_END = """## The printer that stole a desk

By ten o'clock the morning storm had subsided into a light mist that clung to the riverfront trees. I had cleared eight routine password tickets from my queue when Ken called back from the shipping desk in Building B, sounding thoroughly exasperated.

"Frank's workstation has developed a phantom mind of its own," Ken reported. His voice competed with the clatter of shipping pallets. "His freight software works for thirty seconds, and then the screen locks up with network errors. Two minutes later it connects again, only to drop his session when he scans a barcode. It has been doing this dance since we renewed his IP address an hour ago."

I opened a remote desktop session to Frank's machine at `10.100.4.55`. I initiated a continuous ping toward the local default gateway at `10.100.4.1`. The terminal displayed an erratic pattern that defied ordinary hardware failure. Three successful replies appeared with two-millisecond round trips. Three request timeouts followed immediately. Four duplicate packets arrived next, followed by another burst of clean replies.

"The physical link is flapping on the wall jack," I suggested. I wondered if storm moisture had entered an external junction conduit. "I should have Owen bring a cable tester to inspect the drop behind Frank's desk."

"Inspect your Layer 2 tables before you send a technician into a crawlspace, Ethan," Jules cautioned. She glanced up from her secondary monitor. "A damaged copper cable usually produces continuous frame check errors or drops carrier completely. Frank's machine maintains solid link carrier on the switch port. Inspect the [[arp_cache|ARP cache]] while pinging an adjacent workstation."

I executed `arp -a` in the command prompt on Frank's machine. Then I opened a terminal on my administrative station. I ran `arp -a 10.100.4.55` to observe how our network viewed Frank's machine from the distribution layer.

```console
C:\\Users\\admin.ebrooks> arp -a 10.100.4.55
  10.100.4.55           00-14-22-8a-41-ef     dynamic
```

I ran the command again fifteen seconds later. The returned hardware address changed before my eyes.

```console
C:\\Users\\admin.ebrooks> arp -a 10.100.4.55
  10.100.4.55           00-25-b3-18-c2-90     dynamic
```

"Look at the physical MAC address bound to ten-one-hundred-four-fifty-five," I said, pointing at the alternating lines on my screen. "The first hardware address belongs to Frank's Dell OptiPlex desktop. Fifteen seconds later, the address flips to an identifier registered to Hewlett-Packard. Two physical network interfaces are claiming ownership of the exact same IP address."

"A classic duplicate IP address conflict," Jules observed, leaning back in her chair. "Every time one device transmits a frame, it emits an Address Resolution Protocol announcement. That announcement overwrites the switch MAC table and poisons the ARP cache of neighboring workstations. Frank's machine and the mystery device are waging an endless Layer 2 war over that IP address."

Jared Vance checked our centralized DHCP scope logs on his workstation. "Our DHCP server assigned `10.100.4.55` to Frank's Dell workstation during the lease renewal earlier this morning. That means the second device was configured with a static IP address inside our dynamic pool. If that rogue host keeps broadcasting, it will poison the entire warehouse switch stack before the noon freight trucks arrive."

Jules looked at me, her pen hovering over the ticket queue.

"You have two physical devices fighting over one Layer 3 identity, Ethan. One of them is shutting down shipping operations right now, and the other is hiding somewhere on that warehouse floor. How do you isolate the conflict, identify the rogue hardware, and permanently fix the DHCP architecture before Ken shuts down the loading dock?"

I stared at the alternating MAC addresses on my terminal. I needed to isolate the Layer 2 traffic, hunt down the rogue device, and reconfigure our address reservations before the entire freight line collapsed.

## Vocabulary & Concepts

| Concept / Term | Formal Examination Definition | Help Desk Operational Translation |
| :--- | :--- | :--- |
| **[[apipa_address|APIPA (Automatic Private IP Addressing)]]** | A link-local IPv4 address autoconfiguration mechanism where a host assigns itself an address in the 169.254.0.1 to 169.254.255.254 range with a 255.255.0.0 mask when a DHCP server fails to respond. | The operating system fallback when DHCP fails; proves the network cable is connected but no server is offering an IP configuration. |
| **[[dhcp_dora|DHCP DORA Process]]** | The four-step client-server state machine (Discover, Offer, Request, Acknowledge) used by Dynamic Host Configuration Protocol to automatically lease an IP address and network configuration to a client. | The automated conversation where a booting machine broadcasts for help, receives an address offer, requests that address, and receives an acknowledgment. |
| **[[broadcast_domain|Broadcast Domain]]** | A logical division of a computer network within which all connected nodes can reach each other by Layer 2 broadcast transmission, bounded by Layer 3 routers. | The boundary of a local VLAN or subnet; DHCP Discovers and ARP requests cannot cross this boundary without a router or relay agent forwarding them. |
| **[[subnet_mask|Subnet Mask]]** | A 32-bit bitmask that delineates the network prefix from the host identifier within an IPv4 address to determine whether a destination sits on the local or a remote subnet. | The mathematical filter that tells a computer whether another computer is in the same room or requires the default gateway to reach. |
| **[[default_gateway|Default Gateway]]** | A Layer 3 router interface on the local subnet to which a host forwards IP packets destined for remote networks outside its own broadcast domain. | The local exit door for traffic leaving the local subnet; without it, a computer cannot reach any server across the router or on the internet. |
| **[[arp_cache|ARP Cache]]** | A volatile local operating system table that maps Layer 3 IPv4 addresses to their corresponding Layer 2 physical MAC addresses for hosts on the local network segment. | The computer temporary lookup table linking IP addresses to physical network cards; if corrupted or conflicting, traffic goes to the wrong machine. |

## The Handoff Gate

```bridge-card
title: Portland Desk Lab: IPv4 Addressing, Subnet Boundaries, & Local Delivery Triage
target: workbench/03-the-default-gateway-doesnt-care.md
domain: CompTIA Network+ N10-008/009 • Domain 1.4 & 4.1
badge: Hands-On Lab
---
Take over Ethan's triage console. Isolate the Layer 2 MAC address flapping war between Frank's shipping PC and the rogue device, resolve the DHCP dynamic pool collision, audit the /26 subnet boundaries, and draft the Tier 1 Addressing Passdown Note.
```
"""

WORKBENCH_EPILOGUE = """

---

## 6. Shift Resolution Epilogue

```callout-panel
title: "FIGURE 3.2: THE RESOLVED WAREHOUSE DOCK"
badge: "Shift Epilogue"
caption: "Dock view: At 11:20 AM, intake scales and barcode scanners in Building B operate smoothly under clear skies as freight manifests stream across the restored network."
prompt: "Clean graphic novel cutaway panel of a bustling freight warehouse shipping dock in the Pacific Northwest. Pallet jacks and freight scales operate under bright industrial overhead lighting. A desktop monitor displays an active green logistics manifest. Outside open bay doors, rain has cleared over the river. Clean line art, technical precision, no text, no words. 16:9 ratio."
```

Following the Layer 2 triage, I instructed Ken to check the warehouse floor for any newly relocated equipment. Ken groaned over the radio—facilities technician Owen had wheeled a legacy HP LaserJet 4050 into the breakroom yesterday afternoon, copying its static network settings from an outdated label beneath the paper tray.

We unplugged the printer's network drop immediately. The ping replies on Frank's machine leveled out into an unbroken stream of clean two-millisecond responses. To prevent future scope collisions, I logged into the printer's web interface, shifted its addressing to dynamic DHCP reservation, and configured an explicit reservation in our Windows DHCP server at `10.100.4.240`, safely outside the dynamic client allocation pool.

With the tickets resolved and the queues subsiding to their normal rhythm, Jules opened a packet capture file on her secondary monitor. The trace displayed an HTTP exchange originating from Frank's workstation and terminating at a cloud logistics portal in Seattle at `198.51.100.44`.

"Let us review how that packet traversed the network, Ethan," Jules said, turning her chair toward me. "Frank's browser wanted to fetch a web page from `198.51.100.44`. When Frank's network adapter assembled the Ethernet frame on the wire, whose MAC address did it place in the destination field?"

"Frank's computer applied its subnet mask to the target IP address first," I answered, following the logic step by step. "The bitwise comparison proved that `198.51.100.44` was on a remote network. Because the target was remote, the workstation looked up the Layer 2 address of its local default gateway in its ARP cache."

"Exactly," Jules said, clicking on the detailed frame decode in Wireshark. "The destination IP address remained `198.51.100.44` throughout the entire journey across the internet. The time-to-live counter decremented at each hop, but the IP header stayed intact. The Layer 2 Ethernet frame was addressed directly to the gateway's router interface MAC at `10.100.4.1`. When the router received the frame, it stripped the Layer 2 header, evaluated its routing table, generated a brand new Layer 2 frame with its own source MAC, and forwarded the packet along the next hop."

She gestured toward the packet trace on her screen with the tip of her pen.

"The default gateway does not care what application you run, or what operating system you boot. It does not care how urgent your ticket feels. It only cares whether you addressed the Layer 2 frame to its physical MAC address. And it cares whether its routing table contains a valid route to forward your Layer 3 packet toward its destination."

I nodded slowly, watching the encapsulation layers light up under her cursor. I opened my technical journal and recorded the lesson alongside my earlier subnet sketches.

Outside our fourth-floor window, the low cloud deck began to lift over the Willamette. Pale patches of afternoon sky appeared above the river. Jared picked up his empty tea mug and headed toward the server room to audit switch configurations. Jules reached for her helmet, unhooking it from the monitor arm as the afternoon shift logged into the queue. I saved my incident notes into the ticketing system and closed my terminal sessions, standing on solid ground.
"""

def update_narrative():
    raw = NARRATIVE_PATH.read_text(encoding="utf-8")
    split_marker = 'I ran the command again fifteen seconds later. The returned hardware address changed before my eyes.'
    if split_marker not in raw:
        print("Marker not found in narrative")
        return
    part1 = raw.split('## The printer that stole a desk')[0].strip()
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
