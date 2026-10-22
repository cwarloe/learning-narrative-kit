# Visual Art Direction & Technical Illustration Standard
**Repository:** `learning-narrative-kit`  
**Focus:** Frontline Hardware, Network, and Cybersecurity Courseware  
**Target Platform:** Docsify v4 (`docs/portland-desk`) & Grok Imagine

---

## 1. Executive Summary & Art Thesis

Technical learning materials suffer when forced into either extreme:
1. **Abstract flowcharts (e.g. Mermaid):** Useful for pure routing logic or bitwise CIDR math, but completely sterile for physical hardware, bent serial pins, water-damaged patch panels, and voltmeter probes.
2. **Generic Stock Photography:** Smiling models wearing anti-static wristbands, holding clean circuit boards in sterile brightly-lit studios. It feels fake and disconnected from real field work.

### The Style Anchor: "Clear Technical Cutaway" (Ligne Claire)
Our visual identity marries the authentic atmosphere of the Pacific Northwest (rain-slicked pavement, unventilated wiring closets, high-bay metal warehouse framing) with the exacting precision of **clean technical cutaways** (inspired by *iFixit teardowns*, *vintage aerospace service manuals*, and clean European line art like *Hergé* and *Chris Ware*):
* **Lighting:** Bright, shadowless workbench illumination (ring light or dual inspection lamps) on the actual technical fault.
* **Line Work:** Crisp, uniform black ink outlines; every pin, wire, latch, and capacitor is anatomically distinct.
* **Color Accuracy:** True industry-standard component colors (ATX wire color codes: Yellow +12V, Red +5V, Orange +3.3V, Black Ground; phosphor green link lights; amber fault LEDs).

---

## 2. Separation of Concerns: Why AI Images Must Contain Zero Text

Diffusion and image generation models (including Grok Imagine, Midjourney, and DALL-E) treat text as decorative texture rather than semantic symbols. Asking an image generator to draw `"10.84 V"`, `"Pin 2 RXD"`, or `"svch0st.exe"` reliably produces misspelled, alien-looking gibberish.

### The Production Law
> **The AI generates the physical geometry, materials, and lighting. The browser renders the text, callout pins, and technical telemetry.**

1. **Prompt Rule:** Always include:  
   `clean composition, no text, no letters, no words, no numbers, no watermarks, unlabeled components, unprinted display screens.`
2. **Browser Overlay:** Docsify uses the `callout-panel` component and interactive pins to anchor crisp, accessible, typo-free typography directly over the image.

---

## 3. Reference Image (Image-to-Image) Workflow for Grok Imagine

To ensure 100% technical fidelity (preventing hallucinated 7-pin D-sub connectors or incorrect motherboard sockets):
1. **Source a real reference photo** (from Wikimedia Commons, an open-source hardware repo, or a smartphone photo of real hardware on a bench).
2. **Upload the photo into Grok Imagine as an image-to-image reference.**
3. **Apply the technical restyling prompt** below to preserve the physical layout while rendering in clean, uniform technical cutaway style.

---

## 4. Master Aspect Ratio Standards

| Ratio | Best Suited For | Episodes / Components |
| :---: | :--- | :--- |
| **`16:9`** | Standard landscape narrative panels, split-screens, and monitor views. | Ep 01 (Multimeter), Ep 03 (Wall Jack), Ep 05 (Rollover), Ep 07 (Perimeter), Ep 10 (Process Explorer), Ep 11 (Spectrum). |
| **`21:9`** | Cinematic ultrawide panoramic capstone moments. | Ep 06 (The Portland Flood / Sub-basement trench), Ep 12 (Incident War Room). |
| **`4:3`** | Top-down chassis cutaways, component macro shots, document layers. | Ep 00 (OptiPlex Guts), Ep 02 (RAM Latch), Ep 08 (Phone Push), Ep 09 (Malicious PDF). |
| **`1:1`** | Tight macro details of ports, connectors, and pins. | Ep 01 (Bent DB-9 Pin), Ep 03 (RJ45 Keystone Jack). |
| **`3:4`** | Full-body vertical character concept sheets. | Ethan Mercer, Desk Lead Jules Brooks. |

---

