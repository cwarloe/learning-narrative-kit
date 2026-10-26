#!/usr/bin/env python3
"""generate_helpdesk_artifacts.py - Level 1 Support Telemetry & Ticket Generator.

Zero-dependency Python standard library script for the Portland Desk learning track.
Generates authentic Level 1 support datasets:
  1. Simulated Ticket Queue (JSON / CSV formatted for ServiceNow / Zendesk).
  2. Diagnostic Terminal Dumps (ipconfig /all, nslookup, netstat -ano, gpresult /r, route print).
  3. Windows Event Viewer Records (Normalized Event IDs 4624, 4625, 4740, 7045).
  4. Raw Email MIME Headers (.eml and parsed JSON with SPF/DKIM/DMARC headers for phishing triage).

Usage:
  python tools/generate_helpdesk_artifacts.py --generate
  python tools/generate_helpdesk_artifacts.py --verify
  python tools/generate_helpdesk_artifacts.py --generate --verify --out-dir archive/examples/secplus-ports-helpdesk/artifacts
"""

from __future__ import annotations

import argparse
import csv
import email
from email.message import EmailMessage
import json
import os
from pathlib import Path
import re
import sys
from typing import Any, Dict, List, Tuple


DEFAULT_OUT_DIR = Path("archive/examples/secplus-ports-helpdesk/artifacts")


# ==============================================================================
# 1. TICKET QUEUE DATA (Realistic Level 1 Help Desk)
# ==============================================================================

