# Comic Book Typography & Lettering Architecture Guide

**Project:** Portland Desk / Learning Narrative Kit (LNK)  
**Document Purpose:** Master Reference & Specification for Comic Book Lettering, Layered Graphic Typography, and Flashcard Production  
**Status:** Canonical Design Consensus  

---

## 1. Executive Summary & Purpose

This document establishes the official typography hierarchy, font specifications, and lettering rules for the *Portland Desk* curriculum and its visual assets. 

When comic panels, technical schematics, and study flashcards are produced, **art and typography are strictly decoupled into independent layers**:
* **Layer 1 (The Visual Plate):** Pure line art, inks, flat colors, and cartoon cross-hatch shadows. **Zero baked-in text** (preventing AI generation spelling errors, pixelation, and un-editable dialogue).
* **Layer 2 (The Lettering Layer):** Live vector text (SVG or styled HTML) using specialized comic and drafting typefaces mapped to exact narrative and cognitive functions.

---

## 2. The 4-Tier Lettering Hierarchy & Font Roster

In comic book production (and specifically modern DC Comics like *Super Sons*, *Batman*, and *Green Lantern*), lettering is never monolithic. Different narrative voices, sound effects, and captions require distinct typographical tools.

```
+-----------------------------------------------------------------------------------+
| TIER 1: DISPLAY & STRIKE FONTS (Sound FX, Shouts, Highlighter Headers)           |
| Fonts: Bangers, Gagalin, Badaboom BB                                             |
| Role: Maximum volume, punchy impact, 1-3 words only                              |
+-----------------------------------------------------------------------------------+
                                        |
+-----------------------------------------------------------------------------------+
| TIER 2: NARRATIVE CAPTION RECTANGLES (DC Comics Story Voice)                      |
| Fonts: Komika Text (Bold Italic), VTC Letterer Pro, Anime Ace                     |
| Role: All-caps, slight italic slant (8°-10°), uniform stroke, high legibility     |
+-----------------------------------------------------------------------------------+
                                        |
+-----------------------------------------------------------------------------------+
| TIER 3: GRITTY MARKER & SHOP SCRAWLS (Apprentice Notes, Traps, Squeaky Pen)       |
| Fonts: Rock Salt, Permanent Marker, Gochi Hand                                   |
| Role: Human, rushed, imperfect, authentic break-room chisel-tip Sharpie          |
+-----------------------------------------------------------------------------------+
                                        |
+-----------------------------------------------------------------------------------+
| TIER 4: TECHNICAL DRAFTING & HARDWARE SCHEMATICS (Pinouts, Specs, Labels)         |
| Fonts: Architects Daughter, Kalam, JetBrains Mono                                 |
| Role: Clean architectural hand, engineer notes, precise component pin tags       |
+-----------------------------------------------------------------------------------+
```

---

## 3. Font Analysis & Evaluation

### Tier 1: Display, Strikes & High-Impact Callouts

#### **Bangers** (Google Fonts / Vernon Adams)
* **Visual Character:** Tall, heavy, condensed, mid-century superhero comic book display font.
* **Optimal Use:**
  * **Top Highlighter Bands:** The thick marker strike across the top of cards (`EXAM TRIVIA // MEMORIZE`, `HARDWARE ANATOMY`).
  * **Single-Word Diagram Shoutouts:** Large 1-word callouts directly on technical drawings (`HEAT`, `PRESSURE`, `MELTED IN`, `DVI-I`, `VOLATILE`).
* **Do NOT Use For:** Sentences or multi-line paragraphs. Reading more than 3 consecutive words in Bangers causes visual fatigue.

#### **Gagalin** (Iordanis Passas)
* **Visual Character:** Rough, heavy, condensed vintage comic font with distressed, organic ink-bleed edges.
* **Optimal Use:** Industrial shop-floor stamps, high-voltage warning labels, equipment chassis tags, and punchy card numbers (`#14`, `FAULT!`).
* **Do NOT Use For:** Small body text (the distressed texture muddies at small sizes).

---

### Tier 2: Narrative Rectangles & Dialogue (The DC Comics Voice)

