# The Returns Nobody Credited

*Tamarack Feed & Supply Co. • Excel Module 6: Managing Data with Data Tools • Hover over highlighted terms for course definitions.*

## Hank's Year-End Question

Every December, Hank Pruitt reconciled what Tamarack's vendors owed it. When a store sent defective or recalled goods back through the DC, the vendor was supposed to issue a credit. Hank suspected that some never had.

The record of every return was a list the DC kept: about 2,300 rows over three years. Hank asked Eli Mendez to turn it into something he could question. "I want to ask it things," he said. "Which vendors, how much, how old. Without calling you each time."

Eli's sixth SAM module was on Excel's data tools. He started there.

## Deciding What Each Column Means

Before touching the data, the module said to write a [[data_definition_table|data definition table]]: a list of every field, a description of what it held, and the type of data in it. Eli thought it was busywork until he started writing it.

Return ID was a number. Date was a date. Store was text. Vendor was text. Quantity was a whole number. Unit cost was currency. Status was text: Open, Credited, or Denied. Credit date was a date, blank until credited.

Writing "Vendor: text, the vendor's name as it appears on the invoice" made him look at the column, and the column had "Prairie Wire," "Prairie Wire Co.," "Prairie Wire Inc," and "PRAIRIE WIRE" in it. He noted that and moved on, because fixing it would take a day he didn't have.

## Making It a Table

He converted the list to an Excel table. The first row became the [[header_row|header row]], holding the field names, and it stayed visible with filter buttons on each column.

Hank wanted a value for each return. Eli added a column called Credit Value and typed one formula: =[@Quantity]*[@[Unit Cost]]. These were [[structural_references|structural references]], references to parts of the table by name instead of cell address. [@Quantity] meant "the Quantity field in this row." Excel filled the formula down the whole column automatically. That made it a [[calculated_field|calculated field]], with values calculated from other fields rather than entered.

The DC's receiving clerk, Rosa, entered new returns. Scrolling to the bottom of 2,300 rows to type into a narrow row was how typos happened. Eli added the [[excel_data_form|Excel data form]] to the Quick Access Toolbar. It opened a dialog box with every field name and an input box beside it, one record at a time. Rosa said it was like the old system's screen, and she meant it kindly.

## Putting Things in Order

Hank's first question was about the biggest returns. Eli sorted by Credit Value in [[descending_order|descending order]], largest to smallest. The top of the list was a pallet of recalled heat lamps worth $4,100.

Hank's second question needed two sorts at once: returns grouped by vendor, and within each vendor, oldest first. Vendor was the [[primary_sort_field|primary sort field]], determining the main order, sorted alphabetically in [[ascending_order|ascending order]], A to Z. Date was the [[secondary_sort_field|secondary sort field]], ordering the records within each vendor, also ascending, oldest to newest.

Ruth Halvorsen wanted the stores sorted the way she thought of them, which was geographic, north to south: Republic, Colville, Kettle Falls, Chewelah, and so on down to Spokane Valley. Alphabetical put Chewelah first. Eli created a [[custom_list|custom list]], a sort order he typed in once, and sorted by that.

## Asking It Things

Filtering was where Hank's questions really started.

The simplest were [[criteria_filters|criteria filters]], conditions on one column using the filter buttons: Status equals Open. That showed 312 returns with no credit. Hank wanted only Prairie Wire's. The four spellings made that awkward until Eli used a [[wildcard|wildcard]], a symbol that stood for unknown characters. The asterisk stood for any group of characters, so "prairie*" caught all four versions. The question mark stood for a single character, which he didn't need yet.

Hank's next question was too complicated for the filter buttons: open returns from Prairie Wire over $500, or any open return from any vendor more than 180 days old. That was two conditions joined by AND, and two groups joined by OR.

For that, Eli used [[advanced_filtering|advanced filtering]], which handled criteria combining fields with AND and OR. Advanced filtering needed a [[criteria_range|criteria range]]: a separate area above the table where he copied the field names and typed the conditions underneath. Conditions on the same row meant AND. Conditions on different rows meant OR.

Row one: Vendor "prairie*", Status "Open", Credit Value ">500".

Row two: Status "Open", Date "<" a date 180 days back.

The filter returned 97 rows.

## Totals From the Criteria

Hank wanted the total credit value of those 97, and he wanted it to update when the criteria changed.

A [[database_function|Database function]] did exactly that. It performed summary math on a table using criteria in a criteria range. The family was also called the [[dfunction|Dfunction]] group, since each one started with D: DSUM, DCOUNT, DAVERAGE. =DSUM(Returns[#All], "Credit Value", A1:E3) added the Credit Value field for every record matching the criteria range. It said $11,860.

Hank asked for a breakdown by vendor. The [[subtotals|subtotals]] command inserted summary rows into a range, a subtotal under each group, after the data was sorted by that group. Eli went to the Data tab and found the Subtotal button grayed out. The command didn't work on an Excel table. He had to convert the table back to a normal range first.

That meant losing the structural references. Excel converted his Credit Value formula to ordinary cell references, the data form still worked, but new rows would no longer fill the formula automatically. Eli made a copy of the workbook, converted the copy to a range for the subtotals, and kept the table as the working file. Now there were two files, and he wrote "DO NOT ENTER DATA HERE" across the top of the copy.

## What the Credits Were Worth

The subtotals showed $11,860 in open returns that had never been credited. $7,200 of it was Prairie Wire.

Hank called Prairie Wire's new centralized accounts department in Saskatoon. Their returns policy, which had changed when the company was bought, required claims within 180 days of shipment. Most of the open returns were older. Prairie Wire credited $2,900 and denied the rest. Two smaller vendors credited everything once Hank sent the list.

Hank had Rosa start a weekly check of open returns using the advanced filter, and he asked Eli to fix the vendor spellings. Eli fixed them in January, on a Saturday. In February Rosa entered a return from "Prarie Wire."
