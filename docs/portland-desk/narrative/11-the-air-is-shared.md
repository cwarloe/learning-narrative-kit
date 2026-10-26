# Portland Desk — The Air Is Shared

*A Security+ wireless precursor • Hover over highlighted terms for exam definitions and supporting desk jargon.*

Friday morning opened with the whine of the vacuum cleaner in the hallway and a ticket from Maya that had been sent from the lobby.

Jules came out of the server closet with a handheld spectrum analyzer and set it on my desk without a word. The display was already busier than it should have been.

Ken had not called my desk line since the laptop. When he finally wrote, it was a two-line email asking whether the barcode scanners in the warehouse were safe on Wi-Fi. I wrote back that they were. By Thursday I was less sure.

The board dinged with Maya's ticket: *Can't join CorpWifi — worked yesterday — executive meeting in 20.*

## Maya and the password that is everyone

```callout-panel
title: "FIGURE 11.1: 2.4 GHZ VS 5 GHZ SPECTRUM & ROGUE INTERFERENCE"
badge: "RF Wireless Analysis"
caption: "Radio frequency spectrum diagram: The three non-overlapping 2.4 GHz channels (1, 6, 11). Shows an unshielded microwave oven emitting wideband RF interference centered on Channel 6."
prompt: "Clean technical cutaway diagram of radio frequency spectrum channels under bright studio lighting. Bell curves represent Wi-Fi channels 1, 6, and 11 across the 2.4 GHz band, with interference spikes overlapping channel 6. Crisp technical line art, no text, no words. 16:9 ratio."
```

Maya from accounting was in the lobby with a loaner laptop.

"It asks for a password," she said. "I type the one on the sticky under the monitor in Finance. Denied. Also there are two networks named almost the same. One has more bars."

I walked out with a phone running our approved [[wifi_analyzer|Wi-Fi analyzer]] view. Official [[ssid|SSID]] was `CORP-EMPLOYEE`. Beside it appeared `CORP-EMPLOYEE_Guest` and a duplicate `CORP-EMPLOYEE` with an identical network name but an unrecognized BSSID transmitting at maximum signal strength near the street entrance.

"That sticky note is the old guest [[psk|pre-shared key]], Maya," I said. "Connect to `CORP-EMPLOYEE` instead. That uses [[enterprise_wpa|WPA-Enterprise]]—authenticate with your normal badge username and password under [[ieee_8021x|802.1X]] against our [[radius|RADIUS]] server, and accept the company certificate. Don't touch the duplicate network."

Maya squinted at the twin. "So the louder one is…?"

"Treat it as an [[evil_twin|evil twin]] until Network says otherwise," I said. "Same costume, wrong radio. We open a ticket for wireless ops and you work from a dock until they kill it."

She docked. She was late to the board meeting. The twin was still on the air when I walked back.

## WEP, open air, and the portal that feels like security

Todd from sales called from a hotel before a customer demo. He was proud of a workaround.

"Hotel Wi-Fi is open, then a webpage asks for the room number," he said. "That is basically login security, right? Also the customer site still has a dusty AP labeled WEP for the old scanner. They told me to join it for the warehouse tour."

I put him on speaker.

"Open network means no encryption on the air," I said. "The [[captive_portal|captive portal]] is a gate for internet access, not a force field. Anyone on that same open SSID can try [[eavesdropping|wireless eavesdropping]] unless you wrap traffic in a VPN. Use the VPN before mail, before files, before just-quick Slack."

"And WEP?" Todd asked.

"[[wep|WEP]] is a museum piece that still unlocks," Jules said. "Broken by [[iv_attack|IV attacks]] and boredom. If a scanner needs WEP, the scanner is the problem. Do not put your laptop there. Ask them for a wired drop or a modern SSID."

Todd muttered something about customer politics and connected the VPN on the hotel portal network. He did not join the WEP scanner. He said the customer tour would have to live without his laptop.

## Rogue AP in the conference room

Mid-morning Facilities Slack: visitors could not reach the projector, so someone from Marketing had brought a travel router like they do at home. It was plugged into a wall jack under the credenza. SSID: `FreeConfQuick`. Security: none.

"That is a [[rogue_ap|rogue access point]]," I said when I got to the room. "Unauthorized access point. Even if the intent is kindness, it bridges unknown phones onto our wall jack without the wireless controller policies. Unplug it."

Rita blushed into her notebook. We unplugged. Network confirmed the jack was on a user VLAN that should never have been a free café. I filed the ticket with a photo, jack number, and "not malicious, still a rogue."

While we were there, the analyzer showed our real APs alongside faint guest beacons from adjacent retail shops down the street. Not our emergency, but a clear reminder that radio boundaries stop where walls end.

## Disassociation, jamming, and the reconnect reflex

Dev called the help desk from the cafe seating near the lobby glass. His laptop kept dropping Wi-Fi every few minutes, then auto-joined whatever answered first.

"I did not change anything," he said. "It just flaps. Then it asks for passwords it already knew."

Wireless ops had a note on the bridge: bursts of spoofed [[disassociation|deauthentication frames]] aimed at lobby clients where 802.11w Protected Management Frames had not yet been enforced on the legacy WPA2 profile. Not full [[jamming|jamming]]—the air still worked—but enough kicks to make laptops frantic. Frantic laptops are how evil twins collect friends.

"When you get kicked, do not reconnect on autopilot," I said. "Check the SSID character by character. Prefer the dock. If the air is being rude on purpose, escalate — that is a SOC and wireless hunt, not a forget-network ritual."

Dev docked. The flapping stopped because copper does not care about deauth theater.

## Owen and the bench in the lobby

The evil twin was not in the air. It was in the lobby, a small battery-powered access point taped under a bench by the visitor sign-in tablet. I found Owen in the loading dock vestibule, where he was replacing a door closer, and he followed me back.

Owen walked the lobby with me and pointed out what I had walked past for two years: the camera over the front desk did not cover the benches, the badge reader on the inner door was the only controlled boundary, and the cleaning crew propped the side door during evening rounds. He knew the cameras, locks, and doors, and he admitted right away that he did not know what the device under the bench was doing on the network.

"Somebody sat here long enough to tape that up," he said. "Nobody stopped them because the lobby's public. That's on purpose. The question is where public stops." We wrote down the three places it stopped: the inner badge door, the server closet lock, and the camera blind spot that needed fixing.

## The Bench and the Barcode Guns

We found the travel router under the credenza in 3B and shut its switch port. The barcode scanners reassociated with our access points, and Dev's laptop came back over 802.1X.

Owen took the lobby personally. He had the side door re-keyed that week and put in for a second camera. The camera did not come that month.

It still slowed the dock, and it cost me a Saturday. Re-enrolling the scanners onto 802.1X took most of the next morning, and Ken's crew scanned by hand at two doors until noon. He drove up from Gresham that afternoon and stood at my desk to tell me exactly how many pallets that had cost. It was the first time he had spoken to me since the laptop.

Jules had told me to keep the survey data. "Save what normal looks like," she said, "or you'll never know what weird is." I saved the wireless baseline to the shared drive with a note to her and added to it every week after that, mostly because she checked.

## Practice It in the Lab

```bridge-card
title: Portland Desk Lab: Wireless Security, 802.1X Enterprise, & Rogue AP Triage
target: workbench/11-the-air-is-shared.md
domain: CompTIA Security+ SY0-701 • Domain 2.1 & 3.2
badge: The Hands-On Lab
cta: Take the Ticket & Open the Lab ->
---
The lab walks through the incident from this chapter step by step, with the answer shown, and then gives you one new problem that works the same way.
```