#### **Komika Text (Bold Italic)** (Apostrophic Labs / WolfBainX)
* **Visual Character:** The industry-standard digital recreation of pro comic lettering (Richard Starkings / Comicraft cadence).
* **Key Anatomy:**
  * Strictly all-uppercase.
  * Subtle forward italic tilt (8°–10°).
  * Compact horizontal geometry (allows full 15–20 word technical rules to fit in a tight rectangle).
  * Square-ended terminal curves with uniform pen weight.
* **Optimal Use:** The core study prompt, the back-of-card answer, and primary invariant rules. This font gives the card its unmistakable *Super Sons* / DC Comics graphic novel feel.

#### **VTC Letterer Pro** (Vigilante Typeface Corp / WolfBainX)
* **Visual Character:** Classic American superhero comic dialogue font. Slightly squarer than Komika with clean, wide counters.
* **Optimal Use:** In-panel character dialogue and secondary story captions.

#### **Anime Ace 3.0** (Blambot / Nate Piekos)
* **Visual Character:** Iconic indie comic and manga lettering font. Sharp terminal angles, wide spacing, modern digital feel.
* **Optimal Use:** High-tech HUD readouts, crisp diagnostic status displays, and modern comic balloons.

---

### Tier 3: Gritty Markers & Break-Room Scrawls

#### **Rock Salt** (Google Fonts / Brian J. Bonislawsky)
* **Visual Character:** Ultra-authentic, gritty, hurried felt-tip marker script with jagged baseline variations and dry-marker streaks.
* **Optimal Use:** Ethan's last-minute scrawls at the bottom of the card (`Exam trap: DVI-A is analog only!`). It looks 100% like a tired 19-year-old scribbling notes under fluorescent lights with a dying Sharpie.

#### **Permanent Marker** (Google Fonts / Font Diner)
* **Visual Character:** Heavy, classic chisel-tip industrial permanent marker.
* **Optimal Use:** Marker slashes across tape, cardboard labels, wire tags, and underlined warnings.

---

### Tier 4: Technical Schematics & Pinouts

#### **Architects Daughter** (Google Fonts / Kimberly Geswein)
* **Visual Character:** Clean, square-lettered architectural blueprint handwriting.
* **Optimal Use:** Hardware pinout tables, jumper pin labels, multimeter voltage values, and schematic callouts.

---

## 4. Space Utilization & Real Estate Rules

A 3x5 index card is an **active retrieval cognitive engine**, not a novel:

1. **Eliminate Artificial Whitespace:**
   * Margins must be tight (`1rem` to `1.2rem`).
   * The top color highlight must span **85% to 92% across the card width**, commanding the header zone like a real chisel highlighter stroke.
   * Do not leave large empty gaps. Scale typography up (`font-size: 2.6rem - 3.4rem`) so words command the card.
2. **The 60/40 Split Front Face:**
   * **Left 45%:** Large, high-contrast SVG technical sketch with bold cartoon ink lines (3px - 3.5px) and punchy 1-word `Bangers` callouts.
   * **Right 55%:** Huge, bold retrieval question in `Komika Text (Bold Italic)` with an authentic `Rock Salt` mnemonic hint below.
3. **The High-Impact Back Face:**
   * **Top 45%:** Massive, bold answer in green or dark ink (`Komika Text` or `Komika Axis` at `3.2rem - 3.8rem`).
   * **Middle 35%:** Two large, unambiguous invariant rules (not walls of text—tight bullet statements).
   * **Bottom 20%:** The red exam trap in `Rock Salt` or `Permanent Marker`, spanning the full card base with a dashed warning rule.

---

## 5. Lettering Assignment Specification for Comic Artists & Typographers

When handing off artwork to the lettering artist or production engineer:

1. **Asset Handoff:**
   * Deliver line art plates as transparent PNG or clean SVG with **no text**.
2. **Text Source of Truth:**
   * Use the exact Markdown source strings defined in `docs/portland-desk/narrative/` and `docs/portland-desk/workbench/`.
3. **Font Licensing & Web Embedding:**
   * All fonts used in web publications must have valid web licenses (OFL or freeware/distro-ware).
   * Font assets must be converted to `.woff2` and stored in `docs/assets/fonts/`.
4. **CSS & Vector Layering Standards:**
   * In-browser overlays must use live CSS `@font-face` bindings.
   * Text must remain selectable and readable by assistive screen readers (no flattening text into raster bitmaps).