## 5. Master Prompt Style Prefix

Always prefix every Grok Imagine prompt with this consistent descriptor:
```text
Clean technical cutaway illustration in Pacific Northwest instructional manual style, crisp uniform ink linework, bright even inspection lighting, clean neutral ESD mat background, no heavy dark shadows, anatomically and electronically accurate hardware, true component colors, no text, no letters, no words, no watermarks.
```

---

## 6. Complete Episode-by-Episode Image Prompt Directory

### Character Sheet: Ethan Mercer (3:4 Ratio)
```text
Character concept sheet for Ethan Mercer, 19-year-old frontline help desk technician, in clean technical graphic novel line art style. Lanky build, dark hair slightly disheveled, weary but focused eyes, wearing a dark canvas Carhartt-style jacket over a grey hoodie, worn jeans, steel-toed work boots, with a black lanyard holding a contractor ID badge and a stainless-steel 0.5mm mechanical pencil clipped to his pocket. Three panel poses: inspecting an RJ45 cable with a penlight, typing at an industrial terminal, and listening intently to a mentor. Bright even lighting, clean lines, no text, no words. 3:4 ratio.
```

### Character Sheet: Jules Brooks (3:4 Ratio)
```text
Character concept sheet for Jules Brooks, 34-year-old female Level 1 Help Desk Lead, in clean technical graphic novel line art style. Practical, authoritative presence, sharp intelligent facial features, shoulder-length straight dark hair with subtle silver streaks tucked behind one ear, wearing a comfortable flannel shirt or dark blazer over a black t-shirt, wired call-center headset pushed back over one ear, ceramic coffee mug in one hand, matte silver commuter bicycle helmet nearby. Calm, observant mentor expression of an experienced systems troubleshooter. Three panel poses: leaning over a technician's shoulder pointing at a terminal screen, listening on headset, and sketching a network diagram on a whiteboard. Bright even lighting, clean lines, no text, no words. 3:4 ratio.
```

### Episode 00: The Swollen Capacitors & Unseated Memory (4:3 Ratio)
```text
Clean technical cutaway illustration in Pacific Northwest instructional manual style, crisp uniform ink linework, bright even inspection lighting, clean ESD mat background, no heavy dark shadows. Macro technical inspection shot of a desktop PC motherboard interior: in sharp foreground focus are three cylindrical electrolytic capacitors on the green PCB. Two capacitors have prominently domed, bulging silver tops with cracked score lines and dried crusty brown electrolyte residue leaking from the seam. The third capacitor is completely flat and healthy for visual contrast. Directly behind them is a dual-channel memory slot holding a green RAM module with one white plastic retention latch broken off at an angle. Crisp fine ink linework, true component colors, clean unlabeled surfaces, no text, no letters, no words. 4:3 ratio.
```

### Episode 01: The ATX 24-Pin Multimeter Probing (16:9 Ratio)
```text
Transform reference photo into a clean technical cutaway illustration. Bright, even workbench lighting, clean ESD mat background, crisp fine ink linework, no heavy shadows. Accurately preserve the 24-pin connector layout, showing distinct wire colors: Pin 10 yellow +12V wire, red +5V wire, orange +3.3V wire, and black ground wires. A precision red multimeter needle probe is inserted into the rear of Pin 10 yellow wire while mated. Clean unlabeled surfaces, no text, no words. 16:9 ratio.
```

### Episode 01: The Bent DB-9 Serial Pin & Drafting Pencil (1:1 Ratio)
```text
Transform reference photo of a DB-9 male connector into a high-detail macro technical illustration. Bright, even illumination, clean studio lighting. Maintain the exact 9-pin trapezoidal arrangement (5 pins on top, 4 pins on bottom). Pin 2 on the top row is bent backward at a 45-degree angle. A 0.5mm stainless steel drafting pencil with a hollow brass guide sleeve is positioned directly over the bent pin, using the sleeve as a straightening tool. Sharp mechanical accuracy, crisp line art, clean neutral background, no text, no letters. 1:1 ratio.
```

