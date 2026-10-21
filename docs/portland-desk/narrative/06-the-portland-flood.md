# Portland Desk — The Portland Flood

*A CompTIA Network+ Disaster Recovery & Midpoint Infrastructure Capstone • Hover over highlighted terms for technical definitions and triage mechanics.*

An atmospheric river had stalled directly over the Willamette Valley since midday Sunday. The weather service called the system a once-in-a-decade storm. It dumped more than four inches of rain across twelve punishing hours. By three o'clock on Monday morning, the river had surged past flood stage. The swollen current pushed brown stormwater through storm drains and low-lying basements across the industrial district. My phone woke me from a dead sleep at three-thirty with the harsh chirping tone reserved for priority campus outages.

Desk lead Jules Brooks was already speaking on the bridge line when I answered. Her voice came through clear and measured against the faint background hum of the cellular connection. "Building C took on water in the basement telecommunications vault about forty minutes ago, Ethan," she told me. "The river breached the outer retaining wall. The municipal sewer line backed up through the floor drains immediately afterward. The facility houses the regional order desk, field-service dispatch, and plant telemetry loggers for the east district. You should put on your heaviest rain gear and meet Jared and me at the loading dock with your field kit."

I pulled on my insulated coveralls and laced my rubber mud boots by the kitchen door. Five months on the Portland desk had transformed my habits. The work had replaced my old panic with an instinct for preparation. I packed my punchdown tool, an optical fiber light tester, spare patch cords, and two rolls of hook-and-loop cable ties into my canvas bag. As I drove my beat-up truck across the Morrison Bridge through blinding sheets of rain, the dark river churned violently beneath the piers.

## The basement vault at four in the morning

```callout-panel
title: "FIGURE 6.1: SUB-BASEMENT FLOOD & PATCH TRENCH"
badge: "Disaster Recovery"
caption: "Wide panoramic cutaway: The flooded Building C sub-basement. Murky water reflects emergency lights; bundles of blue Cat6 cables drip water above a wall-mounted 48-port patch panel and edge switch stack."
prompt: "Clean technical cutaway illustration of a server room during a water leak under bright emergency lights. Bundles of blue network cables hang above a wall-mounted 48-port patch panel. A rackmount switch with glowing green port LEDs. Clean instructional drawing style, crisp fine lines, no text, no words. 21:9 ratio."
```

I parked in the loading bay of Building C alongside Jared Vance's four-wheel-drive service truck just before four o'clock. The building stood dark except for the amber strobes of the emergency backup generator rumbling on its elevated concrete pad outside. Jared was already unlatching the heavy tailgate. He pulled out two cardboard equipment cartons that held spare forty-eight-port switches. Jules stood beside him in her yellow cycling rain shell. She held a halogen lantern and studied a printed building wiring schematic inside a clear plastic sleeve.

"The power cut out when the utility pole transformer arced on the street corner," Jared explained as he slung a tool harness over his shoulder. "The automatic transfer switch slammed the building over to diesel generator power six seconds later. That transient voltage spike hammered the lower distribution rack before the surge suppression circuits could clamp down. Our monitoring server lost all telemetry packets from the river intake pumps at three-fifteen."

We walked through the service entrance and headed down the concrete stairwell into the sub-basement. The air in the corridor smelled of wet concrete, river silt, and the sharp chemical ozone of overheated electronics. When we reached the bottom landing, eight inches of murky brown water covered the floor. The water lapped steadily against the foundation walls. A submersible sump pump was chugging rhythmically in the far drainage pit. It slowly forced the water toward the exterior outflow pipe.

Jules directed her halogen beam across the flooded chamber toward the open steel equipment rack bolted to the wall. The lower two rack units sat barely two inches above the water line. Dirty water spray had streaked their sheet metal housings. Both of the twenty-four-port access switches mounted in those lower slots were dark. They showed zero link lights across their front interfaces. Above them, the wall-mounted [[patch_panel|patch panel]] remained dry. However, damp condensation coated its numbered RJ-45 jacks and punchdown blocks.

