# Two Old Forklifts

*Tamarack Feed & Supply Co. • Excel Module 4: Analyzing and Charting Financial Data • Hover over highlighted terms for course definitions.*

## The Week the Forklift Was Down

The worst week in Eli Mendez's bonus workbook was the week in August when the DC's number-two propane forklift threw a hydraulic line and sat for six days waiting on a part. The night crew's pallets per hour dropped by a third. It had happened before. The two oldest forklifts were fourteen and sixteen years old, and the repair invoices on them had been climbing for three years.

Eli wanted them replaced. Ruth Halvorsen told him that wanting wasn't a proposal, and that the capital budget meeting was in three weeks. If he could make the case with numbers Hank Pruitt would believe, she would put it on the agenda.

His fourth SAM module was on charts and financial functions. The timing felt arranged.

## What Was Actually Breaking

Eli pulled three years of DC downtime from the maintenance log: every hour a piece of equipment or a dock was out of service, and why. He wanted Ruth to see it, not read it.

[[charts|Charts]] turned numbers into bars, lines, slices, or dots so the relationships showed at a glance. Each chart was built from one or more [[data_series|data series]]: the values from one column or row of the sheet. The trick was matching the chart type to the question.

The first question was which causes mattered most. He made a [[pareto_chart|Pareto chart]], which combined a column chart with a line, sorted the causes from biggest to smallest, and drew the cumulative percentage on top. Forklift breakdowns were the tallest column, at 412 hours. The line showed that forklifts and dock-door failures together accounted for 71 percent of all downtime. Everything else was a long tail.

He tried showing the same thing as a pie. [[pie_charts|Pie charts]] showed the proportions of the whole, which was fine for "forklifts are about half." He pulled the forklift slice out to make the point, an [[exploded_pie_chart|exploded pie chart]] with one wedge separated from the rest. It looked dramatic. Ruth said it looked like a pizza ad and asked him to keep the Pareto.

## Over Time

The second question was whether it was getting worse.

[[line_charts_or_time_series_charts|Line charts]], also called time-series charts, showed how data changed over time. Eli plotted monthly repair costs for each of the four forklifts over thirty-six months. The two old ones climbed. The two newer ones stayed flat.

The months ran along the bottom on the [[category_axis|category axis]], the horizontal or x-axis that held the category names. Dollars ran up the side on the [[value_axis|value axis]], the vertical or y-axis for numbers. He added an [[axis_title|axis title]] to each: "Month" and "Repair cost ($)." Ruth had once seen a chart in a board meeting where nobody could tell whether the axis was dollars or units, and she checked for axis titles first.

[[major_tick_marks|Major tick marks]] marked every $500 on the value axis. Eli added [[minor_tick_marks|minor tick marks]] every $100 between them, then took them off again because they made the chart look like graph paper.

## Comparing the Four

For comparing the forklifts side by side, year by year, he needed columns. [[column_charts|Column charts]] were good for showing changes over a period or comparing items. A plain [[column_chart|column chart]] showed each value as a column whose height was the value. A [[clustered_column_chart|clustered column chart]] put several series side by side within each category: for each year, four columns, one for each forklift. The two old forklifts' columns got taller every year.

Hank asked whether the cost was parts or labor. Eli switched to a [[stacked_column_chart|stacked column chart]], where each forklift's column was split into parts and labor stacked on top of each other, so the total height was still the total cost. Labor was growing faster than parts. Old forklifts were taking longer to fix.

Ruth asked a different question: was the share of labor growing, regardless of the total? For that, he used a [[100_stacked_column_chart|100% stacked column chart]], which made every column the same height and showed each part as a percentage. Labor went from 38 percent of repair cost in the first year to 55 percent in the third.

## The Part Numbers

The maintenance log also listed the most expensive repair parts, and their names were long: "Hydraulic lift cylinder seal kit, 2-stage mast." On a column chart, the names turned sideways and became unreadable.

[[bar_charts|Bar charts]] emphasized differences between items. A [[bar_chart|bar chart]] was a column chart turned on its side, with each bar's length showing its value, and the long names had room to sit horizontally to the left of each bar. Eli made one for the top ten parts. The lift cylinder seal kit had been replaced seven times.

## Age and Cost

The third question was whether age itself predicted repair cost, or whether these two forklifts were just unlucky.

