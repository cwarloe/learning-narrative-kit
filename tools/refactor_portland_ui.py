"""Transforms all 13 Portland Desk workbenches and narratives:
1. Replaces the intimidating 'At a Glance' syllabus tables with grounded Shift Briefing cards + collapsed instructor drawers.
2. Removes cheesy AI emojis (🎯, 🔬, 📖, 🔍, ★) in favor of professional typography.
3. Inserts interactive scratchpad placeholders for learner notes in prediction gates and ticket drafting sections.
4. Ensures strict GFM table blank line separation and pipe safety.
"""

import os
import re
from pathlib import Path

BASE_DIR = Path(r"C:\Users\charl\learning-narrative-kit")

WORKBENCH_METADATA = {
    "00": {
        "setting": "Ethan's kitchen table in East Portland • 11:30 PM with $83 in checking",
        "role": "Aspiring Technician (Pre-Helpdesk, Gresham Warehouse Associate)",
        "goal": "Build the four physical machine invariants (CPU, RAM, Storage, Network) and study triage reflexes so you stop guessing and start diagnosing.",
        "duration": "45–60 minutes • Self-paced • Zero prerequisites",
        "cert": "CompTIA A+ Core 1 (220-1101) & Core 2 (220-1102) Foundations",
        "domains": "Core 1 Domain 2.0 (Networking) & Domain 3.0 (Hardware Triage); Core 2 Domain 1.0 (OS & CLI) & Domain 3.0 (Troubleshooting)",
        "deliverables": "Computing Invariants Matrix • Identity Triad Flow • RAM vs Disk Isolation Drill • Local vs Gateway Triage Drill • Call Your Shot 5-Case Gate • First-Contact Diagnostic Checklist"
    },
    "01": {
        "setting": "Gresham Freight Forwarding Terminal • Graveyard shift, industrial staging floor",
        "role": "Tier 1 Field / Hardware Bench Technician",
        "goal": "Isolate hardware faults and Layer 1 physical failures on an automated shipping scale terminal before the 5:00 AM dispatch.",
        "duration": "40–50 minutes • Hardware Diagnostics",
        "cert": "CompTIA A+ Core 1 (220-1101) & Network+ (N10-008/009)",
        "domains": "A+ Core 1 Domain 3.1 (Motherboard, RAM, CPU, Power) & 3.4 (Peripherals & Serial); Network+ Domain 5.2 (Physical Layer 1 Connectivity)",
        "deliverables": "Physical Diagnostic Flow • POST Code Triage Matrix • ATX Power Supply Voltage Drill • RS-232 Serial Framing Drill • Call Your Shot 5-Case Gate • Tier 1 Physical Passdown Note"
    },
    "02": {
        "setting": "Portland Regional Operations Center • Live service desk bullpen",
        "role": "Tier 1 Support Specialist (Practical Trial under Desk Lead Jules Brooks)",
        "goal": "Troubleshoot live workstation freezes, OS crashes, and graphics driver conflicts using binary search, Safe Mode, and Windows Event Viewer logs.",
        "duration": "40–50 minutes • Operating System Triage",
        "cert": "CompTIA A+ Core 2 (220-1102)",
        "domains": "Domain 1.0 (Operating Systems & Boot Architecture) & Domain 3.0 (Software Troubleshooting & Event Log Decomposition)",
        "deliverables": "Windows Boot & Safe Mode Matrix • Event Viewer Crash Analysis Drill • Clean Boot Service Isolation Drill • Call Your Shot 5-Case Gate • Departmental Resolution Ticket"
    },
    "03": {
        "setting": "East Portland Pump Station & Annex • Operations Service Desk",
        "role": "Level 1 Network Support Specialist (under Jules Brooks & Jared Lindqvist)",
        "goal": "Triage local IP addressing, APIPA 169.254.x.x link-local traps, subnet boundaries, and ARP resolution failures following a storm switch reboot.",
        "duration": "45–55 minutes • Local Network Addressing",
        "cert": "CompTIA Network+ (N10-008/009)",
        "domains": "Domain 1.4 (IPv4 Addressing, Subnetting & CIDR) & Domain 5.2 (Network Troubleshooting, ARP & Default Gateways)",
        "deliverables": "IP Addressing Ground Truth Reference • Subnet Boundary Math Matrix • APIPA & DORA Isolation Drill • ARP Frame Routing Drill • Call Your Shot 5-Case Gate • Network Addressing Passdown Note"
    },
    "04": {
        "setting": "Portland Operations Center • Spring downpour, remote VPN support queue",
        "role": "Level 1 Network Support Specialist (under Jules Brooks & Maya Chen)",
        "goal": "Trace why remote VPN users fail to access internal company services while in-office users succeed, resolving split-horizon DNS and rogue hosts file overrides.",
        "duration": "40–50 minutes • Name Resolution & DNS Plumbing",
        "cert": "CompTIA Network+ (N10-008/009)",
        "domains": "Domain 1.5 (DNS Services, Record Types, Zones) & Domain 5.2 (Troubleshooting Name Resolution & Client Caching)",
        "deliverables": "DNS Hierarchy & Record Matrix • Command Triage Flow (nslookup vs ping) • Stale Cache Flushing Drill • Rogue Hosts File Hunting Drill • Call Your Shot 5-Case Gate • DNS Resolution & VPN Escalation Note"
    },
    "05": {
        "setting": "Portland Operations Center Bullpen • Cold October rain, evening shift",
        "role": "Level 1 Network Support Specialist (under Jules Brooks & Jared Lindqvist)",
        "goal": "Diagnose network connection refusals (RST) versus silent timeouts (firewall drops) using TCP three-way handshake mechanics and netstat socket inspections.",
        "duration": "45–50 minutes • Layer 4 Transport & Sockets",
        "cert": "CompTIA Network+ (N10-008/009)",
        "domains": "Domain 1.1 (OSI Transport Layer & TCP vs UDP) & Domain 5.4 (Network Tools: netstat, port scanners)",
        "deliverables": "TCP Flag Reference & Socket State Flow • RST vs Drop Triage Matrix • Three-Way Handshake Wireshark Drill • Netstat Port & PID Inspection Drill • Call Your Shot 5-Case Gate • Socket Resolution & Escalation Note"
    },
    "06": {
        "setting": "Building C Basement Telecom Vault • 04:00 AM Flood Emergency",
        "role": "Emergency Response Technician (Midpoint Capstone under Jules Brooks & Jared Lindqvist)",
        "goal": "Physically replace flood-damaged core switches, rebuild trunk VLANs, recover from a 150-device DHCP exhaustion storm, and restore municipal operations before 08:00 AM opening.",
        "duration": "60–75 minutes • Disaster Recovery Midpoint Capstone",
        "cert": "CompTIA Network+ (N10-008/009) & A+ Core 1",
        "domains": "Network+ Domain 2.0 (Switching, VLANs, 802.1Q) & Domain 4.0 (Network Operations & Disaster Recovery)",
        "deliverables": "Disaster Recovery Action Matrix • Physical Cable Punchdown & Flea Power Recovery • 802.1Q VLAN Trunking Configuration • DHCP Pool Recovery & Lease Purging • Call Your Shot 5-Case Gate • Post-Outage Master Incident Report"
    },
    "07": {
        "setting": "Level 1 Service Desk Terminal • Operational Queue",
        "role": "Tier 1 Service Desk Specialist (under Desk Lead Jules Brooks)",
        "goal": "Identify and replace unencrypted, cleartext legacy protocols (Telnet, HTTP, POP3, SMTP) with modern TLS encrypted standards across email, administration, and plant telemetry.",
        "duration": "40–50 minutes • Network Security & Protocol Hardening",
        "cert": "CompTIA Security+ (SY0-701)",
        "domains": "Domain 1.0 (Threats & Protocol Vulnerabilities) & Domain 3.0 (Security Architecture: Secure Transit Protocols)",
        "deliverables": "Cleartext vs Encrypted Protocol Matrix • Packet Capture Credential Extraction Drill • Mail Client Port & STARTTLS Drill • Call Your Shot 5-Case Gate • Standard Resolution & Security Escalation Note"
    },
    "08": {
        "setting": "Level 1 Service Desk Terminal • Identity & Access Queue",
        "role": "Tier 1 Service Desk Specialist (under Desk Lead Jules Brooks)",
        "goal": "Triage authentication failures, Active Directory lockouts (Event ID 4740), caller computer detection, and transition users from vulnerable SMS OTP to phishing-resistant MFA.",
        "duration": "40–50 minutes • Identity, Credential & Access Management",
        "cert": "CompTIA Security+ (SY0-701)",
        "domains": "Domain 4.0 (Security Operations: Identity & Access Management 4.2) & NIST SP 800-63B Passphrase Standards",
        "deliverables": "Authentication Factors Matrix • Active Directory Event 4740 Analysis Drill • Passphrase vs Complexity Heuristics • Call Your Shot 5-Case Gate • Account Lockout & MFA Resolution Note"
    },
    "09": {
        "setting": "Level 1 Service Desk Terminal • Mail Defense Queue",
        "role": "Tier 1 Service Desk Specialist (under Desk Lead Jules Brooks)",
        "goal": "Dissect RFC 5322 raw email MIME headers, verify SPF, DKIM, and DMARC cryptographic alignment, and identify typosquatted domains in executive wire fraud attempts.",
        "duration": "40–50 minutes • Email Security & Phishing Analysis",
        "cert": "CompTIA Security+ (SY0-701)",
        "domains": "Domain 1.0 (Social Engineering & BEC) & Domain 2.0 (Cryptographic Email Verification: SPF, DKIM, DMARC)",
        "deliverables": "MIME Header Anatomy & Authentication Triad • Raw Email Hop Inspection Drill • Domain Squatting & Typosquatting Recognition • Call Your Shot 5-Case Gate • Formal Phishing Incident Escalation Note"
    },
    "10": {
        "setting": "Level 1 Service Desk Terminal • Endpoint Detection (EDR) Console",
        "role": "Tier 1 Service Desk Specialist (under Desk Lead Jules Brooks)",
        "goal": "Investigate host malware infections, calculate cryptographic file hashes, decode Base64 living-off-the-land PowerShell commands, and isolate persistence mechanisms.",
        "duration": "45–55 minutes • Endpoint Security & Malware Persistence",
        "cert": "CompTIA Security+ (SY0-701)",
        "domains": "Domain 2.0 (Malware Types & Mitigations) & Domain 4.0 (Host Forensics, Services Event ID 7045, Tasks 4698)",
        "deliverables": "Host Persistence & LOLBin Triage Matrix • Encoded PowerShell Payload Decoding Drill • Sysinternals Autoruns & Registry Key Drill • Call Your Shot 5-Case Gate • Host Infection Containment & Escalation Note"
    },
    "11": {
        "setting": "Level 1 Service Desk Terminal & Wireless LAN Controller (WLC)",
        "role": "Tier 1 Service Desk Specialist (under Desk Lead Jules Brooks)",
        "goal": "Isolate unauthorized rogue wireless access points using RSSI signal triangulation and enforce WPA2/WPA3-Enterprise 802.1X with RADIUS and EAP-TLS certificate validation.",
        "duration": "45–55 minutes • Wireless Security & RF Diagnostics",
        "cert": "CompTIA Security+ (SY0-701)",
        "domains": "Domain 2.0 (Rogue APs, Evil Twins) & Domain 3.0 (Wireless Architecture: WPA3, 802.1X, EAP-TLS vs PEAP)",
        "deliverables": "Wireless Authentication Matrix • 802.11 Association & RADIUS Frame Drill • RSSI Triangulation & Rogue Hunting Drill • Call Your Shot 5-Case Gate • Rogue AP Containment & Remediation Note"
    },
    "12": {
        "setting": "Portland Operations Center Service Desk • Tier 1 CSIRT Incident Station",
        "role": "Tier 1 Support Specialist / Junior CSIRT Responder (Final Capstone under Jules Brooks)",
        "goal": "Correlate a multi-stage enterprise intrusion spanning finance phishing, USB dropper execution, lateral pivot, and industrial OT egress into a definitive CSIRT handoff dossier.",
        "duration": "60–75 minutes • Book 0 Final Capstone (Bridge to Book 1 SOC)",
        "cert": "CompTIA Security+ (SY0-701) Capstone & Incident Response",
        "domains": "Domain 4.0 (Incident Response Lifecycle 4.1, Order of Volatility, Chain of Custody & CSIRT Escalation)",
        "deliverables": "Incident Lifecycle & Volatility Hierarchy Matrix • Live Memory Acquisition & Chain of Custody Drill • Multi-Stage Attack Correlation Drill • Call Your Shot 5-Case Gate • Definitive CSIRT Incident Handoff Dossier"
    }
}

