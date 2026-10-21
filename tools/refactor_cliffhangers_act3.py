#!/usr/bin/env python3
"""Refactor Episodes 08-12 for the Interleaved Cliffhanger & Handoff Model.
Ensures 100% preservation of all original narrative prose.
Ensures exact mirroring between portland-desk/ and docs/portland-desk/.
"""

from pathlib import Path
import shutil

ROOT = Path(r"C:\Users\charl\learning-narrative-kit")
PORTLAND = ROOT / "portland-desk"
DOCS = ROOT / "docs" / "portland-desk"

def refactor_ep08():
    n_file = PORTLAND / "narrative" / "08-prove-who-you-are.md"
    w_file = PORTLAND / "workbench" / "08-prove-who-you-are.md"
    
    n_text = n_file.read_text(encoding="utf-8")
    w_text = w_file.read_text(encoding="utf-8")
    
    split_target = 'She kept the app. She looked like someone who had hoped for a shorter answer.\n\n## Offboarding leftovers and the admin sticky'
    assert split_target in n_text, "EP08 split target not found"
    
    parts = n_text.split('She kept the app. She looked like someone who had hoped for a shorter answer.\n\n## Offboarding leftovers and the admin sticky')
    pre_cliffhanger = parts[0] + 'She kept the app. She looked like someone who had hoped for a shorter answer.'
    remainder_with_bridge = '## Offboarding leftovers and the admin sticky' + parts[1]
    
    # Strip the old bridge-card from remainder
    remainder_prose = remainder_with_bridge.split('```bridge-card')[0].strip()
    
    new_n_text = pre_cliffhanger + """\n\nJules looked across the divider. "Dev's account is locked out from a runaway script hammering the domain controller, Ken is insisting Password plus PIN is multifactor, and Nora has locked herself out with another seasonal password. You have ten minutes before the morning standup. Step up to the console and triage the queue."

## The Handoff Gate

```bridge-card
title: Portland Desk Lab: Identity, Authentication Factors, & Password Policy Triage
target: workbench/08-prove-who-you-are.md
domain: CompTIA Security+ SY0-701 • Domain 4.2 & 1.3
badge: The Hands-On Lab
cta: Take the Ticket & Open the Lab ->
---
Step onto Ethan's shift. Classify authentication factors to stop false MFA claims, inspect Active Directory Security Event Logs (Event ID 4625 and 4740) to locate the rogue caller device locking out accounts, guide users to NIST SP 800-63B passphrases, and complete the Tier 1 Identity Triage note.
```
"""

    epilogue_block = f"""

---

## 6. Shift Resolution Epilogue

```callout-panel
title: "FIGURE 8.2: IDENTITY BOUNDARIES & OFFBOARDING ENFORCEMENT"
badge: "Shift Epilogue"
caption: "Operations floor: At 05:35 PM, the identity queue clears. Ken's phone displays a verified authenticator token, Dev's script runs cleanly against the vault, and offboarding revokes the last orphaned credentials."
prompt: "Clean graphic novel cutaway panel of an IT support technician desk at late afternoon. Warm desk lamp light mixes with rainy window reflection. On the desk, an authenticator app shows a glowing security key verification symbol next to an Active Directory management console showing green status ticks. Ligne Claire style, sharp technical ink linework, no text, no words. 16:9 ratio."
```

With Dev's caller computer identified and silenced in Event Viewer, we cleared the lockout in Active Directory and watched the bad password counter stay at zero. Dev updated his test script to pull credentials directly from the secrets vault, and his stand-up deployment cleared cleanly.

Across the aisle, Ken was back at his desk, staring at his phone. "Sign in with company worked," he called over. "It bounced me through the push prompt, matched the two digits, and let me straight into the CRM. No SMS codes, no password plus PIN."

"Told you," I said. "Two distinct factor types. Identification is claiming who you are; authentication is proving it."

{remainder_prose}
"""
    new_w_text = w_text.strip() + epilogue_block

    n_file.write_text(new_n_text, encoding="utf-8")
    w_file.write_text(new_w_text, encoding="utf-8")
    print("Refactored Episode 08 successfully.")

