# Eleven Workbooks

*Tamarack Feed & Supply Co. • Excel Module 5: Generating Reports from Multiple Worksheets and Workbooks • Hover over highlighted terms for course definitions.*

At the end of every month, each of Tamarack's eleven stores counted its high-value stock — chainsaws, generators, gun safes, welders — and emailed a workbook to head office. Marcy Lund copied the totals from all eleven into a summary by hand. It took her most of a day, and twice a year she copied a number into the wrong row.

In November she asked Eli Mendez whether his Excel course had covered anything that could do this for her. It had, that week.

The first problem was that the eleven workbooks didn't match. Colville listed generators before chainsaws. Deer Park had added a column for serial numbers. Republic's manager typed "chain saw" with a space.

Eli built a [[template|template]]: a workbook file with the layout, formatting, headings, and formulas already in place, saved as a template file with an .xltx extension, so that opening it created a fresh copy instead of overwriting the original. Every store would start each month from the same template, with the same rows in the same order and a cell at the top for the store name. Marcy sent it out with a short note. Curtis at Colville replied asking what had been wrong with his.

The summary workbook had one row per store and one column per product category. Eli could have written a separate formula for each store pointing at each store's file. With eleven stores and nine categories, that was ninety-nine formulas, and every new store would mean nine more.

Instead he used [[indirect_referencing|indirect referencing]]. In a normal formula, the reference was fixed: ='[Colville.xlsx]Count'!C5. With INDIRECT, the reference itself was built by a formula from text in other cells. Column A of the summary held each store's name. The formula combined that name with the file name pattern and the cell address and handed the result to INDIRECT, which went and got the value. One formula, copied down eleven rows and across nine columns, pulled each store's numbers from the right file.

When he tested it, every cell showed #REF!.

The formula was right. The problem was that INDIRECT could only reach into another workbook if that workbook was open. With the eleven store files closed, it had nothing to read. With all eleven open, every number appeared.

He also learned what a [[path|path]] was, the hard way. The store workbooks lived in a shared folder whose path was something like S:\Merchandising\Monthly Counts\2026\November. The path described exactly where the file was, starting from the drive and stepping through each folder in turn, separated by backslashes.

In the middle of testing, Marcy reorganized the shared drive and moved the whole Monthly Counts folder under a new folder called Inventory. Every reference that included the old [[path|path]] broke. The ones Eli had typed into the formula text had to be fixed by hand. Marcy apologized and then pointed out that she reorganized the drive every January.

To test the summary, Eli opened all eleven store files and changed numbers in them to see whether the totals moved correctly. Flipping between twelve windows to check was making him dizzy.

The [[watch_window|Watch Window]] fixed that. It was a small floating window that showed the current values of chosen cells anywhere in the open workbooks. He added the company total for each of the nine categories and the Colville and Republic rows, the two stores most likely to send something odd. Now, when he changed a number in Deer Park's file, he could see the summary's total change in the Watch Window without leaving Deer Park.

He found two mistakes that way. Both were his.

* * *

At the end of the week, Eli brought Marcy two options.

The first kept the eleven separate files. She would open all eleven every month before opening the summary, or the summary would fill up with #REF!. It saved her most of the copying but none of the opening and closing.

The second put all eleven stores into one shared workbook in the cloud, one worksheet per store, each built from the [[template|template]]. [[indirect_referencing|Indirect references]] worked fine between sheets in the same workbook, so the summary would always be current. But every store manager would be able to see every other store's sheet. And when two managers saved at the same time, they would both have to wait.

Marcy picked the second. Curtis at Colville objected to having the other managers see his numbers. Ruth Halvorsen told him that head office had always seen them and so would the other managers now. He complied, and in December he entered his counts two days late.