def clean_emojis(text: str) -> str:
    # Replace cheesy AI emojis with professional typography
    replaces = [
        ('🎯 Call Your Shot — Predict Before You Look', 'Call Your Shot: Predict Before You Look'),
        ('🎯 Call Your Shot: Predict Before You Look', 'Call Your Shot: Predict Before You Look'),
        ('🎯 Call Your Shot', 'Call Your Shot'),
        ('🎯', ''),
        ('🔬 The Lab', 'The Lab'),
        ('🔬 Hands-On Lab', 'Hands-On Lab'),
        ('🔬', ''),
        ('📖 Read Story', 'Incident Story'),
        ('📖', ''),
        ('🔍 Solution & Jules\' Critique', 'Solution & Lead Tech Review'),
        ('🔍 Solution & Technical Analysis', 'Solution & Technical Analysis'),
        ('🔍 Reveal Solution & Jules\' Review', 'Solution & Lead Tech Review'),
        ('🔍 Drill 1 Forensic Findings & Jules\' Debrief', 'Drill 1 Forensic Findings & Lead Review'),
        ('🔍 Solution & Jules\' Technique Breakdown', 'Solution & Lead Technique Breakdown'),
        ('🔍', ''),
        ('★ Midpoint Capstone', 'Midpoint Capstone'),
        ('★ Final Capstone', 'Final Capstone'),
        ('★', 'CAPSTONE:'),
        ('📊', ''),
        ('⚙️', ''),
        ('🌐', '')
    ]
    for old, new in replaces:
        text = text.replace(old, new)
    return text