def refactor_ep09():
    n_file = PORTLAND / "narrative" / "09-dont-click-that.md"
    w_file = PORTLAND / "workbench" / "09-dont-click-that.md"
    
    n_text = n_file.read_text(encoding="utf-8")
    w_text = w_file.read_text(encoding="utf-8")
    
    split_target = 'Dev put the phone face-down. "Deny if I did not ask. I already had that line once. Apparently I needed it twice."\n\n## Doors, shoulders, and the recycling bin'
    assert split_target in n_text, "EP09 split target not found"
    
    parts = n_text.split('Dev put the phone face-down. "Deny if I did not ask. I already had that line once. Apparently I needed it twice."\n\n## Doors, shoulders, and the recycling bin')
    pre_cliffhanger = parts[0] + 'Dev put the phone face-down. "Deny if I did not ask. I already had that line once. Apparently I needed it twice."'
    remainder_with_bridge = '## Doors, shoulders, and the recycling bin' + parts[1]
    
    remainder_prose = remainder_with_bridge.split('```bridge-card')[0].strip()
    
    new_n_text = pre_cliffhanger + """\n\nJules stepped over to my terminal. "We have a spoofed CFO email demanding a forty-eight-thousand-dollar wire change, Sam hovering over an archive attachment, and Dev's phone buzzing with credential stuffing MFA fatigue pushes. You have ten minutes before AP cuts the afternoon batch wire. Pull the raw RFC 5322 MIME headers, trace the originating IP, verify SPF, DKIM, and DMARC alignment, and get the quarantine hash to the mail gateway before money walks out the door."

## The Handoff Gate

```bridge-card
title: Portland Desk Lab: Email Header Decomposition & Phishing Triage
target: workbench/09-dont-click-that.md
domain: CompTIA Security+ SY0-701 • Domain 1.2 & 2.4
badge: The Hands-On Lab
cta: Take the Ticket & Open the Lab ->
---
Step onto Ethan's shift. Deconstruct raw RFC 5322 email headers, trace IP hops in `Received:` lines, verify SPF/DKIM/DMARC alignment against DNS TXT records, uncover typosquatted domains, and draft the Tier 1 Phishing Incident Triage & Security Escalation dossier before the wire transfer executes.
```
"""

    epilogue_block = f"""

---

## 6. Shift Resolution Epilogue

```callout-panel
title: "FIGURE 9.2: MAIL GATEWAY QUARANTINE & GATEWAY TELEMETRY"
badge: "Shift Epilogue"
caption: "Operations center: At 05:40 PM, the rain clears over the Willamette River. On the security monitor, the perimeter mail gateway displays zero accepted connections from the typosquatted domain as AP confirms the payment wire was frozen."
prompt: "Clean graphic novel cutaway panel of an IT support technician desk at twilight. Outside the window, city lights reflect on rain-slicked asphalt. On the monitor, a secure email gateway console displays green accepted logs and bold red quarantined lines. Clean ligne claire style, sharp technical ink linework, no text, no words. 16:9 ratio."
```

With the malicious header trace verified and the originating IP and typosquatted domain blocked at the perimeter gateway, AP confirmed that the fraudulent wire update had been cancelled. Maya Lin's real executive assistant confirmed the legitimate payroll routing was untouched, and Sam's double-extension zip dropper was safely purged from the mail spool.

Across the floor, the human layer kept moving.

{remainder_prose}
"""
    new_w_text = w_text.strip() + epilogue_block

    n_file.write_text(new_n_text, encoding="utf-8")
    w_file.write_text(new_w_text, encoding="utf-8")
    print("Refactored Episode 09 successfully.")

