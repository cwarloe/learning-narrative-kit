# The Receiving App

*Tamarack Feed & Supply Co. • Excel Module 12: Developing an Excel Application • Hover over highlighted terms for course definitions.*

A year after Eli Mendez had inherited Bud Carlsen's damage log, the DC was still logging torn bags the way Eli had set it up in September: a shared workbook on the dock tablet, with AutoComplete doing half the typing. It worked as long as the person typing knew Excel. The new receiving clerks didn't, and in July one of them sorted a single column and scrambled four hundred rows.

Eli's last Excel module was about building an [[excel_application|Excel application]]: a workbook made for one job, with a data entry area, reports and charts, a custom interface, and instructions, so the person using it never had to know how it worked underneath. He decided to rebuild the damage log as one.

He started with an entry sheet that looked like a form. It had a box for the date, one for the product, one for the quantity, one for the carrier, and a Submit button.

The boxes were [[form_controls|form controls]], fields a user typed into or picked from. The product box was a drop-down list fed by the product table, so nobody could type "Prarie Wire" again. The carrier was a set of option buttons, one for each of the four trucking companies that delivered to the DC.

He added a [[validation_rule|validation rule]] to each entry cell, so that Excel would check the data against rules before accepting it. The rule's [[validation_criteria|validation criteria]] set what was acceptable. Quantity had to be a whole number between 1 and 500. Date had to fall within the last fourteen days, because the trucking companies wouldn't accept claims older than that. If someone typed 5000 bags, a message popped up: "Check the quantity. Claims over 500 bags need a supervisor."

Every cell in a worksheet had a [[locked_property|locked property]] that determined whether it could be changed once the sheet was protected. By default every cell was locked, so Eli unlocked only the entry cells, then protected the sheet. The clerks could type in the boxes and nowhere else. The formulas, the product table, and the hidden log sheet were out of reach.

The Submit button needed to do several things in order: copy the entry into the next empty row of the log, add a timestamp and the clerk's name, clear the form, and save. Eli recorded a macro for the first version and then edited the code. The code lived in a [[module|module]], an object in the workbook that stored Visual Basic for Applications code. He opened it in the VBA editor and fixed the parts the recorder had gotten wrong, like the row it always pasted into.

While he was in the editor, he also recorded a small macro he used all the time, one that applied Tamarack's formatting to any table. He stored that one in his [[personal_macro_workbook|Personal Macro workbook]], Personal.xlsb, a hidden workbook that opened every time he started Excel so his own macros were always available.

## Teo Says No

He tested the application on his own computer, and it worked. The next night he copied it to the shared drive and opened it on the dock tablet. A yellow bar said macros had been disabled. The Submit button did nothing.

The blocking came from the [[trust_center|Trust Center]], the central place for Office security settings. After the spring, when a spreadsheet attachment carrying a macro virus had nearly made it into Hank Pruitt's inbox, Teo Vasquez had set every Tamarack computer to disable macros in files that weren't trusted. Teo was not going to change that for a damage log.

"Sign it," Teo said.

A [[digital_signature|digital signature]] was an invisible electronic attachment that verified who had created the file, by checking it against a digital certificate. If Eli signed the workbook's code with a certificate from Tamarack's internal certificate service, and Teo set the Trust Center to trust that publisher, the macros would run, and if anyone changed the code afterward, the signature would break and the macros would stop.

Getting a certificate took a week. Teo had to set up the internal certificate service first, which he had been meaning to do for a year, and he made sure Eli knew that this was the reason it was finally happening.

Once the workbook was signed, the Submit button worked on the tablet. Then Rosa, the receiving clerk, clicked the "Format Report" button Eli had added to the summary sheet. It threw an error.

That button ran Eli's formatting macro, which lived in his Personal Macro workbook. Personal.xlsb was on Eli's computer, not Rosa's. Eli moved the macro into the application's own module, re-signed the file, and waited another day for Teo to push the new trust settings.

* * *

The receiving app went live in August. In its first month, it logged 212 damage entries. None had a misspelled vendor, and no one scrambled the log.

Rosa still kept a paper clipboard on the dock. When Eli asked why, she said the tablet died in the cold room and the clipboard didn't. He started looking into a tablet case with a heater, and then stopped, because Ruth Halvorsen called him into her office that afternoon and offered him the day-shift supervisor job.

He took it. It meant leaving the night crew he had run for five years, and it meant the receiving app would need someone on nights who could fix it when it broke. There wasn't anyone. Eli wrote two pages of instructions, put them on the app's first sheet, and protected that sheet too.
