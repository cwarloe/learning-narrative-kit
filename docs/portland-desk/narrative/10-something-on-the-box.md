# Portland Desk — Something on the Box

*A Security+ malware precursor • Hover over highlighted terms for exam definitions and supporting desk jargon.*

A fierce October squall was rattling the fourth-floor casement windows when the red beacon on the dispatch board lit up. Jules didn't look up from her terminal, but her knuckles were white on her pen.

"Malware isn't a theory in a textbook, Ethan," Jules said, tracking an alert across the network operations dashboard. "Your job is containment: quarantine the dropper, isolate the host, and protect the shared drives. Do not hunt Latin names or argue with a ransom note while the box is actively beaconing across the subnet."

Finance still brought up the delayed wire run whenever the desk came up in a meeting. I had stopped flinching at it. I had not stopped thinking about it.

I clicked into the high-priority queue.

```ticket
id: HD-4419
priority: High
status: Open
queue: Help Desk
from: Maya (Accounting)
host: MAYA-W11
opened: Thu 07:41
subject: PC slow + random ads + please help before standup
```

## Maya and the toolbar that was not on the invoice

```callout-panel
title: "FIGURE 10.1: PROCESS TREE & PERSISTENCE MECHANISM"
badge: "Malware Analysis"
caption: "Technical UI diagram: Sysinternals Process Explorer view. Legitimate svchost processes run under services.exe, while counterfeit svch0st runs out of AppData with an active TCP port 4444 socket."
prompt: "Clean technical illustration of a computer monitor displaying a system process management tree under bright laboratory lighting. Process rows are neatly organized with one highlighted entry showing an anomalous socket connection. Clean line art, no text, no words. 16:9 ratio."
```

Maya from accounting was on the line sounding offended by her own browser. I remoted in with her permission while she narrated, which is how accounting people debug: out loud, in complete sentences, slightly betrayed.

"I installed a PDF merger from a download site," she said. "The merger works. Also now every new tab is a coupon carnival. I have a standup in twelve minutes and I look like I collect toolbars as a hobby."

The homepage was not ours. Three toolbars sat on a browser that had been clean yesterday. A helper wanted to "optimize" RAM, which is a sentence I have learned to distrust. The PDF tool itself was real enough; the bundle was the problem. I asked her to scroll the installer she still had in Downloads. The first checkbox, the one nobody reads, had been pre-ticked.

```gui
kind: browser
chrome: Edge — New tab
heading: Congratulations! Your PDF merger is ready
actions: Remove | Keep for now
---
New tabs open to coupons. Three toolbars. A helper named OptimizeRAM. The merger works. The rest of the machine is trying to sell her a vacation.
```

"You got bundled, Maya," I said. "The free PDF tool was real enough, but the installer snuck in an [[adware|adware]] engine and coupon toolbars—classic [[pups|PUPs]], potentially unwanted programs. Some of these bundles also drop [[spyware|spyware]] that tracks your browsing. It's essentially a [[trojan|trojan]] carrying a hidden [[payload|payload]]. We remove the bundle, reset the browser extensions, and run a full malware scan."

Maya winced. "So I got scammed by a checkbox."

"Next time: company software portal only," I told her. "If it's not on the portal, it's not a utility we support."

We stripped the junk while her standup Slack started to ping. [[antivirus|Antivirus]] quarantined one toolbar DLL on sight. A second helper only tripped after it started injecting ads.

**What the scanner actually said:**

| Detection | What it caught | How it knew |
| :--- | :--- | :--- |
| [[signature_detection|Signature]] | `couponbar.dll` — known bad hash | Name already in the catalog |
| [[heuristic|Heuristic]] | `OptimizeRAM.exe` injecting ads | Behavior, not a famous name yet |
| Clean (so far) | `PDFMerge.exe` | Signed, and it actually merges PDFs |