def get_simulated_tickets() -> List[Dict[str, Any]]:
    return [
        {
            "ticket_id": "INC0063140",
            "requester_name": "Jared Lindqvist",
            "requester_email": "jvance@portland-ops.local",
            "department": "Network Operations",
            "priority": "P3 - Medium",
            "urgency": "Medium",
            "impact": "Low",
            "status": "Resolved",
            "category": "Network Infrastructure",
            "subcategory": "Switch Configuration / Protocol",
            "subject": "Automation script failing against Building C closet switch (Port 23 connection refused)",
            "symptom_description": (
                "My automated configuration backup and VLAN push script failed when targeting the Building C "
                "edge switch (10.0.4.15). Script returned: 'ConnectionRefusedError: [Errno 111] Connection refused on port 23'. "
                "I wrote this script back when we racked gear in Hillsboro. Requesting temporary port 23 allow rule on "
                "management firewall so I can fix the trunk VLAN."
            ),
            "assigned_to": "Ethan Mercer",
            "assigned_group": "Tier 1 Service Desk",
            "created_at": "2026-10-20T08:45:12Z",
            "updated_at": "2026-10-20T09:14:02Z",
            "closed_at": "2026-10-20T09:14:02Z",
            "resolution_code": "Solved (Reconfigured / Hardened)",
            "resolution_notes": (
                "Advised requester that corporate security standard strictly prohibits cleartext Telnet (TCP 23) "
                "across management segments due to credential sniffing vulnerability (enable password exposure). "
                "Assisted requester in modifying the script to establish an encrypted SSH session on TCP 22 with "
                "Ed25519 public key authentication. Verified successful connection and VLAN remediation without opening port 23."
            ),
        },
        {
            "ticket_id": "INC0063141",
            "requester_name": "Maya Lin",
            "requester_email": "mlin@portland-ops.local",
            "department": "Accounting",
            "priority": "P2 - High",
            "urgency": "High",
            "impact": "Individual",
            "status": "Resolved",
            "category": "Email & Collaboration",
            "subcategory": "Mail Client Authentication",
            "subject": "Outlook mail synchronization failing over home and mobile Wi-Fi (Server timeout)",
            "symptom_description": (
                "Mail syncs fine when plugged into the docking station at the desk, but fails immediately on home Wi-Fi "
                "or coffee shop hotspots. Outlook displays alert: 'Receiving reported error (0x8004210A): The operation "
                "timed out waiting for a response from the receiving (POP) server.' Outgoing mail is also stuck in Outbox."
            ),
            "assigned_to": "Ethan Mercer",
            "assigned_group": "Tier 1 Service Desk",
            "created_at": "2026-10-20T09:02:45Z",
            "updated_at": "2026-10-20T09:35:10Z",
            "closed_at": "2026-10-20T09:35:10Z",
            "resolution_code": "Solved (Client Reconfigured)",
            "resolution_notes": (
                "Remote session into user workstation. Audited account settings: inbound was configured for cleartext "
                "legacy POP3 (port 110, unencrypted) and outbound was set to SMTP (port 25). Residential and public "
                "ISPs routinely drop outbound port 25 to mitigate spam bots, and port 110 transmits credentials in cleartext. "
                "Reconfigured account to modern encrypted standards: Inbound IMAPS on TCP 993 (SSL/TLS implicit), and "
                "Outbound authenticated Submission on TCP 587 (STARTTLS). Sent test message; confirmed bidirectional mail flow."
            ),
        },
        {
            "ticket_id": "INC0063142",
            "requester_name": "Dale Okafor",
            "requester_email": "dale.okafor@premier-facilities.vendor",
            "department": "Facilities Vendor",
            "priority": "P3 - Medium",
            "urgency": "Medium",
            "impact": "Department",
            "status": "Resolved",
            "category": "File Transfer & Storage",
            "subcategory": "Appliance Configuration Push",
            "subject": "Requesting inbound FTP (Port 21) access to drop Building A HVAC controller firmware backup",
            "symptom_description": (
                "Need to upload controller configuration snapshots and telemetry logs from our diagnostic field laptop "
                "to the internal facilities repository (192.168.10.85). Vendor installation manual specifies FTP on port 21. "
                "Connection attempts fail with connection timeout."
            ),
            "assigned_to": "Ethan Mercer",
            "assigned_group": "Tier 1 Service Desk",
            "created_at": "2026-10-20T09:40:18Z",
            "updated_at": "2026-10-20T10:15:33Z",
            "closed_at": "2026-10-20T10:15:33Z",
            "resolution_code": "Solved (Alternative Protocol)",
            "resolution_notes": (
                "Declined request to permit unencrypted FTP (TCP 21 / 20) through perimeter firewall, as FTP transmits "
                "passwords and configuration files in cleartext. Clarified technical difference between SFTP (SSH File "
                "Transfer Protocol, port 22) and FTPS (FTP over TLS, implicit port 990/989). Vendor appliance supports FTPS. "
                "Configured TLS listener on jump host and validated secure encrypted file upload."
            ),
        },
        {
            "ticket_id": "INC0063143",
            "requester_name": "Sam Kelly",
            "requester_email": "skelly.contractor@portland-ops.local",
            "department": "Finance (Contractor)",
            "priority": "P2 - High",
            "urgency": "High",
            "impact": "Individual",
            "status": "Resolved",
            "category": "Remote Access & Identity",
            "subcategory": "RDP Access Request",
            "subject": "Requesting public firewall rule for RDP (Port 3389) from hotel in Seattle",
            "symptom_description": (
                "Currently traveling in Seattle for the quarterly close. Need direct Remote Desktop access to my primary "
                "finance workstation (192.168.10.14). Please open TCP 3389 on the external IP for the next 72 hours so "
                "I can finish the audit deliverables from my hotel room."
            ),
            "assigned_to": "Ethan Mercer",
            "assigned_group": "Tier 1 Service Desk",
            "created_at": "2026-10-20T10:20:00Z",
            "updated_at": "2026-10-20T10:45:19Z",
            "closed_at": "2026-10-20T10:45:19Z",
            "resolution_code": "Solved (Compliant Architecture)",
            "resolution_notes": (
                "Explained security policy prohibiting raw RDP (TCP 3389) exposure to the public internet due to constant "
                "brute-force automated scanning and ransomware threat actor targeting. Provisioned contractor onto corporate "
                "VPN client pool with MFA verification. Provided destination address of dedicated jump host accessible "
                "only within VPN tunnel. Verified secure session establishment."
            ),
        },
        {
            "ticket_id": "INC0063144",
            "requester_name": "Lena Chen",
            "requester_email": "lchen@portland-ops.local",
            "department": "Legal",
            "priority": "P2 - High",
            "urgency": "High",
            "impact": "Individual",
            "status": "Resolved",
            "category": "Identity & Directory Services",
            "subcategory": "LDAP / Kerberos Authentication Failure",
            "subject": "Onboarding password reset utility failing from Guest Wi-Fi; Kerberos ticket rejection",
            "symptom_description": (
                "Sitting in the 1st floor lobby awaiting permanent desk assignment. Connected to Guest Wi-Fi. "
                "Self-service password registration utility fails with 'Cannot contact directory server (LDAP error 81)'. "
                "After reconnecting to corporate dock, domain logon reports 'Kerberos pre-authentication failed: "
                "Clock skew too great'."
            ),
            "assigned_to": "Ethan Mercer",
            "assigned_group": "Tier 1 Service Desk",
            "created_at": "2026-10-20T11:05:22Z",
            "updated_at": "2026-10-20T11:42:01Z",
            "closed_at": "2026-10-20T11:42:01Z",
            "resolution_code": "Solved (Service Hardened)",
            "resolution_notes": (
                "Diagnosed two underlying issues: 1) Password reset tool was attempting cleartext LDAP (TCP 389) across "
                "untrusted guest wireless. Reconfigured client endpoint to use secure LDAPS on TCP 636 with corporate root CA. "
                "2) Client system clock had drifted 14 minutes behind domain controllers, violating Kerberos 5-minute maximum "
                "skew tolerance. Triggered resync via NTP (UDP 123) against internal time server (w32tm /resync). "
                "Kerberos ticket granting succeeded immediately."
            ),
        },
        {
            "ticket_id": "INC0063145",
            "requester_name": "Dee Washington",
            "requester_email": "dwashington@portland-ops.local",
            "department": "Network Operations",
            "priority": "P3 - Medium",
            "urgency": "Low",
            "impact": "Department",
            "status": "Resolved",
            "category": "Network Monitoring",
            "subcategory": "SNMP Polling Security",
            "subject": "Network monitoring collector polling switches with community string 'public'",
            "symptom_description": (
                "Internal audit flagged that newly deployed access switches in Building B are answering SNMP GET requests "
                "on UDP 161 using default community string 'public'. Need review of monitoring template before weekly change window."
            ),
            "assigned_to": "Ethan Mercer",
            "assigned_group": "Tier 1 Service Desk",
            "created_at": "2026-10-20T11:50:00Z",
            "updated_at": "2026-10-20T12:20:15Z",
            "closed_at": "2026-10-20T12:20:15Z",
            "resolution_code": "Solved (Config Hardened)",
            "resolution_notes": (
                "SNMP v1 and v2c send community strings across the wire in cleartext plaintext. Migrated network polling "
                "configuration to SNMPv3 utilizing SHA-256 for authentication (auth) and AES-128 for payload privacy/encryption (priv). "
                "Disabled legacy community string 'public' across all managed interfaces."
            ),
        },
        {
            "ticket_id": "INC0063146",
            "requester_name": "Marco Reyes",
            "requester_email": "mreyes@portland-ops.local",
            "department": "Field Engineering",
            "priority": "P3 - Medium",
            "urgency": "Low",
            "impact": "Low",
            "status": "Resolved",
            "category": "Logging & Auditing",
            "subcategory": "Syslog Ingestion",
            "subject": "Request to permit UDP 514 syslog traffic from guest wireless subnet to central SIEM collector",
            "symptom_description": (
                "Working on staging laptops from the guest conference area. Wanted to forward debugging logs to the "
                "collector at 192.168.10.60 on UDP 514 without walking back upstairs to plug into the bench rack."
            ),
            "assigned_to": "Ethan Mercer",
            "assigned_group": "Tier 1 Service Desk",
            "created_at": "2026-10-20T13:10:40Z",
            "updated_at": "2026-10-20T13:35:00Z",
            "closed_at": "2026-10-20T13:35:00Z",
            "resolution_code": "Solved (Redirected to Secure Endpoint)",
            "resolution_notes": (
                "Denied request to route cleartext UDP 514 across guest boundary. Directed technician to forward "
                "log events via Syslog-over-TLS (TCP 6514) with mutual certificate verification, ensuring tamper-proof "
                "confidentiality for diagnostic output."
            ),
        },
        {
            "ticket_id": "INC0063147",
            "requester_name": "Owen Castillo",
            "requester_email": "ocastillo@portland-ops.local",
            "department": "Facilities Maintenance",
            "priority": "P3 - Medium",
            "urgency": "High",
            "impact": "Workgroup",
            "status": "Resolved",
            "category": "Hardware / Endpoint",
            "subcategory": "Printer Firmware Recovery",
            "subject": "High-volume badge printer in Lobby unresponsive; requires emergency TFTP firmware flash",
            "symptom_description": (
                "The badge and visitor pass printer in Main Reception froze during an interrupted auto-update. "
                "Recovery mode requires sending binary ROM over TFTP (UDP 69). Requested opening UDP 69 from technician "
                "laptop on standard user VLAN."
            ),
            "assigned_to": "Ethan Mercer",
            "assigned_group": "Tier 1 Service Desk",
            "created_at": "2026-10-20T14:15:11Z",
            "updated_at": "2026-10-20T14:48:30Z",
            "closed_at": "2026-10-20T14:48:30Z",
            "resolution_code": "Solved (Isolated Staging)",
            "resolution_notes": (
                "TFTP lacks any authentication or encryption mechanisms and is vulnerable to directory traversal and packet spoofing. "
                "Refused to broadcast TFTP across corporate workstation VLAN. Moved technician laptop and printer to isolated "
                "staging switch on air-gapped maintenance VLAN. Completed firmware upload on UDP 69; closed port immediately."
            ),
        },
        {
            "ticket_id": "INC0063148",
            "requester_name": "Leah Moreno",
            "requester_email": "lmoreno@portland-ops.local",
            "department": "Portland Plant Operations",
            "priority": "P2 - High",
            "urgency": "High",
            "impact": "Operational Facility",
            "status": "In Progress",
            "category": "Operational Technology / SCADA",
            "subcategory": "Industrial Telemetry Stream Security",
            "subject": "Plant operations water pump and valve controller telemetry stream connection timeout",
            "symptom_description": (
                "Telemetry telemetry gateway in Building 4 (East Treatment Line) failed to stream sensor metrics to "
                "central plant ops console. Field technician attempted to route unencrypted Modbus/TCP (port 502) and "
                "cleartext DNP3 (port 20000) over the inter-site WAN link. Traffic is currently blocked by edge boundary ACLs. "
                "Plant ops requires continuous pressure and flow monitoring to prevent overflow alarms."
            ),
            "assigned_to": "Ethan Mercer",
            "assigned_group": "Tier 1 Service Desk",
            "created_at": "2026-10-20T14:55:00Z",
            "updated_at": "2026-10-20T15:25:12Z",
            "closed_at": "",
            "resolution_code": "",
            "resolution_notes": (
                "Triage with Leah Moreno (Portland plant operations lead): Industrial control protocols (Modbus 502, DNP3 20000) "
                "have zero native encryption or authentication. Permitting raw cleartext telemetry over WAN exposes critical plant "
                "actuators to unauthorized command injection. Coordinating with Tier 2 Network Security to encapsulate telemetry "
                "into an IPsec ESP tunnel terminated at the plant SCADA boundary firewall. Work in progress."
            ),
        },
        {
            "ticket_id": "INC0063149",
            "requester_name": "Carlos Gomez",
            "requester_email": "cgomez@portland-ops.local",
            "department": "Warehouse / Shipping",
            "priority": "P2 - High",
            "urgency": "High",
            "impact": "Workgroup",
            "status": "Resolved",
            "category": "Hardware & Printing",
            "subcategory": "Print Spooler Service Failure",
            "subject": "Shipping dock thermal barcode printers unresponsive; Print Spooler service stopped",
            "symptom_description": (
                "All shipping label printers across loading bays 1 through 4 went offline simultaneously at 14:30. "
                "Shipping staff cannot generate packing slips or bill of lading manifests. Windows error on print server: "
                "'The Print Spooler service terminated unexpectedly. Error code 0x800706BA (The RPC server is unavailable)'."
            ),
            "assigned_to": "Ethan Mercer",
            "assigned_group": "Tier 1 Service Desk",
            "created_at": "2026-10-20T15:30:22Z",
            "updated_at": "2026-10-20T15:58:45Z",
            "closed_at": "2026-10-20T15:58:45Z",
            "resolution_code": "Solved (Service Restored / Corrupt Spool Purged)",
            "resolution_notes": (
                "Remoted into print server (PORT-PRN-01). Identified corrupt print job in C:\\Windows\\System32\\spool\\PRINTERS "
                "causing spoolsv.exe crash upon RPC (TCP 135) binding. Stopped Print Spooler, purged corrupted .SHD and .SPL files, "
                "restarted service, and verified TCP 445 (SMB) and 135 (RPC) listeners active. Successfully released shipping queue."
            ),
        },
        {
            "ticket_id": "INC0063150",
            "requester_name": "Rachel Adams",
            "requester_email": "radams@portland-ops.local",
            "department": "Executive Office",
            "priority": "P1 - Critical",
            "urgency": "High",
            "impact": "Executive",
            "status": "Resolved",
            "category": "Endpoint Security",
            "subcategory": "BitLocker Recovery",
            "subject": "Executive laptop locked at startup: 'Enter the recovery key for this drive'",
            "symptom_description": (
                "Turned on Dell Latitude laptop after rebooting for an automated Dell Command Update / BIOS firmware flash. "
                "Screen is bright blue demanding a 48-digit BitLocker recovery key. Executive has a board presentation in 30 minutes."
            ),
            "assigned_to": "Ethan Mercer",
            "assigned_group": "Tier 1 Service Desk",
            "created_at": "2026-10-20T16:02:10Z",
            "updated_at": "2026-10-20T16:21:40Z",
            "closed_at": "2026-10-20T16:21:40Z",
            "resolution_code": "Solved (Identity Verified & Key Released)",
            "resolution_notes": (
                "Conducted mandatory out-of-band identity verification via voice callback to department manager. "
                "Accessed Microsoft Entra / Active Directory administrative portal. Located computer object PORT-NB-0482. "
                "Retrieved 48-digit BitLocker recovery key matching Key ID 7B4F-29E1. Read key to user; drive unlocked successfully. "
                "Instructed user to suspend BitLocker prior to executing subsequent UEFI/TPM firmware updates."
            ),
        },
        {
            "ticket_id": "INC0063151",
            "requester_name": "David Kim",
            "requester_email": "dkim@portland-ops.local",
            "department": "Marketing",
            "priority": "P2 - High",
            "urgency": "High",
            "impact": "Individual",
            "status": "Resolved",
            "category": "Identity & Access",
            "subcategory": "Account Lockout Loop",
            "subject": "Active Directory account locking out repeatedly every 5 minutes",
            "symptom_description": (
                "Password was changed yesterday morning. Today, account is locking out continuously every 5 to 10 minutes, "
                "even when not touching the workstation keyboard. Self-service unlock succeeds and then locks out again."
            ),
            "assigned_to": "Ethan Mercer",
            "assigned_group": "Tier 1 Service Desk",
            "created_at": "2026-10-20T16:30:00Z",
            "updated_at": "2026-10-20T16:55:12Z",
            "closed_at": "2026-10-20T16:55:12Z",
            "resolution_code": "Solved (Stale Credential Purged)",
            "resolution_notes": (
                "Inspected Domain Controller Security log for Event ID 4740 (Account Lockout). Filtered by user 'dkim'. "
                "Event 4740 identified Caller Computer Name as 'IPAD-DKIM-04'. Contacted user; discovered personal iPad "
                "connected to guest Wi-Fi was still attempting Exchange ActiveSync authentication with expired password, "
                "rapidly hitting the 5-attempt bad password threshold. Updated password in iPad Settings; lockout cleared."
            ),
        },
        {
            "ticket_id": "INC0063152",
            "requester_name": "Sarah Jenkins",
            "requester_email": "sjenkins@portland-ops.local",
            "department": "Lobby Reception",
            "priority": "P1 - Critical",
            "urgency": "High",
            "impact": "Facility Network",
            "status": "Escalated",
            "category": "Wireless & Network Security",
            "subcategory": "Rogue Access Point Detection",
            "subject": "Unrecognized high-signal Wi-Fi network 'Portland_Guest_Fast' broadcasting near Conference Room B",
            "symptom_description": (
                "Visitors reported seeing a strong unencrypted SSID named 'Portland_Guest_Fast' in the lobby. "
                "IT wireless map does not show any access points registered with this SSID in the reception area. "
                "Physical inspection revealed a small black travel router plugged into a conference room RJ-45 wall jack."
            ),
            "assigned_to": "Ethan Mercer",
            "assigned_group": "Tier 1 Service Desk",
            "created_at": "2026-10-20T17:01:05Z",
            "updated_at": "2026-10-20T17:18:22Z",
            "closed_at": "",
            "resolution_code": "",
            "resolution_notes": (
                "Confirmed active rogue access point bridging external wireless devices directly into corporate internal "
                "VLAN 10. Immediately unplugged hardware device and confiscated for analysis. Disabled switch port "
                "(Fa0/18) on Closet 1A switch. Escalated incident to SOC and physical security for vendor/contractor audit."
            ),
        },
        {
            "ticket_id": "INC0063153",
            "requester_name": "Tom Bradley",
            "requester_email": "tbradley@portland-ops.local",
            "department": "Procurement",
            "priority": "P2 - High",
            "urgency": "High",
            "impact": "Endpoint Threat",
            "status": "Escalated",
            "category": "Email Security & Phishing",
            "subcategory": "Malicious Attachment Triage",
            "subject": "Suspicious urgent vendor invoice email with disc image attachment (.iso)",
            "symptom_description": (
                "Received email claiming our enterprise enterprise account is 90 days overdue. Sender name says 'Supplier Billing', "
                "but email address is 'billing@vendor-invoicing.net'. Email contains attachment named 'INV_Oct2026_9942.pdf.iso'. "
                "User has not opened the attachment."
            ),
            "assigned_to": "Ethan Mercer",
            "assigned_group": "Tier 1 Service Desk",
            "created_at": "2026-10-20T17:22:40Z",
            "updated_at": "2026-10-20T17:35:10Z",
            "closed_at": "",
            "resolution_code": "",
            "resolution_notes": (
                "Extracted raw message headers. Inspected SPF, DKIM, DMARC: SPF failed (origin IP from overseas VPS), "
                "DKIM invalid, DMARC policy=none. Attachment extension uses double camouflage (.pdf.iso) to bypass "
                "standard document filters and mount a malicious executable payload upon click. Isolated workstation, "
                "purged message across mailboxes, and forwarded sample to SOC incident response."
            ),
        },
    ]


