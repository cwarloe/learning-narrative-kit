"""Upgrades all remaining Portland Desk modules (00, 02-12) to the Interleaved Cliffhanger Model
with interactive lnk-terminal micro-simulations, clean technical cutaway panels, and plain English.
"""

import os
import re

EPISODE_DATA = {
    "00": {
        "panel_title": "FIGURE 0.1: THE MOTHERBOARD INSPECTION",
        "panel_badge": "Hardware Anatomy",
        "panel_caption": "Macro technical cutaway: A desktop motherboard on an ESD workbench mat. In the foreground, three cylindrical electrolytic capacitors: two are prominently swollen and domed with dried brown electrolyte residue leaking from the vent seams, beside one healthy flat capacitor. In the background, a dual-channel memory slot holding a green RAM stick with one broken retention latch.",
        "panel_prompt": "Clean technical cutaway illustration in Pacific Northwest instructional manual style, crisp uniform ink linework, bright even inspection lighting, clean ESD mat background, no heavy dark shadows. Macro technical inspection shot of a desktop PC motherboard interior: in sharp foreground focus are three cylindrical electrolytic capacitors on the green PCB. Two capacitors have prominently domed, bulging silver tops with cracked score lines and dried crusty brown electrolyte residue leaking from the seam. The third capacitor is completely flat and healthy for visual contrast. Directly behind them is a dual-channel memory slot holding a green RAM module with one white plastic retention latch broken off at an angle. Crisp fine ink linework, true component colors, clean unlabeled surfaces, no text, no letters, no words. 4:3 ratio.",
        "term_title": "CONSOLE: FIRST CONTACT DIAGNOSTIC TERMINAL",
        "term_shell": "cmd",
        "term_prompt": "C:\\> ",
        "term_objectives": [
            {"id": "obj-whoami", "label": "Identify current user context", "trigger": "whoami"},
            {"id": "obj-host", "label": "Verify machine hostname", "trigger": "hostname"},
            {"id": "obj-loopback", "label": "Test internal TCP/IP network stack", "trigger": "ping 127.0.0.1"},
            {"id": "obj-ip", "label": "Inspect active network adapter settings", "trigger": "ipconfig"}
        ],
        "term_commands": {
            "whoami": "desktop-workbench\\ethan",
            "hostname": "DESKTOP-STAGE01",
            "ping 127.0.0.1": "Pinging 127.0.0.1 with 32 bytes of data:\nReply from 127.0.0.1: bytes=32 time<1ms TTL=128\nReply from 127.0.0.1: bytes=32 time<1ms TTL=128\n\nPing statistics for 127.0.0.1:\n    Packets: Sent = 2, Received = 2, Lost = 0 (0% loss)\n[OK] Internal TCP/IP loopback stack is healthy.",
            "ipconfig": "Windows IP Configuration\n\nEthernet adapter Local Area Connection:\n   Connection-specific DNS Suffix  . : \n   Link-local IPv6 Address . . . . . : fe80::d50b:8134:2e9b:4a12%12\n   IPv4 Address. . . . . . . . . . . : 192.168.1.105\n   Subnet Mask . . . . . . . . . . . : 255.255.255.0\n   Default Gateway . . . . . . . . . : 192.168.1.1"
        }
    },
    "02": {
        "panel_title": "FIGURE 2.1: MOTHERBOARD MEMORY SLOT & BROKEN LATCH",
        "panel_badge": "Motherboard Inspection",
        "panel_caption": "Macro view: On the circuit board, a dual-digit red LED displays code C1. Directly adjacent, the DDR4 RAM slot has a broken white plastic retention latch tilted at 15 degrees, with the memory stick slightly unseated.",
        "panel_prompt": "Clean technical cutaway illustration of a computer motherboard RAM slot under bright, even inspection lighting. A dual-digit 7-segment red LED display reads C1. Beside it, the memory slot has its white plastic end-latch broken off and cocked at a 15-degree angle, with the gold contacts of the RAM module partially unseated. Sharp technical accuracy, no text, no words. 4:3 ratio.",
        "term_title": "POWERSHELL: EVENT VIEWER & STARTUP SERVICE TRIAGE",
        "term_shell": "powershell",
        "term_prompt": "PS C:\\Support> ",
        "term_objectives": [
            {"id": "obj-crash", "label": "Query Application crash logs (Event ID 1000)", "trigger": "Get-EventLog -LogName Application -InstanceId 1000"},
            {"id": "obj-services", "label": "List third-party background services", "trigger": "Get-Service | Where Status -eq Running"},
            {"id": "obj-disable", "label": "Disable crashing audio/display helper service", "trigger": "Stop-Service -Name NahimicService"}
        ],
        "term_commands": {
            "Get-EventLog -LogName Application -InstanceId 1000": "TimeGenerated       Source           EventID Message\n-------------       ------           ------- -------\n10/18 09:14:22 AM   Application Error   1000 Faulting application name: QuickBooks.exe, version: 23.0.4\n                                             Faulting module name: NahimicOSD.dll, version: 2.1.8\n                                             Exception code: 0xc0000005 (Access Violation)\n                                             Fault offset: 0x00012a4f\n                                             Faulting process id: 0x18a4",
            "Get-Service | Where Status -eq Running": "Status   Name               DisplayName\n------   ----               -----------\nRunning  Appinfo            Application Information\nRunning  AudioSrv           Windows Audio\nRunning  Dhcp               DHCP Client\nRunning  Dnscache           DNS Client\nRunning  NahimicService     Nahimic Audio Overlay Helper (Third-Party OSD)\nRunning  Spooler            Print Spooler\nRunning  WinDefend          Microsoft Defender Antivirus Service",
            "Stop-Service -Name NahimicService": "Service 'Nahimic Audio Overlay Helper' (NahimicService) stopped.\nSetting startup type to Disabled...\n[OK] Background injection hook removed. Payroll application launches cleanly."
        }
    },
    "03": {
        "panel_title": "FIGURE 3.1: RJ45 KEYSTONE JACK WITH BENT PIN 3",
        "panel_badge": "Physical Layer",
        "panel_caption": "Macro view looking directly into the open socket of an RJ45 modular jack. All 8 gold spring wire contacts are visible; pin 3 is flattened backward against the plastic slot wall, breaking physical link continuity.",
        "panel_prompt": "Macro technical illustration looking into the front opening of an RJ45 ethernet wall jack under bright inspection lighting. All 8 gold spring wire contacts visible; pin 3 is visibly flattened backward against the white plastic slot wall. Sharp metallic reflections on the gold pins, crisp instructional manual style, no text, no letters. 1:1 ratio.",
        "term_title": "COMMAND PROMPT: GATEWAY & IP CONFIGURATION TRIAGE",
        "term_shell": "cmd",
        "term_prompt": "C:\\Users\\Ethan> ",
        "term_objectives": [
            {"id": "obj-ip", "label": "Inspect adapter IP and default gateway", "trigger": "ipconfig"},
            {"id": "obj-ping-gw", "label": "Ping configured default gateway router", "trigger": "ping 192.168.10.1"},
            {"id": "obj-arp", "label": "Check local ARP cache for gateway MAC address", "trigger": "arp -a"},
            {"id": "obj-renew", "label": "Release and renew DHCP address lease", "trigger": "ipconfig /renew"}
        ],
        "term_commands": {
            "ipconfig": "Windows IP Configuration\n\nEthernet adapter vEthernet (Building B):\n   Connection-specific DNS Suffix  . : corp.local\n   IPv4 Address. . . . . . . . . . . : 169.254.88.192\n   Subnet Mask . . . . . . . . . . . : 255.255.0.0\n   Default Gateway . . . . . . . . . : \n   Note: Self-assigned APIPA address. DHCP Discover timed out.",
            "ping 192.168.10.1": "Pinging 192.168.10.1 with 32 bytes of data:\nDestination host unreachable.\nDestination host unreachable.\n\nPing statistics for 192.168.10.1:\n    Packets: Sent = 2, Received = 0, Lost = 2 (100% loss)",
            "arp -a": "Interface: 169.254.88.192 --- 0xa\n  Internet Address      Physical Address      Type\n  (No ARP entries found for default gateway. Local broadcast domain unreachable.)",
            "ipconfig /renew": "Renewing adapter configuration...\n\nWindows IP Configuration\nEthernet adapter vEthernet (Building B):\n   IPv4 Address. . . . . . . . . . . : 192.168.10.45\n   Subnet Mask . . . . . . . . . . . : 255.255.255.0\n   Default Gateway . . . . . . . . . : 192.168.10.1\n   DHCP Server . . . . . . . . . . . : 192.168.10.1\n[OK] Valid corporate IP leased. Gateway reachable."
        }
    },
    "04": {
        "panel_title": "FIGURE 4.1: SPLIT-HORIZON RESOLVER & HOSTS OVERRIDE",
        "panel_badge": "DNS Architecture",
        "panel_caption": "Schematic cutaway: The local DNS resolution path. When the resolver queries 127.0.0.1 and hosts file before recursive forwarders, a stale hardcoded IP sends traffic to a retired server.",
        "panel_prompt": "Clean technical cutaway diagram of a computer desktop screen displaying DNS resolution paths under bright, even lighting. Flowchart lines connect local hosts file to DNS resolver cache and recursive domain controllers. Clean instructional style, crisp fine lines, no text, no words. 16:9 ratio.",
        "term_title": "COMMAND PROMPT: DNS RESOLUTION & HOSTS FILE TRIAGE",
        "term_shell": "cmd",
        "term_prompt": "C:\\Support> ",
        "term_objectives": [
            {"id": "obj-nslookup", "label": "Query DNS for internal wiki portal", "trigger": "nslookup wiki.corp.local"},
            {"id": "obj-hosts", "label": "Inspect local static hosts file overrides", "trigger": "type C:\\Windows\\System32\\drivers\\etc\\hosts"},
            {"id": "obj-flush", "label": "Flush local resolver cache", "trigger": "ipconfig /flushdns"}
        ],
        "term_commands": {
            "nslookup wiki.corp.local": "Server:  UnKnown\nAddress:  192.168.1.1 (Home Wi-Fi Router)\n\n*** UnKnown can't find wiki.corp.local: Non-existent domain\nWarning: Client is querying local home router DNS instead of internal VPN DC (10.0.0.2).",
            "type C:\\Windows\\System32\\drivers\\etc\\hosts": "# Copyright (c) 1993-2009 Microsoft Corp.\n# Local static host overrides:\n127.0.0.1       localhost\n::1             localhost\n198.51.100.42   wiki.corp.local    # Stale contractor override from 2021!",
            "ipconfig /flushdns": "Windows IP Configuration\n\nSuccessfully flushed the DNS Resolver Cache.\nRe-querying over active VPN tunnel...\nName:    wiki.corp.local\nAddress: 10.0.0.85 (Internal Wiki DC)\n[OK] Internal portal accessible."
        }
    },
    "05": {
        "panel_title": "FIGURE 5.1: RS-232 TO RJ-45 CONSOLE PINOUT CROSSOVER",
        "panel_badge": "Serial Interface",
        "panel_caption": "Schematic wiring diagram: DB-9 female serial connector pinned to an RJ-45 rollover console cable. Pin 2 (RxD) and Pin 3 (TxD) cross over cleanly to pins 3 and 6 on the remote switch port.",
        "panel_prompt": "Clean technical wiring schematic of a DB-9 to RJ-45 console adapter under bright inspection lighting. Precision pinout lines connecting DB-9 pins 2, 3, and 5 to RJ45 modular jack. Clean neutral background, crisp fine ink linework, no heavy shadows, no text, no words. 16:9 ratio.",
        "term_title": "POWERSHELL: TCP SOCKET & LISTENING PORT DIAGNOSTICS",
        "term_shell": "powershell",
        "term_prompt": "PS C:\\Support> ",
        "term_objectives": [
            {"id": "obj-netstat", "label": "Inspect active listening TCP ports and PIDs", "trigger": "netstat -ano | findstr 8080"},
            {"id": "obj-testport", "label": "Test TCP handshake reachability on port 8080", "trigger": "Test-NetConnection -Port 8080"},
            {"id": "obj-process", "label": "Identify daemon process bound to socket", "trigger": "Get-Process -Id 3412"}
        ],
        "term_commands": {
            "netstat -ano | findstr 8080": "  Proto  Local Address          Foreign Address        State           PID\n  TCP    0.0.0.0:8080           0.0.0.0:0              LISTENING       3412\n  TCP    192.168.10.45:8080     192.168.10.112:51244   TIME_WAIT       0\n[OK] Port 8080 is actively LISTENING on PID 3412.",
            "Test-NetConnection -Port 8080": "ComputerName     : localhost\nRemoteAddress    : 127.0.0.1\nRemotePort       : 8080\nInterfaceAlias   : Loopback Pseudo-Interface 1\nSourceAddress    : 127.0.0.1\nTcpTestSucceeded : True\n[OK] TCP 3-way handshake (SYN -> SYN-ACK -> ACK) verified.",
            "Get-Process -Id 3412": "Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id ProcessName\n-------  ------    -----      -----     ------     -- -----------\n    412      18    42100      51200       2.14   3412 InventorySyncDaemon\nStatus: Process active. Port open and receiving frames."
        }
    },
    "06": {
        "panel_title": "FIGURE 6.1: SUB-BASEMENT FLOOD & PATCH TRENCH",
        "panel_badge": "Disaster Recovery",
        "panel_caption": "Wide panoramic cutaway: The flooded Building C sub-basement. Murky water reflects emergency lights; bundles of blue Cat6 cables drip water above a wall-mounted 48-port patch panel and edge switch stack.",
        "panel_prompt": "Clean technical cutaway illustration of a server room during a water leak under bright emergency lights. Bundles of blue network cables hang above a wall-mounted 48-port patch panel. A rackmount switch with glowing green port LEDs. Clean instructional drawing style, crisp fine lines, no text, no words. 21:9 ratio.",
        "term_title": "SWITCH CONSOLE: CISCO IOS VLAN TRUNK & PORT CONFIG",
        "term_shell": "serial",
        "term_prompt": "Switch-BldgC# ",
        "term_objectives": [
            {"id": "obj-vlan", "label": "Verify configured VLAN database", "trigger": "show vlan brief"},
            {"id": "obj-trunk", "label": "Inspect 802.1Q trunk link to distribution switch", "trigger": "show interfaces trunk"},
            {"id": "obj-mode", "label": "Set uplink interface to 802.1Q trunk mode", "trigger": "switchport mode trunk"}
        ],
        "term_commands": {
            "show vlan brief": "VLAN Name                             Status    Ports\n---- -------------------------------- --------- -------------------------------\n1    default                          active    Gi0/4 - Gi0/24\n10   Corp_Workstations                active    Gi0/1, Gi0/2\n20   Telemetry_Loggers                active    Gi0/3\n30   Voice_VoIP                       active    \n99   Management                       active    ",
            "show interfaces trunk": "Port        Mode             Encapsulation  Status        Native vlan\nGi0/24      on               802.1q         trunking      99\n\nPort        Vlans allowed on trunk\nGi0/24      1,10,20,30,99\n[OK] Trunk uplink passing all building VLAN traffic.",
            "switchport mode trunk": "Configuring Interface GigabitEthernet0/24...\nEncapsulation set to 802.1Q.\nUplink set to unconditional trunking.\n[OK] Port Gi0/24 forwarding all corporate VLANs. Line restored."
        }
    },
    "07": {
        "panel_title": "FIGURE 7.1: NETWORK PERIMETER & PORT SCAN VECTOR",
        "panel_badge": "Perimeter Architecture",
        "panel_caption": "Schematic layout: The corporate perimeter firewall. Cleartext Telnet (Port 23) and unencrypted HTTP (Port 80) bypass encrypted tunnels, exposing credentials on the wire.",
        "panel_prompt": "Clean technical schematic of a corporate network perimeter under bright, even lighting. Flowchart lines connect external internet router to internal firewall and server racks with port numbers highlighted in green and red. Crisp technical line art, no text, no words. 16:9 ratio.",
        "term_title": "CONSOLE: PERIMETER PORT SCAN & BANNER INSPECTION",
        "term_shell": "cmd",
        "term_prompt": "C:\\Security> ",
        "term_objectives": [
            {"id": "obj-nmap", "label": "Scan open service ports on warehouse server", "trigger": "nmap -sS -p 21,22,23,80,443 192.168.10.50"},
            {"id": "obj-banner", "label": "Test cleartext Telnet banner response", "trigger": "telnet 192.168.10.50 23"},
            {"id": "obj-ssh", "label": "Verify encrypted SSH connectivity on Port 22", "trigger": "ssh admin@192.168.10.50"}
        ],
        "term_commands": {
            "nmap -sS -p 21,22,23,80,443 192.168.10.50": "Starting Nmap scan on 192.168.10.50...\nPORT     STATE SERVICE\n21/tcp   OPEN  ftp (CLEAR TEXT)\n22/tcp   OPEN  ssh (OpenSSH 8.9p1)\n23/tcp   OPEN  telnet (CRITICAL: CLEARTEXT AUTH)\n80/tcp   OPEN  http\n443/tcp  OPEN  https\nWarning: Port 23 is transmitting passwords in unencrypted ASCII frames.",
            "telnet 192.168.10.50 23": "Connecting to 192.168.10.50...\nConnected to Toledo Scale Controller.\nEscape character is '^]'.\nWARNING: Cleartext session active. Passwords visible to any packet capture on switch.\nAction: Migrate to SSH (Port 22) immediately.",
            "ssh admin@192.168.10.50": "admin@192.168.10.50's password: \nLinux scale-controller-04 5.15.0-generic #42-Ubuntu SMP\nEncrypted session established with AES-256-GCM cipher.\n[OK] Port 23 disabled. Secure management active."
        }
    },
    "08": {
        "panel_title": "FIGURE 8.1: AUTHENTICATION FACTORS & ACCOUNT LOCKOUT",
        "panel_badge": "Identity & Access",
        "panel_caption": "Macro technical view: A corporate smartphone on a clean desk displaying rapid push notifications alongside an Active Directory security event log on a monitor.",
        "panel_prompt": "Clean technical illustration of a smartphone on an office desk next to a computer monitor under bright office lighting. The monitor displays security event logs with red warning highlights. Clean instructional manual style, crisp lines, no text, no words. 4:3 ratio.",
        "term_title": "POWERSHELL: ACTIVE DIRECTORY ACCOUNT LOCKOUT TRIAGE",
        "term_shell": "powershell",
        "term_prompt": "PS C:\\Support> ",
        "term_objectives": [
            {"id": "obj-lockout", "label": "Find account lockout events (Event ID 4740)", "trigger": "Get-WinEvent -FilterHashtable @{LogName='Security';Id=4740}"},
            {"id": "obj-unlock", "label": "Unlock Nora's domain account", "trigger": "Unlock-ADAccount -Identity nora.finance"},
            {"id": "obj-caller", "label": "Identify caller computer causing stale password lockouts", "trigger": "Get-ADUser -Identity nora.finance -Properties *"}
        ],
        "term_commands": {
            "Get-WinEvent -FilterHashtable @{LogName='Security';Id=4740}": "TimeCreated          Id RecordId ProcessId Message\n-----------          -- -------- --------- -------\n10/18 03:17:42 AM  4740   149204       620 A user account was locked out.\n                                            Target Account Name: nora.finance\n                                            Caller Computer Name: WKS-NORA-PHONE (Stale Exchange ActiveSync creds)",
            "Unlock-ADAccount -Identity nora.finance": "Unlocking Active Directory account 'nora.finance' on Domain Controller DC01...\nAccount unlocked successfully.\n[OK] Account status: ACTIVE (Password expired flag: FALSE).",
            "Get-ADUser -Identity nora.finance -Properties *": "DistinguishedName : CN=Nora Vance,OU=Finance,DC=corp,DC=local\nEnabled           : True\nLockedOut         : False\nbadPwdCount       : 0\nLastBadPasswordAttempt : 10/18 03:17:41 AM\nRoot Cause: Nora's company iPhone was sending old password over Wi-Fi after password change."
        }
    },
    "09": {
        "panel_title": "FIGURE 9.1: EMAIL MIME ARCHITECTURE & SPF CHECK",
        "panel_badge": "Email Authentication",
        "panel_caption": "Schematic diagram: Email envelope sender (MAIL FROM) versus message header (From:). Demonstrates how SPF verifies sending IP while DKIM cryptographically signs body hashes.",
        "panel_prompt": "Clean technical cutaway diagram of an email message header structure under bright lighting. Arrows connect sender IP address to DNS TXT record for SPF validation. Clean instructional manual style, crisp fine lines, no text, no words. 4:3 ratio.",
        "term_title": "CONSOLE: RAW MIME EMAIL HEADER & SPF/DKIM INSPECTION",
        "term_shell": "cmd",
        "term_prompt": "C:\\Incident> ",
        "term_objectives": [
            {"id": "obj-headers", "label": "Extract Received-SPF authentication result", "trigger": "findstr /i \"Received-SPF Authentication-Results\" invoice.eml"},
            {"id": "obj-origin", "label": "Extract originating sender IP from hop chain", "trigger": "findstr /i \"Received: from\" invoice.eml"},
            {"id": "obj-quarantine", "label": "Execute mail gateway rule to quarantine lookalike sender", "trigger": "quarantine-sender --domain port1and-ops.com"}
        ],
        "term_commands": {
            "findstr /i \"Received-SPF Authentication-Results\" invoice.eml": "Received-SPF: Fail (protection.outlook.com: domain of port1and-ops.com does not designate 198.51.100.77 as permitted sender)\nAuthentication-Results: spf=fail (sender IP is 198.51.100.77); dkim=none; dmarc=fail action=none header.from=port1and-ops.com\n[ALERT] SPF/DMARC hard failure. Sender domain is typosquatted (numeral 1 substituted for letter l).",
            "findstr /i \"Received: from\" invoice.eml": "Received: from mail-relay.suspicious-host.net (198.51.100.77)\nReceived: from client-smtp-relay (192.0.2.14)\nOriginating IP: 198.51.100.77 (Bucharest, Romania)\nTarget: nora.finance@portland-ops.gov\nSubject: URGENT: Wire Transfer Routing Change",
            "quarantine-sender --domain port1and-ops.com": "Rule created: Block and quarantine all incoming mail from '@port1and-ops.com'.\nMailbox purge executed: 1 malicious phishing message moved to Junk/Quarantine.\n[OK] Phishing threat contained before wire transfer executed."
        }
    },
    "10": {
        "panel_title": "FIGURE 10.1: PROCESS TREE & PERSISTENCE MECHANISM",
        "panel_badge": "Malware Analysis",
        "panel_caption": "Technical UI diagram: Sysinternals Process Explorer view. Legitimate svchost processes run under services.exe, while counterfeit svch0st runs out of AppData with an active TCP port 4444 socket.",
        "panel_prompt": "Clean technical illustration of a computer monitor displaying a system process management tree under bright laboratory lighting. Process rows are neatly organized with one highlighted entry showing an anomalous socket connection. Clean line art, no text, no words. 16:9 ratio.",
        "term_title": "POWERSHELL: HOST PROCESS & PERSISTENCE TRIAGE",
        "term_shell": "powershell",
        "term_prompt": "PS C:\\Incident> ",
        "term_objectives": [
            {"id": "obj-proc", "label": "Find high-CPU process running from temp directories", "trigger": "Get-Process | Where Path -like \"*AppData*\""},
            {"id": "obj-tcp", "label": "Inspect outbound socket connections for rogue process", "trigger": "Get-NetTCPConnection -OwningProcess 4812"},
            {"id": "obj-kill", "label": "Terminate malicious process and remove persistence key", "trigger": "Stop-Process -Id 4812 -Force"}
        ],
        "term_commands": {
            "Get-Process | Where Path -like \"*AppData*\"": "Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id ProcessName Path\n-------  ------    -----      -----     ------     -- ----------- ----\n    842      45    98200     112400     412.18   4812 svch0st     C:\\Users\\Ken\\AppData\\Local\\Temp\\svch0st.exe\n[CRITICAL] Rogue binary impersonating svchost running outside System32!",
            "Get-NetTCPConnection -OwningProcess 4812": "LocalAddress    LocalPort RemoteAddress   RemotePort State       OwningProcess\n------------    --------- -------------   ---------- -----       -------------\n192.168.10.74   49812     203.0.113.88    4444       ESTABLISHED 4812\nWarning: Outbound TCP reverse shell established to remote C2 IP 203.0.113.88:4444.",
            "Stop-Process -Id 4812 -Force": "Process 4812 (svch0st.exe) terminated.\nDeleting registry key: HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\WindowsUpdateSync\nHost isolated from network adapter.\n[OK] Active malware beacon neutralized."
        }
    },
    "11": {
        "panel_title": "FIGURE 11.1: 2.4 GHZ VS 5 GHZ SPECTRUM & ROGUE INTERFERENCE",
        "panel_badge": "RF Wireless Analysis",
        "panel_caption": "Radio frequency spectrum diagram: The three non-overlapping 2.4 GHz channels (1, 6, 11). Shows an unshielded microwave oven emitting wideband RF interference centered on Channel 6.",
        "panel_prompt": "Clean technical cutaway diagram of radio frequency spectrum channels under bright studio lighting. Bell curves represent Wi-Fi channels 1, 6, and 11 across the 2.4 GHz band, with interference spikes overlapping channel 6. Crisp technical line art, no text, no words. 16:9 ratio.",
        "term_title": "COMMAND PROMPT: WI-FI SPECTRUM & ROGUE BSSID SCAN",
        "term_shell": "cmd",
        "term_prompt": "C:\\Support> ",
        "term_objectives": [
            {"id": "obj-scan", "label": "Scan surrounding wireless BSSIDs and channels", "trigger": "netsh wlan show networks mode=bssid"},
            {"id": "obj-rogue", "label": "Identify rogue access point broadcasting on channel 6", "trigger": "netsh wlan show interfaces"}
        ],
        "term_commands": {
            "netsh wlan show networks mode=bssid": "SSID 1 : PortlandOps-Corp (Corporate 802.1X)\n    Authentication : WPA2-Enterprise\n    BSSID 1        : 00-1A-2B-3C-4D-01 (Channel 1, Signal 92%)\n    BSSID 2        : 00-1A-2B-3C-4D-02 (Channel 11, Signal 88%)\n\nSSID 2 : NETGEAR_WAREHOUSE_ANNEX (ROGUE ACCESS POINT)\n    Authentication : WPA2-Personal\n    BSSID 1        : 50-C7-BF-11-22-33 (Channel 6, Signal 98%)\n    Warning: Rogue consumer router operating on Channel 6 with active DHCP server!",
            "netsh wlan show interfaces": "There is 1 interface on the system:\n    Name                   : Wi-Fi\n    Description            : Intel(R) Wi-Fi 6 AX200 160MHz\n    State                  : connected\n    SSID                   : PortlandOps-Corp\n    Channel                : 6 (HIGH PACKET COLLISION FROM ROGUE AP)\n    Signal                 : 65%\nAction: Physically unplug rogue Netgear router in breakroom. Re-assign APs to channels 1, 6, 11."
        }
    },
    "12": {
        "panel_title": "FIGURE 12.1: INCIDENT COMMAND EVIDENCE & WRITE-BLOCKER",
        "panel_badge": "Incident Response",
        "panel_caption": "Forensic bench diagram: An extracted NVMe storage drive connected through a hardware write-blocker to the forensic acquisition laptop. Chain of custody tags and anti-static pouches in view.",
        "panel_prompt": "Clean technical illustration of a computer forensic examination bench under bright laboratory lighting. An external storage drive connects through a small rectangular hardware write-blocker with a glowing green LED to a laptop. Anti-static bags and clean tools on an ESD mat. Sharp technical linework, no text, no words. 16:9 ratio.",
        "term_title": "POWERSHELL: FORENSIC INTEGRITY & SHA-256 HASH VERIFICATION",
        "term_shell": "powershell",
        "term_prompt": "PS C:\\CSIRT> ",
        "term_objectives": [
            {"id": "obj-hash", "label": "Calculate SHA-256 hash of extracted evidence image", "trigger": "Get-FileHash -Algorithm SHA256 .\\evidence_disk0.dd"},
            {"id": "obj-verify", "label": "Verify forensic image hash matches chain of custody", "trigger": "Compare-Object -ReferenceObject $orig -DifferenceObject $new"}
        ],
        "term_commands": {
            "Get-FileHash -Algorithm SHA256 .\\evidence_disk0.dd": "Algorithm       Hash                                                             Path\n---------       ----                                                             ----\nSHA256          A3F8B4C92E1045D87E6B9C1045F2A83C4D5E6F7A8B9C0D1E2F3A4B5C6D7E8F9A .\\evidence_disk0.dd\n[OK] Bit-for-bit forensic image acquired through hardware write-blocker.",
            "Compare-Object -ReferenceObject $orig -DifferenceObject $new": "Hash comparison: MATCH (0 differences).\nChain of Custody verified: Evidence integrity intact.\nFormal handoff dossier packaged for Senior CSIRT Lead Jules Brooks.\n[OK] Incident handoff complete."
        }
    }
}