"The water never crested the third rack unit, but the electrical surge killed both edge switches," Jules said, testing the water with her rubber boot before stepping forward. "We have four hours before the site opens. The order desk clerks will arrive for their morning run at eight o'clock. If this vault is dark at eight o'clock, order entry halts. Logistics dispatch will go blind, and the plant telemetry will drop into fail-safe mode."

## Cold iron and flea power

Jared and I sloshed through the standing water toward the equipment rack. Our rubber boots stirred small ripples across the flooded floor. Before touching any metal chassis, Jared unclipped an electrical test meter. He verified that zero stray voltage leaked into the water from the wall conduits. Once the meter confirmed the rack frame was safe, we set to work stripping the dead hardware from the mounting rails.

"Check the power supplies before you condemn the hardware, Ethan," Jared said, holding his flashlight on the rear power receptacles. "Sometimes an automated generator transfer trips the internal circuit breaker on the power supply without burning the silicon."

I reached behind the first switch and unplugged the redundant power cords. I flipped the rear breaker switch back and forth several times. The internal cooling fans remained motionless, and the status LEDs stayed completely dark. I knew from my hardware training that digital switching supplies often hold residual electrical charges inside their high-voltage capacitors. I held down the front power button for thirty seconds to discharge all residual [[flea_power|flea power]] from the motherboard logic gates. When I plugged the power lead back into the wall outlet, the switch remained completely unresponsive. That test confirmed that the transient surge had destroyed the internal transformer coils.

"The power supplies are fried on both lower switches," I reported, unhooking my ratcheting screwdriver from my belt. "The transient spike breached the varistors and scorched the power distribution boards."

"Then we unrack them and build fresh," Jules said, setting her lantern on an upper conduit bracket. "We have two spare forty-eight-port switches in Jared's truck bed. We are mounting them four rack units higher. That position puts them well above the reach of any future water intrusion."

Jared and I backed out the rack screws and lowered the dead chassis into scrap bins. We carried the replacement hardware down from the loading bay. We hoisted the replacement switches into the upper tier of the rack. We fastened them securely into the cage nuts with stainless steel screws. While Jared ran fresh power feeds to the overhead ceiling bus, I turned my attention to the damp horizontal cabling.

The structural wiring of Building C terminated on a two-hundred-pair [[patch_panel|patch panel]] mounted directly above the switch bays. Moisture from the humid air had condensed across the modular ports. That condensation threatened to cause high resistance or crosstalk across the copper contacts. I pulled a canister of lint-free wipes and electronic contact cleaner from my field kit. I methodically cleaned each modular port. I wiped the plastic bezels dry. Finally, I inspected the color-coded twisted pairs on the reverse punchdown blocks to ensure all connections remained tight.

## Building the three broadcast domains

By five-thirty in the morning, the physical installation was complete. Both replacement switches hummed quietly on clean generator power. Jared plugged a rollover console cable into the management port of the primary switch. He handed the serial adapter over to me. I sat on an overturned plastic equipment crate above the water line, balancing my laptop across my knees.

"Building C carries three distinct operational services across its horizontal cabling," Jules reminded me, shining her penlight onto her laminated network layout map. "VLAN 10 handles order desk workstations and the regional database servers. VLAN 20 carries critical Plant Telemetry Loggers that monitor river intake levels. VLAN 30 is reserved strictly for VoIP dispatch consoles and the plant safety phones. If you cross those streams, you violate company security policy and risk dropping a safety call."

I logged into the switch command line and initialized the baseline configuration. I created each virtual network in the local database. I named them carefully to match our campus inventory standards. Next, I mapped the physical patch connections from the [[patch_panel|patch panel]] into their designated access interfaces. I placed the billing desks on VLAN 10. I assigned the telemetry loggers to VLAN 20. I configured the dispatch handsets on VLAN 30.

