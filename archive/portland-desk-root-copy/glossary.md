# Master Technical Glossary & Domain Reference
*Comprehensive Tier 1 IT Support & Security Operations Reference • CompTIA A+, Network+, and Security+ Alignments*
> [!TIP]
> Use **Ctrl+F** to search instantly, or click a letter below to jump directly to a concept section. Clicking any highlighted term in an incident narrative or hands-on lab navigates directly to its entry below.

### Alphabetical Index

[A](#a) · [B](#b) · [C](#c) · [D](#d) · [E](#e) · [F](#f) · [G](#g) · [H](#h) · [I](#i) · [J](#j) · [K](#k) · [L](#l) · [M](#m) · [N](#n) · [O](#o) · [P](#p) · [Q](#q) · [R](#r) · [S](#s) · [T](#t) · [U](#u) · [V](#v) · [W](#w)

---

## #

<div class="glossary-entry-card" id="term-ieee_8021x">

### 802.1X <span class="glossary-card-badge">EXAM</span>

**Definition:** Port-based network access control — authenticate before full network access; used for enterprise Wi-Fi and wired NAC.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — 802.1X

**Tags:** `#wireless` `#auth`

</div>

---

## A

<div class="glossary-entry-card" id="term-aaa">

### AAA <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Authentication, Authorization, and Accounting — proving identity, deciding what you may do, and logging what you did.

**Tags:** `#support` `#aaa`

</div>

---

<div class="glossary-entry-card" id="term-access_badge">

### Access badge <span class="glossary-card-badge">EXAM</span>

**Definition:** Credential (card, fob, or phone token) presented to readers to open doors for authorized people.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — badges / access cards

**Tags:** `#physical` `#access`

</div>

---

<div class="glossary-entry-card" id="term-access_point">

### Access point (AP) <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Device that bridges wireless clients onto the wired LAN — the radio end of corporate Wi-Fi.

**Tags:** `#support` `#wireless`

</div>

---

<div class="glossary-entry-card" id="term-account_lockout">

### Account lockout <span class="glossary-card-badge">EXAM</span>

**Definition:** Temporarily disabling an account after too many failed authentication attempts to slow password guessing.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — account policies / lockout

**Tags:** `#account` `#policy`

</div>

---

<div class="glossary-entry-card" id="term-accounting">

### Accounting <span class="glossary-card-badge">EXAM</span>

**Definition:** Recording what an authenticated identity did — logs, sessions, and audit trails (the third A in AAA).

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — AAA / auditing

**Tags:** `#aaa`

</div>

---

<div class="glossary-entry-card" id="term-adware">

### Adware <span class="glossary-card-badge">EXAM</span>

**Definition:** Unwanted software that pushes ads, redirects browsing, or tracks habits for advertising — often bundled with free installs.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — adware

**Tags:** `#malware` `#pups`

</div>

---

<div class="glossary-entry-card" id="term-air_gap">

### Air gap <span class="glossary-card-badge">EXAM</span>

**Definition:** Keeping a system physically isolated from other networks — no cable, no Wi-Fi, no convenient USB bridge.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — air gap

**Tags:** `#physical` `#architecture`

</div>

---

<div class="glossary-entry-card" id="term-alarm_system">

### Alarm system <span class="glossary-card-badge">EXAM</span>

**Definition:** Sensors and signaling that notify people of unauthorized entry, door forced open, or other physical events.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — alarms

**Tags:** `#physical` `#detection`

</div>

---

<div class="glossary-entry-card" id="term-antivirus">

### Antivirus / antimalware <span class="glossary-card-badge">EXAM</span>

**Definition:** Endpoint software that detects, blocks, quarantines, or removes known and suspicious malicious code.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — antivirus / antimalware

**Tags:** `#defense`

</div>

---

<div class="glossary-entry-card" id="term-ap_placement">

### AP placement <span class="glossary-card-badge">EXAM</span>

**Definition:** Where access points sit and how loud they transmit — affects coverage, leakage outside the building, and attack surface.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — access point placement / power levels

**Tags:** `#wireless` `#design`

</div>

---

<div class="glossary-entry-card" id="term-apipa_address">

### APIPA (Automatic Private IP Addressing) <span class="glossary-card-badge">EXAM</span>

**Definition:** A link-local IPv4 address autoconfiguration mechanism where a host assigns itself an address in the 169.254.0.1 to 169.254.255.254 range when a DHCP server fails to respond.

**Operational Context:** *Indicates that physical Layer 1 and 2 links are operational, but DHCP DORA broadcast discovery failed to cross the local broadcast domain or VLAN trunk.*

**Certification & Domain Reference:**
- CompTIA Network+ N10-008 Domain 1.4 — IPv4 addressing and link-local autoconfiguration
- CompTIA Network+ N10-009 Domain 4.1 — Troubleshooting IP configuration and DHCP failures

**Tags:** `#ipv4` `#dhcp` `#troubleshooting` `#network-plus`

</div>

---

<div class="glossary-entry-card" id="term-arp_cache">

### ARP Cache <span class="glossary-card-badge">EXAM</span>

**Definition:** A volatile local operating system table that maps Layer 3 IPv4 addresses to their corresponding Layer 2 physical MAC addresses for hosts on the local network segment.

**Operational Context:** *Inspected via `arp -a`, entries expire dynamically to reflect network changes, but can be poisoned or cause flapping during duplicate IP address conflicts.*

**Certification & Domain Reference:**
- CompTIA Network+ N10-008 Domain 1.4 — Address Resolution Protocol and MAC binding
- CompTIA Network+ N10-009 Domain 4.1 — Diagnosing duplicate IPs and Layer 2 flapping

**Tags:** `#arp` `#layer2` `#layer3` `#troubleshooting` `#network-plus`

</div>

---

<div class="glossary-entry-card" id="term-asymmetric">

### Asymmetric encryption <span class="glossary-card-badge">EXAM</span>

**Definition:** Key pair model — public key encrypts or verifies; private key decrypts or signs.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — asymmetric / public-key cryptography

**Tags:** `#crypto`

</div>

---

<div class="glossary-entry-card" id="term-authentication">

### Authentication <span class="glossary-card-badge">EXAM</span>

**Definition:** Proving a claimed identity is genuine — typically with something you know, have, or are.

**Operational Context:** *Distinct from authorization (what you may do after you prove who you are).*

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — authentication methods / identity

**Tags:** `#aaa` `#identity`

</div>

---

<div class="glossary-entry-card" id="term-authenticator_app">

### Authenticator app <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Phone or desktop app that holds soft-token secrets and shows rotating TOTP codes (or push prompts).

**Tags:** `#support` `#mfa`

</div>

---

<div class="glossary-entry-card" id="term-authority">

### Authority <span class="glossary-card-badge">EXAM</span>

**Definition:** Claiming power (executive, IT admin, law enforcement, vendor) so people comply without checking.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — social engineering principles (authority)

**Tags:** `#principles`

</div>

---

<div class="glossary-entry-card" id="term-authorization">

### Authorization <span class="glossary-card-badge">EXAM</span>

**Definition:** Deciding what an authenticated identity is allowed to do (permissions, roles, resources).

**Operational Context:** *Often shortened to authz; not the same as authentication.*

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — authorization / access control

**Tags:** `#aaa` `#access`

</div>

---

<div class="glossary-entry-card" id="term-authz">

### Authorization (authz) <span class="glossary-card-badge">SUPPORT</span>

**Definition:** What an authenticated user or device is allowed to do (distinct from authentication).

**Tags:** `#support` `#aaa`

</div>

---

## B

<div class="glossary-entry-card" id="term-backdoor">

### Backdoor <span class="glossary-card-badge">EXAM</span>

**Definition:** A hidden way into a system that bypasses normal authentication — planted by malware or a malicious insider.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — backdoor

**Tags:** `#malware` `#access`

</div>

---

<div class="glossary-entry-card" id="term-backup_codes">

### Backup codes <span class="glossary-card-badge">SUPPORT</span>

**Definition:** One-time recovery codes issued at MFA enrollment for when the phone or token is unavailable.

**Tags:** `#support` `#mfa`

</div>

---

<div class="glossary-entry-card" id="term-badge_reader">

### Badge reader <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Door hardware that accepts a badge or PIN and signals the lock to open when policy allows.

**Tags:** `#support` `#physical`

</div>

---

<div class="glossary-entry-card" id="term-barricade">

### Barricade <span class="glossary-card-badge">EXAM</span>

**Definition:** Temporary or permanent obstacle used to control vehicle or crowd movement around a site.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — barricades

**Tags:** `#physical` `#perimeter`

</div>

---

<div class="glossary-entry-card" id="term-base64">

### Base64 <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Common encoding that turns binary into ASCII-safe text — looks 'scrambled' but is not encryption.

**Tags:** `#support` `#crypto`

</div>

---

<div class="glossary-entry-card" id="term-baud_rate">

### Baud Rate <span class="glossary-card-badge">EXAM</span>

**Definition:** The rate at which signal states or electrical symbols change per second along a serial communication channel, requiring matching transmitter and receiver clocking.

**Operational Context:** *In binary serial links, a mismatch between sender and receiver baud rates creates severe frame desynchronization and unreadable garbled characters.*

**Certification & Domain Reference:**
- CompTIA A+ Core 1 (220-1101) Objective 3.4: Troubleshoot peripheral interfaces and communications

**Tags:** `#serial` `#communication`

</div>

---

<div class="glossary-entry-card" id="term-biometrics">

### Biometrics (door) <span class="glossary-card-badge">EXAM</span>

**Definition:** Unlocking with something you are — fingerprint, face, iris — often combined with a badge or PIN.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — biometrics

**Tags:** `#physical` `#access`

</div>

---

<div class="glossary-entry-card" id="term-bitlocker_recovery">

### BitLocker Recovery Key <span class="glossary-card-badge">EXAM</span>

**Definition:** A 48-digit numerical password required to unlock a BitLocker-encrypted volume when platform configuration registers (PCRs) detect hardware or firmware changes.

**Operational Context:** *Stored in Active Directory or Azure AD and released to users only after out-of-band identity verification to prevent unauthorized data access.*

**Certification & Domain Reference:**
- CompTIA A+ Core 2 (220-1102) Objective 2.8

**Tags:** `#security` `#encryption`

</div>

---

<div class="glossary-entry-card" id="term-bluejacking">

### Bluejacking <span class="glossary-card-badge">EXAM</span>

**Definition:** Sending unsolicited messages to nearby Bluetooth devices — annoying spam more than full takeover.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — bluejacking

**Tags:** `#bluetooth`

</div>

---

<div class="glossary-entry-card" id="term-bluesnarfing">

### Bluesnarfing <span class="glossary-card-badge">EXAM</span>

**Definition:** Unauthorized access to data on a Bluetooth device — contacts, messages, files — when pairing/security is weak.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — bluesnarfing

**Tags:** `#bluetooth`

</div>

---

<div class="glossary-entry-card" id="term-bluetooth">

### Bluetooth <span class="glossary-card-badge">EXAM</span>

**Definition:** Short-range wireless for peripherals and phones — convenient, and a side channel if pairing is careless.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — Bluetooth risks

**Tags:** `#bluetooth`

</div>

---

<div class="glossary-entry-card" id="term-bluetooth_pairing">

### Bluetooth pairing hygiene <span class="glossary-card-badge">EXAM</span>

**Definition:** Only pair expected devices, prefer confirm codes, turn discovery off when idle — desk-level Bluetooth risk control.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — Bluetooth security practices

**Tags:** `#bluetooth`

</div>

---

<div class="glossary-entry-card" id="term-bollards">

### Bollards <span class="glossary-card-badge">EXAM</span>

**Definition:** Short posts that stop or slow vehicles from ramming doors, glass, or loading docks.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — bollards

**Tags:** `#physical` `#perimeter`

</div>

---

<div class="glossary-entry-card" id="term-bot">

### Bot <span class="glossary-card-badge">EXAM</span>

**Definition:** A compromised device under remote attacker control, waiting for commands.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — bots / botnets

**Tags:** `#malware` `#botnet`

</div>

---

<div class="glossary-entry-card" id="term-botnet">

### Botnet <span class="glossary-card-badge">EXAM</span>

**Definition:** A network of bots controlled together — used for spam, DDoS, crypto-mining, or further compromise.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — botnet

**Tags:** `#malware` `#botnet`

</div>

---

<div class="glossary-entry-card" id="term-brand_impersonation">

### Brand impersonation <span class="glossary-card-badge">EXAM</span>

**Definition:** Copying logos, themes, and wording of a known company so a fake message or site feels official.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — brand impersonation / phishing indicators

**Tags:** `#indicators`

</div>

---

<div class="glossary-entry-card" id="term-break_glass">

### Break-glass account <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Emergency privileged account for outages when normal MFA/IdP paths fail — tightly vaulted and audited.

**Tags:** `#support` `#privilege`

</div>

---

<div class="glossary-entry-card" id="term-broadcast_domain">

### Broadcast Domain <span class="glossary-card-badge">EXAM</span>

**Definition:** A logical division of a computer network within which all connected nodes can reach each other by Layer 2 broadcast transmission.

**Operational Context:** *Bounded by Layer 3 routers and separated by VLAN configurations on switches; DHCP Discover and ARP request broadcasts are confined within this boundary.*

**Certification & Domain Reference:**
- CompTIA Network+ N10-008 Domain 1.4 — Broadcast domains, collision domains, and VLAN segmentation
- CompTIA Network+ N10-009 Domain 2.1 — Switching features and VLAN trunking

**Tags:** `#vlan` `#switching` `#layer2` `#network-plus`

</div>

---

<div class="glossary-entry-card" id="term-browser_padlock">

### Browser padlock <span class="glossary-card-badge">SUPPORT</span>

**Definition:** UI hint that the page is using HTTPS/TLS — not a guarantee the site is honest, only that the channel looks encrypted to a trusted name.

**Tags:** `#support` `#browser`

</div>

---

<div class="glossary-entry-card" id="term-bec">

### Business email compromise (BEC) <span class="glossary-card-badge">EXAM</span>

**Definition:** Fraud that hijacks or fakes business email threads — often to redirect payments or steal wire instructions.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — BEC / business email compromise

**Tags:** `#phishing` `#fraud`

</div>

---

## C

<div class="glossary-entry-card" id="term-cable_lock">

### Cable lock <span class="glossary-card-badge">EXAM</span>

**Definition:** Physical lock that tethers a laptop to furniture so walk-away theft is harder.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — cable locks

**Tags:** `#physical` `#endpoint`

</div>

---

<div class="glossary-entry-card" id="term-captive_portal">

### Captive portal <span class="glossary-card-badge">EXAM</span>

**Definition:** Web login/splash page before internet access — common on guest Wi-Fi; not a substitute for strong link encryption by itself.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — captive portal / guest access

**Tags:** `#wireless` `#guest`

</div>

---

<div class="glossary-entry-card" id="term-cctv">

### CCTV / cameras <span class="glossary-card-badge">EXAM</span>

**Definition:** Video surveillance that records and deters — useful for investigation when retention and coverage are planned.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — cameras / CCTV

**Tags:** `#physical` `#detection`

</div>

---

<div class="glossary-entry-card" id="term-certificate_pinning">

### Certificate / public-key pinning <span class="glossary-card-badge">EXAM</span>

**Definition:** Client remembers an expected cert or key and rejects surprises — stronger against some MitM, brittle when pins go stale.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — certificate pinning

**Tags:** `#pki` `#tls`

</div>

---

<div class="glossary-entry-card" id="term-ca">

### Certificate authority (CA) <span class="glossary-card-badge">EXAM</span>

**Definition:** Trusted issuer that signs certificates after validating identity — the root of many trust decisions.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — certificate authority

**Tags:** `#pki`

</div>

---

<div class="glossary-entry-card" id="term-certificate_chain">

### Certificate chain <span class="glossary-card-badge">EXAM</span>

**Definition:** Path from end-entity certificate through intermediate CA(s) to a trusted root — missing links break trust.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — certificate chain / chaining

**Tags:** `#pki`

</div>

---

<div class="glossary-entry-card" id="term-cert_warning">

### Certificate warning dialog <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Browser interstitial when TLS validation fails — expired, name mismatch, untrusted issuer, or broken chain.

**Tags:** `#support` `#browser`

</div>

---

<div class="glossary-entry-card" id="term-chain_of_custody">

### Chain of custody <span class="glossary-card-badge">EXAM</span>

**Definition:** Documented control of evidence — who had it, when, and what changed — so findings stay credible and you do not casually wipe a laptop IR still needs.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — chain of custody

**Tags:** `#ir` `#evidence`

</div>

---

<div class="glossary-entry-card" id="term-change_ticket">

### Change (change ticket) <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Tracked request to modify production systems (firewall rules, certs, configs) with review/approval.

**Tags:** `#support` `#ops`

</div>

---

<div class="glossary-entry-card" id="term-ciphertext">

### Ciphertext <span class="glossary-card-badge">EXAM</span>

**Definition:** Encrypted output — unreadable without the correct cryptographic key.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — plaintext / ciphertext

**Tags:** `#crypto`

</div>

---

<div class="glossary-entry-card" id="term-clean_boot">

### Clean Boot <span class="glossary-card-badge">EXAM</span>

**Definition:** An operating system startup state achieved by disabling all non-Microsoft background services and startup applications.

**Operational Context:** *Isolates third-party software conflicts through systematic binary elimination without disabling essential Windows core functions.*

**Certification & Domain Reference:**
- CompTIA A+ Core 2 (220-1102) Objective 1.4

**Tags:** `#troubleshooting` `#services`

</div>

---

<div class="glossary-entry-card" id="term-clean_desk">

### Clean desk policy <span class="glossary-card-badge">EXAM</span>

**Definition:** Requirement to clear sensitive papers and lock screens when leaving a workstation — no leftover secrets on the blotter.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — clean desk

**Tags:** `#physical` `#policy`

</div>

---

<div class="glossary-entry-card" id="term-cleartext">

### Cleartext <span class="glossary-card-badge">EXAM</span>

**Definition:** Data sent without encryption so anyone on the path can read or alter it, including credentials.

**Tags:** `#security`

</div>

---

<div class="glossary-entry-card" id="term-certificate">

### Client/server certificate (Wi-Fi) <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Credential material used in enterprise Wi-Fi so clients can verify the real RADIUS/network and not a twin.

**Tags:** `#support` `#auth`

</div>

---

<div class="glossary-entry-card" id="term-cname_record">

### CNAME Record <span class="glossary-card-badge">EXAM</span>

**Definition:** A Canonical Name record in DNS that aliases one domain name or subdomain to another fully qualified domain name rather than directly pointing to an IP address.

**Operational Context:** *Requires the resolving client to perform an additional lookup step to resolve the canonical target name, widely used for cloud service and CDN routing.*

**Certification & Domain Reference:**
- CompTIA Network+ N10-008 Domain 1.5 — Common DNS record types

**Tags:** `#dns` `#records`

</div>

---

<div class="glossary-entry-card" id="term-command_and_control">

### Command and control (C2) <span class="glossary-card-badge">EXAM</span>

**Definition:** The channel attackers use to send orders to compromised hosts and pull stolen data back out.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — command and control

**Tags:** `#c2` `#network`

</div>

---

<div class="glossary-entry-card" id="term-community_string">

### Community string <span class="glossary-card-badge">SUPPORT</span>

**Definition:** A shared secret in SNMPv1/v2c that acts like a password and is sent in cleartext.

**Tags:** `#support` `#monitor` `#security`

</div>

---

<div class="glossary-entry-card" id="term-consensus">

### Consensus (social proof) <span class="glossary-card-badge">EXAM</span>

**Definition:** Implying everyone else already complied — 'your teammates already clicked / updated / paid.'

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — social engineering principles (consensus / social proof)

**Tags:** `#principles`

</div>

---

<div class="glossary-entry-card" id="term-continuity_test">

### Continuity Test <span class="glossary-card-badge">EXAM</span>

**Definition:** An electrical test performed with a multimeter to verify an unbroken, low-resistance conduction path between two points in a circuit or conductor.

**Operational Context:** *Produces an audible tone when a continuous circuit exists, isolating severed copper traces, short circuits to chassis ground, or broken cable cores.*

**Certification & Domain Reference:**
- CompTIA A+ Core 1 (220-1101) Objective 3.1: Motherboard and cabling fault isolation

**Tags:** `#hardware` `#electrical`

</div>

---

<div class="glossary-entry-card" id="term-credential_harvesting">

### Credential harvesting <span class="glossary-card-badge">EXAM</span>

**Definition:** Collecting usernames and passwords (or tokens) via fake login pages or forms.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — phishing / credential harvesting

**Tags:** `#phishing`

</div>

---

<div class="glossary-entry-card" id="term-vaulting">

### Credential vaulting <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Storing privileged passwords in a controlled vault with checkout, rotation, and audit — not a shared spreadsheet.

**Tags:** `#support` `#privilege`

</div>

---

<div class="glossary-entry-card" id="term-crypto_malware">

### Crypto-malware <span class="glossary-card-badge">EXAM</span>

**Definition:** Malware that encrypts files or volumes so victims cannot use their data without a key the attacker controls.

**Operational Context:** *Often the technical engine inside a ransomware incident.*

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — crypto-malware / ransomware

**Tags:** `#malware` `#ransomware`

</div>

---

<div class="glossary-entry-card" id="term-cryptojacking">

### Cryptojacking <span class="glossary-card-badge">EXAM</span>

**Definition:** Hijacking a system's CPU/GPU to mine cryptocurrency for the attacker without consent.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — cryptomalware / cryptojacking

**Tags:** `#malware` `#crypto`

</div>

---

<div class="glossary-entry-card" id="term-csirt">

### CSIRT / IR team <span class="glossary-card-badge">EXAM</span>

**Definition:** Computer Security Incident Response Team (or equivalent IR team) — specialists who own analysis, forensics coordination, and incident command after escalation.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — CSIRT / incident response team

**Tags:** `#ir`

</div>

---

<div class="glossary-entry-card" id="term-csr">

### CSR <span class="glossary-card-badge">EXAM</span>

**Definition:** Certificate signing request — package with your public key and identity details sent to a CA for signing.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — CSR

**Tags:** `#pki`

</div>

---

## D

<div class="glossary-entry-card" id="term-default_gateway">

### Default Gateway <span class="glossary-card-badge">EXAM</span>

**Definition:** A Layer 3 router interface on the local subnet to which a host forwards IP packets destined for remote networks outside its own broadcast domain.

**Operational Context:** *Hosts resolve the default gateway's Layer 2 MAC address via ARP and encapsulate outbound remote packets in Ethernet frames directed to that router interface.*

**Certification & Domain Reference:**
- CompTIA Network+ N10-008 Domain 1.4 — Default gateways and Layer 3 routing primitives
- CompTIA Network+ N10-009 Domain 4.1 — Troubleshooting routing and gateway reachability

**Tags:** `#routing` `#ipv4` `#gateway` `#network-plus`

</div>

---

<div class="glossary-entry-card" id="term-deprovisioning">

### Deprovisioning <span class="glossary-card-badge">EXAM</span>

**Definition:** Removing or disabling accounts and access when someone leaves or no longer needs them.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — account management / offboarding

**Tags:** `#lifecycle`

</div>

---

<div class="glossary-entry-card" id="term-device_driver">

### Device Driver <span class="glossary-card-badge">EXAM</span>

**Definition:** A specialized software program that allows the operating system kernel to communicate with and control physical hardware components.

**Operational Context:** *Corrupted or mismatched graphics drivers running in kernel space can lock the entire desktop when applications invoke hardware acceleration.*

**Certification & Domain Reference:**
- CompTIA A+ Core 2 (220-1102) Objective 1.1

**Tags:** `#hardware` `#kernel`

</div>

---

<div class="glossary-entry-card" id="term-dhcp">

### DHCP (67/68/UDP) <span class="glossary-card-badge">EXAM</span>

**Definition:** Assigns IP configuration. Server listens on 67; client on 68.

**Tags:** `#network`

</div>

---

<div class="glossary-entry-card" id="term-dhcp_dora">

### DHCP DORA Process <span class="glossary-card-badge">EXAM</span>

**Definition:** The four-step client-server state machine (Discover, Offer, Request, Acknowledge) used by Dynamic Host Configuration Protocol to automatically lease an IP address and network configuration to a client.

**Operational Context:** *Operates over UDP ports 67 (server) and 68 (client); requires a DHCP relay agent (ip helper-address) on routers when clients and DHCP servers occupy different broadcast domains.*

**Certification & Domain Reference:**
- CompTIA Network+ N10-008 Domain 1.4 — DHCP operation and address allocation
- CompTIA Network+ N10-009 Domain 1.4 — Network services and dynamic configuration

**Tags:** `#dhcp` `#udp` `#protocols` `#network-plus`

</div>

---

<div class="glossary-entry-card" id="term-dhcp_lease">

### DHCP lease <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Temporary IP configuration handed out by DHCP for a limited time.

**Tags:** `#support` `#network`

</div>

---

<div class="glossary-entry-card" id="term-dhcp_exhaustion">

### DHCP Scope Exhaustion <span class="glossary-card-badge">EXAM</span>

**Definition:** A network denial-of-service condition where a Dynamic Host Configuration Protocol scope has leased all available IP addresses in its configured allocation pool, preventing new or reconnecting devices from acquiring valid Layer 3 network parameters.

**Operational Context:** *Forces booting clients into APIPA link-local addresses (169.254.x.x); commonly occurs when massive device reconnect storms collide with excessively long lease durations.*

**Certification & Domain Reference:**
- CompTIA Network+ N10-008 Domain 1.4 & 4.1 — IPv4 addressing, DHCP pools, and troubleshooting IP assignment
- CompTIA Network+ N10-009 Domain 4.1 — Troubleshooting common network service failures

**Tags:** `#dhcp` `#ipv4` `#troubleshooting` `#network-plus`

</div>

---

<div class="glossary-entry-card" id="term-digital_signature">

### Digital signature <span class="glossary-card-badge">EXAM</span>

**Definition:** Private-key operation that proves origin and integrity of data — verifiers use the matching public key.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — digital signatures

**Tags:** `#crypto` `#pki`

</div>

---

<div class="glossary-entry-card" id="term-dip_switch">

### DIP Switch <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Dual in-line package manual electrical switches mounted on a printed circuit board to configure hardware parameters and operational modes directly.

**Operational Context:** *Commonly used on embedded motherboards, industrial scales, and expansion cards to configure baud rates, hardware addresses, or bus timings without software.*

**Certification & Domain Reference:**
- CompTIA A+ Core 1 (220-1101) Objective 3.1: Motherboard configuration and embedded jumpers

**Tags:** `#hardware` `#embedded`

</div>

---

<div class="glossary-entry-card" id="term-directory_bind">

### Directory bind <span class="glossary-card-badge">SUPPORT</span>

**Definition:** An application authenticating/connecting to a directory service (like LDAP) to look up or validate accounts.

**Tags:** `#support` `#directory`

</div>

---

<div class="glossary-entry-card" id="term-disassociation">

### Disassociation / deauthentication <span class="glossary-card-badge">EXAM</span>

**Definition:** Wireless frames that kick clients off an AP — used in DoS or to force reconnects toward an evil twin.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — disassociation / deauthentication attacks

**Tags:** `#wireless` `#attack`

</div>

---

<div class="glossary-entry-card" id="term-dns">

### DNS (53/UDP/TCP) <span class="glossary-card-badge">EXAM</span>

**Definition:** Resolves names to addresses. UDP 53 for normal lookups; TCP 53 for zone transfers and large responses. Classic DNS is unencrypted.

**Tags:** `#name` `#insecure`

</div>

---

<div class="glossary-entry-card" id="term-dns_leak">

### DNS Leak <span class="glossary-card-badge">EXAM</span>

**Definition:** A network configuration flaw where DNS requests from a VPN-connected host are inadvertently transmitted across unencrypted local network adapters to a public resolver rather than through the secure VPN tunnel.

**Operational Context:** *Occurs frequently in split-tunneling VPN configurations when client multi-homed resolution logic prioritizes the local physical gateway over the virtual tunnel adapter.*

**Certification & Domain Reference:**
- CompTIA Network+ N10-008 Domain 4.2 — Troubleshooting remote access and VPN issues
- CompTIA Security+ SY0-701 Domain 2.5 — Secure remote access configurations

**Tags:** `#vpn` `#dns` `#security`

</div>

---

<div class="glossary-entry-card" id="term-dns_ttl">

### DNS TTL (Time-to-Live) <span class="glossary-card-badge">EXAM</span>

**Definition:** A numeric value configured in a DNS record that dictates the number of seconds a recursive resolver or client cache is permitted to store the record before requesting a fresh query.

**Operational Context:** *Lower values enable rapid zone updates during server migrations but increase server query load, while higher values prolong resolution delays during cutovers.*

**Certification & Domain Reference:**
- CompTIA Network+ N10-008 Domain 1.5 — DNS record parameters and caching

**Tags:** `#dns` `#caching` `#performance`

</div>

---

<div class="glossary-entry-card" id="term-do_not_pay">

### Do not pay (ransomware) <span class="glossary-card-badge">EXAM</span>

**Definition:** Organizational stance: do not pay the ransom — payment funds crime, may not restore data, and is not a recovery plan.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — ransomware response concepts

**Tags:** `#ransomware` `#response`

</div>

---

<div class="glossary-entry-card" id="term-domain">

### Domain <span class="glossary-card-badge">SUPPORT</span>

**Definition:** An administrative realm (often Active Directory) that shares authentication and policy.

**Tags:** `#support` `#directory`

</div>

---

<div class="glossary-entry-card" id="term-dropper">

### Dropper <span class="glossary-card-badge">EXAM</span>

**Definition:** A small malicious program whose job is to deliver and install other malware payloads.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — dropper / malware delivery

**Tags:** `#malware` `#delivery`

</div>

---

<div class="glossary-entry-card" id="term-dumpster_diving">

### Dumpster diving <span class="glossary-card-badge">EXAM</span>

**Definition:** Searching discarded paper or media for secrets — passwords, org charts, invoices, badges.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — dumpster diving

**Tags:** `#physical`

</div>

---

## E

<div class="glossary-entry-card" id="term-edr">

### EDR <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Endpoint detection and response — tooling that records process/network behavior and helps hunt or contain malware.

**Tags:** `#support` `#security`

</div>

---

<div class="glossary-entry-card" id="term-enable_password">

### Enable password <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Privileged password on network gear that unlocks administrative (enable) mode.

**Tags:** `#support` `#network`

</div>

---

<div class="glossary-entry-card" id="term-encoding">

### Encoding <span class="glossary-card-badge">EXAM</span>

**Definition:** Reversible representation change (like Base64) for transport or display — not confidentiality; anyone can decode.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — encoding vs encryption

**Tags:** `#crypto`

</div>

---

<div class="glossary-entry-card" id="term-encryption">

### Encryption <span class="glossary-card-badge">EXAM</span>

**Definition:** Transforming readable data into ciphertext so only parties with the right key can recover the original.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — encryption

**Tags:** `#crypto`

</div>

---

<div class="glossary-entry-card" id="term-ephemeral_port">

### Ephemeral Port <span class="glossary-card-badge">EXAM</span>

**Definition:** A dynamic, short-lived transport layer port assigned automatically by a client operating system from a high-numbered range (typically 49152 to 65535) to identify an outbound session.

**Operational Context:** *Combined with the client IP, destination IP, and destination port to forge the unique 4-tuple socket identifier required for bidirectional TCP session tracking.*

**Certification & Domain Reference:**
- CompTIA Network+ N10-008 Domain 1.4 — Port ranges and ephemeral dynamic assignment
- CompTIA Network+ N10-009 Domain 1.4 — Transport layer addressing and port allocations

**Tags:** `#tcp` `#ports` `#client` `#network-plus`

</div>

---

<div class="glossary-entry-card" id="term-port_exhaustion">

### Ephemeral Port Exhaustion <span class="glossary-card-badge">EXAM</span>

**Definition:** A state where a client operating system depletes its entire range of dynamic outbound ports, preventing any new outbound network connections from establishing.

**Operational Context:** *Frequently triggered by high-frequency scripts or automated backup jobs that rapidly open and close connections, stranding thousands of sockets in the TIME_WAIT state.*

**Certification & Domain Reference:**
- CompTIA Network+ N10-008 Domain 4.1 — Diagnosing socket and resource exhaustion
- CompTIA Network+ N10-009 Domain 4.1 — Troubleshooting network performance and socket bottlenecks

**Tags:** `#tcp` `#sockets` `#performance` `#troubleshooting` `#network-plus`

</div>

---

<div class="glossary-entry-card" id="term-escalation">

### Escalation <span class="glossary-card-badge">EXAM</span>

**Definition:** Handing an issue to a higher or more specialized team when criteria are met — with clean facts, not a Slack panic dump.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — escalation

**Tags:** `#ir`

</div>

---

<div class="glossary-entry-card" id="term-escort">

### Escort <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Authorized person who accompanies a visitor in restricted space so guests are never unattended.

**Tags:** `#support` `#physical`

</div>

---

<div class="glossary-entry-card" id="term-event">

### Event <span class="glossary-card-badge">EXAM</span>

**Definition:** An observable occurrence in a system or network — a login, alert, crash, or odd ticket — that may or may not be a security problem.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — events vs incidents

**Tags:** `#ir`

</div>

---

<div class="glossary-entry-card" id="term-event_viewer">

### Event Viewer <span class="glossary-card-badge">EXAM</span>

**Definition:** A Microsoft Management Console snap-in that logs system, application, and security messages, errors, and audit events.

**Operational Context:** *Provides authoritative timestamps and error codes (such as Event IDs 1000 and 41) that distinguish software crashes from kernel power cuts.*

**Certification & Domain Reference:**
- CompTIA A+ Core 2 (220-1102) Objective 1.4

**Tags:** `#logging` `#triage`

</div>

---

<div class="glossary-entry-card" id="term-evil_twin">

### Evil twin <span class="glossary-card-badge">EXAM</span>

**Definition:** Attacker access point that mimics a trusted SSID to trick clients into connecting and exposing traffic or credentials.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — evil twin

**Tags:** `#wireless` `#attack`

</div>

---

<div class="glossary-entry-card" id="term-expired_cert">

### Expired certificate <span class="glossary-card-badge">EXAM</span>

**Definition:** Certificate past its validity dates — browsers and clients correctly refuse or warn because trust has a calendar.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — certificate expiration / validation

**Tags:** `#pki`

</div>

---

## F

<div class="glossary-entry-card" id="term-facilities">

### Facilities <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Building ops team that owns doors, cameras, lighting, and badge hardware alongside IT policy.

**Tags:** `#support` `#physical`

</div>

---

<div class="glossary-entry-card" id="term-familiarity">

### Familiarity <span class="glossary-card-badge">EXAM</span>

**Definition:** Using known names, slang, or shared context so a request feels like it comes from 'someone like us.'

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — social engineering principles (familiarity)

**Tags:** `#principles`

</div>

---

<div class="glossary-entry-card" id="term-faraday_cage">

### Faraday cage / bag <span class="glossary-card-badge">EXAM</span>

**Definition:** Conductive enclosure that blocks RF — used for evidence phones, test devices, or shielding sensitive gear.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — Faraday cages / bags

**Tags:** `#physical`

</div>

---

<div class="glossary-entry-card" id="term-federation">

### Federation <span class="glossary-card-badge">EXAM</span>

**Definition:** Trust relationship that lets one organization's identity provider assert identity to another system's service provider.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — federation

**Tags:** `#federation`

</div>

---

<div class="glossary-entry-card" id="term-fencing">

### Fencing <span class="glossary-card-badge">EXAM</span>

**Definition:** Perimeter barrier that deters and delays casual entry — height, materials, and gates matter more than looking serious.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — fencing / perimeter

**Tags:** `#physical` `#perimeter`

</div>

---

<div class="glossary-entry-card" id="term-hash">

### File hash <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Fingerprint of a file (MD5/SHA) used to match known-bad samples or prove two files are identical.

**Tags:** `#support` `#detection`

</div>

---

<div class="glossary-entry-card" id="term-fileless">

### Fileless malware <span class="glossary-card-badge">EXAM</span>

**Definition:** Attacks that run in memory or abuse built-in tools so little or no new malware file lands on disk.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — fileless malware

**Tags:** `#malware` `#stealth`

</div>

---

<div class="glossary-entry-card" id="term-firewall">

### Firewall <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Device or software that allows or denies traffic based on rules (addresses, ports, protocols).

**Tags:** `#support` `#network` `#ops`

</div>

---

<div class="glossary-entry-card" id="term-firewall_rule">

### Firewall rule (ports/protocols) <span class="glossary-card-badge">EXAM</span>

**Definition:** An allow or deny decision keyed to source, destination, port, and protocol — the operational place Security+ port knowledge gets used.

**Tags:** `#ops`

</div>

---

<div class="glossary-entry-card" id="term-first_responder">

### First responder <span class="glossary-card-badge">EXAM</span>

**Definition:** First person or team to touch an incident — at many orgs the help desk is that first touch and must preserve options for IR.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — first responders

**Tags:** `#ir`

</div>

---

<div class="glossary-entry-card" id="term-flea_power">

### Flea Power (Residual Energy) <span class="glossary-card-badge">SUPPORT</span>

**Definition:** The residual static electrical charge stored in motherboard capacitors, power supply filter stages, and integrated circuits after primary electrical power is disconnected.

**Operational Context:** *Must be fully discharged by disconnecting power cords and depressing the power button for thirty seconds to clear corrupt memory registers before replacing hardware.*

**Certification & Domain Reference:**
- CompTIA A+ Core 1 220-1101 Domain 3.0 — Hardware break/fix and power triage
- CompTIA Network+ N10-008 Domain 4.1 — Physical hardware troubleshooting methodology

**Tags:** `#hardware` `#power` `#electrical` `#troubleshooting` `#network-plus`

</div>

---

<div class="glossary-entry-card" id="term-ftp">

### FTP (20/21/TCP) <span class="glossary-card-badge">EXAM</span>

**Definition:** File transfer with cleartext commands and credentials. Port 21 is control; 20 is active-mode data. Replace with SFTP or FTPS.

**Tags:** `#file` `#insecure`

</div>

---

<div class="glossary-entry-card" id="term-ftps">

### FTPS (989/990/TCP) <span class="glossary-card-badge">EXAM</span>

**Definition:** FTP wrapped in TLS (implicit mode commonly 990 control / 989 data). Not the same as SFTP.

**Operational Context:** *Classic FTP wrapped in TLS; different ports and firewall story than SFTP.*

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — secure file transfer alternatives to FTP

**Tags:** `#file` `#secure`

</div>

---

## G

<div class="glossary-entry-card" id="term-guest_wifi">

### Guest Wi-Fi <span class="glossary-card-badge">EXAM</span>

**Definition:** Separate wireless access for visitors — should not freely reach internal servers or employee laptops.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — guest network

**Tags:** `#wireless` `#guest`

</div>

---

## H

<div class="glossary-entry-card" id="term-hard_token">

### Hard token <span class="glossary-card-badge">EXAM</span>

**Definition:** Hardware possession factor — a dedicated device that generates or stores one-time codes or cryptographic keys.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — MFA methods / tokens

**Tags:** `#mfa` `#tokens`

</div>

---

<div class="glossary-entry-card" id="term-hashing">

### Hashing <span class="glossary-card-badge">EXAM</span>

**Definition:** One-way fingerprint of data — fixed-length digest used to check integrity, not to hide and later reveal secrets.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — hashing

**Tags:** `#crypto`

</div>

---

<div class="glossary-entry-card" id="term-help_desk">

### Help desk <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Front-line IT support that takes tickets, coaches users, and escalates security signals.

**Tags:** `#support` `#desk`

</div>

---

<div class="glossary-entry-card" id="term-heuristic">

### Heuristic detection <span class="glossary-card-badge">EXAM</span>

**Definition:** Detecting suspicious behavior or code traits even when the exact malware sample is new.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — heuristic / behavior-based detection

**Tags:** `#defense`

</div>

---

<div class="glossary-entry-card" id="term-hidden_ssid">

### Hidden SSID <span class="glossary-card-badge">EXAM</span>

**Definition:** Not broadcasting the network name — weak obscurity; determined clients and attackers can still discover it.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — SSID suppression

**Tags:** `#wireless`

</div>

---

<div class="glossary-entry-card" id="term-hoax">

### Hoax <span class="glossary-card-badge">EXAM</span>

**Definition:** A false warning or rumor spread to cause panic, wasted effort, or unsafe 'fixes.'

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — hoax

**Tags:** `#social-engineering`

</div>

---

<div class="glossary-entry-card" id="term-hosts_file">

### Hosts File <span class="glossary-card-badge">EXAM</span>

**Definition:** An operating system text file that provides static, local mappings between hostnames and IP addresses, evaluated prior to querying external DNS servers.

**Operational Context:** *Located at C:\Windows\System32\drivers\etc\hosts on Windows systems, often modified for temporary testing or exploited by malware to hijack web traffic.*

**Certification & Domain Reference:**
- CompTIA Network+ N10-008 Domain 4.1 — Network troubleshooting tools and client resolver sequence
- CompTIA A+ Core 2 220-1102 — Windows configuration and security files

**Tags:** `#dns` `#troubleshooting` `#windows`

</div>

---

<div class="glossary-entry-card" id="term-hot_aisle">

### Hot / cold aisle (awareness) <span class="glossary-card-badge">EXAM</span>

**Definition:** Data-center layout that separates hot exhaust and cold intake — operational design that also shapes who can walk where.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — hot/cold aisle (physical / environmental)

**Tags:** `#physical` `#datacenter`

</div>

---

<div class="glossary-entry-card" id="term-hsm">

### HSM <span class="glossary-card-badge">EXAM</span>

**Definition:** Hardware security module — hardened device that generates and protects keys so private material rarely leaves the box.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — HSM

**Tags:** `#crypto` `#keys`

</div>

---

<div class="glossary-entry-card" id="term-http">

### HTTP (80/TCP) <span class="glossary-card-badge">EXAM</span>

**Definition:** Cleartext web protocol. Replaced in production by HTTPS.

**Tags:** `#web` `#insecure`

</div>

---

<div class="glossary-entry-card" id="term-https">

### HTTPS (443/TCP) <span class="glossary-card-badge">EXAM</span>

**Definition:** HTTP secured with TLS. Default for modern web traffic.

**Operational Context:** *Use instead of cleartext HTTP for any page that takes credentials or personal data.*

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — implement secure protocols (web)

**Tags:** `#web` `#secure`

</div>

---

## I

<div class="glossary-entry-card" id="term-identification">

### Identification <span class="glossary-card-badge">EXAM</span>

**Definition:** Claiming an identity (username, badge ID, email) before authentication proves it.

**Operational Context:** *Saying who you are is not the same as proving it.*

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — identity concepts

**Tags:** `#identity`

</div>

---

<div class="glossary-entry-card" id="term-identity_provider">

### Identity provider (IdP) <span class="glossary-card-badge">SUPPORT</span>

**Definition:** System that authenticates users and issues assertions/tokens other apps trust (the 'sign in with company' brain).

**Tags:** `#support` `#federation`

</div>

---

<div class="glossary-entry-card" id="term-imap">

### IMAP (143/TCP) <span class="glossary-card-badge">EXAM</span>

**Definition:** Server-side mailbox access in cleartext. Secure version is IMAPS on 993.

**Tags:** `#email` `#insecure`

</div>

---

<div class="glossary-entry-card" id="term-imaps">

### IMAPS (993/TCP) <span class="glossary-card-badge">EXAM</span>

**Definition:** IMAP wrapped in TLS — keeps mail on the server with encryption in transit.

**Tags:** `#email` `#secure`

</div>

---

<div class="glossary-entry-card" id="term-impersonation">

### Impersonation <span class="glossary-card-badge">EXAM</span>

**Definition:** Pretending to be a trusted person or role (boss, IT, vendor, bank) to get compliance.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — impersonation

**Tags:** `#social-engineering`

</div>

---

<div class="glossary-entry-card" id="term-implicit_tls">

### Implicit TLS <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Wrapping a protocol in TLS from the first byte (e.g. SMTPS 465, FTPS 990) rather than upgrading mid-session with STARTTLS.

**Tags:** `#support` `#security`

</div>

---

<div class="glossary-entry-card" id="term-ioc">

### Indicators of compromise (IoC) <span class="glossary-card-badge">EXAM</span>

**Definition:** Observable clues that a system or account may be compromised — hashes, domains, odd processes, weird outbound traffic.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — indicators of compromise / malicious activity

**Tags:** `#detection`

</div>

---

<div class="glossary-entry-card" id="term-industrial_camouflage">

### Industrial camouflage <span class="glossary-card-badge">EXAM</span>

**Definition:** Making a facility blend into the neighborhood so it draws less attention as a high-value target.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — industrial camouflage

**Tags:** `#physical`

</div>

---

<div class="glossary-entry-card" id="term-influence_campaigns">

### Influence campaigns <span class="glossary-card-badge">EXAM</span>

**Definition:** Coordinated efforts to shape opinions or behavior at scale — often mixing social pressure with deceptive content.

**Operational Context:** *On the exam: social engineering at organizational or public scale, not just one inbox.*

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — influence campaigns

**Tags:** `#social-engineering`

</div>

---

<div class="glossary-entry-card" id="term-integrity">

### Integrity <span class="glossary-card-badge">EXAM</span>

**Definition:** Assurance that data has not been altered — often checked with hashes or signatures.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — integrity

**Tags:** `#crypto`

</div>

---

<div class="glossary-entry-card" id="term-intermediate_ca">

### Intermediate CA <span class="glossary-card-badge">EXAM</span>

**Definition:** CA beneath the root that issues end-entity certificates — keeps the root offline and the chain manageable.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — intermediate CA / certificate chain

**Tags:** `#pki`

</div>

---

<div class="glossary-entry-card" id="term-invoice_scam">

### Invoice scam <span class="glossary-card-badge">EXAM</span>

**Definition:** Fraudulent billing or payment-change request that looks like a normal vendor or finance workflow.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — invoice scams / BEC-related fraud

**Tags:** `#fraud`

</div>

---

<div class="glossary-entry-card" id="term-ip_address">

### IP Address <span class="glossary-card-badge">EXAM</span>

**Definition:** A logical 32-bit (IPv4) or 128-bit (IPv6) numerical identifier assigned to a network interface to enable routable packet delivery across interconnected Layer 3 network domains.

**Operational Context:** *Assigned dynamically via DHCP or statically by network administrators, reflecting the host's topological location on a logical subnet rather than its physical hardware identity.*

**Certification & Domain Reference:**
- CompTIA A+ Core 1 (220-1101) Objective 2.6: Configure basic networking host settings

**Tags:** `#networking` `#layer3` `#addressing`

</div>

---

<div class="glossary-entry-card" id="term-isolate">

### Isolate (host isolation) <span class="glossary-card-badge">EXAM</span>

**Definition:** Pulling a suspect machine off the network (or into a tight VLAN) so malware cannot reach shares, peers, or C2.

**Operational Context:** *Desk-first move when ransomware or worm behavior shows up.*

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — isolation / incident response

**Tags:** `#response`

</div>

---

<div class="glossary-entry-card" id="term-isolation">

### Isolation <span class="glossary-card-badge">EXAM</span>

**Definition:** Separating a system from the network or peers to stop spread — pull the cable, disable Wi-Fi, or VLAN-park the host.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — isolation

**Tags:** `#ir` `#containment`

</div>

---

<div class="glossary-entry-card" id="term-iv_attack">

### IV attack (WEP) <span class="glossary-card-badge">EXAM</span>

**Definition:** Exploiting WEP's weak initialization vectors to recover the key — one reason WEP is retired.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — IV attack / WEP weaknesses

**Tags:** `#wireless` `#attack`

</div>

---

## J

<div class="glossary-entry-card" id="term-jamming">

### Jamming <span class="glossary-card-badge">EXAM</span>

**Definition:** Flooding RF so legitimate Wi-Fi cannot communicate — a denial-of-service against the air itself.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — jamming / RF interference (attack)

**Tags:** `#wireless` `#attack`

</div>

---

<div class="glossary-entry-card" id="term-jump_host">

### Jump host / jump box <span class="glossary-card-badge">SUPPORT</span>

**Definition:** A hardened intermediate server you remote into first, then reach internal systems from there.

**Operational Context:** *Intermediate hop so workstations are not directly reachable from remote clients.*

**Tags:** `#support` `#remote` `#network`

</div>

---

<div class="glossary-entry-card" id="term-just_in_time">

### Just-in-time (JIT) access <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Temporary elevation granted only when needed, then revoked — instead of standing admin rights.

**Tags:** `#support` `#privilege`

</div>

---

## K

<div class="glossary-entry-card" id="term-kerberos">

### Kerberos (88/TCP/UDP) <span class="glossary-card-badge">EXAM</span>

**Definition:** Ticket-based authentication used by Active Directory. Issues time-limited tickets instead of sending reusable passwords repeatedly.

**Tags:** `#directory`

</div>

---

<div class="glossary-entry-card" id="term-key_auth">

### Key authentication <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Logging in with a cryptographic key pair instead of (or in addition to) a password.

**Tags:** `#support` `#security`

</div>

---

<div class="glossary-entry-card" id="term-key_escrow">

### Key escrow <span class="glossary-card-badge">EXAM</span>

**Definition:** Storing decryption keys with a trusted third party so data can be recovered under policy — powerful and controversial.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — key escrow

**Tags:** `#crypto` `#keys`

</div>

---

<div class="glossary-entry-card" id="term-key_exchange">

### Key exchange <span class="glossary-card-badge">EXAM</span>

**Definition:** Method for agreeing on a shared secret over an untrusted channel (often using asymmetric math so symmetric keys can follow).

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — key exchange

**Tags:** `#crypto`

</div>

---

<div class="glossary-entry-card" id="term-key_management">

### Key management <span class="glossary-card-badge">EXAM</span>

**Definition:** Lifecycle of creating, storing, rotating, revoking, and destroying cryptographic keys without leaking them.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — key management

**Tags:** `#crypto` `#keys`

</div>

---

<div class="glossary-entry-card" id="term-keylogger">

### Keylogger <span class="glossary-card-badge">EXAM</span>

**Definition:** Software or hardware that records keystrokes to steal passwords, messages, or other typed secrets.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — keylogger

**Tags:** `#malware` `#credential-theft`

</div>

---

## L

<div class="glossary-entry-card" id="term-lateral_movement">

### Lateral movement <span class="glossary-card-badge">EXAM</span>

**Definition:** Spreading from one compromised host to others on the same network — shares, remote tools, stolen creds.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — lateral movement

**Tags:** `#malware` `#network`

</div>

---

<div class="glossary-entry-card" id="term-ldap">

### LDAP (389/TCP/UDP) <span class="glossary-card-badge">EXAM</span>

**Definition:** Directory lookups and authentication in cleartext. Secure version is LDAPS on 636.

**Tags:** `#directory` `#insecure`

</div>

---

<div class="glossary-entry-card" id="term-ldaps">

### LDAPS (636/TCP) <span class="glossary-card-badge">EXAM</span>

**Definition:** LDAP wrapped in TLS.

**Operational Context:** *Directory binds with passwords should not ride cleartext LDAP on untrusted segments.*

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — implement secure protocols (directory services)

**Tags:** `#directory` `#secure`

</div>

---

<div class="glossary-entry-card" id="term-least_privilege">

### Least privilege <span class="glossary-card-badge">EXAM</span>

**Definition:** Grant only the access needed for the job — nothing extra 'just in case.'

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — least privilege

**Tags:** `#access`

</div>

---

<div class="glossary-entry-card" id="term-lighting">

### Lighting (security) <span class="glossary-card-badge">EXAM</span>

**Definition:** Illumination that reduces dark hiding spots and improves camera usefulness — a cheap control that attackers hate.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — lighting

**Tags:** `#physical`

</div>

---

<div class="glossary-entry-card" id="term-link_aggregation">

### Link Aggregation (LACP / 802.3ad) <span class="glossary-card-badge">EXAM</span>

**Definition:** A networking standard (Link Aggregation Control Protocol) that bundles multiple physical Ethernet interfaces into a single logical channel to provide multiplied bandwidth and active-active hardware redundancy.

**Operational Context:** *Protects critical inter-switch uplinks against single-cable failures while preventing Spanning Tree Protocol from blocking the parallel physical links.*

**Certification & Domain Reference:**
- CompTIA Network+ N10-008 Domain 2.1 — Port bonding, link aggregation, and LACP
- CompTIA Network+ N10-009 Domain 2.1 — High availability, trunking, and NIC teaming

**Tags:** `#switching` `#layer2` `#lacp` `#redundancy` `#network-plus`

</div>

---

<div class="glossary-entry-card" id="term-listening_port">

### Listening Port <span class="glossary-card-badge">EXAM</span>

**Definition:** A network port bound by a background server daemon or application process configured to accept incoming connection requests from remote clients.

**Operational Context:** *Represented in operating system tables as 0.0.0.0:<port> or [::]:<port> in the LISTENING state; connections to unbound ports are actively refused or dropped.*

**Certification & Domain Reference:**
- CompTIA Network+ N10-008 Domain 1.4 — Network services and listening ports
- CompTIA Security+ SY0-701 Domain 2.1 — Port security and service exposure

**Tags:** `#tcp` `#ports` `#services` `#network-plus`

</div>

---

<div class="glossary-entry-card" id="term-living_off_the_land">

### Living off the land <span class="glossary-card-badge">EXAM</span>

**Definition:** Abusing built-in OS tools (PowerShell, WMI, scripts) so attacks blend in with admin work.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — living off the land / fileless

**Tags:** `#malware` `#stealth`

</div>

---

<div class="glossary-entry-card" id="term-lobby">

### Lobby <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Public-facing entry where visitors meet reception — highest tailgating risk zone.

**Tags:** `#support` `#physical`

</div>

---

<div class="glossary-entry-card" id="term-door_lock">

### Locks (doors) <span class="glossary-card-badge">EXAM</span>

**Definition:** Mechanical or electronic door hardware — deadbolts, electric strikes, cipher locks — that enforce who may enter.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — locks

**Tags:** `#physical` `#access`

</div>

---

<div class="glossary-entry-card" id="term-logic_bomb">

### Logic bomb <span class="glossary-card-badge">EXAM</span>

**Definition:** Malicious code that sits dormant until a condition or date triggers it (fire after layoff, delete after deadline).

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — logic bomb

**Tags:** `#malware`

</div>

---

## M

<div class="glossary-entry-card" id="term-mac_address">

### MAC Address <span class="glossary-card-badge">EXAM</span>

**Definition:** A globally unique 48-bit physical identifier burned into the firmware of a network interface card by the manufacturer to facilitate Layer 2 frame delivery on local Ethernet segments.

**Operational Context:** *Operates exclusively within a single local broadcast domain, remaining unchanged across networks and never routing across internet boundaries.*

**Certification & Domain Reference:**
- CompTIA A+ Core 1 (220-1101) Objective 2.4: Summarize basic networking concepts

**Tags:** `#networking` `#layer2` `#addressing`

</div>

---

<div class="glossary-entry-card" id="term-mac_filtering">

### MAC filtering <span class="glossary-card-badge">EXAM</span>

**Definition:** Allow/deny Wi-Fi by hardware address — easily spoofed; not a real access-control substitute.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — MAC filtering

**Tags:** `#wireless`

</div>

---

<div class="glossary-entry-card" id="term-mail_gateway">

### Mail gateway <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Email security filter that scans, tags, quarantines, or blocks messages before they reach users.

**Tags:** `#support` `#email`

</div>

---

<div class="glossary-entry-card" id="term-malware">

### Malware <span class="glossary-card-badge">EXAM</span>

**Definition:** Malicious software — any program designed to harm, spy, extort, or take control of a system.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — malware

**Tags:** `#malware`

</div>

---

<div class="glossary-entry-card" id="term-malware_attachment">

### Malware attachment <span class="glossary-card-badge">EXAM</span>

**Definition:** A file (or archive) delivered to install malware when opened — often paired with a urgent story.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — malicious attachments / phishing

**Tags:** `#phishing` `#malware`

</div>

---

<div class="glossary-entry-card" id="term-malware_scan">

### Malware scan <span class="glossary-card-badge">SUPPORT</span>

**Definition:** On-demand or scheduled check by antimalware/EDR that looks for known and suspicious code on a host.

**Tags:** `#support` `#defense`

</div>

---

<div class="glossary-entry-card" id="term-mantrap">

### Mantrap <span class="glossary-card-badge">EXAM</span>

**Definition:** Two-door vestibule that only opens one door at a time so people cannot slip through with someone else.

**Operational Context:** *Also called an access control vestibule on some exams.*

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — mantrap / access control vestibule

**Tags:** `#physical` `#access`

</div>

---

<div class="glossary-entry-card" id="term-mfa_fatigue">

### MFA fatigue <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Attack or habit where a user is spammed with push prompts until they approve one without thinking.

**Tags:** `#support` `#mfa` `#security`

</div>

---

<div class="glossary-entry-card" id="term-mfa_fatigue_attack">

### MFA fatigue attack <span class="glossary-card-badge">EXAM</span>

**Definition:** Spamming MFA push prompts until the user approves one without thinking.

**Operational Context:** *Same muscle as ch2 MFA habits — here it rides a phishing or password-spray path.*

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — MFA / social engineering related attacks

**Tags:** `#mfa` `#phishing`

</div>

---

<div class="glossary-entry-card" id="term-motion_detection">

### Motion detection <span class="glossary-card-badge">EXAM</span>

**Definition:** Sensors that alert when movement occurs in a watched zone — often paired with cameras or alarms.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — motion detection

**Tags:** `#physical` `#detection`

</div>

---

<div class="glossary-entry-card" id="term-msp">

### MSP <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Managed Service Provider; a company that runs IT support for other businesses.

**Tags:** `#support` `#desk`

</div>

---

<div class="glossary-entry-card" id="term-mfa">

### Multifactor authentication (MFA) <span class="glossary-card-badge">EXAM</span>

**Definition:** Requiring two or more different factor types (know / have / are) before access is granted.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — multifactor authentication

**Tags:** `#mfa`

</div>

---

<div class="glossary-entry-card" id="term-multimeter">

### Multimeter <span class="glossary-card-badge">EXAM</span>

**Definition:** A handheld electronic test instrument used to measure electrical voltage (AC/DC), resistance (ohms), and current (amperes) across hardware circuits.

**Operational Context:** *Used by technicians to test power supply rail tolerances (+12V, +5V, +3.3V) and trace broken or grounded conductors.*

**Certification & Domain Reference:**
- CompTIA A+ Core 1 (220-1101) Objective 3.1: Power supply troubleshooting and voltage rail verification

**Tags:** `#hardware` `#electrical`

</div>

---

## N

<div class="glossary-entry-card" id="term-need_to_know">

### Need-to-know <span class="glossary-card-badge">EXAM</span>

**Definition:** Principle of sharing incident details only with people who require them to act — not blasting the whole company Slack.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — need-to-know / least privilege of information

**Tags:** `#ir`

</div>

---

<div class="glossary-entry-card" id="term-perimeter">

### Network perimeter <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Boundary between trusted internal networks and untrusted external networks.

**Tags:** `#support` `#network`

</div>

---

<div class="glossary-entry-card" id="term-segmentation">

### Network segmentation <span class="glossary-card-badge">EXAM</span>

**Definition:** Splitting networks so a compromise or guest device cannot freely reach sensitive systems.

**Operational Context:** *Guest Wi-Fi without segmentation is a hallway into the building.*

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — network segmentation

**Tags:** `#wireless` `#architecture`

</div>

---

<div class="glossary-entry-card" id="term-network_share">

### Network share <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Folder or drive published on the LAN that many PCs can reach — a common path for worm or ransomware spread.

**Tags:** `#support` `#network`

</div>

---

<div class="glossary-entry-card" id="term-network_interface_card">

### NIC (Network Interface Card) <span class="glossary-card-badge">EXAM</span>

**Definition:** A hardware expansion card or onboard controller that implements physical Layer 1 signaling and Layer 2 data link framing to connect a computer to a local network.

**Operational Context:** *Converts internal digital system bus transactions into serialized electrical, optical, or radio transmissions across physical network media.*

**Certification & Domain Reference:**
- CompTIA A+ Core 1 (220-1101) Objective 2.1: Compare and contrast network hardware devices

**Tags:** `#networking` `#hardware` `#layer1`

</div>

---

<div class="glossary-entry-card" id="term-non_repudiation">

### Non-repudiation <span class="glossary-card-badge">EXAM</span>

**Definition:** Difficulty denying you signed or sent something when a valid signature and key custody support the claim.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — non-repudiation

**Tags:** `#crypto`

</div>

---

<div class="glossary-entry-card" id="term-non_volatile_storage">

### Non-Volatile Storage <span class="glossary-card-badge">EXAM</span>

**Definition:** Secondary data persistence hardware such as solid-state drives, magnetic hard disks, or flash memory that retains stored binary data without continuous electrical power.

**Operational Context:** *Houses operating system installations, permanent application binaries, user documents, and system configuration registries across reboots.*

**Certification & Domain Reference:**
- CompTIA A+ Core 1 (220-1101) Objective 3.2: Troubleshoot storage drives and RAID arrays

**Tags:** `#hardware` `#storage` `#architecture`

</div>

---

<div class="glossary-entry-card" id="term-ntp">

### NTP (123/UDP) <span class="glossary-card-badge">EXAM</span>

**Definition:** Synchronizes clocks. Accurate time matters for logs, Kerberos tickets, and certificate validation.

**Tags:** `#network`

</div>

---

## O

<div class="glossary-entry-card" id="term-oauth">

### OAuth <span class="glossary-card-badge">EXAM</span>

**Definition:** Authorization framework often used so apps get limited access tokens without sharing the user's password (desk tickets may say 'OAuth SSO' loosely).

**Operational Context:** *At the desk: usually means the app is wired to the company IdP for sign-in / consent, not a password paste.*

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — OAuth / federation-related access

**Tags:** `#federation`

</div>

---

<div class="glossary-entry-card" id="term-obfuscation">

### Obfuscation <span class="glossary-card-badge">EXAM</span>

**Definition:** Making something harder to read or understand without providing real cryptographic strength by itself.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — obfuscation

**Tags:** `#crypto`

</div>

---

<div class="glossary-entry-card" id="term-offboarding">

### Offboarding <span class="glossary-card-badge">SUPPORT</span>

**Definition:** HR/IT process when someone leaves — disable accounts, reclaim devices, and strip residual access.

**Tags:** `#support` `#lifecycle`

</div>

---

<div class="glossary-entry-card" id="term-offline_backup">

### Offline / immutable backup <span class="glossary-card-badge">EXAM</span>

**Definition:** Backup copies that ransomware cannot reach or alter — offline media, immutable snapshots, or air-gapped stores.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — backups / ransomware recovery

**Tags:** `#ransomware` `#recovery`

</div>

---

<div class="glossary-entry-card" id="term-open_network">

### Open network <span class="glossary-card-badge">EXAM</span>

**Definition:** Wi-Fi with no encryption on the air — anyone nearby can join and often eavesdrop unless a higher layer protects traffic.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — open / insecure wireless

**Tags:** `#wireless` `#risk`

</div>

---

<div class="glossary-entry-card" id="term-open_relay">

### Open relay <span class="glossary-card-badge">SUPPORT</span>

**Definition:** A mail server that accepts and forwards mail from anyone; abused by spammers.

**Tags:** `#support` `#email`

</div>

---

## P

<div class="glossary-entry-card" id="term-passphrase">

### Passphrase <span class="glossary-card-badge">EXAM</span>

**Definition:** A longer memorable phrase used as a password; length often beats dense complexity rules.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — password security

**Tags:** `#password`

</div>

---

<div class="glossary-entry-card" id="term-password">

### Password <span class="glossary-card-badge">EXAM</span>

**Definition:** A secret string used as a knowledge factor for authentication.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — password security

**Tags:** `#password`

</div>

---

<div class="glossary-entry-card" id="term-password_age">

### Password age <span class="glossary-card-badge">EXAM</span>

**Definition:** How long the current password has been in use; tracked so policy can enforce maximum age or detect stale secrets.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — password policies

**Tags:** `#password` `#policy`

</div>

---

<div class="glossary-entry-card" id="term-password_complexity">

### Password complexity <span class="glossary-card-badge">EXAM</span>

**Definition:** Rules requiring mixed character classes (upper, lower, digit, symbol). Helpful, but length and uniqueness matter more.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — password best practices

**Tags:** `#password` `#policy`

</div>

---

<div class="glossary-entry-card" id="term-password_expiration">

### Password expiration <span class="glossary-card-badge">EXAM</span>

**Definition:** Forcing periodic password changes on a schedule. Modern guidance often prefers change-on-compromise over short expiry cycles.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — password policies

**Tags:** `#password` `#policy`

</div>

---

<div class="glossary-entry-card" id="term-password_length">

### Password length <span class="glossary-card-badge">EXAM</span>

**Definition:** How many characters a password has; modern guidance prioritizes sufficient length over ornate complexity alone.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — password best practices

**Tags:** `#password` `#policy`

</div>

---

<div class="glossary-entry-card" id="term-password_manager">

### Password manager <span class="glossary-card-badge">EXAM</span>

**Definition:** Tool that stores unique strong passwords (and often autofills them) so users need not reuse secrets.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — password security / credential management

**Tags:** `#password`

</div>

---

<div class="glossary-entry-card" id="term-password_reuse">

### Password reuse <span class="glossary-card-badge">EXAM</span>

**Definition:** Using the same password across systems or recycling recent passwords — spreads breach impact.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — password best practices

**Tags:** `#password` `#policy`

</div>

---

<div class="glossary-entry-card" id="term-passwordless">

### Passwordless <span class="glossary-card-badge">EXAM</span>

**Definition:** Authentication that replaces passwords with possession and/or biometrics (e.g. security keys, passkeys, device unlock).

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — authentication methods

**Tags:** `#auth-methods`

</div>

---

<div class="glossary-entry-card" id="term-patch_panel">

### Patch Panel <span class="glossary-card-badge">EXAM</span>

**Definition:** A passive, rack-mounted structural interconnect device containing female RJ-45 modular jacks on the front faceplate and 110-style insulation displacement contact punchdown blocks on the rear to terminate horizontal structured cabling.

**Operational Context:** *Protects fragile horizontal solid-core cabling from mechanical wear and tear by allowing technicians to cross-connect ports using flexible stranded patch cables.*

**Certification & Domain Reference:**
- CompTIA Network+ N10-008 Domain 1.2 — Cable management, patch panels, punchdown blocks, and Layer 1 physical infrastructure
- CompTIA Network+ N10-009 Domain 1.2 — Physical media and structured cabling distribution

**Tags:** `#hardware` `#cabling` `#layer1` `#physical` `#network-plus`

</div>

---

<div class="glossary-entry-card" id="term-payload">

### Payload <span class="glossary-card-badge">EXAM</span>

**Definition:** The harmful action malware is built to perform once it runs — encrypt, spy, open a shell, join a botnet.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — malware payload

**Tags:** `#malware`

</div>

---

<div class="glossary-entry-card" id="term-perfect_forward_secrecy">

### Perfect forward secrecy <span class="glossary-card-badge">EXAM</span>

**Definition:** Property where past session keys stay safe even if a long-term private key is later stolen — ephemeral session secrets.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — perfect forward secrecy / PFS

**Tags:** `#crypto` `#tls`

</div>

---

<div class="glossary-entry-card" id="term-persistence">

### Persistence <span class="glossary-card-badge">EXAM</span>

**Definition:** Techniques that keep malware running after reboot — startup entries, services, scheduled tasks, registry Run keys.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — persistence / malware characteristics

**Tags:** `#malware`

</div>

---

<div class="glossary-entry-card" id="term-phish_report_button">

### Phish report button <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Client add-in that sends a suspected message to security for analysis without the user forwarding raw risk elsewhere.

**Tags:** `#support` `#response`

</div>

---

<div class="glossary-entry-card" id="term-phishing">

### Phishing <span class="glossary-card-badge">EXAM</span>

**Definition:** Fraudulent messages (usually email) that trick users into clicking, opening, or giving up secrets.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — phishing

**Tags:** `#phishing`

</div>

---

<div class="glossary-entry-card" id="term-phishing_url">

### Phishing URL <span class="glossary-card-badge">EXAM</span>

**Definition:** A link designed to look legitimate while sending the victim to an attacker-controlled site.

**Operational Context:** *Hover, expand, or check the real host before you click.*

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — indicators of phishing

**Tags:** `#phishing` `#indicators`

</div>

---

<div class="glossary-entry-card" id="term-physical_controls">

### Physical security controls <span class="glossary-card-badge">EXAM</span>

**Definition:** Tangible barriers and processes that protect facilities, people, and hardware — fences, locks, cameras, badges, and the habits that make them work.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — physical security controls

**Tags:** `#physical`

</div>

---

<div class="glossary-entry-card" id="term-piggybacking">

### Piggybacking <span class="glossary-card-badge">EXAM</span>

**Definition:** Entering with consent of the person who opened the door — they held it; you still did not authenticate.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — piggybacking

**Tags:** `#physical` `#attack`

</div>

---

<div class="glossary-entry-card" id="term-pin">

### PIN <span class="glossary-card-badge">EXAM</span>

**Definition:** Personal identification number — a short numeric knowledge factor, not a second factor type when paired with a password.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — authentication factors

**Tags:** `#password` `#factors`

</div>

---

<div class="glossary-entry-card" id="term-pki">

### PKI <span class="glossary-card-badge">EXAM</span>

**Definition:** Public key infrastructure — the people, policies, and systems that issue and manage certificates and trust.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — PKI

**Tags:** `#pki`

</div>

---

<div class="glossary-entry-card" id="term-plaintext">

### Plaintext <span class="glossary-card-badge">EXAM</span>

**Definition:** Data in readable form before encryption — the thing you are trying not to leave lying around.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — plaintext / ciphertext

**Tags:** `#crypto`

</div>

---

<div class="glossary-entry-card" id="term-pop3">

### POP3 (110/TCP) <span class="glossary-card-badge">EXAM</span>

**Definition:** Downloads mail to the client in cleartext. Secure version is POP3S on 995.

**Tags:** `#email` `#insecure`

</div>

---

<div class="glossary-entry-card" id="term-pop3s">

### POP3S (995/TCP) <span class="glossary-card-badge">EXAM</span>

**Definition:** POP3 wrapped in TLS.

**Tags:** `#email` `#secure`

</div>

---

<div class="glossary-entry-card" id="term-port">

### Port <span class="glossary-card-badge">EXAM</span>

**Definition:** A 16-bit number (0–65535) that multiplexes traffic to a specific service or process on a host.

**Tags:** `#basics`

</div>

---

<div class="glossary-entry-card" id="term-post_routine">

### POST (Power-On Self-Test) <span class="glossary-card-badge">EXAM</span>

**Definition:** An initial diagnostic sequence executed by system firmware (BIOS or UEFI) immediately upon startup to verify and initialize core hardware components before loading the OS.

**Operational Context:** *Validates CPU registers, system memory integrity, display controllers, and bus interfaces, halting or emitting diagnostic beep/hex codes if essential hardware fails.*

**Certification & Domain Reference:**
- CompTIA A+ Core 1 (220-1101) Objective 3.1: Motherboard and boot sequence troubleshooting

**Tags:** `#hardware` `#firmware` `#boot`

</div>

---

<div class="glossary-entry-card" id="term-post_code">

### POST Code <span class="glossary-card-badge">EXAM</span>

**Definition:** A hexadecimal diagnostic code output by system firmware during the Power-On Self-Test to identify hardware initialization progress and specific subsystem failures.

**Operational Context:** *Displayed on onboard seven-segment displays or port 80h diagnostic cards before video display drivers initialize.*

**Certification & Domain Reference:**
- CompTIA A+ Core 1 (220-1101) Objective 3.1: Given a scenario, resolve problems with motherboard, RAM, CPU, and power

**Tags:** `#hardware` `#diagnostics`

</div>

---

<div class="glossary-entry-card" id="term-pretexting">

### Pretexting <span class="glossary-card-badge">EXAM</span>

**Definition:** Inventing a believable story or role to justify asking for information or access.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — pretexting

**Tags:** `#social-engineering`

</div>

---

<div class="glossary-entry-card" id="term-privacy_filter">

### Privacy / screen filter <span class="glossary-card-badge">EXAM</span>

**Definition:** Overlay that narrows the viewing angle so neighbors and café eyes cannot easily read the display.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — privacy screens / filters

**Tags:** `#physical` `#endpoint`

</div>

---

<div class="glossary-entry-card" id="term-private_key">

### Private key <span class="glossary-card-badge">EXAM</span>

**Definition:** Secret half of a key pair — decrypts or signs; must stay protected or the trust story collapses.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — public/private keys

**Tags:** `#crypto` `#pki`

</div>

---

<div class="glossary-entry-card" id="term-privilege_escalation">

### Privilege escalation <span class="glossary-card-badge">EXAM</span>

**Definition:** Gaining higher rights than the initial foothold — user to admin, or admin to SYSTEM/kernel.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — privilege escalation

**Tags:** `#malware` `#access`

</div>

---

<div class="glossary-entry-card" id="term-privileged_access">

### Privileged access <span class="glossary-card-badge">EXAM</span>

**Definition:** Elevated rights (admin, root, domain) that can change systems or read sensitive data — tightly controlled.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — privileged access management concepts

**Tags:** `#privilege`

</div>

---

<div class="glossary-entry-card" id="term-pam">

### Privileged access management (PAM) <span class="glossary-card-badge">EXAM</span>

**Definition:** Controls for privileged accounts — vaulting shared secrets, just-in-time elevation, and session oversight.

**Operational Context:** *Desk-level: admins check out a vaulted password or request temporary elevation instead of sharing a sticky.*

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — privileged access management

**Tags:** `#privilege`

</div>

---

<div class="glossary-entry-card" id="term-process_list">

### Process list <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Running programs visible in Task Manager or EDR — odd names, odd parents, or odd CPU can be early clues.

**Tags:** `#support` `#desk`

</div>

---

<div class="glossary-entry-card" id="term-protected_distribution">

### Protected cable distribution <span class="glossary-card-badge">EXAM</span>

**Definition:** Hardened or monitored pathways for sensitive cabling so taps and tampering are harder.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — protected cable distribution

**Tags:** `#physical`

</div>

---

<div class="glossary-entry-card" id="term-protocol">

### Protocol <span class="glossary-card-badge">EXAM</span>

**Definition:** A formal set of message formats and rules that networked systems use to exchange data.

**Tags:** `#basics`

</div>

---

<div class="glossary-entry-card" id="term-provisioning">

### Provisioning <span class="glossary-card-badge">EXAM</span>

**Definition:** Creating accounts and assigning access when someone joins or changes roles.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — account management / provisioning

**Tags:** `#lifecycle`

</div>

---

<div class="glossary-entry-card" id="term-proximity_card">

### Proximity / RFID badge <span class="glossary-card-badge">EXAM</span>

**Definition:** Badge that unlocks when held near a reader — convenient, and clonable if not paired with PIN or biometrics.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — proximity cards / RFID

**Tags:** `#physical` `#access`

</div>

---

<div class="glossary-entry-card" id="term-psk">

### PSK (pre-shared key) <span class="glossary-card-badge">EXAM</span>

**Definition:** Shared Wi-Fi password mode — everyone uses the same key; fine for small spaces, weak for accountability and rotation.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — PSK / personal mode

**Tags:** `#wireless` `#auth`

</div>

---

<div class="glossary-entry-card" id="term-public_key">

### Public key <span class="glossary-card-badge">EXAM</span>

**Definition:** Shareable half of a key pair — used to encrypt to someone or verify their digital signature.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — public/private keys

**Tags:** `#crypto` `#pki`

</div>

---

<div class="glossary-entry-card" id="term-pups">

### PUPs (potentially unwanted programs) <span class="glossary-card-badge">EXAM</span>

**Definition:** Software users may have 'agreed' to install that is unwanted, deceptive, or risky — toolbars, bundles, junk helpers.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — PUPs / potentially unwanted programs

**Tags:** `#malware` `#pups`

</div>

---

<div class="glossary-entry-card" id="term-push_notification">

### Push notification (MFA) <span class="glossary-card-badge">EXAM</span>

**Definition:** Approve/deny prompt sent to a registered device as a possession check.

**Operational Context:** *Convenient, but users can be trained into tapping Approve under fatigue or social pressure.*

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — MFA methods

**Tags:** `#mfa`

</div>

---

## Q

<div class="glossary-entry-card" id="term-quarantine">

### Quarantine <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Holding suspicious mail or files away from the inbox so users cannot open them until reviewed.

**Tags:** `#support` `#email`

</div>

---

<div class="glossary-entry-card" id="term-quid_pro_quo">

### Quid pro quo <span class="glossary-card-badge">EXAM</span>

**Definition:** Offering a benefit (help, gift, refund, free support) in exchange for information or a risky action.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — quid pro quo

**Tags:** `#social-engineering`

</div>

---

## R

<div class="glossary-entry-card" id="term-radius">

### RADIUS <span class="glossary-card-badge">EXAM</span>

**Definition:** Authentication server protocol commonly behind enterprise Wi-Fi — checks user/device credentials for 802.1X.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — RADIUS / AAA

**Tags:** `#wireless` `#auth`

</div>

---

<div class="glossary-entry-card" id="term-ram_memory">

### RAM (Random Access Memory) <span class="glossary-card-badge">EXAM</span>

**Definition:** High-speed volatile semiconductor memory utilized by the processor to hold active program instructions, operating system kernel routines, and working data sets while powered.

**Operational Context:** *Loses all stored data instantly when electrical power is removed or interrupted during a reboot.*

**Certification & Domain Reference:**
- CompTIA A+ Core 1 (220-1101) Objective 3.1: Resolve problems with motherboard, RAM, CPU, and power

**Tags:** `#hardware` `#memory` `#architecture`

</div>

---

<div class="glossary-entry-card" id="term-ransomware">

### Ransomware <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Malware that encrypts systems or data and demands payment; internet-exposed remote desktop is a common entry.

**Tags:** `#support` `#security`

</div>

---

<div class="glossary-entry-card" id="term-rdp">

### RDP (3389/TCP) <span class="glossary-card-badge">EXAM</span>

**Definition:** Microsoft Remote Desktop. Encrypted in modern use, but Internet-exposed RDP is a leading ransomware entry — keep it behind a VPN.

**Operational Context:** *Do not expose raw 3389 to the internet; prefer VPN then jump host.*

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — firewall ports/protocols; secure remote access

**Tags:** `#remote`

</div>

---

<div class="glossary-entry-card" id="term-reception">

### Reception / access desk <span class="glossary-card-badge">EXAM</span>

**Definition:** Front-desk checkpoint that verifies visitors, issues badges, and is the first human filter into the building.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — reception / access control personnel

**Tags:** `#physical` `#personnel`

</div>

---

<div class="glossary-entry-card" id="term-recursive_resolver">

### Recursive Resolver <span class="glossary-card-badge">EXAM</span>

**Definition:** A DNS server that accepts queries from client stub resolvers and traverses the hierarchical DNS tree to obtain and return the definitive answer to the requester.

**Operational Context:** *Caches resolution answers locally according to record time-to-live values to accelerate subsequent queries from corporate workstations.*

**Certification & Domain Reference:**
- CompTIA Network+ N10-008 Domain 1.5 — DNS hierarchy and query flow

**Tags:** `#dns` `#networking` `#infrastructure`

</div>

---

<div class="glossary-entry-card" id="term-rat">

### Remote access Trojan (RAT) <span class="glossary-card-badge">EXAM</span>

**Definition:** A trojan that gives an attacker interactive remote control of the victim machine.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — RAT / remote access trojan

**Tags:** `#malware` `#remote`

</div>

---

<div class="glossary-entry-card" id="term-removable_media">

### Removable media risk <span class="glossary-card-badge">EXAM</span>

**Definition:** USB sticks and other portable media as a malware delivery path — plug in, autorun or open, infect.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — removable media / physical vectors

**Tags:** `#delivery`

</div>

---

<div class="glossary-entry-card" id="term-replay_attack">

### Replay attack <span class="glossary-card-badge">EXAM</span>

**Definition:** Capturing valid wireless or auth traffic and re-sending it later to gain access or disrupt sessions.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — replay attacks

**Tags:** `#wireless` `#attack`

</div>

---

<div class="glossary-entry-card" id="term-reporting_path">

### Reporting path <span class="glossary-card-badge">EXAM</span>

**Definition:** The official way to report suspected phishing or social engineering (button, mailbox, SOC, ticket) so response can start.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — reporting / incident awareness

**Tags:** `#response`

</div>

---

<div class="glossary-entry-card" id="term-resolver_cache">

### Resolver cache <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Local store of recent DNS answers; flushing it forces fresh lookups.

**Tags:** `#support` `#network`

</div>

---

<div class="glossary-entry-card" id="term-rogue_ap">

### Rogue access point <span class="glossary-card-badge">EXAM</span>

**Definition:** Unauthorized AP on the network or in range — intentional attack gear or a well-meaning employee 'helping' coverage.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — rogue access point

**Tags:** `#wireless` `#attack`

</div>

---

<div class="glossary-entry-card" id="term-rbac">

### Role-based access control (RBAC) <span class="glossary-card-badge">EXAM</span>

**Definition:** Assign permissions to roles (job functions), then assign users to roles — instead of one-off rights per person.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — access control models (RBAC)

**Tags:** `#access`

</div>

---

<div class="glossary-entry-card" id="term-rootkit">

### Rootkit <span class="glossary-card-badge">EXAM</span>

**Definition:** Malware that hides deep in the system (often kernel-level) to conceal processes, files, or persistence from normal tools.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — rootkit

**Tags:** `#malware` `#stealth`

</div>

---

<div class="glossary-entry-card" id="term-rs232_serial">

### RS-232 Serial <span class="glossary-card-badge">EXAM</span>

**Definition:** A legacy standard for serial binary data transmission between data terminal equipment (DTE) and data circuit-terminating equipment (DCE), commonly utilizing DB-9 connectors.

**Operational Context:** *Frequently deployed in rugged industrial equipment, automated weighing scales, barcode scanners, and network management consoles.*

**Certification & Domain Reference:**
- CompTIA A+ Core 1 (220-1101) Objective 3.4: Given a scenario, troubleshoot and resolve peripheral and display problems

**Tags:** `#hardware` `#serial`

</div>

---

## S

<div class="glossary-entry-card" id="term-sae">

### SAE <span class="glossary-card-badge">EXAM</span>

**Definition:** Simultaneous Authentication of Equals — WPA3 handshake that resists offline dictionary attacks better than WPA2-PSK.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — WPA3 / SAE

**Tags:** `#wireless` `#encryption`

</div>

---

<div class="glossary-entry-card" id="term-safe_mode">

### Safe Mode <span class="glossary-card-badge">EXAM</span>

**Definition:** A diagnostic boot state that loads Windows with a minimal set of essential drivers and system services.

**Operational Context:** *Used to determine whether a system crash or hang originates in base operating system files or third-party software and drivers.*

**Certification & Domain Reference:**
- CompTIA A+ Core 2 (220-1102) Objective 1.4

**Tags:** `#boot` `#diagnostics`

</div>

---

<div class="glossary-entry-card" id="term-salting">

### Salting <span class="glossary-card-badge">EXAM</span>

**Definition:** Random value mixed into password hashing so identical passwords do not produce identical hashes.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — salting

**Tags:** `#crypto` `#auth`

</div>

---

<div class="glossary-entry-card" id="term-saml">

### SAML <span class="glossary-card-badge">EXAM</span>

**Definition:** Security Assertion Markup Language — common enterprise SSO protocol exchanging XML assertions between IdP and service.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — federation protocols (SAML)

**Tags:** `#federation`

</div>

---

<div class="glossary-entry-card" id="term-sandbox">

### Sandbox <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Isolated analysis environment where attachments or links can be opened safely for detonation checks.

**Tags:** `#support` `#security`

</div>

---

<div class="glossary-entry-card" id="term-scarcity">

### Scarcity <span class="glossary-card-badge">EXAM</span>

**Definition:** Claiming limited time, seats, or stock so the victim rushes a decision.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — social engineering principles (scarcity)

**Tags:** `#principles`

</div>

---

<div class="glossary-entry-card" id="term-secure_area">

### Secure area <span class="glossary-card-badge">EXAM</span>

**Definition:** Restricted space (server room, wiring closet, records vault) with stronger controls than the open floor.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — secure areas

**Tags:** `#physical`

</div>

---

<div class="glossary-entry-card" id="term-security_guard">

### Security guard <span class="glossary-card-badge">EXAM</span>

**Definition:** Human presence that can challenge, escort, and respond — flexible where cameras only watch.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — security guards / personnel

**Tags:** `#physical` `#personnel`

</div>

---

<div class="glossary-entry-card" id="term-security_incident">

### Security incident <span class="glossary-card-badge">EXAM</span>

**Definition:** A violation or imminent threat of violation of security policy, acceptable use, or standard security practices — not every scary ticket qualifies.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — security incidents

**Tags:** `#ir`

</div>

---

<div class="glossary-entry-card" id="term-security_key">

### Security key <span class="glossary-card-badge">EXAM</span>

**Definition:** Hardware authenticator (often USB/NFC) that proves possession via cryptography — phishing-resistant when used as a second factor or passwordless.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — MFA / hardware authenticators

**Tags:** `#mfa` `#tokens`

</div>

---

<div class="glossary-entry-card" id="term-self_signed">

### Self-signed certificate <span class="glossary-card-badge">EXAM</span>

**Definition:** Certificate signed by its own key instead of a trusted CA — fine for lab toys, scary in production browsers.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — self-signed certificates

**Tags:** `#pki`

</div>

---

<div class="glossary-entry-card" id="term-server_room">

### Server room <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Secure area housing critical compute and network gear — usually badge-plus and camera-covered.

**Tags:** `#support` `#physical`

</div>

---

<div class="glossary-entry-card" id="term-sftp">

### SFTP (22/TCP) <span class="glossary-card-badge">EXAM</span>

**Definition:** File transfer tunneled inside SSH. Different protocol from FTP; uses port 22, not 20/21.

**Operational Context:** *Not the same as FTPS — file transfer inside SSH, usually port 22.*

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — secure file transfer alternatives to FTP

**Tags:** `#file` `#secure`

</div>

---

<div class="glossary-entry-card" id="term-shared_admin_account">

### Shared admin account <span class="glossary-card-badge">SUPPORT</span>

**Definition:** One privileged login used by multiple people — breaks accountability and complicates offboarding.

**Tags:** `#support` `#privilege`

</div>

---

<div class="glossary-entry-card" id="term-shoulder_surfing">

### Shoulder surfing <span class="glossary-card-badge">EXAM</span>

**Definition:** Watching someone type a PIN, password, or badge code from nearby — eyes as the attack tool.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — shoulder surfing

**Tags:** `#physical` `#attack`

</div>

---

<div class="glossary-entry-card" id="term-signage">

### Signage <span class="glossary-card-badge">EXAM</span>

**Definition:** Posted notices that warn, direct, or mark restricted areas — supporting control, not a substitute for locks.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — signage

**Tags:** `#physical`

</div>

---

<div class="glossary-entry-card" id="term-signal_strength">

### Signal strength <span class="glossary-card-badge">SUPPORT</span>

**Definition:** How loud the AP looks to a client — useful for coverage tickets and for noticing a twin that is 'too strong' in the wrong place.

**Tags:** `#support` `#wireless`

</div>

---

<div class="glossary-entry-card" id="term-signature_detection">

### Signature-based detection <span class="glossary-card-badge">EXAM</span>

**Definition:** Matching files or patterns against known malware fingerprints (hashes, byte patterns).

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — signature-based detection

**Tags:** `#defense`

</div>

---

<div class="glossary-entry-card" id="term-sso">

### Single sign-on (SSO) <span class="glossary-card-badge">EXAM</span>

**Definition:** Authenticate once to an identity provider, then access multiple apps without separate logins for each.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — SSO / federation

**Tags:** `#federation`

</div>

---

<div class="glossary-entry-card" id="term-single_factor">

### Single-factor authentication <span class="glossary-card-badge">EXAM</span>

**Definition:** Using only one authentication factor type. Password plus PIN is still single-factor — both are something you know.

**Operational Context:** *Two knowledge secrets do not equal MFA.*

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — MFA vs single-factor

**Tags:** `#factors` `#mfa`

</div>

---

<div class="glossary-entry-card" id="term-site_survey">

### Site survey <span class="glossary-card-badge">EXAM</span>

**Definition:** Measuring coverage, interference, and dead zones so APs are placed and tuned for both performance and security boundaries.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — site survey

**Tags:** `#wireless` `#design`

</div>

---

<div class="glossary-entry-card" id="term-smb">

### SMB (445/TCP) <span class="glossary-card-badge">EXAM</span>

**Definition:** Windows file and printer sharing. Never expose to the Internet; a frequent worm and ransomware path.

**Tags:** `#file`

</div>

---

<div class="glossary-entry-card" id="term-smishing">

### Smishing <span class="glossary-card-badge">EXAM</span>

**Definition:** SMS phishing — fraudulent texts that push links, codes, or urgent actions.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — smishing

**Tags:** `#phishing` `#sms`

</div>

---

<div class="glossary-entry-card" id="term-sms_otp">

### SMS OTP <span class="glossary-card-badge">EXAM</span>

**Definition:** One-time code delivered by text message. Better than password alone, but weaker than app or hardware factors (SIM swap, interception).

**Operational Context:** *Acceptable stopgap; prefer app or security key when policy allows.*

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — MFA methods / SMS risks

**Tags:** `#mfa` `#otp`

</div>

---

<div class="glossary-entry-card" id="term-smtp">

### SMTP (25/TCP) <span class="glossary-card-badge">EXAM</span>

**Definition:** Server-to-server mail relay, historically cleartext. Clients should submit on 587 or 465 instead.

**Tags:** `#email` `#insecure`

</div>

---

<div class="glossary-entry-card" id="term-smtp_submission">

### SMTP submission (587/TCP) <span class="glossary-card-badge">EXAM</span>

**Definition:** Authenticated client mail submission, typically upgraded with STARTTLS. Modern send port.

**Tags:** `#email` `#secure`

</div>

---

<div class="glossary-entry-card" id="term-smtps">

### SMTPS (465/TCP) <span class="glossary-card-badge">EXAM</span>

**Definition:** SMTP wrapped in TLS from the first byte (implicit TLS).

**Tags:** `#email` `#secure`

</div>

---

<div class="glossary-entry-card" id="term-snmp">

### SNMP (161/162/UDP) <span class="glossary-card-badge">EXAM</span>

**Definition:** Device monitoring. 161 polls agents; 162 receives traps. v1/v2c send community strings in cleartext — prefer SNMPv3.

**Tags:** `#monitor` `#insecure`

</div>

---

<div class="glossary-entry-card" id="term-snmpv3">

### SNMPv3 <span class="glossary-card-badge">EXAM</span>

**Definition:** SNMP with authentication and encryption. Same ports as classic SNMP, but credentials are no longer cleartext community strings.

**Tags:** `#monitor` `#secure`

</div>

---

<div class="glossary-entry-card" id="term-soc">

### SOC <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Security operations center — team that monitors alerts, investigates wireless attacks, and coordinates response.

**Tags:** `#support` `#security`

</div>

---

<div class="glossary-entry-card" id="term-social_engineering">

### Social engineering <span class="glossary-card-badge">EXAM</span>

**Definition:** Manipulating people into revealing information or taking unsafe actions — trust and pressure instead of breaking crypto.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — social engineering techniques

**Tags:** `#social-engineering`

</div>

---

<div class="glossary-entry-card" id="term-socket_state">

### Socket State <span class="glossary-card-badge">EXAM</span>

**Definition:** The operational status of a network communication endpoint within the TCP state machine, such as LISTENING, ESTABLISHED, CLOSE_WAIT, or TIME_WAIT.

**Operational Context:** *Inspected via diagnostic utilities such as netstat or ss to verify whether a server daemon is awaiting connections or whether client sockets are stalled in teardown.*

**Certification & Domain Reference:**
- CompTIA Network+ N10-008 Domain 1.4 — Ports, protocols, and socket states
- CompTIA Network+ N10-009 Domain 4.1 — Troubleshooting transport layer connectivity

**Tags:** `#tcp` `#socket` `#netstat` `#network-plus`

</div>

---

<div class="glossary-entry-card" id="term-soft_token">

### Soft token <span class="glossary-card-badge">EXAM</span>

**Definition:** Software-based possession factor — typically an authenticator app generating one-time codes.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — MFA methods / tokens

**Tags:** `#mfa` `#tokens`

</div>

---

<div class="glossary-entry-card" id="term-something_you_are">

### Something you are <span class="glossary-card-badge">EXAM</span>

**Definition:** Inherence factor — biometrics such as fingerprint, face, or iris.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — authentication factors / biometrics

**Tags:** `#factors`

</div>

---

<div class="glossary-entry-card" id="term-something_you_have">

### Something you have <span class="glossary-card-badge">EXAM</span>

**Definition:** Possession factor — phone authenticator, hardware token, security key, or smart card.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — authentication factors

**Tags:** `#factors`

</div>

---

<div class="glossary-entry-card" id="term-something_you_know">

### Something you know <span class="glossary-card-badge">EXAM</span>

**Definition:** Knowledge factor — password, PIN, passphrase, or security question answer.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — authentication factors

**Tags:** `#factors`

</div>

---

<div class="glossary-entry-card" id="term-somewhere_you_are">

### Somewhere you are <span class="glossary-card-badge">EXAM</span>

**Definition:** Location / context attribute — geo, network segment, or trusted site used as an additional signal.

**Operational Context:** *Often treated as a contextual attribute rather than a classic factor.*

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — authentication attributes / context

**Tags:** `#factors`

</div>

---

<div class="glossary-entry-card" id="term-spanning_tree">

### Spanning Tree Protocol (STP / 802.1D / 802.1w) <span class="glossary-card-badge">EXAM</span>

**Definition:** A Layer 2 network protocol that monitors bridge topology and dynamically places redundant switch ports into blocking state to prevent catastrophic broadcast storms and switching loops.

**Operational Context:** *Transitions ports through listening, learning, and forwarding states (or rapid sync) to ensure a single, loop-free active path exists across redundant campus switches.*

**Certification & Domain Reference:**
- CompTIA Network+ N10-008 Domain 2.1 — Switching features, loop prevention, and Spanning Tree Protocol
- CompTIA Network+ N10-009 Domain 2.1 — Layer 2 protocols and high-availability switching

**Tags:** `#switching` `#layer2` `#stp` `#loops` `#network-plus`

</div>

---

<div class="glossary-entry-card" id="term-spear_phishing">

### Spear phishing <span class="glossary-card-badge">EXAM</span>

**Definition:** Targeted phishing aimed at a specific person or small group, customized with personal or role details.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — spear phishing

**Tags:** `#phishing`

</div>

---

<div class="glossary-entry-card" id="term-split_dns">

### Split-Horizon DNS <span class="glossary-card-badge">EXAM</span>

**Definition:** A domain name system architecture where internal and external queries for the same domain receive different IP address answers based on the client's network vantage point.

**Operational Context:** *Resolves private RFC 1918 addresses to hosts on the corporate LAN while providing external gateways or public landing pages to queries originating from the public internet.*

**Certification & Domain Reference:**
- CompTIA Network+ N10-008 Domain 1.5 — DNS services and architectures
- CompTIA Security+ SY0-701 Domain 2.5 — Network architecture and segmentation

**Tags:** `#dns` `#architecture` `#security`

</div>

---

<div class="glossary-entry-card" id="term-spoofing">

### Spoofing <span class="glossary-card-badge">EXAM</span>

**Definition:** Faking a sender identity — display name, email address, caller ID, or site look — to appear trusted.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — spoofing / impersonation

**Tags:** `#indicators`

</div>

---

<div class="glossary-entry-card" id="term-spyware">

### Spyware <span class="glossary-card-badge">EXAM</span>

**Definition:** Malware that secretly collects information about users, systems, or activity and sends it to an attacker.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — spyware

**Tags:** `#malware` `#privacy`

</div>

---

<div class="glossary-entry-card" id="term-ssh">

### SSH (22/TCP) <span class="glossary-card-badge">EXAM</span>

**Definition:** Encrypted remote shell and tunnel. Also carries SFTP and SCP. The standard Telnet replacement.

**Operational Context:** *Secure replacement for cleartext Telnet on remote admin paths.*

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — implement secure protocols (remote access)

**Tags:** `#remote` `#secure`

</div>

---

<div class="glossary-entry-card" id="term-ssid">

### SSID <span class="glossary-card-badge">EXAM</span>

**Definition:** Service set identifier — the network name a wireless network advertises (or tries to hide).

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — SSID / wireless basics

**Tags:** `#wireless`

</div>

---

<div class="glossary-entry-card" id="term-starttls">

### STARTTLS <span class="glossary-card-badge">SUPPORT</span>

**Definition:** A command that upgrades an existing cleartext connection to TLS mid-session (common on mail submission).

**Operational Context:** *Upgrades an existing cleartext mail session mid-stream (common on submission port 587).*

**Tags:** `#support` `#email` `#security`

</div>

---

<div class="glossary-entry-card" id="term-steganography">

### Steganography <span class="glossary-card-badge">EXAM</span>

**Definition:** Hiding a message inside other media (image, audio, file) so the secret's existence is less obvious.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — steganography

**Tags:** `#crypto`

</div>

---

<div class="glossary-entry-card" id="term-subnet_mask">

### Subnet Mask <span class="glossary-card-badge">EXAM</span>

**Definition:** A 32-bit bitmask that delineates the network prefix from the host identifier within an IPv4 address to determine whether a destination sits on the local or a remote subnet.

**Operational Context:** *Applied via bitwise logical ANDing by the host operating system to determine whether an IP packet can be delivered directly via local ARP or must be forwarded to the default gateway.*

**Certification & Domain Reference:**
- CompTIA Network+ N10-008 Domain 1.4 — IPv4 subnetting and classless inter-domain routing
- CompTIA Network+ N10-009 Domain 1.4 — Network addressing and subnet masks

**Tags:** `#ipv4` `#subnetting` `#cidr` `#network-plus`

</div>

---

<div class="glossary-entry-card" id="term-symmetric">

### Symmetric encryption <span class="glossary-card-badge">EXAM</span>

**Definition:** Same key encrypts and decrypts — fast for bulk data; key distribution is the hard part.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — symmetric encryption

**Tags:** `#crypto`

</div>

---

<div class="glossary-entry-card" id="term-syslog">

### Syslog (514/UDP) <span class="glossary-card-badge">EXAM</span>

**Definition:** Cleartext log forwarding to a collector. Secure with syslog over TLS on 6514.

**Tags:** `#monitor` `#insecure`

</div>

---

<div class="glossary-entry-card" id="term-syslog_tls">

### Syslog over TLS (6514/TCP) <span class="glossary-card-badge">EXAM</span>

**Definition:** Syslog carried inside TLS so log data stays confidential and intact in transit.

**Tags:** `#monitor` `#secure`

</div>

---

## T

<div class="glossary-entry-card" id="term-tacacs">

### TACACS+ (49/TCP) <span class="glossary-card-badge">EXAM</span>

**Definition:** Cisco AAA protocol that encrypts the full payload and separates authentication, authorization, and accounting.

**Tags:** `#aaa`

</div>

---

<div class="glossary-entry-card" id="term-tailgating">

### Tailgating <span class="glossary-card-badge">EXAM</span>

**Definition:** Following an authorized person through a door without badging yourself — exploiting politeness.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — tailgating

**Tags:** `#physical` `#attack`

</div>

---

<div class="glossary-entry-card" id="term-tcp">

### TCP <span class="glossary-card-badge">EXAM</span>

**Definition:** Connection-oriented transport that sequences and acknowledges data so lost packets can be recovered.

**Tags:** `#transport`

</div>

---

<div class="glossary-entry-card" id="term-reset_packet">

### TCP Reset (RST) <span class="glossary-card-badge">EXAM</span>

**Definition:** A TCP control segment with the RST flag asserted, sent by a host to abruptly terminate a connection or actively reject an inbound packet directed to an unbound port.

**Operational Context:** *Causes client applications to report 'Connection refused', confirming that the physical link and routing are functional but no listening daemon accepted the SYN packet.*

**Certification & Domain Reference:**
- CompTIA Network+ N10-008 Domain 4.1 — Network troubleshooting and packet analysis
- CompTIA Network+ N10-009 Domain 4.1 — Diagnosing TCP connection rejections and resets

**Tags:** `#tcp` `#flags` `#troubleshooting` `#network-plus`

</div>

---

<div class="glossary-entry-card" id="term-tcp_handshake">

### TCP Three-Way Handshake <span class="glossary-card-badge">EXAM</span>

**Definition:** The connection establishment process in Transmission Control Protocol where a client and server exchange SYN, SYN-ACK, and ACK packets to synchronize sequence numbers and allocate resources before data transfer.

**Operational Context:** *Guarantees reliable bidirectional delivery and sequence synchronization; if the SYN packet drops or encounters no listening service, data exchange cannot begin.*

**Certification & Domain Reference:**
- CompTIA Network+ N10-008 Domain 1.1 — OSI and TCP/IP transport models
- CompTIA Network+ N10-009 Domain 1.1 — Network protocols and TCP connection establishment

**Tags:** `#tcp` `#transport` `#handshake` `#network-plus`

</div>

---

<div class="glossary-entry-card" id="term-telnet">

### Telnet (23/TCP) <span class="glossary-card-badge">EXAM</span>

**Definition:** Remote shell that sends everything — including passwords — in cleartext. Replace with SSH.

**Operational Context:** *Do not allow on management paths; replace with SSH.*

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — insecure protocols / secure alternatives

**Tags:** `#remote` `#insecure`

</div>

---

<div class="glossary-entry-card" id="term-tftp">

### TFTP (69/UDP) <span class="glossary-card-badge">EXAM</span>

**Definition:** Tiny file transfer with no authentication. Acceptable only on trusted networks for device configs or PXE — never across a perimeter.

**Tags:** `#file` `#insecure`

</div>

---

<div class="glossary-entry-card" id="term-ticket">

### Ticket <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Tracked support request — the work unit the desk opens, updates, and closes.

**Tags:** `#support` `#desk`

</div>

---

<div class="glossary-entry-card" id="term-tls">

### TLS <span class="glossary-card-badge">EXAM</span>

**Definition:** Transport Layer Security — the encryption layer that wraps many application protocols into secure versions.

**Tags:** `#security`

</div>

---

<div class="glossary-entry-card" id="term-totp">

### TOTP <span class="glossary-card-badge">EXAM</span>

**Definition:** Time-based one-time password — short codes from a shared secret that rotate on a clock (common in authenticator apps).

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — MFA / OTP

**Tags:** `#mfa` `#otp`

</div>

---

<div class="glossary-entry-card" id="term-trojan">

### Trojan <span class="glossary-card-badge">EXAM</span>

**Definition:** Malware disguised as something useful or expected so the user installs it willingly.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — trojan

**Tags:** `#malware`

</div>

---

<div class="glossary-entry-card" id="term-troubleshooting_methodology">

### Troubleshooting Methodology <span class="glossary-card-badge">EXAM</span>

**Definition:** The standardized six-step diagnostic framework used to identify, isolate, resolve, and document computing failures.

**Operational Context:** *On the desk, it is the discipline of binary search: eliminating half the potential failure domains with every test before touching settings.*

**Certification & Domain Reference:**
- CompTIA A+ Core 2 (220-1102) Objective 1.4

**Tags:** `#methodology` `#diagnostic`

</div>

---

<div class="glossary-entry-card" id="term-trust_store">

### Trust store <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Collection of root/intermediate CAs the OS or browser trusts by default — the quiet list behind the padlock.

**Tags:** `#support` `#pki`

</div>

---

<div class="glossary-entry-card" id="term-typo_squatting">

### Typosquatting <span class="glossary-card-badge">EXAM</span>

**Definition:** Registering lookalike domains with typos or near-miss spellings of a trusted brand.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — typosquatting / URL indicators

**Tags:** `#indicators`

</div>

---

## U

<div class="glossary-entry-card" id="term-udp">

### UDP <span class="glossary-card-badge">EXAM</span>

**Definition:** Connectionless transport that sends datagrams without guaranteed delivery; used when speed or simplicity matters more than recovery.

**Tags:** `#transport`

</div>

---

<div class="glossary-entry-card" id="term-urgency">

### Urgency <span class="glossary-card-badge">EXAM</span>

**Definition:** Pressure to act immediately so the victim skips verification.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — social engineering principles (urgency)

**Tags:** `#principles`

</div>

---

<div class="glossary-entry-card" id="term-usb_data_blocker">

### USB data blocker <span class="glossary-card-badge">EXAM</span>

**Definition:** Inline adapter that passes power only — blocks data lines so a public charge port cannot talk to the phone.

**Operational Context:** *Often nicknamed a USB condom.*

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — USB data blockers

**Tags:** `#physical` `#endpoint`

</div>

---

<div class="glossary-entry-card" id="term-user_reported">

### User-reported <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Phish or suspicious message flagged by an employee (report button or forward) rather than only by automated filters.

**Tags:** `#support` `#response`

</div>

---

## V

<div class="glossary-entry-card" id="term-virus">

### Virus <span class="glossary-card-badge">EXAM</span>

**Definition:** Malware that attaches to files or programs and spreads when the host file runs or is shared.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — virus

**Tags:** `#malware`

</div>

---

<div class="glossary-entry-card" id="term-vishing">

### Vishing <span class="glossary-card-badge">EXAM</span>

**Definition:** Voice phishing — social engineering over phone or voice calls.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — vishing

**Tags:** `#phishing` `#voice`

</div>

---

<div class="glossary-entry-card" id="term-visitor_log">

### Visitor log <span class="glossary-card-badge">EXAM</span>

**Definition:** Record of who entered, when, and who escorted them — accountability for guests and contractors.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — visitor logs / escorts

**Tags:** `#physical` `#personnel`

</div>

---

<div class="glossary-entry-card" id="term-vlan">

### VLAN <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Virtual LAN; a logical network segment that isolates traffic without separate physical wiring.

**Tags:** `#support` `#network`

</div>

---

<div class="glossary-entry-card" id="term-vlan_trunking">

### VLAN Trunking (802.1Q) <span class="glossary-card-badge">EXAM</span>

**Definition:** A Layer 2 bridging mechanism allowing multiple virtual local area networks to traverse a single physical link by inserting a 4-byte 802.1Q VLAN tag into the Ethernet frame header.

**Operational Context:** *Carries isolated traffic classes—including Corporate, Telemetry, and VoIP—across campus backbone links without requiring dedicated physical cables for each broadcast domain.*

**Certification & Domain Reference:**
- CompTIA Network+ N10-008 Domain 2.1 — Configure and apply switching features (VLANs, 802.1Q trunking, native VLAN)
- CompTIA Network+ N10-009 Domain 2.1 — Network switching concepts and inter-VLAN transport

**Tags:** `#vlan` `#switching` `#layer2` `#802.1q` `#network-plus`

</div>

---

<div class="glossary-entry-card" id="term-vpn">

### VPN <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Encrypted tunnel for traffic — still wise on untrusted Wi-Fi even when the café page looks friendly.

**Tags:** `#support` `#network`

</div>

---

<div class="glossary-entry-card" id="term-concentrator">

### VPN concentrator <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Device/service that terminates many VPN tunnels for remote users.

**Tags:** `#support` `#network`

</div>

---

## W

<div class="glossary-entry-card" id="term-war_driving">

### War driving <span class="glossary-card-badge">EXAM</span>

**Definition:** Roaming an area to discover and map Wi-Fi networks — often looking for weak or open targets.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — war driving

**Tags:** `#wireless` `#recon`

</div>

---

<div class="glossary-entry-card" id="term-watering_hole">

### Watering hole <span class="glossary-card-badge">EXAM</span>

**Definition:** Compromising a site a target group already trusts, then waiting for victims to visit.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — watering hole

**Tags:** `#phishing` `#web`

</div>

---

<div class="glossary-entry-card" id="term-wep">

### WEP <span class="glossary-card-badge">EXAM</span>

**Definition:** Wired Equivalent Privacy — obsolete Wi-Fi encryption that is easily broken; treat as insecure legacy.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — WEP (insecure)

**Tags:** `#wireless` `#encryption`

</div>

---

<div class="glossary-entry-card" id="term-whaling">

### Whaling <span class="glossary-card-badge">EXAM</span>

**Definition:** Phishing aimed at high-value targets such as executives or other senior decision-makers.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — whaling

**Tags:** `#phishing`

</div>

---

<div class="glossary-entry-card" id="term-wifi_analyzer">

### Wi-Fi analyzer <span class="glossary-card-badge">EXAM</span>

**Definition:** Tool that shows SSIDs, channels, signal strength, and sometimes security modes — useful for survey and spotting twins.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — wireless analyzers / site survey tools

**Tags:** `#wireless` `#tools`

</div>

---

<div class="glossary-entry-card" id="term-wildcard_cert">

### Wildcard certificate <span class="glossary-card-badge">EXAM</span>

**Definition:** Certificate that covers many hostnames under one domain (like *.example.com) — convenient, broader blast radius if stolen.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — wildcard certificates

**Tags:** `#pki`

</div>

---

<div class="glossary-entry-card" id="term-controller">

### Wireless controller <span class="glossary-card-badge">SUPPORT</span>

**Definition:** Central brain that manages many APs — SSIDs, encryption mode, rogue detection, guest policy.

**Tags:** `#support` `#wireless`

</div>

---

<div class="glossary-entry-card" id="term-eavesdropping">

### Wireless eavesdropping <span class="glossary-card-badge">EXAM</span>

**Definition:** Capturing Wi-Fi frames from the air — catastrophic on open/WEP, still a concern if clients join the wrong network.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — eavesdropping / sniffing

**Tags:** `#wireless` `#attack`

</div>

---

<div class="glossary-entry-card" id="term-worm">

### Worm <span class="glossary-card-badge">EXAM</span>

**Definition:** Self-replicating malware that spreads across networks without needing a user to open a file each time.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — worm

**Tags:** `#malware` `#network`

</div>

---

<div class="glossary-entry-card" id="term-enterprise_wpa">

### WPA-Enterprise (802.1X) <span class="glossary-card-badge">EXAM</span>

**Definition:** Wi-Fi that authenticates each user/device via 802.1X (usually RADIUS) instead of one shared password.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — WPA2/WPA3-Enterprise / 802.1X

**Tags:** `#wireless` `#auth`

</div>

---

<div class="glossary-entry-card" id="term-wpa2">

### WPA2 <span class="glossary-card-badge">EXAM</span>

**Definition:** Wi-Fi Protected Access 2 — widely deployed Wi-Fi security using strong encryption (AES-CCMP) when configured correctly.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — WPA2

**Tags:** `#wireless` `#encryption`

</div>

---

<div class="glossary-entry-card" id="term-wpa3">

### WPA3 <span class="glossary-card-badge">EXAM</span>

**Definition:** Newer Wi-Fi security standard with stronger protections (including SAE) against offline password attacks and better open-network options.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — WPA3

**Tags:** `#wireless` `#encryption`

</div>

---

<div class="glossary-entry-card" id="term-wps">

### WPS <span class="glossary-card-badge">EXAM</span>

**Definition:** Wi-Fi Protected Setup — convenience pairing feature with a history of brute-force weaknesses; disable when possible.

**Certification & Domain Reference:**
- CompTIA Security+ SY0-701 — WPS risks

**Tags:** `#wireless` `#risk`

</div>

---