def refactor_ep10():
    n_file = PORTLAND / "narrative" / "10-something-on-the-box.md"
    w_file = PORTLAND / "workbench" / "10-something-on-the-box.md"
    
    n_text = n_file.read_text(encoding="utf-8")
    w_text = w_file.read_text(encoding="utf-8")
    
    split_target = 'She stayed on the slow spare printer for the rest of the day and was not polite about it. I wrote that in the ticket because politeness is not a restore code either.\n\n## Keyboards, roots, and the process that hides'
    assert split_target in n_text, "EP10 split target not found"
    
    parts = n_text.split('She stayed on the slow spare printer for the rest of the day and was not polite about it. I wrote that in the ticket because politeness is not a restore code either.\n\n## Keyboards, roots, and the process that hides')
    pre_cliffhanger = parts[0] + 'She stayed on the slow spare printer for the rest of the day and was not polite about it. I wrote that in the ticket because politeness is not a restore code either.'
    remainder_with_bridge = '## Keyboards, roots, and the process that hides' + parts[1]
    
    remainder_prose = remainder_with_bridge.split('```bridge-card')[0].strip()
    
    new_n_text = pre_cliffhanger + """\n\nJules turned from the ops bridge, her headset resting around her collar. "Ken's laptop is spinning fans at 100% executing encoded PowerShell payloads across warehouse shares, an unknown USB dropper sits on the scan bench, and Dana's endpoint is locked with a crypto-malware demand. If you let that PowerShell beacon run another thirty seconds, the entire warehouse VLAN is toast. Isolate the network endpoints, decode that Base64 payload, hunt down the persistence run keys in Autoruns, and log Event ID 7045 before lateral movement takes down the domain."

## The Handoff Gate

```bridge-card
title: Portland Desk Lab: Host Malware Triage, Persistence Mechanisms, & EDR Analysis
target: workbench/10-something-on-the-box.md
domain: CompTIA Security+ SY0-701 • Domain 2.1 & 4.1
badge: The Hands-On Lab
cta: Take the Ticket & Open the Lab ->
---
Take over Ethan's workstation. Decode obfuscated Base64 PowerShell scripts, inspect Sysinternals Autoruns and Windows Security logs for Event ID 7045 and registry persistence, isolate infected endpoints from the network, and submit the Tier 1 Host Infection Containment Dossier.
```
"""

    epilogue_block = f"""

---

## 6. Shift Resolution Epilogue

```callout-panel
title: "FIGURE 10.2: PERSISTENCE HUNT & HOST CONTAINMENT"
badge: "Shift Epilogue"
caption: "Operations bullpen: At 05:45 PM, the terminal fans spin down to a whisper. On Ethan's dual monitor setup, Sysinternals Autoruns shows the malicious Run key stripped, and Ken's laptop sits isolated on the quarantine bench awaiting a bare-metal reimage."
prompt: "Clean graphic novel cutaway panel of an IT support technician workbench in the late afternoon. An open laptop with its Ethernet cable unplugged sits on an anti-static mat next to a monitor displaying a process management console with clean status indicators. Ligne claire style, sharp technical ink linework, no text, no words. 16:9 ratio."
```

With Ken's laptop disconnected and the obfuscated PowerShell payload decoded, SOC pushed an enterprise rule blocking the C2 domain. We extracted the malicious scheduled task `CacheCleanup`, purged the persistence Run keys in Autoruns, and scheduled both endpoints for a clean bare-metal reimage. Dana's locked files were queued for an offline snapshot restore from the immutable backup vault.

Across the bullpen, the rest of the shift brought the quieter, deeper variants of persistence.

{remainder_prose}

Jules shut her laptop and stretched. "Tomorrow someone will bring a branded flash drive from a conference and swear it is just drivers."

"I will put it on the junk scan box," I said.

"Good," Jules said. "That box is lonely." I locked the drawer and went out to catch the MAX.
"""
    new_w_text = w_text.strip() + epilogue_block

    n_file.write_text(new_n_text, encoding="utf-8")
    w_file.write_text(new_w_text, encoding="utf-8")
    print("Refactored Episode 10 successfully.")