```console
Switch-BuildingC# configure terminal
Switch-BuildingC(config)# vlan 10
Switch-BuildingC(config-vlan)# name CORP_WATER_BILLING
Switch-BuildingC(config-vlan)# vlan 20
Switch-BuildingC(config-vlan)# name PLANT_TELEMETRY
Switch-BuildingC(config-vlan)# vlan 30
Switch-BuildingC(config-vlan)# name VOIP_DISPATCH
Switch-BuildingC(config-vlan)# exit
```

"Now configure the campus distribution uplink," Jared instructed, leaning over my shoulder as he checked the overhead fiber junction box. "We are running dual gigabit fiber connections back to the core distribution router in Building A. If you bring those links up as individual access ports, you will create an immediate broadcast storm or strand two of your virtual networks."

"We need an 802.1Q trunk," I answered, applying the principles I had practiced during quiet graveyard shifts. "We must configure [[vlan_trunking|VLAN trunking]] across the fiber interfaces. That configuration allows a single physical medium to encapsulate and transport frames from all three virtual local area networks simultaneously."

I navigated to the fiber transceiver interfaces on ports GigabitEthernet 1/0/49 and 1/0/50. I configured both ports for 802.1Q trunk encapsulation. I explicitly permitted VLANs 10, 20, and 30 across the trunk pipe while defining native VLAN 99 for untagged management frames. To prevent a single severed fiber strand from taking down our connection, I bundled both physical interfaces into an active Link Aggregation Control Protocol channel.

```console
Switch-BuildingC(config)# interface range GigabitEthernet 1/0/49 - 50
Switch-BuildingC(config-if-range)# switchport trunk encapsulation dot1q
Switch-BuildingC(config-if-range)# switchport mode trunk
Switch-BuildingC(config-if-range)# switchport trunk allowed vlan 10,20,30,99
Switch-BuildingC(config-if-range)# switchport trunk native vlan 99
Switch-BuildingC(config-if-range)# channel-group 1 mode active
Switch-BuildingC(config-if-range)# exit
```

"Now check the logical bundle status," Jules said, watching the terminal display. "Never assume a bundle is healthy just because the physical link lights turn green."

I executed `show etherchannel summary` on the terminal. The console confirmed that Port-Channel 1 was operational in Layer 2 mode. The channel bundled both physical fiber interfaces under [[link_aggregation|link aggregation]] into a single two-gigabit logical trunk. 

Next, I verified our loop prevention topology by querying the bridge status across all active virtual networks. Redundant fiber links connected our switch to the campus backbone. An unmanaged loop would circulate broadcast frames until the switch processor locked up. The terminal output showed that [[spanning_tree|Spanning Tree Protocol]] had established our central distribution switch in Building A as the root bridge. Our local port-channel sat in the forwarding state without blocking. That result confirmed a deterministic, loop-free data path across the campus.

```console
Switch-BuildingC# show spanning-tree vlan 10

VLAN0010
  Spanning tree enabled protocol rstp
  Root ID    Priority    24586
             Address     0014.f25a.8100
             Cost        3
             Port        53 (Port-channel1)
  Bridge ID  Priority    32778
             Address     0022.bdd3.4480
  Interface           Role Sts Cost      Prio.Nbr Type
  ------------------- ---- --- --------- -------- --------------------------------
  Po1                 Root FWD 3         128.53   P2p 
```

"Layer 1 and Layer 2 are solid," I said, looking up from my laptop screen. "The patch panel is dry, the trunk is forwarding all three VLANs, and the link aggregation group is carrying traffic. The plant telemetry loggers should be reaching the core database."

## The morning stampede

At seven-fifteen, the city electrical utility restored commercial grid power to the district. Outside our basement vault, the diesel generator cycled down with a heavy mechanical shudder. The campus transfer switch transferred the electrical load back to the municipal grid. Overhead fluorescent tubes flickered on throughout Building C, illuminating the wet stairwells and hallways.

