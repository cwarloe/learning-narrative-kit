# The Damage Log

*Tamarack Supply • Excel Module 1: Getting Started with Excel • Hover over highlighted terms for course definitions.*

## Two Deadlines on the Same Sunday

Eli Mendez had been the night shift lead at Tamarack's distribution center for four years, and in September he signed up for the evening business course at the community college because Ruth Halvorsen had told him, more or less directly, that the day-shift supervisor job would go to someone who could do the numbers.

The course ran on [[sam_skills_assessment_manager|SAM]], the college's online system for learning and testing Microsoft Office skills. On his first login Eli found the [[sam_path|SAM Path]] for the semester: a long list of training modules and exams in order, twelve of them before December. The [[activity_calendar|Activity Calendar]] showed the first three due dates as colored blocks. The [[activity_list|Activity List]] showed the same assignments as rows, with a status column that said "Not Started" for all of them.

The first one that mattered was a [[sam_projects|SAM Project]] due Sunday night: build a small worksheet in the real application, upload it, and get an automatic grade.

On Wednesday, the DC's other deadline arrived. A truckload of mineral feed had come in with sixty-one bags torn, and the trucking company's claims department wanted the damage documented by Sunday or they would deny the claim. The documentation was a spreadsheet the retired night lead, Bud Carlsen, had kept for nine years. Nobody had opened it since he left.

Eli figured he would learn the software on one and use it on the other.

## What the Program Was

The SAM Path started with a [[sam_training|SAM Training]] module, which walked him through the program step by step in his browser and made him click the right thing before it let him go on.

[[microsoft_excel|Microsoft Excel]] was the spreadsheet program in the Office suite. The course materials mostly just called it [[excel|Excel]], and so did everyone at Tamarack. A [[spreadsheet|spreadsheet]] was the grid itself: rows of numbers and text in cells. Excel called each grid a worksheet.

Every cell had an address made of its column letter and row number. A [[cell_reference|cell reference]] like B4 meant column B, row 4. A [[range_reference|range reference]] like A2:F62 meant the whole rectangle from A2 in the upper left to F62 in the lower right. Eli had known that much from looking over Marcy Lund's shoulder. The training made him type both twenty times.

## Bud's Spreadsheet

On Thursday night, between trucks, Eli opened Bud's file on the DC office computer.

It had one worksheet with nine years of damage, about four thousand rows. Every time Eli scrolled down past the first screen, the column headings disappeared and he lost track of which column was the date and which was the bag count. The training module had shown him how to [[freeze|freeze]] panes, so he froze the top row. Now the headings stayed put while four thousand rows went by underneath them.

The columns were a mess in a way Eli could see but not yet name. Some dates sat on the right side of their cells and some on the left. The bag counts were mostly on the right, except in a stretch from 2019 where they were on the left.

The second SAM training module explained it. Excel sorted every entry into a type. [[numeric_data|Numeric data]] was any number you could do math with, and it lined up on the right. [[text_data|Text data]] was any mix of letters, numbers, and symbols, and it lined up on the left. [[date_data|Date data]] was a value in a format Excel recognized as a date, and [[time_data|time data]] a value it recognized as a time. Both were secretly numbers, so they also lined up on the right.

Bud had typed some dates as "3/14/2021," which Excel recognized, and some as "March 14th," which it didn't, so those were text. In 2019 he had typed bag counts with the word "bags" after them, so "12 bags" was text and couldn't be added. The trucking company's form wanted a total.

## Fixing Cells

Eli double-clicked a cell with "12 bags" in it. The cursor appeared inside the cell, and the status bar at the bottom of the window said "Edit." That was [[edit_mode|Edit mode]], where you changed the contents of a cell directly. He deleted the word "bags" and pressed Enter. The 12 jumped to the right side of the cell. It was a number now.

There were 140 of those. Edit mode one at a time would take all night.

The SAM training had a lesson on [[flash_fill|Flash Fill]], which looked for a pattern in what you typed and filled in the rest. Eli inserted an empty column next to the bag counts, typed 12 next to "12 bags," typed 7 next to "7 bags," and pressed Ctrl+E. Excel filled the remaining 138 cells with just the numbers. He checked twenty of them against the originals, because the training also said Flash Fill guessed, and they were right.

He did the same with the "March 14th" dates, and Flash Fill turned them into real dates.

## Deleting Versus Clearing

The worst part of Bud's sheet was a block of thirty rows from 2017 that duplicated the thirty rows above them exactly. Eli selected the duplicate rows and pressed the Delete key. The cells went blank, but the empty rows stayed.