# ==============================================================================
# 2. DIAGNOSTIC TERMINAL DUMPS (Authentic System Output)
# ==============================================================================

def get_terminal_dumps() -> Dict[str, str]:
    dumps: Dict[str, str] = {}

    # ipconfig /all
    dumps["ipconfig_all.txt"] = """Windows IP Configuration

   Host Name . . . . . . . . . . . . : PORT-WS-1042
   Primary Dns Suffix  . . . . . . . : portland-ops.local
   Node Type . . . . . . . . . . . . : Hybrid
   IP Routing Enabled. . . . . . . . : No
   WINS Proxy Enabled. . . . . . . . : No
   DNS Suffix Search List. . . . . . : portland-ops.local

Ethernet adapter Local Area Connection 1:

   Connection-specific DNS Suffix  . : portland-ops.local
   Description . . . . . . . . . . . : Intel(R) Ethernet Connection (7) I219-LM
   Physical Address. . . . . . . . . : 00-2B-67-14-99-4A
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::49b2:9408:2f41:178a%12(Preferred)
   IPv4 Address. . . . . . . . . . . : 192.168.10.45(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Lease Obtained. . . . . . . . . . : Tuesday, October 20, 2026 7:45:10 AM
   Lease Expires . . . . . . . . . . : Wednesday, October 21, 2026 7:45:10 AM
   Default Gateway . . . . . . . . . : 192.168.10.1
   DHCP Server . . . . . . . . . . . : 192.168.10.254
   DHCPv6 IAID . . . . . . . . . . . : 201337447
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-29-7B-9A-00-2B-67-14-99-4A
   DNS Servers . . . . . . . . . . . : 192.168.10.10
                                       192.168.10.11
   NetBIOS over Tcpip. . . . . . . . : Enabled
"""

    # nslookup drill
    dumps["nslookup_drill.txt"] = """C:\\Users\\ethan> nslookup mail.portland-ops.local
Server:  dc01.portland-ops.local
Address:  192.168.10.10

Name:    mail.portland-ops.local
Address:  192.168.10.50

C:\\Users\\ethan> nslookup -type=mx portland-ops.local
Server:  dc01.portland-ops.local
Address:  192.168.10.10

portland-ops.local      MX preference = 10, mail exchanger = mail.portland-ops.local

C:\\Users\\ethan> nslookup 192.168.10.20
Server:  dc01.portland-ops.local
Address:  192.168.10.10

Name:    mgmt-sw-closetc.portland-ops.local
Address:  192.168.10.20

C:\\Users\\ethan> nslookup benefits.internal.corp
Server:  dc01.portland-ops.local
Address:  192.168.10.10

Name:    benefits.internal.corp
Address:  192.168.10.80

C:\\Users\\ethan> nslookup evil-phish-domain.bad
Server:  dc01.portland-ops.local
Address:  192.168.10.10

*** dc01.portland-ops.local can't find evil-phish-domain.bad: Non-existent domain
"""

    # netstat -ano
    dumps["netstat_ano.txt"] = """Active Connections

  Proto  Local Address          Foreign Address        State           PID
  TCP    0.0.0.0:135            0.0.0.0:0              LISTENING       840
  TCP    0.0.0.0:445            0.0.0.0:0              LISTENING       4
  TCP    0.0.0.0:3389           0.0.0.0:0              LISTENING       1184
  TCP    127.0.0.1:5357         0.0.0.0:0              LISTENING       4
  TCP    192.168.10.45:139      0.0.0.0:0              LISTENING       4
  TCP    192.168.10.45:51234    192.168.10.20:22       ESTABLISHED     3892
  TCP    192.168.10.45:51240    10.0.4.15:23          SYN_SENT        4120
  TCP    192.168.10.45:51255    192.168.10.80:443      ESTABLISHED     5120
  TCP    192.168.10.45:51260    192.168.10.80:80       TIME_WAIT       0
  TCP    192.168.10.45:51270    192.168.10.50:993      ESTABLISHED     2410
  TCP    192.168.10.45:51272    192.168.10.50:110      CLOSE_WAIT      2410
  TCP    192.168.10.45:51280    192.168.10.10:636      ESTABLISHED     840
  TCP    192.168.10.45:51282    192.168.10.10:389      TIME_WAIT       0
  TCP    [::]:135               [::]:0                 LISTENING       840
  TCP    [::]:445               [::]:0                 LISTENING       4
  TCP    [::]:3389              [::]:0                 LISTENING       1184
  UDP    0.0.0.0:68             *:*                                    840
  UDP    0.0.0.0:123            *:*                                    1024
  UDP    0.0.0.0:161            *:*                                    1490
  UDP    0.0.0.0:5353           *:*                                    2180
  UDP    0.0.0.0:5355           *:*                                    2180
  UDP    192.168.10.45:137      *:*                                    4
  UDP    192.168.10.45:138      *:*                                    4
"""

    # gpresult /r
    dumps["gpresult.txt"] = """Microsoft (R) Windows (R) Operating System Group Policy Result tool v2.0
c 2026 Microsoft Corporation. All rights reserved.

Created on Tuesday, October 20, 2026 at 11:15:32 AM

RSOP data for PORTLAND-OPS\\ethan on PORT-WS-1042 : Logging Mode
--------------------------------------------------------------

OS Configuration:            Member Workstation
OS Version:                  10.0.19045
Site Name:                   Portland-Headquarters
Roaming Profile:             N/A
Local Profile:               C:\\Users\\ethan
Connected over a slow link?: No

USER SETTINGS
--------------
    CN=Ethan Mercer,OU=HelpDesk,OU=Staff,DC=portland-ops,DC=local
    Last time Group Policy was applied: 10/20/2026 at 10:45:12 AM
    Group Policy was applied from:      dc01.portland-ops.local
    Group Policy slow link threshold:   500 kbps
    Domain Name:                        portland-ops
    Domain Type:                        Windows 2016 or newer

    Applied Group Policy Objects
    -----------------------------
        Default Domain Policy
        SecOps-Workstation-Hardening-2026
        BitLocker-Enforcement-GPO
        Edge-Browser-Enterprise-Baseline

    The following GPOs were not applied because they were filtered out
    -------------------------------------------------------------------
        Domain Controllers Policy
            Filtering:  Not Applied (Empty)
        Restricted-Admin-Tier0
            Filtering:  Denied (Security)

    The user is a part of the following security groups
    ---------------------------------------------------
        Domain Users
        Tier1-HelpDesk-Support
        Remote Desktop Users
        Local-Workstation-Admins
"""

    # route print
    dumps["route_print.txt"] = """===========================================================================
Interface List
 12...00 2b 67 14 99 4a ......Intel(R) Ethernet Connection (7) I219-LM
  1...........................Software Loopback Interface 1
===========================================================================

IPv4 Route Table
===========================================================================
Active Routes:
Network Destination        Netmask          Gateway       Interface  Metric
          0.0.0.0          0.0.0.0     192.168.10.1   192.168.10.45      25
        127.0.0.0        255.0.0.0         On-link         127.0.0.1     331
        127.0.0.1  255.255.255.255         On-link         127.0.0.1     331
  127.255.255.255  255.255.255.255         On-link         127.0.0.1     331
     192.168.10.0    255.255.255.0         On-link    192.168.10.45     281
    192.168.10.45  255.255.255.255         On-link    192.168.10.45     281
   192.168.10.255  255.255.255.255         On-link    192.168.10.45     281
        224.0.0.0        240.0.0.0         On-link         127.0.0.1     331
        224.0.0.0        240.0.0.0         On-link    192.168.10.45     281
  255.255.255.255  255.255.255.255         On-link         127.0.0.1     331
  255.255.255.255  255.255.255.255         On-link    192.168.10.45     281
===========================================================================
Persistent Routes:
  Network Address          Netmask  Gateway Address  Metric
       10.240.0.0      255.255.0.0     192.168.10.1       1
===========================================================================
"""
    return dumps


