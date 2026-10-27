# Flashcard & Field Slate Architecture Specification
**Portland Desk (Book 0: Zero-to-One)**  
*Document Version: 1.0. Active standard for field slates; ranks per `AGENTS.md` precedence.*

---

## 1. Executive Summary & Design Mandate

The Portland Desk curriculum distinguishes strictly between **Active Retrieval Flashcards** (atomic memory trivia) and **Structural Job Aids** (pocket decision flowcharts and pinouts). This prevents cognitive thrashing and eliminates the trap of trying to memorize complex procedural workflows on flashcards.

This document formalizes:
1. **Physical Provenance:** Exactly how Ethan Brooks manufactures and carries these physical tools within the story.
2. **Digital In-Situ Embedding:** Where these instruments appear within the daily reading and lab workflow.
3. **Macro Deck Hubs (`#/slates` and `#/flashcards`):** How learners access aggregated slates and cumulative spaced-repetition decks across all 13 modules.
4. **Physical Fabrication & Print Standard:** Print-ready cut sheets for 3x5 index cards and 4x6 laminated cardstock.

---

## 2. Physical & Narrative Provenance (How Ethan Makes Them)

```mermaid
flowchart TD
    subgraph S1["Kitchen Table Epiphany (Module 00)"]
        Fail["Failed Attempt 1: 592 / 675<br/>(400 Brute-Force Flashcards)"] --> Table["Kitchen Table Talk with Frank Mercer<br/>(Machinist Tradecraft Perspective)"]
        Table --> Sort["Four Rubber Bands Mug<br/>(Red | Green | Yellow | Blue)"]
    end

    subgraph S2["Physical Manufacturing"]
        Sort -->|Flashcard Cut| RedDeck["Red Band (~40 Cards)<br/>Walgreens 3x5 Blank Ruled Cards<br/>Blue Bic Pen + Red Highlighter Top Stripe"]
        Sort -->|Job Aid Pivot| Slates["Green, Yellow, Blue (13 Slates)<br/>FedEx Office on 82nd Ave ($0.23/page)<br/>Matte 4x6 Cardstock + 2\" Scotch Heavy-Duty Tape Lamination<br/>Single Hand-Punched Corner Lanyard Eyelet"]
    end

    subgraph S3["Workplace Deployment"]
        RedDeck --> PocketDrill["Morning Transit / Lunch Break<br/>10-Second Active Retrieval Drills"]
        Slates --> BenchUse["On the Bench & In the Rack<br/>Physical Reference While Inspecting Hardware"]
    end
```

### The 3x5 Red Band Cards ("The Passport Deck")
* **Raw Material:** Standard Walgreens 3x5 lined/blank index cards ($1.19 per 100-pack).
* **Marking:** Handwritten in dark blue Bic ballpoint pen with a single bold swipe of red chisel-tip highlighter along the top edge. Bound by a single red rubber band.
* **The 10-Second Audit:** If the answer takes more than 10 seconds to say aloud, the card is too long. No paragraphs, no procedural steps.
* **Content Scope:** Port numbers, ATX rail voltages, pin counts, binary boundary definitions, and specific diagnostic tool indicators (e.g., discriminant values, loopback addresses).

### The 4x6 Double-Sided Field Slates (Green, Yellow, Blue Bands)
* **Raw Material:** Heavyweight 4x6 matte index cardstock printed at the 24-hr FedEx Office on 82nd Ave ($0.23 per double-sided monochrome sheet).
* **DIY Lamination:** Sealed on both faces with overlapping strips of 2-inch Scotch heavy-duty packaging tape to protect against coffee, warehouse dust, and grease.
* **Field Hardware:** Single corner hole punched with a handheld brass eyelet or hole punch, slipped onto an aluminum carabiner inside Ethan's canvas field bag.
* **Content Scope:**
  * **Side A (Tactical Ground Truth):** Invariants, pinouts, voltage truth tables, and protocol anatomy.
  * **Side B (Binary Search Compass):** Step-by-step diagnostic decision trees, CLI commands, and failure triage logic.

---

## 3. Digital Architecture: Where Do They Live in the Product?

