# The Crew Bonus

*Tamarack Feed & Supply Co. • Excel Module 3: Performing Calculations with Formulas and Functions • Hover over highlighted terms for course definitions.*

In August, during the worst week of the heat, Walt Brandvold walked through the distribution center and told the night crew that if they got through Chick Days' fall rush and the feed season without a lost-time injury, there would be a bonus. He didn't say how much. He didn't say how it would be figured. He told Ruth Halvorsen about it the next morning, and Ruth told Hank Pruitt, and Hank asked who was going to calculate it.

In October, the answer turned out to be Eli Mendez, because he ran the night crew, because he was taking the Excel course, and because Hank wanted the calculation in a workbook he could check rather than in Eli's head.

Ruth gave him the rules she and Walt had worked out. A base amount per person, scaled by productivity tier. Only people who'd worked at least sixty days in the quarter. Nobody with a safety incident. Paid with the second paycheck after quarter end. Hank added one rule of his own: every number had to trace back to the timeclock export or the warehouse system, and nothing could be typed in by hand.

Eli's third SAM module was formulas and functions. He worked through it on two nights, and on the third, after the last truck was unloaded, he sat down at the computer in the DC office and opened the timeclock export.

The first thing he needed was hours. Each row in the export had an employee ID, a date, a clock-in time, and a clock-out time.

A formula in Excel started with an equal sign and used [[arithmetic_operators|arithmetic operators]] to calculate: + to add, - to subtract, * to multiply, / to divide, ^ for exponents. Time in Excel was stored as a fraction of a day, so hours worked was clock-out minus clock-in, times 24. In the formula =(D2-C2)*24, the 24 was one of the [[constants|constants]]: a value that didn't change from row to row. The minus and the asterisk were [[operators|operators]], symbols that combined the values into one result.

The night shift crossed midnight, so for some rows clock-out was smaller than clock-in and the answer came out negative. Eli fixed it the way the SAM example showed, by adding 1 day when the out time was earlier. That needed a [[logical_function|logical function]], one that returned different values depending on whether a condition was true: =IF(D2<C2, D2+1-C2, D2-C2)*24. The < was a [[comparison_operator|comparison operator]], a symbol showing how two values related. The others were >, =, >=, <=, and <>.

The IF function had three [[argument|arguments]] separated by commas: the condition, what to return if it was true, what to return if it was false. Each function had its own [[syntax|syntax]], the rules for which arguments went where and in what order. Eli got it wrong twice before he got it right, and the formula bar showed him exactly where.

Ruth's eligibility rule had two parts, and both had to be true: at least sixty days worked and no safety incidents. Eli used the [[and_function|AND function]], which returned TRUE only if every argument was true. =AND(F2>=60, G2=0).

Then Hank remembered an exception. Two people had been on light duty for part of the quarter after non-work injuries, and one had been on approved family leave. Walt had said they should still qualify if they'd been on the crew when he made the promise. That needed the [[or_function|OR function]], which returned TRUE if any argument was true. Eli [[nested|nested]] it, putting one function inside another: =OR(AND(F2>=60, G2=0), H2="Light duty", H2="Leave").

The words "Light duty" and "Leave" in quotation marks were each a [[text_string|text string]], a series of characters Excel compared as text rather than numbers. When Eli forgot the quotation marks the first time, Excel showed #NAME? in the cell. That was an [[error_value|error value]], a message saying something in the formula kept Excel from calculating an answer.

The tiers were based on pallets moved per hour, from the warehouse system. Ruth stopped at the DC office the next evening on her way home, still in her coat, because she wanted to know what a normal number was before she set the tier cutoffs.

Eli started with the [[average_function|AVERAGE function]] over the whole crew. It returned 41.3 pallets per hour. The [[average|average]], the sum divided by the count, was the number most people meant by "normal."

Ruth didn't trust it. One new hire, a big kid named Tyler, had logged 4 pallets an hour his first week while he learned the forklift, and three of the senior people ran over 60. "Is 41 what a normal person does," she asked, "or is it what the fast ones and Tyler add up to?"

Eli's SAM module had a section on [[central_tendency|central tendency]]: single numbers that tried to describe the typical value in a series. There were three. The [[mean|mean]] was the average, and it could be pulled around by extreme values. The [[median|median]] was the middle value when all the values were lined up in order, which ignored how extreme the ends were. The [[mode|mode]] was the value that showed up most often.

The median came out to 44. That was closer to what Eli would have guessed from watching the floor. For the mode, he used the [[mode_mult_function|MODE.MULT function]], which returned 45. Pallets per hour were rounded to whole numbers in the warehouse system, and 45 came up more than any other value.

Ruth set the tier cutoffs around the median.

Two nights later Hank called down from head office. He wanted the bonus checked against overtime. If a crew had hit its numbers by working a lot more hours, that was a different story.

The first version of what Hank wanted was a [[conditional_sum|conditional sum]]: total overtime hours for the night crew only. SUMIF added the values in a range that matched one condition. A [[conditional_count|conditional count]], COUNTIF, counted the cells that met one condition: how many shifts ran over ten hours. A [[conditional_average|conditional average]], AVERAGEIF, averaged values that met a condition: average shift length on Saturdays.

But Hank wanted those numbers by crew and by month, which was two conditions. The SAM module had functions for that. The [[sumifs_function|SUMIFS function]] added values that met several criteria at once: overtime hours where the crew was "Night" and the month was October. The [[countifs_function|COUNTIFS function]] counted rows meeting several criteria. The [[averageifs_function|AVERAGEIFS function]] averaged them. The [[maxifs_function|MAXIFS function]] found the highest value meeting the criteria, which was the night crew's best week, and the [[minifs_function|MINIFS function]] found the lowest, which was the week the propane forklift was down.