# ==============================================================================
# 3. WINDOWS EVENT VIEWER RECORDS (Security Events 4624, 4625, 4740, 7045)
# ==============================================================================

def get_security_events() -> List[Dict[str, Any]]:
    return [
        {
            "event_id": 4624,
            "provider_name": "Microsoft-Windows-Security-Auditing",
            "time_created": "2026-10-20T08:14:22.108421Z",
            "computer": "dc01.portland-ops.local",
            "description": "An account was successfully logged on.",
            "data": {
                "TargetUserName": "ethan",
                "TargetDomainName": "PORTLAND-OPS",
                "LogonType": 2,  # Interactive (Console / Keyboard)
                "LogonTypeName": "Interactive",
                "AuthenticationPackageName": "Negotiate",
                "WorkstationName": "PORT-DESK-01",
                "IpAddress": "127.0.0.1",
                "IpPort": "0",
                "ProcessName": "C:\\Windows\\System32\\winlogon.exe",
                "Status": "0x0",
            },
        },
        {
            "event_id": 4624,
            "provider_name": "Microsoft-Windows-Security-Auditing",
            "time_created": "2026-10-20T08:35:40.412890Z",
            "computer": "dc01.portland-ops.local",
            "description": "An account was successfully logged on.",
            "data": {
                "TargetUserName": "skelly.contractor",
                "TargetDomainName": "PORTLAND-OPS",
                "LogonType": 10,  # RemoteInteractive (Terminal Services / RDP)
                "LogonTypeName": "RemoteInteractive",
                "AuthenticationPackageName": "Negotiate",
                "WorkstationName": "HOTEL-LAPTOP",
                "IpAddress": "10.240.1.45",  # From VPN pool
                "IpPort": "54210",
                "ProcessName": "C:\\Windows\\System32\\svchost.exe",
                "Status": "0x0",
            },
        },
        {
            "event_id": 4625,
            "provider_name": "Microsoft-Windows-Security-Auditing",
            "time_created": "2026-10-20T16:24:12.338210Z",
            "computer": "dc01.portland-ops.local",
            "description": "An account failed to log on.",
            "data": {
                "TargetUserName": "dkim",
                "TargetDomainName": "PORTLAND-OPS",
                "LogonType": 3,  # Network (Exchange ActiveSync / NTLM)
                "LogonTypeName": "Network",
                "AuthenticationPackageName": "MICROSOFT_AUTHENTICATION_PACKAGE_V1_0",
                "WorkstationName": "IPAD-DKIM-04",
                "IpAddress": "192.168.20.114",  # Guest Wi-Fi subnet
                "IpPort": "49882",
                "Status": "0xC000006D",
                "SubStatus": "0xC000006A",  # Bad password
                "FailureReason": "Unknown user name or bad password.",
            },
        },
        {
            "event_id": 4625,
            "provider_name": "Microsoft-Windows-Security-Auditing",
            "time_created": "2026-10-20T16:26:05.109240Z",
            "computer": "dc01.portland-ops.local",
            "description": "An account failed to log on.",
            "data": {
                "TargetUserName": "dkim",
                "TargetDomainName": "PORTLAND-OPS",
                "LogonType": 3,
                "LogonTypeName": "Network",
                "AuthenticationPackageName": "MICROSOFT_AUTHENTICATION_PACKAGE_V1_0",
                "WorkstationName": "IPAD-DKIM-04",
                "IpAddress": "192.168.20.114",
                "IpPort": "49888",
                "Status": "0xC000006D",
                "SubStatus": "0xC0000234",  # User logon with account locked
                "FailureReason": "The user account has been automatically locked because too many invalid logon attempts were made.",
            },
        },
        {
            "event_id": 4740,
            "provider_name": "Microsoft-Windows-Security-Auditing",
            "time_created": "2026-10-20T16:26:05.115400Z",
            "computer": "dc01.portland-ops.local",
            "description": "A user account was locked out.",
            "data": {
                "TargetUserName": "dkim",
                "TargetDomainName": "PORTLAND-OPS",
                "SubjectUserName": "dc01$",
                "SubjectDomainName": "PORTLAND-OPS",
                "CallerComputerName": "IPAD-DKIM-04",
                "TargetSid": "S-1-5-21-3928174412-1082938471-2948192837-1402",
            },
        },
        {
            "event_id": 7045,
            "provider_name": "Service Control Manager",
            "time_created": "2026-10-20T17:15:30.984012Z",
            "computer": "PORT-WS-1054.portland-ops.local",
            "description": "A service was installed in the system.",
            "data": {
                "ServiceName": "PSEXESVC",
                "ImagePath": "%SystemRoot%\\PSEXESVC.exe",
                "ServiceType": "user mode service",
                "StartType": "demand start",
                "ServiceAccount": "LocalSystem",
                "AuditNote": "Sysinternals PsExec remote execution service installed; frequently leveraged in lateral movement.",
            },
        },
    ]