def refactor_ep11():
    n_file = PORTLAND / "narrative" / "11-the-air-is-shared.md"
    w_file = PORTLAND / "workbench" / "11-the-air-is-shared.md"
    
    n_text = n_file.read_text(encoding="utf-8")
    w_text = w_file.read_text(encoding="utf-8")
    
    split_target = 'Dev docked. The flapping stopped because copper does not care about deauth theater.\n\n## Guest Wi-Fi, segmentation, and the printer that should not see payroll'
    assert split_target in n_text, "EP11 split target not found"
    
    parts = n_text.split('Dev docked. The flapping stopped because copper does not care about deauth theater.\n\n## Guest Wi-Fi, segmentation, and the printer that should not see payroll')
    pre_cliffhanger = parts[0] + 'Dev docked. The flapping stopped because copper does not care about deauth theater.'
    remainder_with_bridge = '## Guest Wi-Fi, segmentation, and the printer that should not see payroll' + parts[1]
    
    remainder_prose = remainder_with_bridge.split('```bridge-card')[0].strip()
    
    new_n_text = pre_cliffhanger + """\n\nJules leaned over from the wireless management console. "We have a rogue consumer router bridging unknown devices straight onto the corporate data VLAN in conference room 3B, an active Evil Twin spoofing our SSID in the lobby, and deauthentication flood attacks kicking laptops off the air. If those barcode scanners in the warehouse lose connection or authenticate to the rogue, shipping stops. Grab the Wi-Fi analyzer, decode the 802.11 association frames, triangulate the rogue BSSID signal, and trace the physical switch port to shut down the rogue AP before the morning standup."

## The Handoff Gate

```bridge-card
title: Portland Desk Lab: Wireless Security, 802.1X Enterprise, & Rogue AP Triage
target: workbench/11-the-air-is-shared.md
domain: CompTIA Security+ SY0-701 • Domain 2.1 & 3.2
badge: The Hands-On Lab
cta: Take the Ticket & Open the Lab ->
---
Step onto Ethan's shift. Decode 802.11 association frames and RADIUS Access-Request packets, triangulate rogue BSSID signal strength (RSSI), locate the unauthorized switch port, and submit the Tier 1 Rogue AP Containment & Wireless Remediation note.
```
"""

    epilogue_block = f"""

---

## 6. Shift Resolution Epilogue

```callout-panel
title: "FIGURE 11.2: WIRELESS HEATMAP & ROGUE AP LOCALIZATION"
badge: "Shift Epilogue"
caption: "Operations floor: At 05:40 PM, the wireless controller console displays 100% green enterprise authentication. The rogue AP on port Gi1/0/14 has been administratively disabled, and lobby clients authenticate cleanly over 802.1X RADIUS."
prompt: "Clean graphic novel cutaway panel of an IT support technician reviewing a wireless heat map on a wall-mounted monitor in an operations office. The heat map shows clean green RF signal distributions across building zones, with an unauthorized red hotspot marked as deactivated. Crisp ligne claire style, sharp technical ink linework, no text, no words. 16:9 ratio."
```

With the rogue AP located under the conference credenza and its switch port administratively disabled in Cisco IOS, warehouse barcode scanners reassociated smoothly with the legitimate corporate radios. The deauthentication bursts targeting lobby clients subsided once the rogue BSSID was silenced, and Dev's laptop reconnected over authenticated 802.1X RADIUS.

Across the rest of the facility, wireless architecture and hygiene fell into place.

{remainder_prose}
"""
    new_w_text = w_text.strip() + epilogue_block

    n_file.write_text(new_n_text, encoding="utf-8")
    w_file.write_text(new_w_text, encoding="utf-8")
    print("Refactored Episode 11 successfully.")

