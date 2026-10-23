import os

os.chdir(r"C:\Users\charl\learning-narrative-kit")

def update_file(path, replacements):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
        elif old.replace("\n", "\r\n") in content:
            content = content.replace(old.replace("\n", "\r\n"), new.replace("\n", "\r\n"))
        elif old.replace("\r\n", "\n") in content:
            content = content.replace(old.replace("\r\n", "\n"), new.replace("\r\n", "\n"))
        else:
            print(f"WARNING: substring not found in {path}:\n  {old[:60]}...")
            
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print(f"Successfully processed {path}")

# ==============================================================================
# WORKBENCH 02: TERMINAL REALIGNMENT TO PDXPAY / AMDKMDAG.SYS
# ==============================================================================
wb02_old_terminal = """```lnk-terminal
title: "POWERSHELL: EVENT VIEWER & STARTUP SERVICE TRIAGE"
shell: "powershell"
prompt: "PS C:\\Support> "
replay: true
objectives:
  - id: "obj-crash"
    label: "Query Application crash logs (Event ID 1000)"
    trigger: "Get-EventLog -LogName Application -InstanceId 1000"
  - id: "obj-services"
    label: "List third-party background services"
    trigger: "Get-Service | Where Status -eq Running"
  - id: "obj-disable"
    label: "Disable crashing audio/display helper service"
    trigger: "Stop-Service -Name NahimicService"
---
Get-EventLog -LogName Application -InstanceId 1000: |
  TimeGenerated       Source           EventID Message
  -------------       ------           ------- -------
  10/18 09:14:22 AM   Application Error   1000 Faulting application name: QuickBooks.exe, version: 23.0.4
                                               Faulting module name: NahimicOSD.dll, version: 2.1.8
                                               Exception code: 0xc0000005 (Access Violation)
                                               Fault offset: 0x00012a4f
                                               Faulting process id: 0x18a4

Get-Service | Where Status -eq Running: |
  Status   Name               DisplayName
  ------   ----               -----------
  Running  Appinfo            Application Information
  Running  AudioSrv           Windows Audio
  Running  Dhcp               DHCP Client
  Running  Dnscache           DNS Client
  Running  NahimicService     Nahimic Audio Overlay Helper (Third-Party OSD)
  Running  Spooler            Print Spooler
  Running  WinDefend          Microsoft Defender Antivirus Service

Stop-Service -Name NahimicService: |
  Service 'Nahimic Audio Overlay Helper' (NahimicService) stopped.
  Setting startup type to Disabled...
  [OK] Background injection hook removed. Payroll application launches cleanly.

```"""

wb02_new_terminal = """```lnk-terminal
title: "POWERSHELL: EVENT VIEWER & GRAPHICS DRIVER TRIAGE"
shell: "powershell"
prompt: "PS C:\\Support> "
replay: true
objectives:
  - id: "obj-crash"
    label: "Query Application crash logs (Event ID 1000)"
    trigger: "Get-WinEvent -FilterHashtable @{LogName='Application'; ProviderName='Application Error'; Id=1000} -MaxEvents 1"
  - id: "obj-tdr"
    label: "Inspect graphics kernel driver TDR event in System log (Event ID 4101)"
    trigger: "Get-WinEvent -FilterHashtable @{LogName='System'; ProviderName='Display'; Id=4101} -MaxEvents 1"
  - id: "obj-accel"
    label: "Disable conflicting GPU hardware acceleration in PDX-Pay config"
    trigger: "Set-Content -Path 'C:\\Program Files\\PDX-Pay\\config.ini' -Value 'HardwareAcceleration=0'"
---
Get-WinEvent -FilterHashtable @{LogName='Application'; ProviderName='Application Error'; Id=1000} -MaxEvents 1: |
  TimeCreated          Id ProviderName        Message
  -----------          -- ------------        -------
  10/18 09:14:22 AM  1000 Application Error   Faulting application name: PDXPayClient.exe, version: 4.2.1
                                              Faulting module name: amdkmdag.sys, version: 23.20.11
                                              Exception code: 0xc0000005 (Access Violation in graphics pipeline)
                                              Faulting process id: 0x21a4

Get-WinEvent -FilterHashtable @{LogName='System'; ProviderName='Display'; Id=4101} -MaxEvents 1: |
  TimeCreated          Id ProviderName        Message
  -----------          -- ------------        -------
  10/18 09:14:23 AM  4101 Display             Display driver amdkmdag stopped responding and has successfully recovered.
                                              Timeout Detection and Recovery (TDR) event triggered during D3D11 device call.

Set-Content -Path 'C:\\Program Files\\PDX-Pay\\config.ini' -Value 'HardwareAcceleration=0': |
  [OK] Updated C:\\Program Files\\PDX-Pay\\config.ini: HardwareAcceleration disabled.
  Restarting PDXPayClient.exe in software rendering mode...
  Process started (PID 5128). Payroll ledger loaded successfully without display freeze.
  [PASS] Application stability restored.

```"""

