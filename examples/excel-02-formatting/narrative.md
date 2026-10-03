# The Board Packet

*Tamarack Supply • Excel Module 2: Formatting Workbook Text and Data • Hover over highlighted terms for course definitions.*

## Seven Copies by Thursday

Ruth Halvorsen had to present the distribution center's quarterly numbers to Tamarack's board on Thursday, and on Monday she asked Eli Mendez to get the DC sheet ready to print. The numbers were done. Hank Pruitt had checked them. What Ruth needed was for them to look like something a board would read.

"Seven copies," she said. "Three of them are over seventy and they'll read it on paper with a pen. Make it so they don't have to ask me what anything means."

Eli's second SAM module that week was on [[formatting|formatting]]: changing how content looked on the screen and on the page through fonts, sizes, colors, and alignment, without changing the values underneath. He had been planning to do the training on Wednesday. He did it Monday night instead.

## The Dollar Signs

The sheet came from Hank's accounting export, and every number was in [[general_format|General format]], which displayed values more or less the way they had been typed. A damage cost of 1107.5 showed as 1107.5. A credit from the trucking company showed as -650. Nothing lined up.

Eli's first instinct was the dollar-sign button. That applied [[accounting_format|Accounting format]]: the dollar sign pinned to the left edge of each cell, a comma separator for thousands, two decimal places, numbers lined up by their decimal points, negative numbers in parentheses, and zeros shown as dashes. The column looked like a ledger.

Hank came by and approved. Ruth didn't. "Kip Andersen is going to ask me why half the numbers have parentheses," she said. "He did last year."

The other option was [[currency_format|Currency format]], which put the dollar sign right next to the first digit and showed negatives with a minus sign. Eli made a copy of the sheet in each format and put them side by side. Hank pointed out that in Currency, the dollar signs wandered back and forth down the column depending on how long each number was, and the column was harder to add by eye. Ruth said Kip didn't add columns by eye. She chose Accounting anyway, because Hank was the one who'd have to answer questions about the numbers, and asked Eli to add a note at the bottom explaining the parentheses.

## Making Things Fit

The product names were cut off. Eli double-clicked the border between the column letters, and [[autofit|AutoFit]] widened the column to fit its longest entry. That entry turned out to be a product name someone had typed with a note in it: "Mineral 12:12 50lb — damaged on dock see email from Bud." The column became as wide as the screen.

He undid it, shortened the note, and AutoFit again.

Row heights were in [[point|points]], the same unit as font size, one seventy-second of an inch. The body text was 11-point. Eli remembered "over seventy" and made it 12, and the header row 14.

## Choosing a Look

The workbook used a company [[theme|theme]] Marcy Lund had set up last year: a coordinated set of colors, fonts, and effects that gave every Tamarack spreadsheet the same look. The [[theme_colors|theme colors]] included Tamarack's dark green for headings and a tan for fill. Marcy had defined the green using the [[rgb_color_model|RGB color model]], entering exact amounts of red, green, and blue so it matched the logo on the trucks.

Eli applied a [[cell_style|cell style]] to the header row, one click that set the font, size, fill, and border together. He hovered over a few others first and watched Live Preview change the row.

Then he made a mistake that took him an hour to understand. He copied the DC sheet's cells and pasted them into a new, blank workbook so he could send Ruth just one sheet. The green headings turned blue. The fonts changed too.

The new workbook used Excel's default theme, not Marcy's. The headings were set to "theme color: Accent 1," which in Marcy's theme meant Tamarack green and in the default theme meant blue. The headings were also in a [[theme_font|theme font]], which changed whenever the theme changed. Eli could either apply Marcy's theme to the new workbook or stop depending on the theme.

For the totals row, which needed to stay red on any copy, he picked red from the [[standard_colors|standard colors]] instead, the ten colors that were always available and stayed the same no matter the theme. For the note at the bottom he used a [[standard_font|standard font]] that wouldn't change either. Then he applied Marcy's theme to the workbook and the green came back.

## The Font Question

Ruth looked at a test print and asked whether it could be easier to read on paper.

The theme font was a [[sans_serif_fonts|sans serif font]], without the small strokes at the ends of each letter. It was clean on a screen. Marcy had chosen it for that. For long printed text, some people found [[serif_fonts|serif fonts]] easier, with the short decorative lines at the tops and bottoms of characters that helped the eye along a line.

There wasn't much long text on a spreadsheet. Eli kept the sans serif for the numbers and used a serif font only for the explanation note. Ruth said she couldn't tell the difference and it was fine.

## Dates

The report had two kinds of dates. In the table, each damage event had a date in [[short_date_format|Short Date format]], 09/14/2026, which fit in a narrow column. At the top of the page, Ruth wanted the report date written out for the board, so Eli used [[long_date_format|Long Date format]]: Thursday, October 1, 2026. Same kind of value underneath, two different ways of showing it.

## The Page

The sheet had nine columns. In [[portrait_orientation|portrait orientation]], taller than wide, the last three columns printed on a second page by themselves. The board would have to hold two pages side by side to read one row.

Eli changed the [[page_orientation|page orientation]] to [[landscape_orientation|landscape orientation]], wider than tall. Eight columns fit. He narrowed the [[margin|margins]], the space between the content and the edges of the paper, and the ninth column fit too.

He added a [[header|header]] that printed at the top of every page with the report name and the long date, and a [[footer|footer]] at the bottom with "Page 1 of 3" and the file name. If a page got separated from the others, someone could put it back.

Ruth asked for one more thing: a picture of how damaged goods moved from the truck to a claim, because the board kept asking. Eli used a [[smartart_graphics|SmartArt graphic]], a ready-made diagram of shapes and text, and picked a simple process layout with five steps: received, inspected, logged, photographed, claimed. He made "photographed" bold, since that was the step that had cost seventeen bags in September.

## What Thursday Looked Like

Ruth sent the file to the office's color printer Wednesday night. It jammed on copy three, and the receptionist ran the rest on the copier, which printed only in black and white.

The red totals row printed as dark gray, the same as everything else. The tan fill disappeared. On four of the seven copies, the one row Eli had colored red to show it was the loss line looked like every other row.

Kip Andersen asked why some of the numbers had parentheses. Ruth pointed to the note at the bottom. Kip said he'd read the note and still wanted to know why accountants couldn't just use a minus sign like everybody else. Hank started to answer, and Ruth moved on to the next page.

After the meeting, Ruth told Eli the report was the clearest the DC had ever sent and asked if next time he could make the loss row bold as well as red, so it would survive the copier. Eli's SAM score that week was 88.