# ==============================================================================
# 4. RAW EMAIL MIME HEADERS & PHISHING SAMPLES
# ==============================================================================

def get_phishing_dataset() -> Tuple[List[Dict[str, Any]], Dict[str, str]]:
    eml_files: Dict[str, str] = {}
    samples_meta: List[Dict[str, Any]] = []

    # Sample 1: Phishing Invoice with .iso attachment and SPF Fail
    eml_invoice = """Delivered-To: tbradley@portland-ops.local
Received: from mail-relay.portland-ops.local (mail-relay.portland-ops.local [192.168.10.50])
	by imap.portland-ops.local with ESMTP id 82B93FA1
	for <tbradley@portland-ops.local>; Tue, 20 Oct 2026 17:21:05 +0000
Received: from vps104-bogus-sender.net (vps104-bogus-sender.net [198.51.100.84])
	by mail-relay.portland-ops.local with ESMTP id 93A87BF4
	for <tbradley@portland-ops.local>; Tue, 20 Oct 2026 17:21:03 +0000
Authentication-Results: mail-relay.portland-ops.local;
	spf=fail (sender IP 198.51.100.84 is not in designated SPF record of vendor-invoicing.net) smtp.mailfrom=bounce@vps104-bogus-sender.net;
	dkim=none (no signature found);
	dmarc=fail (p=none dis=none) header.from=vendor-invoicing.net
From: "Supplier Billing Department" <billing@vendor-invoicing.net>
Reply-To: "Emergency Collections" <collect@phish-drop.org>
To: tbradley@portland-ops.local
Subject: URGENT: Outstanding Balance Invoice #INV-98231 - Immediate Payment Required
Date: Tue, 20 Oct 2026 17:20:45 +0000
Message-ID: <20261020172045.99428174.phish@vps104-bogus-sender.net>
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="----=_NextPart_000_01D2"
X-Priority: 1 (Highest)
X-Mailer: Microsoft Outlook 16.0

This is a multi-part message in MIME format.

------=_NextPart_000_01D2
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: 7bit

Dear Valued Customer,

Your account shows an overdue balance totaling $44,850.00. Failure to remit payment within 24 hours will result in immediate suspension of facility services and legal escalation.

Review the attached invoice specifications to confirm remittance details.

Sincerely,
Accounts Receivable Services
------=_NextPart_000_01D2
Content-Type: application/x-iso9660-image; name="INV_Oct2026_9942.pdf.iso"
Content-Disposition: attachment; filename="INV_Oct2026_9942.pdf.iso"
Content-Transfer-Encoding: base64

UEsDBBQAAAAIAAAAAAAAAAAAAAAAAAAAAAA=
------=_NextPart_000_01D2--
"""
    eml_files["sample_phish_invoice.eml"] = eml_invoice
    samples_meta.append({
        "sample_id": "PHISH-01",
        "filename": "sample_phish_invoice.eml",
        "subject": "URGENT: Outstanding Balance Invoice #INV-98231 - Immediate Payment Required",
        "sender_header": "billing@vendor-invoicing.net",
        "reply_to": "collect@phish-drop.org",
        "origin_ip": "198.51.100.84",
        "authentication_results": {
            "spf": "fail",
            "dkim": "none",
            "dmarc": "fail",
        },
        "attachment_name": "INV_Oct2026_9942.pdf.iso",
        "is_phishing": True,
        "indicators": [
            "SPF failure: Sending IP not authorized by claimed domain",
            "Mismatched Reply-To address pointing to external free/drop domain",
            "Double camouflage file extension (.pdf.iso) concealing executable container",
            "Artificial urgency and threat of service suspension",
        ],
        "recommended_triage_action": "Isolate recipient endpoint, quarantine message across gateway, extract hash for SIEM/EDR blocklist.",
    })

    # Sample 2: Executive Impersonation / CEO Wire Fraud
    eml_spoof = """Delivered-To: mlin@portland-ops.local
Received: from mail-relay.portland-ops.local (mail-relay.portland-ops.local [192.168.10.50])
	by imap.portland-ops.local with ESMTP id 77C12EF1
	for <mlin@portland-ops.local>; Tue, 20 Oct 2026 16:15:10 +0000
Received: from out-relay-12.mailgun.org (out-relay-12.mailgun.org [159.135.225.12])
	by mail-relay.portland-ops.local with ESMTP id 65B90AA2
	for <mlin@portland-ops.local>; Tue, 20 Oct 2026 16:15:08 +0000
Authentication-Results: mail-relay.portland-ops.local;
	spf=softfail (portland-ops.local: domain of ceo-desk-office@gmail.com does not designate 159.135.225.12 as permitted sender);
	dkim=fail (signature does not match header payload);
	dmarc=fail (p=quarantine dis=quarantine) header.from=portland-ops.local
From: "Walt Brandvold" <walt@portland-ops.local>
Reply-To: "Walt Brandvold (Mobile Office)" <walt.executive.desk77@gmail.com>
To: mlin@portland-ops.local
Subject: Confidential: Immediate vendor wire authorization required
Date: Tue, 20 Oct 2026 16:14:50 +0000
Message-ID: <CA+V=8A9184B1028@mail.gmail.com>
MIME-Version: 1.0
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: 7bit

Maya,

I am currently in an offsite partner negotiation with spotty cellular reception. 

We need to finalize an emergency deposit for critical plant equipment before 5:00 PM today. Please process an expedited wire transfer of $78,400 to the attached escrow routing details. Keep this strictly between us until the contract announcement tomorrow.

Reply here as soon as the wire tracking confirmation is issued.

Walt Brandvold
Chief Executive Officer
"""
    eml_files["sample_spoofed_exec.eml"] = eml_spoof
    samples_meta.append({
        "sample_id": "PHISH-02",
        "filename": "sample_spoofed_exec.eml",
        "subject": "Confidential: Immediate vendor wire authorization required",
        "sender_header": "walt@portland-ops.local",
        "reply_to": "walt.executive.desk77@gmail.com",
        "origin_ip": "159.135.225.12",
        "authentication_results": {
            "spf": "softfail",
            "dkim": "fail",
            "dmarc": "fail",
        },
        "attachment_name": None,
        "is_phishing": True,
        "indicators": [
            "Executive impersonation / Business Email Compromise (BEC)",
            "External Reply-To header pointing to personal Gmail address",
            "DMARC failure on internal corporate domain header",
            "Pressure to bypass established dual-control finance approval procedures",
        ],
        "recommended_triage_action": "Quarantine email, alert accounting team to verify out-of-band, report sender to mail gateway blacklist.",
    })

    # Sample 3: Legitimate Corporate HR Benefits Statement
    eml_legit = """Delivered-To: ethan@portland-ops.local
Received: from mail-relay.portland-ops.local (mail-relay.portland-ops.local [192.168.10.50])
	by imap.portland-ops.local with ESMTP id 11A89DC3
	for <ethan@portland-ops.local>; Tue, 20 Oct 2026 09:10:00 +0000
Received: from hr-app01.portland-ops.local (hr-app01.portland-ops.local [192.168.10.72])
	by mail-relay.portland-ops.local with ESMTP id 22F81B99
	for <ethan@portland-ops.local>; Tue, 20 Oct 2026 09:09:58 +0000
Authentication-Results: mail-relay.portland-ops.local;
	spf=pass (hr-app01.portland-ops.local: 192.168.10.72 is authorized sender) smtp.mailfrom=hr-benefits@portland-ops.local;
	dkim=pass (signature verified for portland-ops.local);
	dmarc=pass (p=reject) header.from=portland-ops.local
From: "People Operations & Benefits" <hr-benefits@portland-ops.local>
Reply-To: <hr-benefits@portland-ops.local>
To: ethan@portland-ops.local
Subject: Annual Open Enrollment 2027: Confirmation of Current Health Selections
Date: Tue, 20 Oct 2026 09:09:50 +0000
Message-ID: <20261020090950.771239@hr-app01.portland-ops.local>
MIME-Version: 1.0
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: 7bit

Hi Ethan,

This is your automated confirmation statement regarding Open Enrollment for the 2027 plan year.

To review or modify your existing dental, medical, and retirement withholding contributions, navigate to the internal portal at:
https://benefits.internal.corp:443/

Open enrollment closes on Friday, November 13 at 5:00 PM PST.

Best regards,
People Operations Team
"""
    eml_files["sample_legit_payroll.eml"] = eml_legit
    samples_meta.append({
        "sample_id": "LEGIT-01",
        "filename": "sample_legit_payroll.eml",
        "subject": "Annual Open Enrollment 2027: Confirmation of Current Health Selections",
        "sender_header": "hr-benefits@portland-ops.local",
        "reply_to": "hr-benefits@portland-ops.local",
        "origin_ip": "192.168.10.72",
        "authentication_results": {
            "spf": "pass",
            "dkim": "pass",
            "dmarc": "pass",
        },
        "attachment_name": None,
        "is_phishing": False,
        "indicators": [
            "SPF pass: Internal server IP explicitly listed in SPF record",
            "DKIM pass: Cryptographic signature verified against corporate DNS key",
            "DMARC pass: Header matches envelope domain perfectly",
            "Links point to authentic internal HTTPS resource on port 443",
        ],
        "recommended_triage_action": "Mark clean / Allow delivery.",
    })

    return samples_meta, eml_files


