# Eleven Packets, Then Twelve

*Tamarack Feed & Supply Co. • Excel Module 11: Exploring PivotTable Design • Hover over highlighted terms for course definitions.*

Ruth Halvorsen sent each store manager a monthly packet: their own sales, their own categories, and how they compared. For three years, Marcy Lund had built it by filtering one PivotTable eleven times and copying each result into a new sheet. Now there were twelve stores, and Marcy asked Eli Mendez whether his course had anything better. His eleventh SAM module was on PivotTable design.

It did. Eli built one PivotTable with Store in the filter area, then used [[show_report_filters_pages|Show Report Filters Pages]]. Excel created a separate worksheet for each store, each with a copy of the PivotTable filtered to that store and named after it. Twelve sheets, in about four seconds. Marcy watched it twice.

Ruth wanted each store compared to Spokane Valley, the flagship, so a manager could see at a glance where they were ahead or behind.

Eli set the values to show as "% Difference From." Excel asked for two things. The [[base_field|base field]] was the field used for the comparison: Store. The [[base_item|base item]] was the specific item within that field everything else would be compared to: Spokane Valley. Every store's category sales now showed as a percentage above or below Spokane Valley's.

Davenport showed minus 71 percent in feed. Eli pointed out that Davenport had been open three months and Spokane Valley for thirty years. Ruth said the managers would understand. Eli was less sure.

The question still left over from the spring was whether Davenport had grown the business or just taken it from Spokane Valley. Eli selected the two stores in the PivotTable's row labels and grouped them. That created a [[manual_group|manual group]]: a new item combining the two, which appeared as a new field in the PivotTable. He named it "Spokane Valley trade area." Compared to last year's Spokane Valley alone, the combined area was up 9 percent.

The sales data had a Transaction Type field with two items: Sale and Return. Hank Pruitt wanted net sales, sales minus returns, as its own column. Eli added a [[calculated_item|calculated item]] to the Transaction Type field, a user-defined formula between items in the same field: Net = Sale - Return. It appeared next to the other two.

* * *

The next morning, Marcy's separate category PivotTable, in a different sheet of the same workbook, had Davenport and Spokane Valley grouped together too. She hadn't touched it.

Both PivotTables had been built from the same table, so Excel had them share one [[pivottable_cache|PivotTable cache]], the object that stored a copy of the data a PivotTable used. Grouping items changed the cache, and every PivotTable on that cache saw the change.

To keep them independent, Eli rebuilt Marcy's PivotTable with the old [[pivottable_wizard|PivotTable Wizard]], the creation tool from before Excel 2016. It still opened with Alt, D, P, and unlike the modern button, it could give the PivotTable its own separate cache. Marcy's PivotTable stopped changing when Eli's did.

Hank's monthly summary sheet referred to cells in the PivotTable: total company sales was =B47. Then Eli added the twelfth store, the PivotTable grew a row, and B47 became the Spokane Valley trade area subtotal. Hank's summary was wrong for a day before he noticed.

The [[getpivotdata_function|GETPIVOTDATA function]] extracted a value from a PivotTable by naming the field and item instead of the cell, so it found "Grand Total of Sales" wherever it moved. Eli replaced every reference in Hank's summary with GETPIVOTDATA. The formulas were longer. Hank said he preferred longer and right.

Marcy wanted the same packets built from the merchandising data mart Dana Okafor had set up last year instead of from exported tables. The data mart was an [[online_analytic_processing|Online Analytic Processing]] database, built to make structured data fast to query and report on.

Eli connected a PivotTable to it, and some of what he'd built stopped working. The calculated item option was grayed out; calculated items weren't available for OLAP-based PivotTables. Grouping didn't work the same way either.

There were other tools instead. He defined [[named_sets|named sets]], which set which items appeared in each part of the PivotTable from the data model. One set, "Original five," held the first five stores, and another, "New since 2010," held the rest. For Hank's summary, he used the [[data_cube|Data Cube]] functions, also called cube functions, which pulled individual values straight from the data mart into ordinary cells: =CUBEVALUE pulled total net sales for any store and month he named, with no PivotTable at all.

Net sales had to come from a measure Dana wrote in the data mart, because Eli couldn't add a calculated item there. Dana took a week to get to it.

* * *

The packets went out on the fifth of the month, twelve sheets generated in four seconds. Ruth had decided to keep the comparison to Spokane Valley.

The Davenport manager, three months into her job, called Ruth the same afternoon about the minus 71 percent. Ruth explained it. The manager said she understood the math and asked whether the other eleven managers had seen her number. They had. Ruth said she would add a column next month comparing each store to its own first year. Eli added it. In Davenport's case, the column was blank.
