# Visual Art Direction & Prompt Catalog: Tamarack Feed & Supply (Part 1: MIS 1–10)
**Repository:** `learning-narrative-kit`  
**Companion Track:** Tamarack Feed & Supply Company (A Narrative Primer for ITM 310)  
**Target Platform / Generator:** Grok Imagine (Aurora / FLUX-based synthesis)  
**Complements:** `docs/research/VISUAL_ART_DIRECTION.md` (Portland Desk Standard)

---

## 1. Executive Summary & Production Thesis

Following the visual art standards established for the *Learning Narrative Kit*:
1. **The Zero-Text Rule:** All generated artwork is completely wordless. The AI produces physical geometry, atmospheric lighting, and character acting. Browser/SVG engines or graphic design layers handle typography, ensuring zero AI spelling hallucinations, instant editing, and interactive hover tooltips.
2. **Grounded Realism Over Superhero Fantasy:** Tamarack is a rural farm-and-hardware business in eastern Washington and north Idaho. The aesthetic combines the kinetic composition of Jorge Jimenez / DC Comics with the physical authenticity of working feed mills, rural loading docks, dusty CRT monitors, and unventilated storage closets.
3. **Dual Visual Archetypes:**
   * **Full-Page Comic Spreads (`2:3` Portrait):** 4-to-5 panel sequential layouts capturing the *Goal $\rightarrow$ Complication $\rightarrow$ Pivot* narrative flow.
   * **Technical Cutaway & Narrative Plates (`16:9` / `3:2` Landscape or `4:3` / `3:4` Portrait):** Single, continuous, highly detailed illustrations capturing physical artifacts or system schemas.

---

## 2. Master Character DNA Anchors (Prompt Locks)

When generating artwork featuring recurring characters, include their exact, immutable description block in the prompt to preserve visual continuity across chapters:

* **Dana Okafor:**
  > `"Dana Okafor, early 30s Black female business systems analyst, athletic build, styled natural dark hair tied back cleanly, rectangular tortoiseshell glasses, expressive focused eyes, wearing a sharp navy blazer over a collared shirt."`
* **Curtis:**
  > `"Curtis, 62-year-old weathered feed store manager, short grey hair with a yellow pencil behind his ear, denim work jacket over faded flannel, grease-stained hands, observant posture."`
* **Arlo Nygaard:**
  > `"Arlo Nygaard, 64-year-old rural farm supply store manager, deeply weathered face with crow's feet, short cropped grey hair, trimmed grey-white beard, small wire-rimmed reading glasses, wearing a heavy red-and-black buffalo plaid wool flannel jacket and a brown knit beanie."`
* **Walt Brandvold:**
  > `"Walt Brandvold, late 50s energetic third-generation business owner, receding grey-blonde hair, animated posture, rolled-up light blue Oxford button-down shirt with no tie."`
* **Ruth Halvorsen:**
  > `"Ruth Halvorsen, 50s pragmatic Chief Operating Officer, sharp observant posture, grey bob haircut, charcoal blazer, holding a ceramic coffee mug."`
* **Teo Vasquez:**
  > `"Teo Vasquez, late 30s overworked IT manager, dark disheveled hair, dark-rimmed glasses, rolled-up sleeves, lanyard with keycards."`
* **Marcy Lund:**
  > `"Marcy Lund, 50s head buyer and merchandiser, horn-rimmed glasses, practical knit sweater, surrounded by ring binders and inventory catalogs."`
* **Gordon Ashby:**
  > `"Gordon Ashby, 68-year-old lean cattle rancher, canvas ranch jacket, scuffed leather boots, dust-stained western hat, weathered face with a dry humorous squint."`

---

## 3. Master Style Descriptors

### Style A: Grounded DC Comics / Jorge Jimenez Sequential Art (`2:3` Portrait)
```text
A full-page 5-panel comic book spread with clean white gutters, illustrated in the modern DC Comics graphic novel style of Jorge Jimenez. Crisp sharp black ink linework, heavy dynamic hatching, cinematic lighting, grounded Pacific Northwest farm-supply retail setting. Realistic human anatomy, expressive acting, clean empty panel backgrounds ready for lettering overlay. Wordless sequential visual storytelling. NO speech bubbles, NO dialogue text, NO captions, NO written words. 2:3 ratio.
```

### Style B: Clear Technical Cutaway & Fine Art Plate (`16:9` or `3:2` Landscape / `4:3` Portrait)
```text
Clean technical cutaway illustration in Pacific Northwest instructional manual style, crisp uniform ink linework, bright even inspection lighting, neutral background, no heavy dark shadows. Anatomically and electronically accurate hardware, true component colors, clean unlabeled surfaces, no text, no letters, no words, no watermarks, no speech bubbles.
```