def refactor_workbench_file(file_path: Path, ep_id: str):
    text = file_path.read_text(encoding='utf-8')
    meta = WORKBENCH_METADATA.get(ep_id)
    if not meta:
        return

    # 1. Clean emojis first
    text = clean_emojis(text)

    # 2. Extract Title
    title_m = re.search(r'^#\s+(.+)$', text, re.MULTILINE)
    title = title_m.group(1).strip() if title_m else "Portland Desk Lab"

    # 3. Replace the intimidating top blockquote and At a Glance table with Shift Briefing + Collapsed Instructor Drawer
    # Find start of blockquote and end of At a Glance section (before ## 1.)
    pattern = r'(> \*\*Track:\*\*.*?\n\n## At a [Gg]lance\s*\n\s*\|[^\n]+\|\s*\n\s*\|[-: |]+\|\s*\n.*?\n---)'
    
    new_header = f"""> **The Situation:** {meta['setting']}  
> **Your Role:** {meta['role']}  
> **The Objective:** {meta['goal']}  
> **Estimated Time:** {meta['duration']}  

---

<details class="instructor-ref">
<summary>Instructor & Certification Reference (Click to Expand)</summary>

* **Aligned Certification:** {meta['cert']}
* **Exam Domains:** {meta['domains']}
* **Core Competencies & Deliverables:** {meta['deliverables']}

</details>

---"""

    match = re.search(pattern, text, re.DOTALL)
    if match:
        text = text[:match.start()] + new_header + text[match.end():]
    else:
        # Fallback for slightly different blockquote pattern
        alt_pattern = r'(> \*\*Track:\*\*.*?\n\n## At a [Gg]lance\s*\n.*?\n---)'
        alt_match = re.search(alt_pattern, text, re.DOTALL)
        if alt_match:
            text = text[:alt_match.start()] + new_header + text[alt_match.end():]

    # 4. Insert interactive scratchpad in Call Your Shot section
    # Look for "### Quick Check 3: Call Your Shot"
    cbyt_pattern = r'(### Quick Check 3:.*?\n\n)(.*?)(?=\n#### Case|\n#### Ticket)'
    cbyt_match = re.search(cbyt_pattern, text, re.DOTALL)
    if cbyt_match and "scratchpad-container" not in text:
        scratchpad_html = f"""<div class="scratchpad-container">
  <div class="scratchpad-header">
    <span class="scratchpad-title">Interactive Hypothesis Scratchpad</span>
    <span class="scratchpad-save-indicator" id="save-ind-{ep_id}-cbyt">Saved in browser</span>
  </div>
  <div class="scratchpad-body">
    <textarea id="notes-{ep_id}-cbyt" placeholder="Type your predicted failure layer, expected command output, and root cause hypothesis here before opening solutions..."></textarea>
  </div>
  <div class="scratchpad-footer">
    <span>Private notes saved locally in your browser. Not graded.</span>
    <button type="button" class="scratchpad-copy-btn" onclick="copyScratchpad('notes-{ep_id}-cbyt')">Copy Notes</button>
  </div>
</div>\n\n"""
        text = text[:cbyt_match.end(1)] + cbyt_match.group(2) + scratchpad_html + text[cbyt_match.end():]

    # 5. Insert interactive scratchpad in Section 4 (Ticket Notes)
    sec4_pattern = r'(## 4\. Your Ticket Notes.*?\n\n)(.*?)(?=\n###|\n```|\n|)'
    sec4_match = re.search(sec4_pattern, text, re.DOTALL)
    if sec4_match and f"notes-{ep_id}-ticket" not in text:
        ticket_scratchpad = f"""<div class="scratchpad-container">
  <div class="scratchpad-header">
    <span class="scratchpad-title">Your Ticket Draft & Resolution Scratchpad</span>
    <span class="scratchpad-save-indicator" id="save-ind-{ep_id}-ticket">Saved in browser</span>
  </div>
  <div class="scratchpad-body">
    <textarea id="notes-{ep_id}-ticket" style="min-height: 140px;" placeholder="Draft your ticket notes, diagnosis, and resolution steps here before comparing with the reference standard below..."></textarea>
  </div>
  <div class="scratchpad-footer">
    <span>Private notes saved locally in your browser. Not graded.</span>
    <button type="button" class="scratchpad-copy-btn" onclick="copyScratchpad('notes-{ep_id}-ticket')">Copy Notes</button>
  </div>
</div>\n\n"""
        insert_pos = sec4_match.end(1)
        text = text[:insert_pos] + ticket_scratchpad + text[insert_pos:]

    # 6. Ensure strict blank lines before tables
    # Any line with |---| should have a header above it, and the line above header must be blank
    lines = text.splitlines()
    fixed_lines = []
    for i, line in enumerate(lines):
        if re.match(r'^\s*\|?\s*[-:]+[-| :]+\s*\|?\s*$', line):
            # Previous line was header
            if len(fixed_lines) >= 2:
                prev_line = fixed_lines[-2]
                if prev_line.strip() and not prev_line.strip().startswith('#') and not prev_line.strip().startswith('---'):
                    # Insert blank line before header
                    header = fixed_lines.pop()
                    fixed_lines.append('')
                    fixed_lines.append(header)
        fixed_lines.append(line)

    text = '\n'.join(fixed_lines) + '\n'

    file_path.write_text(text, encoding='utf-8')
    print(f"Refactored: {file_path}")

def clean_narrative_file(file_path: Path):
    text = file_path.read_text(encoding='utf-8')
    cleaned = clean_emojis(text)
    if cleaned != text:
        file_path.write_text(cleaned, encoding='utf-8')
        print(f"Cleaned emojis: {file_path}")

def main():
    for root_dir in [BASE_DIR / 'portland-desk', BASE_DIR / 'docs' / 'portland-desk']:
        if not root_dir.exists():
            continue
        
        # Clean narratives
        for nf in root_dir.glob('narrative/*.md'):
            clean_narrative_file(nf)
        
        # Clean README and _sidebar
        clean_narrative_file(root_dir / 'README.md')
        clean_narrative_file(root_dir / '_sidebar.md')

        # Refactor workbenches
        for wf in sorted(root_dir.glob('workbench/*.md')):
            ep_id = wf.name[:2]
            refactor_workbench_file(wf, ep_id)

    print("All 13 modules updated with Shift Briefing cards, scratchpads, and emoji removal.")

if __name__ == '__main__':
    main()
