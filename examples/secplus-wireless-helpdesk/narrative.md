# Portland Desk — The Air Is Shared

*A Security+ wireless precursor • Hover over highlighted terms for exam definitions and supporting desk jargon.*

Friday rain has decided to be mist, which Portland treats as optimism. I am Ethan, still week-something at the [[help_desk|help desk]], and today the queue is not malware on a stick — it is radios arguing about who is allowed to talk.

Jules has a sticky under *which decision?* that says *which SSID am I actually on?* Bike helmet on the monitor arm. She is not teaching RF theory. She is keeping people from joining a stranger's access point because the name looked familiar.

"The air is shared," she says when I reach for a blank card. "Wired has a cable you can point at. Wireless has manners and math. Your job is the manners — verify the network, prefer enterprise over café vibes, and escalate anything that looks like a twin."

I open the queue. Coffee. Portland doing Portland. First [[ticket|ticket]] subject: *Can't join CorpWifi — worked yesterday — board meeting in 20.*

## Maya and the password that is everyone

Maya from accounting is in the lobby with a loaner laptop and a face that blames the rain.

"It asks for a password," she says. "I type the one on the sticky under the monitor in Finance. Denied. Also there are two networks named almost the same. One has more bars."

I walk out with a phone running our approved [[wifi_analyzer|Wi-Fi analyzer]] view. Official [[ssid|SSID]] is `CORP-EMPLOYEE`. Beside it, `CORP-EMPLOYEE_Guest` and a suspicious `CORP-EMPLOYE` with the last letter missing and a [[signal_strength|signal strength]] that is louder near the street than near the AP closet.

"Lobby sticky password is the old [[psk|PSK]] world," I say. "Shared key. Everyone knows it, which means everyone and their cousin know it. We moved employees to [[enterprise_wpa|WPA-Enterprise]] — [[ieee_8021x|802.1X]] with your badge account against [[radius|RADIUS]]. No more hallway password. Join `CORP-EMPLOYEE`, use your user ID, trust the company [[certificate|certificate]] prompt we already documented — and do not join the loud almost-name."

Maya squints at the twin. "So the louder one is…?"

"Treat it as an [[evil_twin|evil twin]] until Network says otherwise," I say. "Same costume, wrong radio. Twin wants your password or your session. We open a [[ticket|ticket]] for wireless ops and you work from a dock until they kill it."

Jules appears long enough to add, "PSK is a potluck. Enterprise is a guest list."

## WEP, open air, and the portal that feels like security

Ken from sales calls from a hotel before a customer demo. He is proud of a workaround.

"Hotel Wi-Fi is open, then a webpage asks for the room number," he says. "That is basically login security, right? Also the customer site still has a dusty AP labeled WEP for 'the old scanner.' They told me to join it for the warehouse tour."

I put him on speaker so Jules can suffer with me.

"[[open_network|Open network]] means no encryption on the air," I say. "The [[captive_portal|captive portal]] is a gate for internet access, not a force field. Anyone on that same open SSID can try [[eavesdropping|wireless eavesdropping]] unless you wrap traffic in a [[vpn|VPN]]. Use the VPN before mail, before files, before 'just quick Slack.'"

"And WEP?" Ken asks.

"[[wep|WEP]] is a museum piece that still unlocks," Jules says. "Broken by [[iv_attack|IV attacks]] and boredom. If a scanner needs WEP, the scanner is the problem. Do not put your laptop there. Ask them for a wired drop or a modern SSID."

Ken mutters something about customer politics and connects the VPN on the hotel portal network like a person who wants to keep his job. Ticket note: portal ≠ encryption; WEP ≠ nostalgia, it is a finding.

## Rogue AP in the conference room

Mid-morning Facilities Slack: visitors cannot reach the projector, so someone from Marketing brought a travel router "like we do at home." It is plugged into a wall jack under the credenza. SSID: `FreeConfQuick`. Security: none. Helpfulness: maximum. Judgment: absent.

"That is a [[rogue_ap|rogue access point]]," I say when I get to the room. "Unauthorized [[access_point|access point]]. Even if the intent is kindness, it bridges unknown phones onto our wall jack without the [[controller|wireless controller]] policies. Unplug it. Soft voice. Hard unplug."

Rita blushes into her notebook. We unplug. Network confirms the jack is on a user VLAN that should never have been a free café. I file the ticket with photo, jack number, and "not malicious, still a rogue." Jules adds a sticky for the room: *travel routers are not conference A/V.*

While we are there, the analyzer shows our real APs plus a faint outside SSID that has been mapping the block for an hour — classic [[war_driving|war driving]] energy from a car with too many antennas. Not our emergency. Still a reminder that discovery is cheap.

## Disassociation, jamming, and the reconnect reflex

Afternoon: Dev from engineering — reimage graduate — pings that his laptop keeps dropping Wi-Fi every few minutes, then auto-joins whatever answers first. He is in the cafe seating near the lobby glass.

"I did not change anything," he says. "It just flaps. Then it asks for passwords it already knew."

Wireless ops has a note on the bridge: bursts of [[disassociation|disassociation / deauthentication]] frames aimed at lobby clients. Not full [[jamming|jamming]] — the air still works — but enough kicks to make laptops frantic. Frantic laptops are how evil twins collect friends.

"When you get kicked, do not reconnect on autopilot," I say. "Check the SSID character by character. Prefer the dock. If the air is being rude on purpose, escalate — that is a [[soc|SOC]] / wireless hunt, not a 'forget network' ritual."

Dev docks. The flapping stops because copper does not care about deauth theater. Jules writes under the sticky: *reconnect is a decision, not a reflex.*