---

## 4. Episode-by-Episode Image Prompt Directory (Part 1: MIS 1–10)

### MIS 1: Information Systems in Business (*The Pallet Discrepancy*)
* **Format:** Full-Page Comic Spread | **Aspect Ratio:** `2:3` (Portrait)
* **Goal:** Contrast the digital inventory system (`112`) with physical pallet count (`53`) and Curtis's paper ledger habit.
```text
A full-page 5-panel comic book spread with clean white gutters, illustrated in the modern DC Comics graphic novel style of Jorge Jimenez. Crisp sharp black ink linework, cinematic lighting, grounded Pacific Northwest farm-supply warehouse setting. 

Characters: Dana Okafor (early 30s Black female analyst, rectangular glasses, navy blazer), Curtis (62-year-old manager, grey hair, yellow pencil behind ear, denim jacket), Walt Brandvold (late 50s owner, blue Oxford shirt), Ruth Halvorsen (50s COO with coffee mug).

Panels Layout:
Panel 1 (Top Wide): Early morning warehouse bay in Colville, Washington. Sunlight and dust motes cutting through high clerestory windows down tall industrial pallet racks. Curtis gestures down the wide concrete aisle.
Panel 2 (Middle Left Macro): Dusty vintage green-phosphor CRT inventory monitor displaying the glowing green number '112' with a blinking block cursor. No sentences or other text.
Panel 3 (Middle Center): Bay Four. Dana Okafor holding a clipboard, looking down with a furrowed brow at a leaning wooden pallet holding only 53 torn burlap feed sacks with loose grain spilled across the concrete floor.
Panel 4 (Middle Right): Curtis opening a worn clothbound ledger notebook, tapping a blunt pencil stub against his handwritten physical count columns.
Panel 5 (Bottom Wide): Tamarack conference room. Walt Brandvold standing enthusiastically at a whiteboard drawing software flowchart boxes with dry-erase marker, while Ruth Halvorsen sits at the table sipping coffee with a skeptical raised eyebrow.

STRICT INSTRUCTION: Wordless sequential visual storytelling. NO speech bubbles, NO dialogue text, NO captions, NO written words anywhere on the page. Clean empty panel backgrounds ready for lettering overlay. Pure character acting, composition, and visual storytelling. 2:3 ratio.
```

---

### MIS 2: Computers and Hardware (*The Tape Backup & The Closet Server*)
* **Format:** Clean Technical Cutaway Plate | **Aspect Ratio:** `16:9` (Landscape)
* **Goal:** Show the improvised physical vulnerability of on-premises servers and untested tape media.
```text
Clean technical cutaway illustration in Pacific Northwest instructional manual style, crisp uniform ink linework, bright even inspection lighting, clean workshop background, no heavy dark shadows. 

Scene:
An aging open-frame server rack squeezed inside a cramped, wood-paneled feed-room supply closet. Bundles of blue Cat5e ethernet patch cables drape across the chassis like vines. A 2U rackmount server chassis has its top lid removed, revealing dual CPU heatsinks, green circuit board traces, cooling fans, and a hot-swap hard drive bay where a single amber fault LED indicator glows brightly next to three green drive LEDs. Propped on an upturned blue plastic milk crate on the concrete floor is a dusty household box fan blowing air into the rack. On a shelf above sits a dusty DLT magnetic backup tape cartridge with an unlabeled white write-on strip.

STRICT INSTRUCTION: Clean unlabeled surfaces, no text, no letters, no words, no numbers, no watermarks, no speech bubbles. True hardware component colors (blue cables, green PCB, amber and green LEDs). 16:9 ratio.
```

---

### MIS 3: Data and Business Intelligence (*Four Mailers to One Porch*)
* **Format:** Character / Narrative Plate | **Aspect Ratio:** `4:3` (Standard)
* **Goal:** Capture the primary key / foreign key duplication error (Gordon Ashby receiving four catalogs).
```text
Clean technical graphic novel illustration in the distinct aesthetic of Jorge Jimenez, sharp architectural linework, realistic human anatomy, cool overcast Pacific Northwest morning lighting.

Scene:
Rancher Gordon Ashby, a 68-year-old lean cattle rancher in a canvas ranch jacket, scuffed leather boots, and a dust-stained cowboy hat, stands at the wooden counter of the Tamarack Colville store. His mud-spattered white pickup truck is visible through the plate-glass window behind him. On the worn timber counter, Gordon drops four identical glossy retail advertising flyers side by side like a winning poker hand. Each flyer has identical cover artwork of a calf feeder, but four blank white mailing address label rectangles on the back. Gordon looks across the counter with a dry, humorous squint. 

Dana Okafor stands behind the counter holding a yellow legal pad with an ink-drawn entity relationship diagram showing two database tables with a broken key arrow.

STRICT INSTRUCTION: Clean composition, no text, no letters, no words, no numbers on the flyers or mailing labels, no speech bubbles. 4:3 ratio.
```