# ==============================================================================
# WORKBENCH 08: TERMINAL OBJECTIVE ORDER & EVENT 4740 XML PARSING
# ==============================================================================
wb08_old_terminal = """```lnk-terminal
title: "POWERSHELL: ACTIVE DIRECTORY ACCOUNT LOCKOUT TRIAGE"
shell: "powershell"
prompt: "PS C:\\Support> "
replay: true
objectives:
  - id: "obj-lockout"
    label: "Find account lockout events (Event ID 4740)"
    trigger: "Get-WinEvent -FilterHashtable @{LogName='Security';Id=4740}"
  - id: "obj-unlock"
    label: "Unlock Nora's domain account"
    trigger: "Unlock-ADAccount -Identity nora.finance"
  - id: "obj-caller"
    label: "Identify caller computer causing stale password lockouts"
    trigger: "Get-ADUser -Identity nora.finance -Properties *"
---
Get-WinEvent -FilterHashtable @{LogName='Security';Id=4740}: |
  TimeCreated          Id RecordId ProcessId Message
  -----------          -- -------- --------- -------
  10/18 03:17:42 AM  4740   149204       620 A user account was locked out.
                                              Target Account Name: nora.finance
                                              Caller Computer Name: WKS-NORA-PHONE (Stale Exchange ActiveSync creds)

Unlock-ADAccount -Identity nora.finance: |
  Unlocking Active Directory account 'nora.finance' on Domain Controller DC01...
  Account unlocked successfully.
  [OK] Account status: ACTIVE (Password expired flag: FALSE).

Get-ADUser -Identity nora.finance -Properties *: |
  DistinguishedName : CN=Nora Vance,OU=Finance,DC=corp,DC=local
  Enabled           : True
  LockedOut         : False
  badPwdCount       : 0
  LastBadPasswordAttempt : 10/18 03:17:41 AM
  Root Cause: Nora's company iPhone was sending old password over Wi-Fi after password change.

```"""

