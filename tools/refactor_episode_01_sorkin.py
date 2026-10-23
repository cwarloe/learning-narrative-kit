#!/usr/bin/env python3
"""Update Episode 01 narrative and workbench with grounded Sorkin-style arc."""

from pathlib import Path
import shutil

ROOT = Path(r"C:\Users\charl\learning-narrative-kit")
PORTLAND = ROOT / "portland-desk"
DOCS = ROOT / "docs" / "portland-desk"

def update_ep01_workbench():
    w_file = PORTLAND / "workbench" / "01-the-paper-cert.md"
    content = w_file.read_text(encoding="utf-8")
    
    target_header = "## 6. The Shift Resolution & Epilogue: 05:04 AM"
    assert target_header in content, "Target header not found in Ep 01 workbench"
    
    pre = content.split(target_header)[0]
    
    epilogue_text = """## 6. The Shift Resolution & Epilogue: 05:04 AM

```callout-panel
title: "FIGURE 1.2: LINE FOUR RESTORATION & 05:04 AM DISPATCH"
badge: "Shift Epilogue"
caption: "Cross-dock floor: At 05:04 AM, Line 4 runs at full speed under the high-bay lamps. Parcels route smoothly into outgoing cages while Ken Vance signals the yard tractors to roll."
prompt: "Clean graphic novel cutaway panel of an industrial freight warehouse cross-dock at dawn. Overhead metal-halide lamps illuminate an automated conveyor line carrying cardboard boxes into freight trailers. In the foreground, a young technician in a high-vis orange vest leans against a steel cabinet holding a digital multimeter. A supervisor with an aluminum clipboard signals with a raised hand toward the loading bays. Pacific Northwest silicon noir style, crisp ink linework, no text, no words. 16:9 ratio."
```

*The following operational debrief records the physical resolution on the warehouse floor once the clock divider fix is verified:*

With the clock divider calculation verified on the console, I located DIP switch bank `SW1` in the lower corner of the motherboard. Using the fine flat tip of my father's jeweler's screwdriver, I reached into the chassis. I clicked switch 3 from ON down to OFF, and pushed switch 4 from OFF up to ON.

The mechanical click of the miniature plastic toggles felt sharp and definitive in the quiet cabinet.

I restarted the serial communication daemon from the terminal prompt. The torrent of garbled characters vanished instantly. It was replaced by a clean, rhythmic stream of formatted telemetry:

```
SCALE_04: READY - 042.8 LBS - DIVERTER NORMAL
SCALE_04: READY - 043.1 LBS - DIVERTER NORMAL
```

Ken did not waste time with compliments. He reached past my shoulder, jammed his thumb into the master green start button on the motor console, and let out a loud whistle down the main warehouse aisle.

"Line four is live!" Ken shouted into his two-way radio. "Get the yard tractors moving! Load Seattle on bay seven and Boise on bay nine!"

The heavy three-phase electric motors spooled up with an industrial groan. The rubber sorting belts accelerated to full operational speed, and the pneumatic diverter arms began their rhythmic clapping as parcel after parcel was weighed, scanned, and routed into the outgoing freight cages. The clock on the warehouse wall read 4:47 AM. When the final cross-dock trailer pulled away from loading bay nine, the time was 5:04 AM. The morning route was saved, and the warehouse avoided thousands of dollars in cancelled delivery fees.

Ken walked back to the cabinet, wiping grease off his forehead with the back of his glove. He looked at the Kapton-taped ribbon cable, then down at the sheared plastic memory latch resting on the bottom of the enclosure.

"You cost us twenty minutes with that power switch, Brooks," Ken said, his voice blunt and tired over the conveyor clatter. "And you snapped a memory clip I'll have to explain to facilities on Monday. But when the wheels came off, you didn't run away, and you listened to the meter. Grab a hand scanner and help clear the chute at bay four—we have sixteen minutes to pack the tail."

I spent the next forty-five minutes sweating in my steel-toed boots, hand-stacking fifty-pound cartons until my back burned. 

At 6:15 AM, when the shift finally ended, I sat down on an upturned wooden pallet behind the sorting enclosure. I rested my forearms against my knees and caught my breath. My hands were covered in black conveyor grease. My knuckles were bleeding where I had scraped them against the sharp chassis partition.

I pulled my smartphone from my jacket pocket and looked at the browser screen. My flashcard application was still running in the background, displaying a multiple-choice question about the maximum theoretical throughput of a PCI Express bus. The digital flashcards had felt authoritative and complete when I was sitting in my bedroom, but they had taught me nothing about the reality of industrial machinery. Those flashcards had not warned me that copper wires chafe against stamped steel. They had said nothing about serial pins bending when hurried workers yank on cables, or unmatched clock rates turning real operational data into noise.

I had earned my certifications on paper, but out on the cold concrete floor of the warehouse, I had finally begun to learn the tradecraft of repair. Two months later, when Ken signed off on an internal apprentice training voucher, I updated my resume with real physical layer diagnostics and applied for the Tier 1 opening at the Portland Regional Operations Center.
"""
    w_file.write_text(pre + epilogue_text, encoding="utf-8")
    print("Updated workbench 01.")

def mirror_files():
    for f in ["narrative/01-the-paper-cert.md", "workbench/01-the-paper-cert.md"]:
        shutil.copy2(PORTLAND / f, DOCS / f)
    print("Mirrored Ep 01 to docs/portland-desk/.")

if __name__ == "__main__":
    update_ep01_workbench()
    mirror_files()