That was [[clearing|clearing]]: removing what was in the cells, data or formatting or both, and leaving the cells themselves where they were. What he wanted was [[deleting|deleting]], which removed the cells entirely and moved everything below them up. He right-clicked the row numbers. A [[shortcut_menu|shortcut menu]] appeared, a short list of commands related to what he'd clicked, with Delete in the middle. Above it floated a [[mini_toolbar|Mini toolbar]] with font and fill buttons he didn't need. He chose Delete. The thirty empty rows disappeared and everything below moved up.

Then he noticed column G was missing. The column letters went A, B, C, D, E, F, H.

Bud had been [[hiding|hiding]] a column: still part of the worksheet, just not shown. Eli selected F and H, right-clicked, and chose Unhide. [[unhiding|Unhiding]] it showed what Bud had kept out of sight: the dollar value of every damaged bag, which was exactly what the claim form asked for.

## Moving Things Around

The trucking company's form wanted the columns in a different order: date, product, bags, value. Eli selected the value column and used [[drag_and_drop|drag and drop]] to move it, grabbing the border of the selection and pulling it to its new place. The first time, Excel warned him that there was already data there and asked whether to replace it. He said no, tried again holding Shift, and the column slid in between the others instead of on top of them.

He needed the last month's rows on a separate sheet for the claim. He selected them and pressed Ctrl+C. The selection went to the [[clipboard|Clipboard]], Windows's temporary holding area for copied things. On a new sheet he clicked A1 and pressed Ctrl+V to [[paste|paste]] them in.

Eli was learning that every [[keyboard_shortcut|keyboard shortcut]] he used saved him a trip to the ribbon. When he couldn't remember one, he pressed the Alt key, and small letters appeared over every tab and button: [[keytips|KeyTips]]. Alt, then H, then the letters for whatever he needed. When he hovered over a button he didn't know, a [[screentip|ScreenTip]] appeared with its name, what it did, and sometimes its shortcut.

## The Tablet on the Dock

On Friday, the dock supervisor asked whether the damage log could be filled in on the DC's tablet, so drivers could enter torn bags at the truck instead of on paper.

Eli opened the file on the tablet. The ribbon's buttons were too small to hit with a gloved finger. A button on the Quick Access Toolbar switched the interface into [[touch_mode|Touch Mode]], which made the ribbon taller, the buttons bigger, and the spaces between them wider. Back at the office computer, he switched to [[mouse_mode|Mouse Mode]], which put everything back to normal size.

On the tablet he also discovered [[autocomplete|AutoComplete]]. When a driver typed "Min" in the product column, Excel suggested "Mineral 12:12 50lb" from the entries already in that column, and the driver just pressed Enter. It cut the typos in half.

He set up a new row for each day using the [[fill_handle|fill handle]], the small square at the lower-right corner of a selected cell. He typed one date, grabbed the square, and dragged it down; Excel filled in the next thirty dates in order.

## Making It Readable

The claim form had to look professional. Eli selected the claim range, and a small button appeared at its lower-right corner. That was the [[quick_analysis_tool|Quick Analysis tool]], with common formatting and totals one click away. He chose Totals, and a sum appeared under the bag count and value columns.

He hovered over a few table styles on the ribbon. With each one, the sheet changed to show what it would look like. That was [[live_preview|Live Preview]], which showed the result before you clicked. He picked the plainest.

The column headings were cut off. He dragged the border between two column letters wider, and a small label showed the width in characters and in [[pixel|pixels]], the individual points of color on the screen. He made the product column 160 pixels wide and the headings fit.

Last, he opened the File tab. The worksheet disappeared and a full-screen menu took its place: [[backstage_view|Backstage view]], where you managed the file itself. He used Save As to give the claim its own name and saved it as a PDF. The trucking company had also sent a link to a claims [[add_in|add-in]] that would add its own commands to Excel's ribbon. Eli didn't install it. Teo had told everyone at the DC, after the spring, not to install anything that came in an email.

## What Sunday Cost

The claim went to the trucking company on Saturday at 11 p.m. It covered sixty-one bags, $1,107.50. The company paid for forty-four of them two weeks later and denied seventeen on the grounds that the photos didn't show the bag labels. Bud would have known to photograph the labels. Nobody had told Eli.

He started his SAM Project at 9 p.m. Sunday and submitted it at 11:52, eight minutes before the deadline. He got a 74. Two points came off for a column width, three for a missing total, and the rest for steps he'd done the long way instead of the way the instructions asked. The first [[sam_exams|SAM Exam]] was due in two weeks. On Monday Eli put it on the Activity Calendar at work too, in a color Ruth would see.
