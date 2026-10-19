#!/usr/bin/env python3
"""Apply vocabulary ruleset to Portland Desk narratives.

Removes excessive marks on everyday, atmospheric, or redundant words,
retaining 10-18 high-value exam and analytical concepts per episode.
DOES NOT rewrite any prose text - only changes [[term_id|text]] -> text.
"""

import re
from pathlib import Path

KIT_ROOT = Path(__file__).resolve().parent.parent

# Set of IDs to strictly unmark across the courseware (common office / atmosphere / noise words)
GLOBAL_UNMARK_IDS = {
    "ticket", "help_desk", "password", "pin", "identification", "authentication",
    "single_factor", "somewhere_you_are", "password_age", "password_expiration",
    "password_length", "password_complexity", "password_reuse", "password_manager",
    "soft_token", "hard_token", "security_key", "backup_codes", "push_notification",
    "shoulder_surfing", "offboarding", "provisioning", "deprovisioning",
    "shared_admin_account", "vaulting", "accounting", "break_glass", "just_in_time",
    "authorization", "privileged_access", "passwordless", "federation",
    "msp", "vlan", "port", "protocol", "protocols", "firewall", "perimeter",
    "change_ticket", "tcp", "udp", "domain", "directory_bind", "guest_wifi",
    "community_string", "syslog", "authz", "aaa", "tftp", "open_relay",
    "ransomware", "http", "https", "network", "packet", "concentrator", "jump_host",
    "phishing_url", "urgency", "phish_report_button", "mail_gateway", "user_reported",
    "malware_attachment", "authority", "spoofing", "impersonation", "invoice_scam",
    "soc", "pretexting", "familiarity", "scarcity", "consensus", "tailgating",
    "dumpster_diving", "sandbox", "hoax", "reporting_path", "influence_campaigns",
    "social_engineering", "quarantine", "malware", "malware_scan", "isolate",
    "do_not_pay", "offline_backup", "process_list", "network_share", "removable_media",
    "signal_strength", "certificate", "open_network", "vpn", "access_point",
    "controller", "war_driving", "ap_placement", "bluetooth", "bluetooth_pairing",
    "replay_attack", "segmentation", "hidden_ssid", "mac_filtering"
}

def clean_file(path: Path):
    if not path.is_file():
        return
    text = path.read_text(encoding="utf-8")
    original = text
    seen_ids = set()

    def replace_mark(match):
        tid = match.group(1)
        surface = match.group(2) if match.group(2) else tid

        # Rule 1: Always unmark global noise/everyday words
        if tid in GLOBAL_UNMARK_IDS:
            return surface

        # Rule 2: Keep only first occurrence of each technical term to avoid mid-scene spam
        if tid in seen_ids:
            return surface

        seen_ids.add(tid)
        return match.group(0)

    # Match [[id|surface]] or [[id]]
    pattern = re.compile(r"\[\[([a-zA-Z0-9_-]+)(?:\|([^\]]+))?\]\]")
    cleaned = pattern.sub(replace_mark, text)

    if cleaned != original:
        path.write_text(cleaned, encoding="utf-8")
        before_count = len(pattern.findall(original))
        after_count = len(pattern.findall(cleaned))
        print(f"Cleaned {path.name}: {before_count} -> {after_count} marks")

def main():
    targets = [
        "07-the-port-that-is-open.md",
        "08-prove-who-you-are.md",
        "09-dont-click-that.md",
        "10-something-on-the-box.md",
        "11-the-air-is-shared.md"
    ]
    for filename in targets:
        clean_file(KIT_ROOT / "portland-desk" / "narrative" / filename)
        clean_file(KIT_ROOT / "docs" / "portland-desk" / "narrative" / filename)

if __name__ == "__main__":
    main()