wb08_new_terminal = """```lnk-terminal
title: "POWERSHELL: ACTIVE DIRECTORY ACCOUNT LOCKOUT TRIAGE"
shell: "powershell"
prompt: "PS C:\\Support> "
replay: true
objectives:
  - id: "obj-lockout"
    label: "Query Security log for lockout event 4740"
    trigger: "Get-WinEvent -FilterHashtable @{LogName='Security';Id=4740} -MaxEvents 1"
  - id: "obj-caller"
    label: "Extract CallerComputerName from Event 4740 XML"
    trigger: "(Get-WinEvent -FilterHashtable @{LogName='Security';Id=4740} -MaxEvents 1).ToXml()"
  - id: "obj-unlock"
    label: "Unlock Nora's domain account after isolating caller device"
    trigger: "Unlock-ADAccount -Identity nora.finance"
---
Get-WinEvent -FilterHashtable @{LogName='Security';Id=4740} -MaxEvents 1: |
  TimeCreated          Id RecordId ProcessId Message
  -----------          -- -------- --------- -------
  10/18 03:17:42 AM  4740   149204       620 A user account was locked out.
                                              Target Account Name: nora.finance
                                              Caller Computer Name: WKS-NORA-PHONE

(Get-WinEvent -FilterHashtable @{LogName='Security';Id=4740} -MaxEvents 1).ToXml(): |
  <Event xmlns='http://schemas.microsoft.com/win/2004/08/events/event'>
    <EventData>
      <Data Name='TargetUserName'>nora.finance</Data>
      <Data Name='TargetDomainName'>HARROWMERE</Data>
      <Data Name='CallerComputerName'>WKS-NORA-PHONE</Data>
    </EventData>
  </Event>
  [OK] Caller computer identified: WKS-NORA-PHONE (Nora's corporate mobile phone caching expired credentials).
  Action Taken: Nora toggled Airplane Mode ON to halt automated background ActiveSync attempts.

Unlock-ADAccount -Identity nora.finance: |
  Unlocking Active Directory account 'nora.finance' on Domain Controller DC01...
  Account unlocked successfully.
  [OK] Account status: ACTIVE (badPwdCount reset to 0).
  [PASS] Stale credentials isolated before account unlock. Lockout loop defused.

```"""

# ==============================================================================
# WORKBENCH 10: PROCESS VS REGISTRY PERSISTENCE SEPARATION
# ==============================================================================
wb10_old_terminal = """```lnk-terminal
title: "POWERSHELL: HOST PROCESS & PERSISTENCE TRIAGE"
shell: "powershell"
prompt: "PS C:\\Incident> "
replay: true
objectives:
  - id: "obj-proc"
    label: "Find high-CPU process running from temp directories"
    trigger: "Get-Process | Where Path -like \"*AppData*\""
  - id: "obj-tcp"
    label: "Inspect outbound socket connections for rogue process"
    trigger: "Get-NetTCPConnection -OwningProcess 4812"
  - id: "obj-kill"
    label: "Terminate malicious process and remove persistence key"
    trigger: "Stop-Process -Id 4812 -Force"
---
Get-Process | Where Path -like "*AppData*": |
  Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id ProcessName Path
  -------  ------    -----      -----     ------     -- ----------- ----
      842      45    98200     112400     412.18   4812 svch0st     C:\\Users\\todd.miller\\AppData\\Local\\Temp\\svch0st.exe
  [CRITICAL] Rogue binary impersonating svchost running outside System32!

Get-NetTCPConnection -OwningProcess 4812: |
  LocalAddress    LocalPort RemoteAddress   RemotePort State       OwningProcess
  ------------    --------- -------------   ---------- -----       -------------
  192.168.10.74   49812     203.0.113.88    4444       ESTABLISHED 4812
  Warning: Outbound TCP reverse shell established to remote C2 IP 203.0.113.88:4444.

Stop-Process -Id 4812 -Force: |
  Process 4812 (svch0st.exe) terminated.
  Deleting registry key: HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\WindowsUpdateSync
  Host isolated from network adapter.
  [OK] Active malware beacon neutralized.

```"""