## Guest Wi-Fi, segmentation, and the printer that should not see payroll

Nora needs a vendor on site to update a badge printer. Vendor wants Wi-Fi. Nora wants them productive. Finance wants them nowhere near file shares.

"[[guest_wifi|Guest Wi-Fi]]," I say. "Different SSID, [[captive_portal|captive portal]] for AUP, and — this is the part people skip — [[segmentation|network segmentation]] so guest cannot route to payroll, cameras, or the [[help_desk|help desk]] VLAN. Guest without segmentation is just hospitality for lateral movement."

We put the vendor on `CORP-GUEST`, watch them fail to ping an internal share (good), and succeed at the vendor's own update CDN (also good). Nora asks if we should hide the employee SSID so guests are less confused.

"[[hidden_ssid|Hidden SSID]] is obscurity cosplay," Jules says. "It still leaks in other frames. Real control is enterprise auth and segmentation — not pretend the network has no name."

Someone in the thread suggests MAC allow-lists for the printer VLAN. I type carefully: "[[mac_filtering|MAC filtering]] is a speed bump you can spoof with a screenshot. Do not build a security program out of burned-in addresses."

## WPA2, WPA3, WPS, and the survey that is not vibes

Network drops by the desk with a short hallway class because Friday allows it. They are rolling a pilot.

"Employees stay on [[wpa2|WPA2]]-Enterprise today," the engineer says. "Pilot floor gets [[wpa3|WPA3]]-Enterprise with [[sae|SAE]] for the personal SSID we still keep for a few IoT leftovers. SAE is why WPA3-PSK is less embarrassed about offline password guessing than WPA2-PSK. And turn [[wps|WPS]] off on anything that still admits it exists — convenience pairing with a brute-force hobby."

I ask about coverage complaints on the east cubes. They pull last week's [[site_survey|site survey]]: heat map, channel overlap, one AP transmitting like it is trying to cover the MAX stop.

"[[ap_placement|AP placement]] and power," the engineer says. "Too loud outside means easier eavesdropping and easier twins. Survey is how we know. Vibes are how we get tickets titled 'Wi-Fi bad.'"

I write it down like a person who will otherwise invent vibes at 4 p.m.

## Controllers, certificates, and the Monday meeting reflex

Before Bluetooth eats the last hour, I rewrite one more wiki line the desk will actually use. The [[controller|wireless controller]] is where SSID policy lives — encryption mode, guest splash, rogue detection flags — not in a sticky under someone's monitor. When a laptop fails enterprise join, we check whether the user clicked past a [[certificate|certificate]] warning, whether they are on the right [[ssid|SSID]], and whether a booster app installed a fake trust store. That triad catches more pain than channel trivia.

Jules makes me say it once for the queue: "If the meeting started, that is not permission to join the loud lookalike. Dock, hotspot from a known phone through VPN, or wait. Embarrassment is cheaper than a harvested password."

I put that sentence in the ticket template. Future-me will need it.

## Bluetooth in the cube farm

Late day, Lila's laptop keeps pairing prompts for a keyboard she does not own. Jordan found a cheap earbud spam message that says *Hi cute phone.* Sam wants to leave Bluetooth discovery on "so my watch feels loved."

"[[bluetooth|Bluetooth]] is a second air," I say. "Short range, real risk. Unsolicited messages are [[bluejacking|bluejacking]] — mostly rude. Actual data theft over weak pairing is [[bluesnarfing|bluesnarfing]]. Desk hygiene: [[bluetooth_pairing|pairing hygiene]] — only expected devices, confirm the code, discovery off when you are not actively pairing. Headphones are fine. Strangers in your stack are not."

Lila declines the ghost keyboard. Jordan laughs at bluejacking and then actually turns discovery off. Sam looks betrayed by his watch and complies anyway.

## Replay, certificates, and the line that sticks

End of day we close a stubborn laptop that keeps failing enterprise join. User installed a free "Wi-Fi booster" profile that pinned a wrong trust anchor. They were one impatient click from sending their password to a lookalike.

"Enterprise helps only if you protect the [[certificate|certificate]] check," I say. "If the client ignores trust, [[replay_attack|replay]] and twin games get easier. Clicking through certificate warnings on Wi-Fi is the same sin as clicking through them on banks."

I update the wiki blurb the desk actually reads: join the real SSID, prefer [[enterprise_wpa|802.1X]] over hallway PSK, VPN on open/portal networks, never WEP, unplug rogue travel routers, do not reconnect blind after weird drops, guest stays segmented, hide-SSID and MAC filters are not controls, WPS off, survey over vibes, and Bluetooth only for things you meant to invite.

5:40. Queue quieter. Mist still optimistic. I close notes: Maya on enterprise, Ken on VPN, Rita's rogue unplugged, Dev docked through deauth, vendor on guest with walls, pilot floor on WPA3 talk, Lila's ghost keyboard declined.

Jules clips her bike lights on. "How many radio acronyms did you memorize?"

"None," I say. "I collected a few decisions — which [[ssid|SSID]], PSK versus [[ieee_8021x|802.1X]], guest versus inside, dock versus panic-reconnect — and a few threat shapes — [[evil_twin|evil twin]], [[rogue_ap|rogue AP]], [[disassociation|disassociation]] — so the sticky stays true."

She almost smiles. "Good. Monday someone will join the loud lookalike because the meeting started. You already have the line."

I badge into the mist and walk toward the MAX. Portland is still raining, just politely. The cards in my drawer still think ports are the hard part. Today's decisions were about remembering the air belongs to everyone in range — including people who did not badge in.
