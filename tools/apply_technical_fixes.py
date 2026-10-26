#!/usr/bin/env python3
"""Technical fixes and cast disambiguation across Portland Desk courseware."""

import re
from pathlib import Path
import shutil

ROOT = Path(r"C:\Users\charl\learning-narrative-kit")
PORTLAND = ROOT / "portland-desk"
DOCS = ROOT / "docs" / "portland-desk"

def fix_ep04():
    for base in [PORTLAND, DOCS]:
        for sub in ["narrative", "workbench"]:
            f = base / sub / "04-the-name-is-not-the-number.md"
            if not f.exists(): continue
            text = f.read_text(encoding="utf-8")
            
            # Disambiguate Maya Chen -> Lena Chen
            text = text.replace("Maya Chen", "Lena Chen")
            
            # In narrative, fix GoDaddy park page
            if sub == "narrative":
                godaddy_old = "Instead, the browser spun for five seconds and displayed a bright orange GoDaddy parked domain page. The page announced that `harrowmere.local` was available for purchase or had no active web host configured."
                godaddy_new = "Instead, the browser spun for five seconds, timed out, and displayed a connection failure: `DNS_PROBE_FINISHED_NXDOMAIN`. The browser reported that the server IP address could not be found."
                text = text.replace(godaddy_old, godaddy_new)
                
                # Replace standalone "Maya said", "Maya asked", "Maya explained" in Ep 04
                text = text.replace('"And what does his home router do when a client asks it to resolve an unfamiliar internal host?" Maya asked.',
                                    '"And what does his home router do when a client asks it to resolve an unfamiliar internal host?" Lena asked.')
                text = text.replace('"Now look at what happens when Greg tries to browse the public corporate domain name," Maya said.',
                                    '"Now look at what happens when Greg tries to browse the public corporate domain name," Lena said.')
                text = text.replace('"We use [[split_dns|split-horizon DNS]] for all of our regional infrastructure," Maya explained.',
                                    '"We use [[split_dns|split-horizon DNS]] for all of our regional infrastructure," Lena explained.')
            
            f.write_text(text, encoding="utf-8")
    print("Fixed Episode 04 (Lena Chen & GoDaddy removal).")

def fix_ep06():
    for base in [PORTLAND, DOCS]:
        f = base / "narrative" / "06-the-portland-flood.md"
        text = f.read_text(encoding="utf-8")
        
        old_cmd = "Get-DhcpServerv4Scope -ScopeId 10.20.10.0 | Format-List ScopeId, Free, InUse, State\n\nScopeId : 10.20.10.0\nFree    : 0\nInUse   : 200\nState   : Active"
        new_cmd = "Get-DhcpServerv4ScopeStatistics -ScopeId 10.20.10.0 | Format-List ScopeId, Free, InUse, PercentageInUse\n\nScopeId         : 10.20.10.0\nFree            : 0\nInUse           : 200\nPercentageInUse : 100"
        
        assert old_cmd in text, "Old DHCP command not found in Ep 06 narrative"
        text = text.replace(old_cmd, new_cmd)
        f.write_text(text, encoding="utf-8")
    print("Fixed Episode 06 DHCP statistics cmdlet.")