---

### MIS 4: Personal, Legal, Ethical, and Organizational Issues (*The Viral Video*)
* **Format:** Full-Page Comic Spread | **Aspect Ratio:** `2:3` (Portrait)
* **Goal:** The crisis of an unauthorized, out-of-context video accusing the company of selling toxic feed.
```text
A full-page 5-panel comic book spread with clean white gutters, illustrated in the modern DC Comics graphic novel style of Jorge Jimenez. Crisp sharp black ink linework, high emotional tension, moody Pacific Northwest interior office lighting.

Characters: Jesse (19-year-old store clerk, hoodie), Ruth Halvorsen (50s COO), Dana Okafor (early 30s analyst).

Panels Layout:
Panel 1 (Top Wide): Dimly lit Tamarack breakroom in the early morning. Half-eaten box of donuts on the table. Jesse nervously hands his glowing smartphone across the table to Ruth Halvorsen.
Panel 2 (Middle Left Macro): Extreme close-up of the smartphone screen displaying a vertical social media video interface: a blurry, shaky video of sick calves in a muddy feedlot pen, with angry red emoji reactions and comment icons bubbling up the side. The feed bag in the mud is an unfamiliar yellow sack (not Tamarack's green bag).
Panel 3 (Middle Center): Ruth’s face in tight dramatic lighting, eyes wide with cold focus as she taps the screen to freeze-frame on the feed sack.
Panel 4 (Middle Right): Jesse sitting in the driver's seat of his parked compact car in the dark store parking lot, fingers flying frantically across his phone screen as dashboard lights reflect in his glasses.
Panel 5 (Bottom Wide): Tamarack boardroom. Ruth standing tall at the end of the table with arms crossed, pointing at a printout of the feedlot video frame on the projector screen, laying down the company's factual response policy before the executive team.

STRICT INSTRUCTION: Wordless sequential visual storytelling. NO speech bubbles, NO dialogue text, NO captions, NO written words on the phone or screen. Pure character tension, composition, and visual storytelling. 2:3 ratio.
```

---

### MIS 5: Protecting Information Resources (*The Fake Seed Wire & The Parking Lot USB*)
* **Format:** Clean Technical Split / Macro Plate | **Aspect Ratio:** `16:9` (Landscape)
* **Goal:** Visualizing Business Email Compromise (BEC) wire fraud alongside physical social engineering (USB drops).
```text
Clean technical cutaway illustration in Pacific Northwest instructional manual style, crisp uniform ink linework, bright even inspection lighting, neutral background, no heavy dark shadows.

Two-part split composition:
Left Side (The Physical Trap): Extreme ground-level macro view of rain-slicked gravel near the Deer Park store loading dock at dusk. A puddle reflects industrial floodlights. Half-submerged in wet gravel and pine needles lies a bright neon-blue plastic USB thumb drive with a blank white paper label strip on its casing. A heavy steel-toed work boot is stepping directly beside it.

Right Side (The Digital Trap): An open office desk under a brass desk lamp. Controller Hank Pruitt’s hand rests frozen on an optical computer mouse. On the monitor, an email client displays a message with a prominent red "URGENT WIRE APPROVAL" button. A stylized magnifying glass cutaway above the screen reveals a subtle typographical mismatch in the sender email address domain header.

STRICT INSTRUCTION: Clean unlabeled surfaces, no text, no letters, no words, no speech bubbles. High technical and forensic accuracy. 16:9 ratio.
```

---