def upgrade_workbench(ep_id, data):
    wb_file = f"docs/portland-desk/workbench/{ep_id}-*.md"
    import glob
    matches = glob.glob(f"docs/portland-desk/workbench/{ep_id}-*.md")
    if not matches:
        return False
    path = matches[0]

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if lnk-terminal already present
    if "```lnk-terminal" in content:
        return False

    # Build lnk-terminal block
    term_block = f"""
### 2.3 Interactive Diagnostic Console: Live Telemetry & Triage

Use the interactive console below to test commands, inspect telemetry, and verify your troubleshooting steps.

```lnk-terminal
title: "{data['term_title']}"
shell: "{data['term_shell']}"
prompt: "{data['term_prompt']}"
replay: true
objectives:
"""
    for obj in data["term_objectives"]:
        term_block += f'  - id: "{obj["id"]}"\n    label: "{obj["label"]}"\n    trigger: "{obj["trigger"]}"\n'
    term_block += "---\n"
    for cmd, out in data["term_commands"].items():
        # Indent out lines by 2 spaces
        indented = "\n".join("  " + l for l in out.splitlines())
        term_block += f"{cmd}: |\n{indented}\n\n"
    term_block += "```\n\n---\n"

    # Insert before Quick Check 3
    if "### Quick Check 3:" in content:
        content = content.replace("### Quick Check 3:", term_block + "\n### Quick Check 3:")
    elif "## 3. Quick Checks" in content:
        content = content.replace("## 3. Quick Checks", term_block + "\n## 3. Quick Checks")

    # Insert callout-panel in Section 1 or 2 if not present
    if "```callout-panel" not in content:
        panel_block = f"""
```callout-panel
title: "{data['panel_title']}"
badge: "{data['panel_badge']}"
caption: "{data['panel_caption']}"
prompt: "{data['panel_prompt']}"
```
"""
        # Place after Section 1 header or near beginning
        if "## 1. The Situation & Ground Truth" in content:
            content = content.replace("## 1. The Situation & Ground Truth", "## 1. The Situation & Ground Truth\n" + panel_block)

    # Write back to both portland-desk and docs/portland-desk
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    doc_path = path.replace("portland-desk", "docs/portland-desk")
    with open(doc_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Upgraded workbench for Episode {ep_id}")
    return True

def upgrade_narrative(ep_id, data):
    import glob
    matches = glob.glob(f"docs/portland-desk/narrative/{ep_id}-*.md")
    if not matches:
        return False
    path = matches[0]

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Insert callout-panel if not present
    if "```callout-panel" not in content:
        panel_block = f"""
```callout-panel
title: "{data['panel_title']}"
badge: "{data['panel_badge']}"
caption: "{data['panel_caption']}"
prompt: "{data['panel_prompt']}"
```
"""
        # Insert after first section heading
        m = re.search(r'\n## [^\n]+\n', content)
        if m:
            pos = m.end()
            content = content[:pos] + panel_block + content[pos:]

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    doc_path = path.replace("portland-desk", "docs/portland-desk")
    with open(doc_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Upgraded narrative for Episode {ep_id}")
    return True

def main():
    for ep_id, data in EPISODE_DATA.items():
        upgrade_workbench(ep_id, data)
        upgrade_narrative(ep_id, data)
    print("Done upgrading all modules!")

if __name__ == '__main__':
    main()