def fix_ep03():
    for base in [PORTLAND, DOCS]:
        f = base / "narrative" / "03-the-default-gateway-doesnt-care.md"
        text = f.read_text(encoding="utf-8")
        
        # 1. WS-BLDGB-04 gets .54 instead of .55
        text = text.replace("IPv4 Address: 10.100.4.55\n   Subnet Mask: 255.255.255.0\n   Default Gateway: 10.100.4.1",
                            "IPv4 Address: 10.100.4.54\n   Subnet Mask: 255.255.255.0\n   Default Gateway: 10.100.4.1")
        
        # 2. DORA wording fix
        text = text.replace('"The machine executed the [[dhcp_dora|DHCP DORA]] exchange during system boot," I realized. I traced the four-step protocol exchange in my head. "The client broadcasted a DHCP Discover frame across the local wire. No server returned an Offer before the timer expired. The operating system assigned itself a link-local address so adjacent devices could still exchange frames."',
                            '"The client broadcast DHCP Discover frames during boot," I realized. "No server returned an Offer before the timer expired, so the DORA exchange failed and Windows fell back to an [[apipa_address|APIPA]] link-local address."')
        
        # 3. CAM / MAC table fix
        cam_old = """```console
SW-BLDGB-DIST01# show ip arp 10.100.4.55
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  10.100.4.55             0   0014.228a.41ef  ARPA   Vlan4
```

"Look at the CAM table," Jared said, pointing to the console output as the MAC address table flapped between ports. "Frank's Dell desktop is on port GigabitEthernet1/0/12. But someone has a Hewlett-Packard network interface plugged into port GigabitEthernet1/0/28 answering to the exact same IP."

"Duplicate IP conflict," Jules said, leaning back. "Every time one of them talks, its ARP announcement overwrites the switch's MAC address table and poisons the ARP cache on neighboring PCs. Traffic flips back and forth depending on who spoke last."

Jared Lindqvist checked the DHCP server scope logs. "Our DHCP server leased `10.100.4.55` to Frank's Dell during the morning renewal. That means the second device has a hardcoded static IP sitting squarely inside our dynamic pool. If that rogue box keeps broadcasting, it'll bounce the whole dock off the network before the noon freight trucks get here.\""""

        cam_new = """```console
SW-BLDGB-DIST01# show ip arp 10.100.4.55
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  10.100.4.55             0   0014.228a.41ef  ARPA   Vlan4

SW-BLDGB-DIST01# show mac address-table address 0014.228a.41ef
Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
   4    0014.228a.41ef    DYNAMIC     Gi1/0/12

SW-BLDGB-DIST01# show mac address-table address 0025.b318.c290
Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
   4    0025.b318.c290    DYNAMIC     Gi1/0/28
```

"ARP proves two physical MACs are fighting over IP ten-dot-one-hundred-dot-four-dot-fifty-five," Jared said, tapping the terminal. "And the switch MAC address table tells us the ports: Frank's Dell desktop is patched into GigabitEthernet1/0/12, but someone plugged a Hewlett-Packard network card into GigabitEthernet1/0/28 with the exact same IP hardcoded."

"Duplicate IP conflict," Jules said, leaning back. "Every time one of them talks, its gratuitous ARP announcement poisons the switch MAC table and the ARP cache on neighboring PCs. Traffic flips back and forth depending on who spoke last."

Jared Lindqvist checked the DHCP server scope logs. "Our DHCP server leased `10.100.4.55` to Frank's Dell during the morning renewal. That means the second device has a hardcoded static IP sitting squarely inside our dynamic pool. If that rogue box keeps broadcasting, it will bounce the whole dock off the network before the noon freight trucks get here.\""""

        assert cam_old in text, "CAM old block not found in Ep 03"
        text = text.replace(cam_old, cam_new)
        f.write_text(text, encoding="utf-8")
    print("Fixed Episode 03 (IP continuity & ARP/MAC table separation).")

def fix_act3_ken_disambiguation():
    # Disambiguate "Ken in sales" -> "Todd in sales" / "Todd Miller"
    files = [
        "narrative/08-prove-who-you-are.md",
        "workbench/08-prove-who-you-are.md",
        "narrative/09-dont-click-that.md",
        "workbench/09-dont-click-that.md",
        "narrative/10-something-on-the-box.md",
        "workbench/10-something-on-the-box.md",
        "narrative/11-the-air-is-shared.md",
        "workbench/11-the-air-is-shared.md",
        "narrative/12-when-the-ticket-escalates.md",
        "workbench/12-when-the-ticket-escalates.md",
    ]
    for base in [PORTLAND, DOCS]:
        for fname in files:
            f = base / fname
            if not f.exists(): continue
            text = f.read_text(encoding="utf-8")
            
            # Replace sales Ken with Todd / Todd Miller
            text = text.replace("Ken in sales", "Todd in sales")
            text = text.replace("Ken from sales", "Todd from sales")
            text = text.replace("Ken and the MFA", "Todd and the MFA")
            text = text.replace("Ken Vance (Sales", "Todd Miller (Sales")
            text = text.replace("Ken Vance in Sales", "Todd Miller in Sales")
            text = text.replace("KEN-SALES-14", "TODD-SALES-14")
            text = text.replace("ken.lee", "todd.miller")
            text = text.replace("kvance@portland-ops.org (Warehouse", "tmiller@portland-ops.org (Inside Sales")
            text = text.replace("Ken was enrolled", "Todd was enrolled")
            text = text.replace("Ken's enrollment", "Todd's enrollment")
            text = text.replace("Ken's phone", "Todd's phone")
            text = text.replace("Ken's laptop", "Todd's laptop")
            text = text.replace("Ken's machine", "Todd's machine")
            text = text.replace("Ken's USB", "Todd's USB")
            text = text.replace("Ken's CRM", "Todd's CRM")
            text = text.replace("Ken plugged", "Todd plugged")
            text = text.replace("Ken ignored the text", "Todd ignored the text")
            text = text.replace("Ken from the warehouse annex", "Todd from inside sales")
            
            f.write_text(text, encoding="utf-8")
    print("Disambiguated Act 3 sales rep to Todd Miller across all Act 3 files.")

if __name__ == "__main__":
    fix_ep04()
    fix_ep06()
    fix_ep03()
    fix_act3_ken_disambiguation()