# ==============================================================================
# 5. GENERATION & VERIFICATION ENGINES
# ==============================================================================

def generate_artifacts(out_dir: Path, output_format: str = "both") -> Dict[str, Any]:
    out_dir.mkdir(parents=True, exist_ok=True)
    dumps_dir = out_dir / "terminal_dumps"
    eml_dir = out_dir / "eml_samples"
    dumps_dir.mkdir(parents=True, exist_ok=True)
    eml_dir.mkdir(parents=True, exist_ok=True)

    results: Dict[str, Any] = {"files_written": []}

    # 1. Tickets
    tickets = get_simulated_tickets()
    if output_format in ("json", "both"):
        json_path = out_dir / "tickets.json"
        json_path.write_text(json.dumps(tickets, indent=2), encoding="utf-8")
        results["files_written"].append(str(json_path))

    if output_format in ("csv", "both"):
        csv_path = out_dir / "tickets.csv"
        if tickets:
            keys = list(tickets[0].keys())
            with open(csv_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=keys)
                writer.writeheader()
                writer.writerows(tickets)
            results["files_written"].append(str(csv_path))

    # 2. Terminal Dumps
    dumps = get_terminal_dumps()
    for name, content in dumps.items():
        # Write to subfolder
        sub_path = dumps_dir / name
        sub_path.write_text(content, encoding="utf-8")
        results["files_written"].append(str(sub_path))
        # Write to root for convenient flat reference
        root_path = out_dir / name
        root_path.write_text(content, encoding="utf-8")
        results["files_written"].append(str(root_path))

    # 3. Security Events
    events = get_security_events()
    events_path = out_dir / "security_events.json"
    events_path.write_text(json.dumps(events, indent=2), encoding="utf-8")
    results["files_written"].append(str(events_path))

    # 4. Phishing EML and Metadata
    phish_meta, eml_files = get_phishing_dataset()
    phish_meta_path = out_dir / "phishing_samples.json"
    phish_meta_path.write_text(json.dumps(phish_meta, indent=2), encoding="utf-8")
    results["files_written"].append(str(phish_meta_path))

    for name, content in eml_files.items():
        sub_eml = eml_dir / name
        sub_eml.write_text(content, encoding="utf-8")
        results["files_written"].append(str(sub_eml))
        root_eml = out_dir / name
        root_eml.write_text(content, encoding="utf-8")
        results["files_written"].append(str(root_eml))

    results["total_tickets"] = len(tickets)
    results["total_events"] = len(events)
    results["total_phishing_samples"] = len(phish_meta)
    results["total_dumps"] = len(dumps)
    return results