We establish a **Dual-Layer Architecture**: contextual in-page tools for immediate application, and centralized macro hubs for review and printing.

```
┌────────────────────────────────────────────────────────────────────────┐
│                              PORTLAND DESK                             │
│                                                                        │
│   ┌────────────────────────┐              ┌────────────────────────┐   │
│   │   IN-SITU APPLICATION  │              │    MACRO DECK HUBS     │   │
│   │                        │              │                        │   │
│   │  Workbench Section 2:  │              │  #/slates :            │   │
│   │  4x6 Field Slate Embed │              │  Field Slates Hangar   │   │
│   │  (Dual-face live tab)  │              │  (13 slates + print)   │   │
│   │                        │              │                        │   │
│   │  Workbench Section 3:  │              │  #/flashcards :        │   │
│   │  3x5 Red Warmup Deck   │              │  Cumulative Spaced     │   │
│   │  (3-5 atomic cards)    │              │  Repetition Trainer    │   │
│   └────────────────────────┘              └────────────────────────┘   │
└────────────────────────────────────────────────────────────────────────┘
```

### Layer 1: In-Situ Placement (Per Episode)

1. **In the Story Narrative:**
   * At the pivotal troubleshooting moment, Ethan physically reaches into his canvas bag or breast pocket, unclips his laminated slate, or flips a red index card.
   * A callout badge highlights the exact tool in play with a direct link to inspect the slate.

2. **In Workbench Section 2 (Technical Reference & Triage Matrix):**
   * The complete, high-fidelity **4x6 Field Slate** is embedded directly at the top of Section 2 using the ````job-aid type="slate" ```` fence.
   * Instant `[Side A] | [Side B]` tabs allow the learner to flip between the reference diagram and the decision matrix without leaving their place.

3. **In Workbench Section 3 (Quick Checks & Skill Reps):**
   * Before attempting the Symmetrical Challenge tickets, the learner encounters the **3x5 Red Band Warmup Deck** (3–5 atomic cards).
   * Interactive 3D flip card lets the learner test their recall under the 10-second rule before applying that knowledge to the live ticket.

---

### Layer 2: Centralized Macro Hubs (Course-Wide)

#### Hub A: The Field Slates Hangar (`#/slates`)
* **Route:** Accessible from the top header navigation or sidebar drawer under `Reference Tools > Field Slates`.
* **Deck Catalog:** Houses all 13 double-sided Field Slates (Slates 00 through 12).
* **Filter by Band:**
  * **Green Band (Hardware Anatomy):** Slates 00, 01, 02.
  * **Blue Band (The Wire & Boundary):** Slates 03, 04, 05, 06.
  * **Yellow Band (Identity & Threat Triage):** Slates 07, 08, 09, 10, 11, 12.
* **Print Engine:** Includes a `[ Print Complete Field Slate Set ]` button with dedicated `@media print` CSS:
  * Formats slates 2-up per standard 8.5" x 11" page with dashed corner crop marks.
  * Side A and Side B arranged for standard duplex (double-sided) edge-to-edge printing.

#### Hub B: The Cumulative Passport Deck (`#/flashcards`)
* **Route:** Accessible from `Practice & Drills > Red Band Passport Deck`.
* **Spaced Repetition Engine:** Aggregates all unlocked Red Band cards across completed modules (e.g. 3 cards in Mod 00 + 4 cards in Mod 01 + 4 cards in Mod 02 = 11 cards unlocked).
* **Interactive Drill Modes:**
  1. **Speed Blitz (10-Second Countdown):** Prompts the card, starts an audible/visual 10-second ticker, and forces rapid recall.
  2. **Interleaved Shuffle:** Mixes port numbers, ATX voltages, and subnet boundaries randomly to prevent rote location memorization.
  3. **Leitner Mastery (Box 1 / Box 2 / Box 3):** Saves mastery status in browser `localStorage`. Difficult cards appear frequently; mastered cards graduate to weekly review.
* **Print Sheet:** Generates an Avery 5388 (3x5 index card 3-up) printable PDF/HTML view.

---

## 4. Episode-by-Episode Slate & Flashcard Mapping