[[xy_scatter_charts|XY (scatter) charts]] showed the relationship between two sets of numbers. Eli plotted every forklift the company had owned in the last decade, including some sold off. Age was on the horizontal axis and annual repair cost on the vertical. The dots climbed from left to right, gently until about year ten, then steeply. The two old forklifts were in the steep part.

## Cost and Downtime Together

Ruth wanted one chart that showed both repair dollars and downtime hours. They had very different scales: thousands of dollars against dozens of hours. On a single axis, the hours would be a flat line at the bottom.

Eli built a combination chart. Repair cost was a column series plotted against the [[primary_axis|primary axis]] on the left. Downtime hours was a line series plotted against a [[secondary_axis|secondary axis]] on the right, with its own scale. Now both rose together, visibly.

He added a [[data_callout|data callout]], a label in a bubble pointing at a single data point, to August of last year: "Hyd. line failure — 6 days down."

## The Loan

Now Eli had to show what replacing them would cost. Hank had dealer quotes: $68,000 for two new propane forklifts.

Excel's [[financial_functions|financial functions]] analyzed loans and investments. Hank's bank offered 7.5 percent annual interest over five years.

The $68,000 was the [[principal|principal]], the amount being borrowed. [[interest|Interest]] was what the lender added on top. The PMT function calculated the payment: =PMT(7.5%/12, 60, -68000). The rate was divided by 12 because the payments were monthly, 60 was the number of payments, and the principal was entered as a negative number. Excel's financial functions treated money moving in one direction as positive and the other as negative, and entering the loan as negative made the payment come out positive. The answer was $1,362.58 a month. Over sixty months, that was $81,755 total, which meant about $13,755 in interest.

The dealer had a financing offer of its own: $1,400 a month for sixty months, "no money down." It sounded close to the bank's. Eli used the PV function to find out what that stream of payments was worth today, at the bank's rate. The [[present_value|present value]], the current value of a loan or investment, came out to $69,867. The dealer's deal was $1,867 more expensive than the bank's, in today's dollars.

Hank had a third option: no loan. Put $1,000 a month into an equipment reserve account at 4 percent for three years, then buy. The FV function calculated the [[future_value|future value]], what an investment would be worth at a future date: about $38,200. That was enough for one forklift, three years from now, if both old ones lasted that long. Eli's scatter chart suggested they wouldn't.

## The Budget Picture

For the board, Ruth wanted one picture of what the DC's equipment budget would look like if the proposal passed.

Eli used a [[waterfall_chart|waterfall chart]], which tracked how a total built up or broke down through additions and subtractions. It started with this year's equipment budget, added the new loan payments, subtracted the repair costs that would go away, subtracted the rental forklift they'd paid for during last year's breakdowns, and ended at next year's budget. The ending bar was a little lower than the starting bar.

Marcy Lund saw it and asked for something she could use for her own budget. Eli showed her [[hierarchy_charts|hierarchy charts]], which showed how groups contributed to a whole. A [[treemap_chart|treemap chart]] drew the DC's budget as nested rectangles: equipment, labor, facilities, and inside equipment, each forklift as its own rectangle sized by cost. A [[sunburst_chart|sunburst chart]] showed the same hierarchy as rings, with the top-level categories in the middle and the details on the outer rings. Marcy liked the treemap. She said the sunburst looked like a target.

## Getting It Ready

Ruth wanted the combination chart on its own page in the board packet. Eli moved it to a [[chart_sheet|chart sheet]], a separate sheet in the workbook that held only the chart and was still linked to the data. He cleaned up the [[chart_elements|chart elements]], removing the gridlines, moving the legend to the bottom, and making the title say what the chart meant: "Repair cost and downtime rise together on the two oldest forklifts."

For the printout, he adjusted the [[scaling|scaling]] on the data sheet so all of it fit on one page wide.

## What Hank Saw

Hank reviewed everything on Monday, starting with the line chart.

He pointed at the value axis. Eli had let Excel set the [[scale|scale]] automatically, and it had chosen a minimum of $1,500 instead of $0, because all the monthly values fell between $1,500 and $4,000. With the bottom of the axis cut off, the old forklifts' repair costs looked like they had quadrupled. They had roughly doubled.

"If Kip Andersen catches that," Hank said, "he won't believe anything else in the packet."

Eli reset the axis to start at zero. The lines were flatter. They still climbed, but the chart was less dramatic, and Eli was sorry to see the drama go.

The board approved one forklift, not two, on the bank loan. They asked for the second to come back next year with another year of repair data. Eli thought about the scatter chart and the steep part of the curve, and he kept the file.