def refactor_ep12():
    n_file = PORTLAND / "narrative" / "12-when-the-ticket-escalates.md"
    w_file = PORTLAND / "workbench" / "12-when-the-ticket-escalates.md"
    
    n_text = n_file.read_text(encoding="utf-8")
    w_text = w_file.read_text(encoding="utf-8")
    
    split_target = 'I almost said I had learned the phases. I did not. I had learned that my first useful move of the day was an undo.\n\n## After the rain'
    assert split_target in n_text, "EP12 split target not found"
    
    parts = n_text.split('I almost said I had learned the phases. I did not. I had learned that my first useful move of the day was an undo.\n\n## After the rain')
    pre_cliffhanger = parts[0] + 'I almost said I had learned the phases. I did not. I had learned that my first useful move of the day was an undo.'
    remainder_with_bridge = '## After the rain' + parts[1]
    
    remainder_prose = remainder_with_bridge.split('```bridge-card')[0].strip()
    
    new_n_text = pre_cliffhanger + """\n\nJules set a red binder and an anti-static evidence pouch onto my desk. "We have an active credential compromise, unauthorized cloud mailbox rule exfiltration, and a live compromised laptop sitting on the counter. If you reboot or shut it down, volatile RAM evidence evaporates. If you leave it connected, data leaks out. You have twenty minutes to execute the Order of Volatility, pull the live memory capture, compute the SHA-256 hash, establish chain of custody, and draft the formal CSIRT Escalation Dossier before the incident response team steps onto the floor."

## The Handoff Gate

```bridge-card
title: Portland Desk Lab: The Incident Escalation & SOC Handoff Crucible
target: workbench/12-when-the-ticket-escalates.md
domain: CompTIA Security+ SY0-701 • Domain 4.0 Incident Response & Operations
badge: Final Capstone Lab
cta: Take the Ticket & Open the Lab ->
---
Step onto Ethan's shift for the Book 0 Final Capstone: navigate multi-stage incident triage, execute Order of Volatility and cryptographic evidence hashing, master the 5-case CBYT prediction gate, and deliver the formal CSIRT Incident Handoff Dossier to Jules Mercer.
```
"""

    # In w_text, replace "## The Bridge to Book 1: The Step Beyond the Desk" with Section 6
    bridge_target = '## The Bridge to Book 1: The Step Beyond the Desk'
    assert bridge_target in w_text, "EP12 bridge target not found in workbench"
    
    pre_bridge = w_text.split(bridge_target)[0].strip()
    bridge_content = bridge_target + w_text.split(bridge_target)[1]
    
    epilogue_block = f"""

---

## 6. Shift Resolution Epilogue

```callout-panel
title: "FIGURE 12.2: CSIRT INCIDENT HANDOFF & THE BRIDGE TO BOOK 1"
badge: "Shift Epilogue"
caption: "Operations bullpen: At 05:45 PM, the autumn rain eases over the Willamette River. Jules Mercer hands Ethan a dark navy blue security badge opening the fifth-floor Security Operations Center bridge."
prompt: "Clean graphic novel cutaway panel of an IT support operations floor at twilight. Warm indoor desk light contrasts with blue twilight outside the floor-to-ceiling windows showing city bridges and river. A senior technician hands a new security access keycard lanyard to a junior technician across an open incident binder. Clean ligne claire style, sharp technical ink linework, no text, no words. 16:9 ratio."
```

{remainder_prose}

{bridge_content}
"""
    new_w_text = pre_bridge + epilogue_block

    n_file.write_text(new_n_text, encoding="utf-8")
    w_file.write_text(new_w_text, encoding="utf-8")
    print("Refactored Episode 12 successfully.")

def mirror_to_docs():
    for subdir in ["narrative", "workbench"]:
        src_dir = PORTLAND / subdir
        dst_dir = DOCS / subdir
        for f in src_dir.glob("*.md"):
            shutil.copy2(f, dst_dir / f.name)
    print("Mirrored all narrative and workbench files to docs/portland-desk/.")

if __name__ == "__main__":
    refactor_ep08()
    refactor_ep09()
    refactor_ep10()
    refactor_ep11()
    refactor_ep12()
    mirror_to_docs()