| Episode | 4x6 Field Slate (Section 2) | Band | Side A / Side B Focus | Red Band Warmup Cards (Section 3) |
|---|---|---|---|---|
| **00** | Slate 00: Core Machine Compass | / | Motherboard Topography & PSU Rails / Triage Flow | Loopback IP, RAM beep codes, swollen capacitor sign |
| **01** | Slate 01: The Industrial Serial Bench | Green | 24-Pin ATX Voltages / RS-232 Pinout & Baud Settings | ATX +12V/+5V rail colors, Null Modem vs Straight, baud 9600 |
| **02** | Slate 02: Fleet Endpoint Triage | Blue | BitLocker Recovery Architecture / Event Viewer IDs | BitLocker 48-digit key format, Event ID 41, BSOD STOP code |
| **03** | Slate 03: The Subnet & Gateway Matrix | Blue | IPv4 CIDR Subnetting Table / ARP vs MAC Resolution | APIPA 169.254 range, RFC 1918 private ranges, default route 0.0.0.0/0 |
| **04** | Slate 04: The DNS Resolution Chain | Yellow | Root Hints to Authoritative / dig & nslookup Flags | Port 53 UDP vs TCP, DNS record types (A, AAAA, CNAME, MX, PTR) |
| **05** | Slate 05: Layer 1 Copper & Optical | Green | T568A vs T568B Pinout / Multimode vs Singlemode Specs | 100m Ethernet max length, wire pairs for PoE, 850nm vs 1310nm |
| **06** | Slate 06: Disaster Recovery & Switching | Blue | VLAN Trunking 802.1Q / DHCP Scope Exhaustion Matrix | 802.1Q tag size (4 bytes), DHCP DORA ports (67/68), trunk native VLAN |
| **07** | Slate 07: Security Boundaries & Transport | Yellow | Common Ports & Services / Cleartext vs Cipher Risk | Port 22 SSH vs Port 23 Telnet, Port 443 HTTPS, 3389 RDP |
| **08** | Slate 08: Identity & Authentication | Yellow | Kerberos TGT vs Service Tickets / LDAP vs LDAPS | Port 88 Kerberos, Port 389 vs 636 LDAP, AAA triad definitions |
| **09** | Slate 09: Social Engineering & Email Auth | Yellow | SPF / DKIM / DMARC Record Syntax & Header Analysis | SPF txt syntax, DKIM cryptographic signature header, quarantine vs reject |
| **10** | Slate 10: Endpoint Malware Remediation | Blue | CompTIA 7-Step Malware Procedure / Persistence Keys | Safe Mode boot trigger, Run/RunOnce registry hives, isolation step |
| **11** | Slate 11: Wireless 802.11 & 802.1X | Yellow | WPA3 SAE vs 802.1X EAP-TLS / Rogue AP vs Evil Twin | 2.4GHz non-overlapping channels (1, 6, 11), RADIUS ports (1812/1813) |
| **12** | Slate 12: Incident Handoff & Chain of Custody | Blue | Order of Volatility / Evidence Hash Verification | Order of volatility (RAM before Disk), SHA-256 integrity, chain of custody |

---

## 5. Physical Print Template Specifications

### 4x6 Field Slate Print Specs (Standard Duplex Cut Sheet)
* **Canvas:** Standard US Letter (8.5" x 11") in Landscape mode.
* **Layout:** 2 cards per sheet (front and back aligned).
* **Margins & Bleed:** 0.25" exterior border with dotted cut guidelines (`border: 1px dashed #64748b`).
* **Paper Stock Recommendation:** 110 lb (199 gsm) Index Cardstock or 80 lb Cover.
* **Finishing:** Cold pouch laminate or 2-inch packaging tape overlay with 3mm corner radius.

### 3x5 Flashcard Print Specs
* **Standard Compatibility:** Compatible with Avery 5388 / 3-per-page 3" x 5" perforated cardstock or standard 8.5" x 11" with 0.5" gutter.
* **Front:** High-contrast Question / Mini-Scenario with Comic Neue / Bangers headline.
* **Back:** 1-sentence punchy atomic answer (under 10 seconds).