def verify_artifacts(target_dir: Path) -> Tuple[bool, List[str]]:
    errors: List[str] = []
    checks: List[str] = []

    if not target_dir.is_dir():
        return False, [f"Target directory does not exist: {target_dir}"]

    # Check 1: tickets.json
    t_json = target_dir / "tickets.json"
    if not t_json.is_file():
        errors.append(f"Missing tickets.json at {t_json}")
    else:
        try:
            data = json.loads(t_json.read_text(encoding="utf-8"))
            if not isinstance(data, list) or len(data) == 0:
                errors.append("tickets.json must contain a non-empty list of tickets")
            else:
                required_ticket_keys = {
                    "ticket_id", "requester_name", "department", "priority",
                    "status", "category", "subject", "symptom_description"
                }
                for i, ticket in enumerate(data):
                    missing = required_ticket_keys - set(ticket.keys())
                    if missing:
                        errors.append(f"Ticket #{i} ({ticket.get('ticket_id')}) missing keys: {missing}")
                checks.append(f"Validated {len(data)} tickets in tickets.json")
        except Exception as e:
            errors.append(f"Failed to parse tickets.json: {e}")

    # Check 2: tickets.csv
    t_csv = target_dir / "tickets.csv"
    if not t_csv.is_file():
        errors.append(f"Missing tickets.csv at {t_csv}")
    else:
        try:
            with open(t_csv, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                rows = list(reader)
                if len(rows) == 0:
                    errors.append("tickets.csv must contain data rows")
                else:
                    checks.append(f"Validated {len(rows)} CSV rows in tickets.csv")
        except Exception as e:
            errors.append(f"Failed to parse tickets.csv: {e}")

    # Check 3: Terminal dumps
    expected_dumps = [
        ("ipconfig_all.txt", "Subnet Mask"),
        ("nslookup_drill.txt", "Server:"),
        ("netstat_ano.txt", "Active Connections"),
        ("gpresult.txt", "Applied Group Policy Objects"),
        ("route_print.txt", "Active Routes"),
    ]
    for dump_name, signature in expected_dumps:
        dump_file = target_dir / dump_name
        if not dump_file.is_file():
            # Check terminal_dumps subfolder
            sub_file = target_dir / "terminal_dumps" / dump_name
            if not sub_file.is_file():
                errors.append(f"Missing diagnostic dump {dump_name}")
                continue
            dump_file = sub_file
        content = dump_file.read_text(encoding="utf-8")
        if signature not in content:
            errors.append(f"Diagnostic dump {dump_name} missing signature phrase '{signature}'")
        else:
            checks.append(f"Validated diagnostic dump: {dump_name}")

    # Check 4: security_events.json
    s_events = target_dir / "security_events.json"
    if not s_events.is_file():
        errors.append(f"Missing security_events.json at {s_events}")
    else:
        try:
            ev_data = json.loads(s_events.read_text(encoding="utf-8"))
            if not isinstance(ev_data, list) or len(ev_data) == 0:
                errors.append("security_events.json must be a non-empty list")
            else:
                found_event_ids = set()
                for ev in ev_data:
                    found_event_ids.add(ev.get("event_id"))
                required_ids = {4624, 4625, 4740, 7045}
                missing_ids = required_ids - found_event_ids
                if missing_ids:
                    errors.append(f"security_events.json missing required event IDs: {missing_ids}")
                else:
                    checks.append(f"Validated Event IDs {required_ids} in security_events.json")
        except Exception as e:
            errors.append(f"Failed to parse security_events.json: {e}")

    # Check 5: phishing_samples.json & .eml files
    p_json = target_dir / "phishing_samples.json"
    if not p_json.is_file():
        errors.append(f"Missing phishing_samples.json at {p_json}")
    else:
        try:
            p_data = json.loads(p_json.read_text(encoding="utf-8"))
            if not isinstance(p_data, list) or len(p_data) == 0:
                errors.append("phishing_samples.json must be a non-empty list")
            else:
                checks.append(f"Validated {len(p_data)} metadata records in phishing_samples.json")
        except Exception as e:
            errors.append(f"Failed to parse phishing_samples.json: {e}")

    eml_samples = ["sample_phish_invoice.eml", "sample_spoofed_exec.eml", "sample_legit_payroll.eml"]
    for eml_name in eml_samples:
        eml_file = target_dir / eml_name
        if not eml_file.is_file():
            sub_eml = target_dir / "eml_samples" / eml_name
            if not sub_eml.is_file():
                errors.append(f"Missing EML sample {eml_name}")
                continue
            eml_file = sub_eml
        try:
            content = eml_file.read_text(encoding="utf-8")
            msg = email.message_from_string(content)
            if not msg.get("Authentication-Results"):
                errors.append(f"{eml_name} missing Authentication-Results header")
            else:
                checks.append(f"Validated MIME structure and SPF/DKIM/DMARC in {eml_name}")
        except Exception as e:
            errors.append(f"Failed to parse MIME email {eml_name}: {e}")

    success = len(errors) == 0
    return success, checks if success else errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Portland Desk Level 1 Support Artifact Generator & Verifier"
    )
    parser.add_argument(
        "--generate",
        action="store_true",
        help="Generate synthetic help desk tickets, command dumps, event logs, and MIME headers",
    )
    parser.add_argument(
        "--verify",
        action="store_true",
        help="Verify the schema, presence, and integrity of generated artifacts",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=DEFAULT_OUT_DIR,
        help=f"Target directory for artifacts (default: {DEFAULT_OUT_DIR})",
    )
    parser.add_argument(
        "--format",
        choices=["json", "csv", "both"],
        default="both",
        help="Output format for ticket queue (default: both)",
    )

    args = parser.parse_args()

    # If neither flag provided, default to generating and verifying
    if not args.generate and not args.verify:
        args.generate = True
        args.verify = True

    target_dir = args.out_dir.resolve()

    if args.generate:
        print(f"[*] Generating help desk artifacts in: {target_dir}")
        res = generate_artifacts(target_dir, output_format=args.format)
        print(f"[+] Wrote {len(res['files_written'])} files successfully:")
        print(f"    - Tickets: {res['total_tickets']} records ({args.format})")
        print(f"    - Terminal dumps: {res['total_dumps']} files (ipconfig, nslookup, netstat, gpresult, route)")
        print(f"    - Windows events: {res['total_events']} records (4624, 4625, 4740, 7045)")
        print(f"    - Phishing samples: {res['total_phishing_samples']} samples (.eml + JSON)")

    if args.verify:
        print(f"[*] Verifying schema and integrity in: {target_dir}")
        passed, messages = verify_artifacts(target_dir)
        if passed:
            for m in messages:
                print(f"  [PASS] {m}")
            print("\nRESULT: ALL HELP DESK ARTIFACTS VERIFIED (PASS)")
            return 0
        else:
            for err in messages:
                print(f"  [FAIL] {err}", file=sys.stderr)
            print("\nRESULT: VERIFICATION FAILED", file=sys.stderr)
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