Upstairs on the first and second floors, more than one hundred and fifty company devices powered on at the exact same moment. Desktop workstations in the order desk bullpen booted into their login screens. Wall-mounted logistics monitors reconnected their displays. Rows of VoIP handsets on dispatch desks initialized their operating firmware.

Within three minutes, my mobile service phone began vibrating continuously in my pocket. Jared opened our network monitoring dashboard on his tablet. A sea of yellow and red warning icons populated the Building C device overview. 

"The billing workstations are throwing network errors," Jared announced as he pointed his tablet screen toward us. "The clerks are arriving early to prepare the monthly billing cycle. None of their machines can resolve the billing server. They are pulling sixteen-nine addresses and displaying disconnected socket errors."

"Did the fiber trunk drop?" Jules asked, her eyes narrowing as she stepped toward my console.

"The trunk interface is up and passing frames," I replied, running `show interfaces trunk` on the console. "The port-channel is green. I will connect to the Windows DHCP server in the central datacenter and check the scope status for VLAN 10."

I opened a remote PowerShell terminal to our primary domain controller. I queried the active DHCP scope servicing the order desk subnet at `10.20.10.0/24`. The output revealed an immediate operational problem.

```console
PS C:\Users\emercer> Get-DhcpServerv4Scope -ScopeId 10.20.10.0 | Format-List ScopeId, Free, InUse, State

ScopeId : 10.20.10.0
Free    : 0
InUse   : 200
State   : Active
```

"Look at the address counter on this scope," I called out, tracing the numbers on the display. "The available free address count is zero. The active in-use count is at two hundred. We have hit complete [[dhcp_exhaustion|DHCP scope exhaustion]] on the order desk subnet."

"How can a department with eighty desks exhaust a pool of two hundred addresses?" Jared asked, scratching his beard in frustration. "Did someone plug an unauthorized rogue wireless router into a wall jack upstairs?"

I ran `Get-DhcpServerv4Lease -ScopeId 10.20.10.0` and piped the output into a sorting filter. Long rows of hostnames and physical hardware addresses scrolled rapidly across my monitor alongside lease expiration timestamps. The diagnostic data revealed a clear operational failure. The scope lease duration was configured for eight days, an old legacy setting left behind from a previous office configuration. 

When the power cut during the storm, eighty desktop computers dropped off the network. When commercial power returned, those machines powered back on alongside fifty docking stations, twenty network printers, and fifteen field tablets carried in by arriving logistics drivers. Because the old leases were still active in the database, the DHCP server refused to reassign those addresses to new client requests. The eighty booting workstations broadcasted DHCP Discover packets across VLAN 10. They received zero Offers from the exhausted server and fell back to link-local APIPA assignments.

"The scope ran out of leases because the lease duration is set to eight days," I explained to Jules and Jared, using the binary search method Jules had drilled into me. "Over one hundred offline leases from last week are locking up the pool. When all one hundred and fifty devices booted at once, the server exhausted its remaining twenty addresses in sixty seconds."

Jules set her flashlight down on the rack rail and looked directly at me.

"We have twenty-five minutes before the parts counter opens upstairs, Ethan," Jules said, her voice cutting through the hum of the cooling fans. "Eighty order clerks are locked out, twenty printers are dead, and the dispatchers cannot reach the safety line. If this building is not fully online at eight o'clock, Rivergate cannot take or ship a single order. What is your plan of action? How do you flush the stale leases, re-architect the scope duration, expand the dynamic pool without colliding with static equipment, and verify the entire four-layer protocol stack before that bell rings? Call your shot, Ethan."

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
Take over Ethan's console at 07:35 AM in the flooded vault. Execute the PowerShell DHCP reconciliation to clear 84 stale leases, reduce lease durations, expand pool capacity, and run the Layer 1-4 verification checklist before the 08:00 AM opening.
```