wb10_new_terminal = """```lnk-terminal
title: "POWERSHELL: HOST PROCESS & PERSISTENCE TRIAGE"
shell: "powershell"
prompt: "PS C:\\Incident> "
replay: true
objectives:
  - id: "obj-proc"
    label: "Find high-CPU process running from temp directories"
    trigger: "Get-Process | Where Path -like \"*AppData*\""
  - id: "obj-tcp"
    label: "Inspect outbound socket connections for rogue process"
    trigger: "Get-NetTCPConnection -OwningProcess 4812"
  - id: "obj-kill"
    label: "Terminate malicious process executing in memory"
    trigger: "Stop-Process -Id 4812 -Force"
  - id: "obj-persist"
    label: "Purge persistence run key from Registry"
    trigger: "Remove-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Run' -Name 'WindowsUpdateSync'"
---
Get-Process | Where Path -like "*AppData*": |
  Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id ProcessName Path
  -------  ------    -----      -----     ------     -- ----------- ----
      842      45    98200     112400     412.18   4812 svch0st     C:\\Users\\todd.miller\\AppData\\Local\\Temp\\svch0st.exe
  [CRITICAL] Rogue binary impersonating svchost running outside System32!

Get-NetTCPConnection -OwningProcess 4812: |
  LocalAddress    LocalPort RemoteAddress   RemotePort State       OwningProcess
  ------------    --------- -------------   ---------- -----       -------------
  192.168.10.74   49812     203.0.113.88    4444       ESTABLISHED 4812
  Warning: Outbound TCP reverse shell established to remote C2 IP 203.0.113.88:4444.

Stop-Process -Id 4812 -Force: |
  Process 4812 (svch0st.exe) terminated in volatile memory.
  [WARNING] Process eliminated from RAM, but persistence mechanism remains on disk!

Remove-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Run' -Name 'WindowsUpdateSync': |
  [OK] Registry value 'WindowsUpdateSync' removed from HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Run.
  Persistence mechanism neutralized. Host isolated from network pending forensic acquisition.

```"""

# ==============================================================================
# WORKBENCH 11: TERMINAL OBJECTIVE 2 LABEL REFINEMENT
# ==============================================================================
wb11_old_terminal_label = """  - id: "obj-rogue"
    label: "Identify rogue access point broadcasting on channel 6"
    trigger: "netsh wlan show interfaces" """

wb11_new_terminal_label = """  - id: "obj-rogue"
    label: "Inspect active adapter channel collision and link quality"
    trigger: "netsh wlan show interfaces" """

# ==============================================================================
# WORKBENCH 12: POWERSHELL HASH COMPARISON & NIA ALVAREZ
# ==============================================================================
wb12_old_terminal = """objectives:
  - id: "obj-hash"
    label: "Calculate SHA-256 hash of extracted evidence image"
    trigger: "Get-FileHash -Algorithm SHA256 .\\evidence_disk0.dd"
  - id: "obj-verify"
    label: "Verify forensic image hash matches chain of custody"
    trigger: "Compare-Object -ReferenceObject $orig -DifferenceObject $new"
---
Get-FileHash -Algorithm SHA256 .\\evidence_disk0.dd: |
  Algorithm       Hash                                                             Path
  ---------       ----                                                             ----
  SHA256          A3F8B4C92E1045D87E6B9C1045F2A83C4D5E6F7A8B9C0D1E2F3A4B5C6D7E8F9A .\\evidence_disk0.dd
  [OK] Bit-for-bit forensic image acquired through hardware write-blocker.

Compare-Object -ReferenceObject $orig -DifferenceObject $new: |
  Hash comparison: MATCH (0 differences).
  Chain of Custody verified: Evidence integrity intact.
  Formal handoff dossier packaged for Senior CSIRT Lead Jules Brooks.
  [OK] Incident handoff complete."""

wb12_new_terminal = """objectives:
  - id: "obj-hash"
    label: "Calculate SHA-256 hash of extracted evidence image"
    trigger: "Get-FileHash -Algorithm SHA256 .\\evidence_disk0.dd"
  - id: "obj-verify"
    label: "Verify forensic image hash matches chain of custody"
    trigger: "(Get-FileHash .\\evidence_disk0.dd).Hash -eq $custodyHash"
---
Get-FileHash -Algorithm SHA256 .\\evidence_disk0.dd: |
  Algorithm       Hash                                                             Path
  ---------       ----                                                             ----
  SHA256          A3F8B4C92E1045D87E6B9C1045F2A83C4D5E6F7A8B9C0D1E2F3A4B5C6D7E8F9A .\\evidence_disk0.dd
  [OK] Bit-for-bit forensic image acquired through hardware write-blocker.

(Get-FileHash .\\evidence_disk0.dd).Hash -eq $custodyHash: |
  True
  [VERIFIED] Cryptographic hash matches original intake record exactly (0 differences).
  Chain of Custody verified: Evidence integrity intact.
  Formal handoff dossier packaged for Senior CSIRT Lead Nia Alvarez and Jules Brooks.
  [OK] Incident handoff complete."""