Maya still wanted to keep the merger. I told her the portal had a licensed one. She said she would look after standup. I left the merger off the machine and the ticket open until she actually used the portal copy, because "I'll look later" is how toolbars come back on Friday.

## Sam and the USB that walked in

Sam dropped a branded USB on the counter like a person returning a library book he knew was overdue.

"Client handed me the 'final deck,'" he said. "My laptop AV yelled before Explorer even finished thinking about it. I did not open it. I walked it here. I would like a sticker that says that."

Jules appeared as if summoned by plastic. "Say the vector out loud."

"Removable media," I said. "USB as delivery. Could be a [[virus|virus]] that infects files when you open them. Could be a [[dropper|dropper]] that writes a second stage. Could be nothing but a false positive. We do not find out by curiosity on a domain laptop, and we do not find out by plugging it into the machine that just yelled."

We scanned the stick on a designated junk machine that does not mount network shares. The junk box lives under the counter with a strip of tape that says `NO DOMAIN / NO SHARES / YES YOU WAIT`. Sam waited. The scan did not.

```console
caption: junk-scan · PowerShell
PS C:\junk-scan> Get-Volume -DriveLetter E | Format-List FileSystemLabel, Size
FileSystemLabel : CLIENT_DECK
Size            : 7733248

PS C:\junk-scan> Start-MpScan -ScanPath E:\ -ScanType Custom
E:\SOW_final.pdf.exe   Threat: Trojan:Win32/Dropper.B   Action: Quarantine
SHA256: 9f2c…c41a
```

Sam looked personally betrayed by a flash drive. "It said PDF on the sticker."

"The sticker is not a file extension," I said. "The catalog already knew this one. You did the right half — you did not open it. The other half is we keep it labeled and we do not take it back to your desk as a souvenir."

"Client will email a cloud link instead," he muttered. "I am putting this stick in a drawer labeled evidence, not homework."

## Worms, shares, and the machine that will not sit still

Mid-morning Ops Slack lit up in a way that is never about one person: three warehouse PCs showing the same odd scheduled task, same weird outbound DNS, same sudden interest in mapping drives. Not one user. A pattern.

Todd from sales called while I was still reading the thread. His fans were loud enough that I heard them through the handset.

"My laptop is scanning the building," he said. "Shares I do not recognize. I did not click anything today. I was copying a deck onto the warehouse share and then everything got interested in everything else."

I looked at the [[edr|EDR]] alert Jules forwarded. The process tree showed a script spawning copies of itself, then touching every writable share it could see. No new EXE name — just living tools doing unliving things.

```alert
product: EDR
severity: High
title: Share enumeration from a signed binary
host: TODD-SALES-14
user: todd.miller
process: powershell.exe
time: 10:17
---
Parent is a scheduled task created this morning. Child is a copy of the same script written to two more hosts. No new EXE. Living tools, unliving job.
```

```tree
caption: TODD-SALES-14 · process tree
powershell.exe  (signed, company cert)
  powershell.exe -nop -w hidden -enc JABzA...
    net.exe view /domain
    cmd.exe /c copy update.ps1 \\WH-PACK-02\share$
    schtasks.exe /create /tn "CacheCleanup"
```

"That spread pattern is [[worm|worm]] behavior," I said. "Self-replicating across the LAN. Even if the first foothold was a person, the second through twentieth do not need another click. Pull the cable — isolate the host. Do not finish the file copy first. Isolation is the desk move. Analysis is later, and it is not your analysis."

Todd unplugged his laptop. He still had a proposal deck mid-copy and he said so, twice, because the deck was for a client whose account was up for renewal. I told him the copy could wait and the client could bill us for being alive. I opened an escalate ticket for the SOC with hostnames, the scheduled-task name, and the outbound domains as light [[ioc|indicators of compromise]]. Jules, still on the Ops thread: "Good. Leave the shares dirty. We need them dirty."

## Ransomware at desk volume

Lunch was a rumor until it was a ticket, which is how rumors graduate.

