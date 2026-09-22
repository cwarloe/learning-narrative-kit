# Portland Desk — The Air Is Shared

*A Security+ wireless precursor • Hover over highlighted terms for exam definitions and supporting desk jargon.*

The first [[ticket|ticket]] of Friday was *Can't join CorpWifi — worked yesterday — board meeting in 20.* Jules's sticky under *which decision?* said *which SSID am I actually on?*

"Wired has a cable you can point at," she said when I reached for a blank card. "Wireless has manners and math. Verify the network. Prefer enterprise over café vibes. Escalate anything that looks like a twin."

I opened the [[help_desk|help desk]] queue.

## Maya and the password that is everyone

Maya from accounting was in the lobby with a loaner laptop.

"It asks for a password," she said. "I type the one on the sticky under the monitor in Finance. Denied. Also there are two networks named almost the same. One has more bars."

I walked out with a phone running our approved [[wifi_analyzer|Wi-Fi analyzer]] view. Official [[ssid|SSID]] was `CORP-EMPLOYEE`. Beside it, `CORP-EMPLOYEE_Guest` and a suspicious `CORP-EMPLOYE` with the last letter missing and a [[signal_strength|signal strength]] that was louder near the street than near the AP closet.

"The lobby sticky password is the old [[psk|PSK]] world," I said. "Shared key. Everyone knows it, which means everyone and their cousin know it. We moved employees to [[enterprise_wpa|WPA-Enterprise]] — [[ieee_8021x|802.1X]] with your badge account against [[radius|RADIUS]]. Join `CORP-EMPLOYEE`, use your user ID, trust the company [[certificate|certificate]] prompt we already documented, and do not join the loud almost-name."

Maya squinted at the twin. "So the louder one is…?"

"Treat it as an [[evil_twin|evil twin]] until Network says otherwise," I said. "Same costume, wrong radio. We open a ticket for wireless ops and you work from a dock until they kill it."

She docked. She was late to the board meeting. The twin was still on the air when I walked back.

## WEP, open air, and the portal that feels like security

Ken from sales called from a hotel before a customer demo. He was proud of a workaround.

"Hotel Wi-Fi is open, then a webpage asks for the room number," he said. "That is basically login security, right? Also the customer site still has a dusty AP labeled WEP for the old scanner. They told me to join it for the warehouse tour."

I put him on speaker.

"[[open_network|Open network]] means no encryption on the air," I said. "The [[captive_portal|captive portal]] is a gate for internet access, not a force field. Anyone on that same open SSID can try [[eavesdropping|wireless eavesdropping]] unless you wrap traffic in a [[vpn|VPN]]. Use the VPN before mail, before files, before just-quick Slack."

"And WEP?" Ken asked.

"[[wep|WEP]] is a museum piece that still unlocks," Jules said. "Broken by [[iv_attack|IV attacks]] and boredom. If a scanner needs WEP, the scanner is the problem. Do not put your laptop there. Ask them for a wired drop or a modern SSID."

Ken muttered something about customer politics and connected the VPN on the hotel portal network. He did not join the WEP scanner. He said the warehouse tour would have to live without his laptop.

## Rogue AP in the conference room

Mid-morning Facilities Slack: visitors could not reach the projector, so someone from Marketing had brought a travel router like they do at home. It was plugged into a wall jack under the credenza. SSID: `FreeConfQuick`. Security: none.

"That is a [[rogue_ap|rogue access point]]," I said when I got to the room. "Unauthorized [[access_point|access point]]. Even if the intent is kindness, it bridges unknown phones onto our wall jack without the [[controller|wireless controller]] policies. Unplug it."

Rita blushed into her notebook. We unplugged. Network confirmed the jack was on a user VLAN that should never have been a free café. I filed the ticket with a photo, jack number, and "not malicious, still a rogue."

While we were there, the analyzer showed our real APs plus a faint outside SSID that had been mapping the block for an hour — classic [[war_driving|war driving]] energy from a car with too many antennas. Not our emergency. Still a reminder that discovery is cheap.

## Disassociation, jamming, and the reconnect reflex

Afternoon: Dev from engineering pinged that his laptop kept dropping Wi-Fi every few minutes, then auto-joined whatever answered first. He was in the cafe seating near the lobby glass.

"I did not change anything," he said. "It just flaps. Then it asks for passwords it already knew."

Wireless ops had a note on the bridge: bursts of [[disassociation|disassociation / deauthentication]] frames aimed at lobby clients. Not full [[jamming|jamming]] — the air still worked — but enough kicks to make laptops frantic. Frantic laptops are how evil twins collect friends.

