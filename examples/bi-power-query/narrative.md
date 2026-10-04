# Fifteen-Minute Readings

*Tamarack Feed & Supply Co. • BI Tools for Data Analysis: Power Query • Hover over highlighted terms for course definitions.*

## The Tanks Start Talking

In June, Tamarack put remote monitors on 900 of its customers' propane tanks. Each monitor read the tank's level every fifteen minutes and sent it to the monitor vendor's cloud. The idea, Hank Pruitt's idea, was to stop sending trucks to tanks that were half full and stop missing tanks that were nearly empty.

The vendor's website showed one tank at a time. Hank wanted all 900 in a workbook every Monday, next to each customer's delivery history and the weather, so the dispatcher could plan the week's routes. He asked Dana Okafor, and Dana, who had more projects than hours, asked Eli Mendez to help, since Eli's course had just reached its Power Query module.

## What Kind of Data This Was

Dana started with the arithmetic, because she wanted Hank to understand why this wasn't just another spreadsheet.

Nine hundred tanks times ninety-six readings a day came to 86,400 rows a day, and about 31 million a year. That was [[big_data|big data]], at least by Tamarack's standards: data large and complex enough that the usual tools struggled with it. The course described big data by its characteristics. The [[volume|Volume]] was the sheer amount, so large that storing it was a problem in itself. Excel's worksheet limit was about a million rows, so one year of readings wouldn't fit on a sheet thirty times over. The [[velocity|Velocity]] was how fast it changed; new rows arrived every fifteen minutes whether anyone looked or not. The [[variety|Variety]] was how many different kinds of sources had to come together: the monitor readings, the delivery records from the billing system, customer details from the loyalty system, and daily temperatures from a weather service.

"So we don't put it in a spreadsheet," Hank said.

"We put a summary in a spreadsheet," Dana said. "Something has to get it from there to here."

## Getting It In

The something was [[power_query|Power Query]], the tool built into Excel for connecting to almost any data source and shaping what came back before it reached the workbook.

The monitor vendor exported readings as [[comma_separated_values_csv_files|Comma Separated Values (CSV) files]]: plain text, one record per line, fields separated by commas. Eli connected Power Query to the vendor's export folder, and it read every file in it.

The first import was wrong. Customer names came through split across two columns, with "Hollister" in one and "Dale Jr." in the next. Some customer names in the vendor's system had been typed as "Hollister, Dale Jr." with a comma, and the comma was also the [[delimiter|delimiter]], the separator between fields. The vendor hadn't put quotation marks around those names. Eli couldn't fix the vendor's export, so he changed the query to ignore the vendor's name column entirely and pull customer names from the loyalty system by account number instead.

The weather data came from a different vendor in a file that used semicolons as the delimiter. Power Query guessed that one correctly.

## The Steps It Remembered

Each thing Eli did in the Power Query editor — remove the name column, change the reading column from text to a number, filter out monitors that reported zero because their batteries were dead, group by tank and day — appeared as a step in a list on the right side of the screen. Each Monday, Power Query would replay the steps on the new files.

Underneath, each step was written in [[m|M]], the query language Power Query used. The course called M a [[mashup_query_language|mashup query language]], a language for queries that extracted data from different sources and transformed it. Eli opened the Advanced Editor and saw the steps written out as code. He didn't need to write it. He needed to be able to read it, because the next week something broke.

## The Monday It Broke

On the second Monday in July, Hank opened the workbook and the tank summary was blank.

The vendor had added a column to its export, "Signal Strength," between "Tank ID" and "Reading." One of Eli's steps referred to columns by position: change the third column to a number. The third column was now signal strength, and the readings were left as text, which made every summary calculation fail. Eli found the step in the M code, changed it to refer to the column by name, and refreshed. It took him forty minutes. The dispatcher planned Monday's routes from the previous week's printout.

The refresh itself took eleven minutes on Hank's laptop, which Hank mentioned every Monday after that.

## What the Workbook Was For

Once it ran, Dana explained what they'd built, using the course's terms, because Ruth Halvorsen wanted to know whether it was worth paying the monitor vendor's subscription after the trial.

[[business_intelligence|Business Intelligence]], in the course's sense, was the category of software tools that pulled useful information out of big data. Power Query and the workbook were small examples. [[bi|BI]] more broadly gave the company a view of its operations, historical, current, and predictive, that it could use to compete. Tamarack's competitors' propane customers still called when they ran out.

Hank's Monday workbook was also a [[data_driven_decision_support_system|data-driven decision support system]]: a set of tools that let an analyst interpret big data to make a decision, in this case which tanks to fill this week. The dispatcher was the decision-maker. The workbook didn't route the trucks.

What Ruth actually asked for was [[analytics|analytics]], analysis aimed at a strategic question: should Tamarack put monitors on all 4,000 propane customers? In the first five weeks, the summary showed the trucks had made 31 percent fewer stops at tanks over half full. It also showed that 60 of the 900 monitors had stopped reporting, mostly in places with poor cell coverage, and those were the customers farthest out, where a missed delivery hurt the most.

Ruth approved the monitors for 1,500 more tanks, not 4,000, and asked for a coverage map first. Hank asked whether the refresh would take three times as long. Eli said it would probably take longer.