### MIS 6: Global Information Systems (*The Fencing Rep in Saskatoon*)
* **Format:** Full-Page Split Comic Spread | **Aspect Ratio:** `2:3` (Portrait)
* **Goal:** The friction of centralized global enterprise systems vs. local relationship buying.
```text
A full-page 4-panel comic book spread with clean white gutters, illustrated in the modern DC Comics graphic novel style of Jorge Jimenez. Sharp architectural contrast between rural Spokane warehouse and a sleek international corporate hub.

Characters: Marcy Lund (50s head buyer, horn-rimmed glasses, practical sweater), Dale Kowalchuk (fencing vendor rep, headset).

Panels Layout:
Panel 1 (Top Wide Split): 
- Left half: Marcy Lund in her cramped, paper-strewn Spokane office, surrounded by stacks of three-ring binder price catalogs from the last ten years, holding a telephone receiver to her ear with an impatient, frustrated grimace.
- Right half: A vast, sterile, glass-and-steel open corporate call center in Saskatoon, Canada. Rows of identical cubicles under bright fluorescent lights. Dale sitting with a phone headset, looking apologetic while pointing at a locked software interface on his monitor.
Panel 2 (Middle Left Macro): Marcy's desk calculator showing an unapproved bulk freight discount calculation with a red strike-through line drawn across a paper purchase order.
Panel 3 (Middle Right Macro): Dale’s computer screen displaying an enterprise approval routing tree with three greyed-out padlock icons blocking discount authorization without international headquarters sign-off.
Panel 4 (Bottom Wide): Marcy slamming the phone receiver back onto its desk cradle in Spokane, looking out through the rain-streaked window toward the outdoor yard where flatbed trailers wait for wire fencing.

STRICT INSTRUCTION: Wordless sequential visual storytelling. NO speech bubbles, NO dialogue text, NO captions, NO written sentences. Clean empty panels ready for lettering overlay. 2:3 ratio.
```

---

### MIS 7: Enterprise Systems (*Chick Days Disaster*)
* **Format:** Full-Page Comic Spread | **Aspect Ratio:** `2:3` (Portrait)
* **Goal:** The tangible chaos of an ERP supply chain swap—400 live baby chicks at the wrong store.
```text
A full-page 5-panel comic book spread with clean white gutters, illustrated in the modern DC Comics graphic novel style of Jorge Jimenez. Crisp sharp black ink linework, realistic anatomy, snowy Pacific Northwest lighting.

Characters: Arlo Nygaard (64-year-old rural manager, grey beard, wire glasses, red-and-black plaid jacket, beanie), Dana Okafor (early 30s Black female analyst, glasses, navy blazer), freight truck driver.

Panels Layout:
Panel 1 (Top Wide): Snowy Republic loading dock at dawn (6:15 AM). Arlo and a freight delivery driver heaving open the metal roll-up truck door with dynamic motion lines, revealing stacks of perforated brown chick boxes inside. Sound effect graphic above the door: 'KRR-RAAK!'.
Panel 2 (Middle Left): Arlo holding up a metal clipboard with a freight delivery manifest, staring down in shock and disbelief. The document lines are visible with a prominent blank quantity box.
Panel 3 (Middle Center Inset): Tight circular cutaway into a ventilation hole of a brown cardboard chick box, showing tiny fuzzy yellow chicks huddled together peeking out with black bead eyes. Sound effect graphic: 'cheep cheep!'.
Panel 4 (Middle Right): Arlo in the dusty store back room shouting into an old wall-mounted telephone receiver, clutching his forehead in exasperation.
Panel 5 (Bottom Wide): Head office in Spokane Valley. Dana Okafor sitting at her desk holding her office phone, looking stunned. Behind her is a whiteboard with a cleanly drawn flowchart diagram: '[Hatchery] -> [DC] -> [Stores] -> [POS]' with red warning arrows indicating a broken supply chain handoff.

STRICT INSTRUCTION: Wordless sequential storytelling. NO speech bubbles, NO dialogue text, NO captions, NO written words. Only the sound effects 'KRR-RAAK!' and 'cheep cheep!'. Clean empty panels ready for lettering overlay. 2:3 ratio.
```

---