Dana in facilities called with a voice that had decided to be calm on purpose. I have learned to trust that voice more than the all-caps ones.

"Every PDF on my desktop is `.locked`," she said. "Wallpaper says pay in crypto. I have not paid. I have not clicked Pay. I am looking at a notepad that wants to be my IT department, and I am calling you instead of my cousin."

I asked her to hold the phone toward the screen long enough to confirm it was the thing and not a joke macro from the warehouse.

```gui
kind: ransomware
chrome: NOTEPAD.EXE — README_RESTORE.txt
heading: Your files are encrypted
actions: Do not pay | Disconnect
---
Send Bitcoin to the address below within 72 hours. Open the chat if you want a 'test decrypt.' We are very professional.
```

"Ransomware," I said. "The encrypting engine is [[crypto_malware|crypto-malware]]. Desk order, out loud, so we both hear it: disconnect, isolate, do not run a decryptor from a forum, and do not pay. Payment is not a restore button. The chat in the notepad is not support. It is a second chance to talk to the person who already has your files."

Dana unplugged. Jules was already on the bridge with SOC. They asked about backups before they asked about anything theatrical. Dana's team folder had overnight snapshots that lived where her laptop could not write — offline / immutable backup territory, not the other folder on the same PC, which would have been encrypted too and would have made this a much worse Thursday.

| Move | What it does | What it costs |
| --- | --- | --- |
| Unplug / isolate | Stops the encryptor from seeing more shares | Dana's morning, and the label printer |
| Pay the notepad | Funds the next notepad | The files, probably, and the next victim |
| Restore from offline backup | Puts last night back | Today's work, and a watched week |

"Your line to users is isolate and escalate," Jules told me after she muted. "Not Bitcoin tutorials. If they ask when the files come back, the honest answer is after SOC and backups, not this afternoon."

Dana asked if she should try the attacker's support chat anyway, "just to see if the test file comes back." I said no. She asked when her files would be back. I said after SOC and backups, not this afternoon. She stayed on the slow spare printer for the rest of the day and was not polite about it. I wrote that in the ticket because politeness is not a restore code either.

Jules turned from the ops bridge, her headset resting around her collar. "Todd's laptop is spinning fans at 100% executing encoded PowerShell payloads across warehouse shares, an unknown USB dropper sits on the scan bench, and Dana's endpoint is locked with a crypto-malware demand. If you let that PowerShell beacon run another thirty seconds, the entire warehouse VLAN is toast. Isolate the network endpoints, decode that Base64 payload, hunt down the persistence run keys in Autoruns, and trace Event ID 7045 in the System log before lateral movement takes down the domain."

## Ken and the signature that checked out

Ken called from Gresham before ten. His logistics laptop had the same coupon-carnival browser as Maya's, and when I pulled the installer properties remotely, the dropper was digitally signed. The signature checked out. The publisher name was a real software company.

"It's signed," I told Jules. "Valid certificate, valid chain. That's why the AV let it through."

"Signed by whom?" she asked.

I looked again. The certificate was real, but the company had published a revocation notice for it four days earlier, after its signing key was stolen. My laptop's check had not pulled the revocation list yet. A valid signature had told me who held the key. It had not told me whether the right person was holding it. I had trusted it for about two minutes, which was long enough to tell Ken his laptop was probably fine.

## The Handoff Gate

```bridge-card
title: Portland Desk Lab: Host Malware Triage, Persistence Mechanisms, & EDR Analysis
target: workbench/10-something-on-the-box.md
domain: CompTIA Security+ SY0-701 • Domain 2.1 & 4.1
badge: The Hands-On Lab
cta: Take the Ticket & Open the Lab ->
---
Take over Ethan's workstation. Decode obfuscated Base64 PowerShell scripts, inspect Sysinternals Autoruns and Windows System logs for Event ID 7045 (or Security log Event ID 4697) and registry persistence, isolate infected endpoints from the network, and submit the Tier 1 Host Infection Containment Dossier.
```