# ==============================================================================
# NARRATIVE 12: TIMELINE EXPANSION (22 MONTHS) & NIA ALVAREZ BRIDGE
# ==============================================================================
n12_replacements = [
    (
        "Eleven months on the service desk had taught me that the quietest tickets are often the ones carrying the sharpest edges.",
        "Twenty-two months on the service desk had taught me that the quietest tickets are often the ones carrying the sharpest edges."
    ),
    (
        "Eleven months ago, I would have reached straight into the drawer for the bootable USB.",
        "Twenty-two months ago, I would have reached straight into the drawer for the bootable USB."
    ),
    (
        'The Enterprise CSIRT and the incident commander will be on this floor in twenty minutes. When they walk through those double doors, they don\'t want guesses, they don\'t want apologies, and they don\'t want wiped hard drives."',
        'Senior CSIRT Lead Nia Alvarez and the incident command team from Chicago are bridging onto our operations floor in twenty minutes. When Nia joins this bridge, she doesn\'t want guesses, she doesn\'t want apologies, and she doesn\'t want wiped hard drives."'
    ),
    (
        "I looked down at the red binder. Eleven months ago, I was a twenty-year-old kid on the Gresham loading dock, clutching an eight-hundred-page textbook and terrified of failing a multiple-choice test in a Beaverton strip mall. \n\nToday, there were no multiple-choice questions. The municipal grid was on the line, and the desk had handed me the pen.",
        "I looked down at the red binder. Twenty-two months ago, I was an anxious nineteen-year-old kid on the Gresham loading dock, clutching an eight-hundred-page textbook and terrified of failing a multiple-choice test in a Beaverton strip mall. \n\nToday, there were no multiple-choice questions. The municipal grid was on the line, and Jules had handed me the incident pen to brief Nia Alvarez."
    ),
    (
        "deliver the formal CSIRT Escalation Dossier to Jules Brooks before the incident command team takes the floor.",
        "deliver the formal CSIRT Escalation Dossier to Senior CSIRT Lead Nia Alvarez and Jules Brooks before the incident command team takes the floor."
    ),
    (
        "deliver the formal CSIRT Incident Handoff Dossier to Jules Brooks.",
        "deliver the formal CSIRT Incident Handoff Dossier to Senior CSIRT Lead Nia Alvarez and Jules Brooks."
    )
]

for prefix in ["portland-desk/", "docs/portland-desk/"]:
    update_file(prefix + "workbench/02-the-live-board.md", [(wb02_old_terminal, wb02_new_terminal)])
    update_file(prefix + "workbench/08-prove-who-you-are.md", [(wb08_old_terminal, wb08_new_terminal)])
    update_file(prefix + "workbench/10-something-on-the-box.md", [(wb10_old_terminal, wb10_new_terminal)])
    update_file(prefix + "workbench/11-the-air-is-shared.md", [
        ("label: \"Identify rogue access point broadcasting on channel 6\"\n    trigger: \"netsh wlan show interfaces\"",
         "label: \"Inspect active adapter channel collision and link quality\"\n    trigger: \"netsh wlan show interfaces\"")
    ])
    update_file(prefix + "workbench/12-when-the-ticket-escalates.md", [(wb12_old_terminal, wb12_new_terminal)])
    update_file(prefix + "narrative/12-when-the-ticket-escalates.md", n12_replacements)

print("Sprint 2 updates applied successfully.")