Eli tripped once on syntax. In SUMIF, the range to add came last. In SUMIFS, it came first. He swapped them and got a number that was obviously wrong, then caught it.

Each employee's tier came from their pallets per hour, and their name and base bonus amount came from a separate HR list, which set the base by role. Both were jobs for a [[lookup_function|lookup function]], which retrieved a value from a table based on something you gave it.

The HR list was a [[lookup_table|lookup table]], a table holding the data to retrieve. The employee ID was the [[lookup_values|lookup value]], the thing being looked for. The name and base amount were the [[return_values|return values]], what came back. The IDs had to match exactly; employee 1047 was not employee 1046. That was an [[exact_match_lookup|exact match lookup]].

The tiers were different. Ruth's tier table had cutoffs: 0 pallets per hour was Tier 0, 38 was Tier 1, 44 was Tier 2, 52 was Tier 3. A person at 47 wasn't in the table, but fell between 44 and 52, so they were Tier 2. That was an [[approximate_match_lookup|approximate match lookup]], where the value fell within a range. The cutoffs had to be sorted from smallest to largest or the lookup would return the wrong tier. The first time, Eli had Tier 3 at the top and everyone came out Tier 3.

Ruth asked for a plain-language tier name next to each number. Eli used the [[ifs_function|IFS function]], which tested multiple conditions in order without nesting a stack of IFs: =IFS(J2=3, "Gold", J2=2, "Silver", J2=1, "Bronze", J2=0, "Base").

The bonus came out in odd amounts: $412.6875. Hank didn't want odd amounts on paychecks.

The [[round_function|ROUND function]] rounded to the nearest digit you specified: =ROUND(K2, 2) gave $412.69. Hank wanted whole dollars, and he wanted them rounded down, so nobody could say the company had rounded up for some people. The [[rounddown_function|ROUNDDOWN function]] cut off digits instead of rounding: =ROUNDDOWN(K2, 0) gave $412. The [[int_function|INT function]] gave the same answer for a positive number like this one, and Eli used it to count full weeks worked: =INT(F2/5). The two weren't the same function. The SAM module's practice sheet had a negative adjustment of -1.9, and ROUNDDOWN turned it into -1, moving toward zero, while INT turned it into -2, the next lowest integer. Bonuses were never negative, so Eli left a note in the workbook and moved on.

Ruth wanted the bonus amounts in multiples of five dollars so they looked deliberate. The [[mround_function|MROUND function]] rounded to the nearest multiple of a number: =MROUND(K2, 5) gave $415. That rounded up for some people. Hank and Ruth argued about it by email, with Eli copied on every message. Hank lost.

Pallets per hour stayed rounded to whole numbers. Showing 44.271 suggested a precision the warehouse system's counts didn't have. The SAM module called this choosing [[significant_digits|significant digits]]: displaying only as many digits as the measurement could support.

The payout date came from Ruth's rule: the second paycheck after quarter end. Eli needed to count working days.

The [[networkdays_function|NETWORKDAYS function]] calculated the number of working days between two dates, leaving out weekends and any holidays listed. He used it to check the sixty-day rule against each person's hire date, for the three people who'd started mid-quarter. The [[workday_function|WORKDAY function]] went the other direction: given a start date and a number of working days, it returned the date that many working days later. Payroll processed ten working days after quarter end; WORKDAY told him that was October 14.

At the top of the sheet, Eli put "Calculated as of" and the [[today_function|TODAY function]], which returned the current date. Hank came by the next day, opened the file, and asked why the date had changed. TODAY was one of the [[volatile_functions|volatile functions]]: it recalculated every time Excel recalculated anything in the workbook, so the "as of" date was always today. For an audit trail, that was useless. Eli replaced it with a typed date and a note.

Hank also wanted every printed page to show which file it came from, since there were already three versions. Eli used the [[cell_function|CELL function]], which returned information about a cell. =CELL("filename", A1) returned the file's full path and sheet name, and he put it in the corner of the printout.

The last number Hank wanted was the total payout: each person's bonus times one if they qualified and zero if they didn't, all added up. Eli could add a helper column and sum it. The SAM module showed another way.

An [[array_formula|array formula]] performed multiple calculations in one step. =SUM(L2:L38*M2:M38) multiplied each bonus by each eligibility flag, row by row, and added the results, all in one cell. In older versions of Excel he would have had to press Ctrl+Shift+Enter. His version just worked. The total was $9,840.

Before he sent the workbook to Hank, Eli cleaned up its appearance. A few rows showed #N/A where the lookup hadn't found an employee ID in the HR list. He wrapped the lookup in the [[iferror_function|IFERROR function]], which replaced any error value with something you chose. He chose a zero, so the totals downstream would still add up. The sheet looked clean.

Hank checked the total against payroll and approved it. Walt announced the bonus at the Friday crew meeting. Everyone got the amount on their list.

## Marco's Pay Stub

On payday, a forklift driver named Marco Reyes came to Eli's desk with his pay stub and asked where his bonus was. He had worked eighty-one days, he'd had no incidents, and he ran fifty-three pallets an hour.

Eli found it in three minutes. Marco's employee ID in the HR list had a typo: 1174 instead of 1147. The lookup couldn't find him and returned #N/A, and IFERROR turned it into a zero. His base amount became zero, and zero times any tier multiplier was still zero. The total had been $415 short.

Hank cut Marco a separate check the following week. Eli removed the IFERROR and replaced it with one that said "ID NOT FOUND" in red, so that the next missing person would be visible instead of clean. Marco took the check and said thanks. He also said that he'd waited a week for money the company had announced in front of everyone, and that people on the crew had asked him whether he'd done something wrong.