### MIS 8: Supporting Decisions and Processes (*The Napkin vs. The Model*)
* **Format:** Side-by-Side Comparison Plate | **Aspect Ratio:** `16:9` (Landscape)
* **Goal:** Contrast intuitive gut decision-making (Walt's bar napkin) against geospatial decision support models (GIS isochrones).
```text
Clean technical cutaway illustration in Pacific Northwest instructional manual style, crisp uniform ink linework, bright even lighting, neutral background, no heavy dark shadows.

Scene:
A wooden boardroom conference table showing the direct collision between instinct and algorithmic decision support.

Foreground Left (The Gut Instinct): A wrinkled, beer-stained tavern cocktail paper napkin smoothed flat against the oak wood. Drawn in ballpoint pen ink that has bled into the paper fibers is a crude hand-sketched highway map showing Highway 95, an 'X' marking Sandpoint, Idaho, and a handwritten circle. Beside it rests an empty amber beer glass casting a warm shadow.

Background Right (The Algorithmic Model): A large dual-monitor workstation display. The screen renders a full-color GIS heat map of northern Idaho and eastern Washington. Smooth concentric drive-time contour rings (isochrones) radiate outward from existing Tamarack stores in green and yellow. A massive, vivid red cannibalization density cloud overlaps the Sandpoint area, showing where market demand would cannibalize existing store sales. Dana Okafor and a female regional planning consultant observe the screen with calm certainty.

STRICT INSTRUCTION: Clean unlabeled surfaces, no text, no letters, no words, no numbers, no speech bubbles. High cartographic and graphic fidelity. 16:9 ratio.
```

---

### MIS 9: Artificial Intelligence and Automation (*The Dewormer Syringe Intercept*)
* **Format:** Dynamic Procedural Comic Spread | **Aspect Ratio:** `2:3` (Portrait)
* **Goal:** Expert systems vs. human domain knowledge—intercepting a lethal species contraindication at point of sale.
```text
A full-page 4-panel comic book spread with clean white gutters, illustrated in the modern DC Comics graphic novel style of Jorge Jimenez. High-stakes procedural retail tension, crisp inking, expressive faces.

Characters: Curtis (62-year-old veteran manager, denim jacket), Jesse (19-year-old clerk), an anxious local farmer in mud-stained overalls.

Panels Layout:
Panel 1 (Top Wide): The checkout counter at the Tamarack Colville store. An anxious farmer in overalls places a large plastic oral dosing syringe of livestock dewormer on the counter next to a handheld barcode scanner.
Panel 2 (Middle Left Macro): Extreme close-up of the dewormer syringe label. A prominent red-bordered warning box shows a bold black silhouette of a cow with a green checkmark, and a bold red universal 'NO' circle-slash over the silhouette of a goat kid.
Panel 3 (Middle Right Dynamic): Curtis's weathered hand lunges into the frame with lightning speed, his fingers firmly gripping the plastic syringe barrel right before Jesse's barcode scanner beam can hit the code. Jesse's eyes go wide behind the cash register.
Panel 4 (Bottom Wide): Curtis holding the proper goat-safe medication bottle from the back shelf, showing it side-by-side to the grateful farmer at the counter, while pointing at the warning label on the first box to teach both the clerk and the customer.

STRICT INSTRUCTION: Wordless sequential visual storytelling. NO speech bubbles, NO dialogue text, NO captions, NO written words. Pure visual tension, character acting, and procedural safety. 2:3 ratio.
```

---

### MIS 10: Emerging Trends, Technologies, and Applications (*The 97°F Meltdown & The Cloud Expo*)
* **Format:** Full-Page Comic Spread | **Aspect Ratio:** `2:3` (Portrait)
* **Goal:** The contrast between physical server closet fragility and the promises of distributed edge and public cloud architectures.
```text
A full-page 5-panel comic book spread with clean white gutters, illustrated in the modern DC Comics graphic novel style of Jorge Jimenez. Crisp sharp black ink linework, dramatic lighting contrast between sweltering server closet and futuristic trade expo.

Characters: Teo Vasquez (late 30s IT manager, glasses, rolled sleeves), Dana Okafor (early 30s analyst, navy blazer), Brenda (cloud vendor sales engineer in corporate polo).

Panels Layout:
Panel 1 (Top Left Macro): Digital indoor thermometer taped to the steel upright of an open server rack with masking tape. The red LED display glows brightly: '97.4°F' with a blinking warning bell icon.
Panel 2 (Top Right): Teo Vasquez on his knees in the cramped feed-room closet, sweat on his brow, wiping dust from a rattling household box fan balanced on an upturned blue plastic milk crate blowing hot air into the rack.
Panel 3 (Middle Wide): The server rack NAS unit display screen shutting down with amber drive lights blinking out into complete darkness, as office lights in the hallway flicker.
Panel 4 (Bottom Left): Two days later at the bustling Boise Farm-Retail Tech Expo. Dana and Teo standing in an expansive, neon-lit exhibition hall, gazing up at towering, illuminated corporate trade booths with glowing cloud logos.
Panel 5 (Bottom Right): Brenda, an ERP sales engineer, turning her laptop screen around to show Dana and Teo a clean architectural diagram: a small backroom store server icon labeled with an edge icon, connecting to a central cloud server through a dotted line across mountains.

STRICT INSTRUCTION: Wordless sequential storytelling. NO speech bubbles, NO dialogue text, NO captions, NO written words. Only the digital LED '97.4°F' on the thermometer. Clean empty panels ready for lettering overlay. 2:3 ratio.
```