### Episode 02: Motherboard Memory Slot & Broken Latch (4:3 Ratio)
```text
Transform reference motherboard photo into a clean technical instruction manual illustration. Bright, even inspection lighting, sharp macro focus. The long memory DIMM slot is clearly visible on the circuit board, with one white plastic end-latch broken off and cocked at a 15-degree angle, causing the gold edge contacts of the RAM module to be slightly unseated from the socket pins. A small dual-digit digital display glows red nearby. Crisp component outlines, clean PCB traces, no heavy shadows, no text, no letters. 4:3 ratio.
```

### Episode 03: The /26 Subnet Boundary & Default Gateway (16:9 Ratio)
`	ext
Clear technical cutaway illustration of a network architecture schematic under bright neutral lighting. Two adjacent server chassis on a 19-inch equipment rack connected to a central switch. A glowing logical boundary line divides Subnet A (192.168.10.0) and Subnet B (192.168.10.64). Packets halt at the subnet boundary line before reaching the router gateway interface. Crisp technical drawing style, Ligne Claire, no text, no letters. 16:9 ratio.
`

### Episode 04: Split-Horizon DNS & Hosts File (16:9 Ratio)
```text
Clean technical cutaway diagram of a computer desktop screen displaying DNS resolution paths under bright, even lighting. Flowchart lines connect local hosts file to DNS resolver cache and recursive domain controllers. Clean instructional style, crisp fine lines, no text, no words. 16:9 ratio.
```

### Episode 05: Layer 4 TCP State Machine & TIME_WAIT Exhaustion (16:9 Ratio)
```text
Clean technical cutaway diagram of a network protocol state machine under bright inspection lighting. Flowchart lines illustrate TCP four-way handshake connection termination from FIN-WAIT to TIME-WAIT to CLOSED. A highlighted warning box depicts dynamic ephemeral port exhaustion. Crisp technical drawing style, Ligne Claire, no text, no letters. 16:9 ratio.
```

### Episode 06: The Sub-Basement Flood & Patch Trench (21:9 Ratio)
```text
Clean technical cutaway illustration of a server room during a water leak under bright emergency lights. Bundles of blue network cables hang above a wall-mounted 48-port patch panel. A rackmount switch with glowing green port LEDs. Clean instructional drawing style, crisp fine lines, no text, no words. 21:9 ratio.
```

### Episode 07: Network Perimeter & Port Scan (16:9 Ratio)
```text
Clean technical schematic of a corporate network perimeter under bright, even lighting. Flowchart lines connect external internet router to internal firewall and server racks with port numbers highlighted in green and red. Crisp technical line art, no text, no words. 16:9 ratio.
```

### Episode 08: Authentication Factors & Lockout (4:3 Ratio)
```text
Clean technical illustration of a smartphone on an office desk next to a computer monitor under bright office lighting. The monitor displays security event logs with red warning highlights. Clean instructional manual style, crisp lines, no text, no words. 4:3 ratio.
```

### Episode 09: Email MIME Architecture & SPF (4:3 Ratio)
```text
Clean technical cutaway diagram of an email message header structure under bright lighting. Arrows connect sender IP address to DNS TXT record for SPF validation. Clean instructional manual style, crisp fine lines, no text, no words. 4:3 ratio.
```

### Episode 10: Process Tree & Rogue Persistence (16:9 Ratio)
```text
Clean technical illustration of a computer monitor displaying a system process management tree under bright laboratory lighting. Process rows are neatly organized with one highlighted entry showing an anomalous socket connection. Clean line art, no text, no words. 16:9 ratio.
```

### Episode 11: Wireless Spectrum & Rogue AP Interference (16:9 Ratio)
```text
Clean technical cutaway diagram of radio frequency spectrum channels under bright studio lighting. Bell curves represent Wi-Fi channels 1, 6, and 11 across the 2.4 GHz band, with interference spikes overlapping channel 6. Crisp technical line art, no text, no words. 16:9 ratio.
```

### Episode 12: Forensic Acquisition & Write-Blocker (16:9 Ratio)
```text
Clean technical illustration of a computer forensic examination bench under bright laboratory lighting. An external storage drive connects through a small rectangular hardware write-blocker with a glowing green LED to a laptop. Anti-static bags and clean tools on an ESD mat. Sharp technical linework, no text, no words. 16:9 ratio.
```