"When you get kicked, do not reconnect on autopilot," I said. "Check the SSID character by character. Prefer the dock. If the air is being rude on purpose, escalate — that is a [[soc|SOC]] and wireless hunt, not a forget-network ritual."

Dev docked. The flapping stopped because copper does not care about deauth theater.

## Guest Wi-Fi, segmentation, and the printer that should not see payroll

Nora needed a vendor on site to update a badge printer. The vendor wanted Wi-Fi. Nora wanted them productive. Finance wanted them nowhere near file shares.

"[[guest_wifi|Guest Wi-Fi]]," I said. "Different SSID, captive portal for AUP, and — this is the part people skip — [[segmentation|network segmentation]] so guest cannot route to payroll, cameras, or the help desk VLAN. Guest without segmentation is just hospitality for lateral movement."

We put the vendor on `CORP-GUEST`, watched them fail to ping an internal share, and succeed at the vendor's own update CDN. Nora asked if we should hide the employee SSID so guests were less confused.

"[[hidden_ssid|Hidden SSID]] is obscurity," Jules said. "It still leaks in other frames. Real control is enterprise auth and segmentation."

Someone in the thread suggested MAC allow-lists for the printer VLAN. I typed carefully: "[[mac_filtering|MAC filtering]] is a speed bump you can spoof with a screenshot."

## WPA2, WPA3, WPS, and the survey that is not vibes

Network dropped by the desk with a short hallway class. They were rolling a pilot.

"Employees stay on [[wpa2|WPA2]]-Enterprise today," the engineer said. "Pilot floor gets [[wpa3|WPA3]]-Enterprise with [[sae|SAE]] for the personal SSID we still keep for a few IoT leftovers. SAE is why WPA3-PSK is less embarrassed about offline password guessing than WPA2-PSK. And turn [[wps|WPS]] off on anything that still admits it exists — convenience pairing with a brute-force hobby."

I asked about coverage complaints on the east cubes. They pulled last week's [[site_survey|site survey]]: heat map, channel overlap, one AP transmitting like it was trying to cover the MAX stop.

"[[ap_placement|AP placement]] and power," the engineer said. "Too loud outside means easier eavesdropping and easier twins. Survey is how we know. Vibes are how we get tickets titled Wi-Fi bad."

I wrote it down.

## Controllers, certificates, and the Monday meeting reflex

Before Bluetooth ate the last hour, I rewrote one more wiki line the desk will actually use. The wireless controller is where SSID policy lives — encryption mode, guest splash, rogue detection flags — not in a sticky under someone's monitor. When a laptop fails enterprise join, we check whether the user clicked past a certificate warning, whether they are on the right SSID, and whether a booster app installed a fake trust store.

Jules made me say it once for the queue: "If the meeting started, that is not permission to join the loud lookalike. Dock, hotspot from a known phone through VPN, or wait."

I put that sentence in the ticket template.

## Bluetooth in the cube farm

Late day, Lila's laptop kept pairing prompts for a keyboard she did not own. Jordan found a cheap earbud spam message that said *Hi cute phone.* Sam wanted to leave Bluetooth discovery on so his watch felt loved.

"[[bluetooth|Bluetooth]] is a second air," I said. "Short range, real risk. Unsolicited messages are [[bluejacking|bluejacking]] — mostly rude. Actual data theft over weak pairing is [[bluesnarfing|bluesnarfing]]. Desk hygiene: [[bluetooth_pairing|pairing hygiene]] — only expected devices, confirm the code, discovery off when you are not actively pairing."

Lila declined the ghost keyboard. Jordan turned discovery off. Sam looked betrayed by his watch and complied anyway.

## Replay, certificates, and the line that sticks

End of day we closed a stubborn laptop that kept failing enterprise join. The user had installed a free "Wi-Fi booster" profile that pinned a wrong trust anchor. They were one impatient click from sending their password to a lookalike.

"Enterprise helps only if you protect the certificate check," I said. "If the client ignores trust, [[replay_attack|replay]] and twin games get easier. Clicking through certificate warnings on Wi-Fi is the same sin as clicking through them on banks."

I updated the wiki blurb: join the real SSID, prefer 802.1X over hallway PSK, VPN on open and portal networks, never WEP, unplug rogue travel routers, do not reconnect blind after weird drops, guest stays segmented, hide-SSID and MAC filters are not controls, WPS off, survey over vibes, and Bluetooth only for things you meant to invite.

At 5:40 I closed notes. Maya was on enterprise and late. Ken was on VPN and not on WEP. Rita's rogue was unplugged. Dev was docked through deauth. The vendor was on guest with walls. Lila's ghost keyboard was declined. The twin in the lobby was still Network's problem.

Jules clipped her bike lights on. "Monday someone will join the loud lookalike because the meeting started."

I already had the line. I went out into the mist.
