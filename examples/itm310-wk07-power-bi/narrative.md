# The Buying Group

*Tamarack Feed & Supply Co. • ITM 310 Week 7: Intro to Power BI • Hover over highlighted terms for course definitions.*

The feed buying group met for the first time on a Tuesday in late October, in the Tamarack conference room, after three years of being a good idea. Walt Brandvold sat at the head of the table. Gene Palmer had driven down from Kettle Falls, where his family had run Palmer's Feed & Seed since before Walt was born. Linda Ostby ran the Grange Supply in Deer Park and had come with a legal pad she didn't write on. Marcy Lund had the agenda.

The reason they were finally meeting was the Inland Valley Mill. In December the mill would set next year's prices, and its rep had told Marcy, almost in passing, that dealers buying more than 1,500 tons a year got a price break. None of the three companies bought that much alone. Together, Marcy thought, they might.

"So we show him a number," Walt said. "Combined tons. How hard is that?"

Dana Okafor had been asked to the meeting to answer exactly that question, and she had decided the honest answer was "harder than it looks, and here's how we'll do it anyway." Three companies, three point-of-sale systems, and three owners who had never run a data project. If the project was going to survive the first disagreement, it needed a process the owners could follow without trusting her.

She used [[crisp_dm|CRISP-DM]], the standard process she'd learned in school for BI and data mining projects. Nobody owned it and it didn't care which software you used, which mattered in a room where Gene ran an accounting package Tamarack had never heard of. She drew the six phases on the whiteboard and circled the first.

```steps
caption: Dana's whiteboard: the CRISP-DM life cycle
> Business Understanding: what are we trying to prove, and to whom?
Data Understanding: what do the three exports actually contain?
Data Preparation: make them into one dataset
Modeling: build the model and the calculations
Evaluation: does the report answer the question?
Deployment: who uses it, where, and how often?
```

"We're going to spend today on the first one," she said. "If we skip it, we'll build a very nice report about the wrong thing."

[[business_understanding|Business understanding]] meant stating the objective from the business side first, turning it into a BI problem, and only then planning. Walt's version of the objective was "get the price break." Dana pushed for something a report could actually answer, and Marcy pushed for something the mill rep couldn't argue with. Gene pushed back on both.

"I'm not putting my prices in front of Walt," he said, pleasantly. "Or my customers."

That settled more than it seemed to. The group would share volumes, by product and month, and nothing else. Dana wrote the result on the board as three lines.

```table
caption: The statement everyone signed off on
| Statement | What it says |
|---|---|
| Business objective | Qualify the three dealers, buying together, for the Inland Valley Mill's 1,500-ton price break next year. |
| BI objective | Show combined tons purchased from the mill over the last twelve months, by product, by month, and by dealer. |
| Success criteria | A combined number the mill rep can trace back to each dealer's own records, with no prices or customer data shared. |
```

Linda read it twice and asked who would see the dealer-by-dealer numbers. Dana said everyone in the room. Linda wrote her first note on the legal pad.

## Two Evenings at the DC

The three exports came in over the next week, and on Thursday night Dana brought them down to the DC office, where Eli Mendez had stayed after his shift to help. Eli had built Ruth's Power BI report in September and was the only person at Tamarack who had used it for more than an afternoon.

They started with [[data_understanding|data understanding]]: before changing anything, get familiar with the data and find out what was wrong with it. Eli opened each file in Power BI Desktop with [[get_data|Get Data]] and looked at the first rows.

```table
caption: The first row of each dealer's export
| Dealer | Columns in the file | First row |
|---|---|---|
| Tamarack | Item, Description, Bags, BagLbs, Month | 40817 · Inland Valley Mill - Layer Pellets 50# · 100 · 50 · 2026-03 |
| Palmer's | Product, Qty, Unit, Month, Price | PAL-17 · Inland Valley Mill - Lyr Pellet · 40 · 40# bag · Mar-26 · 15.10 |
| Deer Park | SKU, Mill Product, Pounds, Period | DP-220 · Inland Valley Mill - All Stock 14% · 4000 · March 2026 |
```

Nothing matched. Tamarack counted bags with a weight column. Palmer's counted bags with the weight buried in a text field, spelled "Lyr Pellet," and with Gene's prices still attached. Deer Park counted pounds. Each file used its own product codes, and the dates came in three formats.

Dana kept a list as they went, because data understanding was supposed to produce one: product names inconsistent, units inconsistent, Palmer's file contains prices that must not leave this room. While sorting Deer Park's pounds largest to smallest, Eli found one more. A single June row read 400,000 pounds of all-stock feed. Linda's whole store moved less than a tenth of that in a month.

"Typo?" Eli asked.

"Probably. We don't get to decide that." Dana added it to the list as a question for Linda.

[[data_preparation|Data preparation]] took the rest of that night and most of the next. The course slides warned that this phase could eat eighty or ninety percent of a project. Dana had thought that was an exaggeration until about nine-thirty on Thursday.

The work happened in the [[query_editor|Query Editor]], Power BI's tool for [[etl|ETL]]: extract the data from each file, transform it into one shape, and load it into the model. Eli did Palmer's first, because it was the worst. Each thing he did became a line in the query's [[applied_steps|Applied Steps]], which Power BI would replay every time the data refreshed.

```steps
caption: Query Editor · Palmer's query · Applied Steps
Source
Promoted Headers
Removed Columns (Price): Gene's rule, before anything else
Split Column by Delimiter: Product at " - " into Mill and Product
Replaced Value: "Lyr Pellet" with "Layer Pellets"
Added Custom: Pounds = Qty × the number in Unit
Changed Type: Month to a date
```

The split was the step Dana watched most closely. Every dealer's product field started with the mill's name, then a space, a hyphen, and a space, then the product. Telling the Query Editor that " - " was the [[delimiter|delimiter]] cut the field cleanly into two columns, Mill and Product, and the Mill column made it easy to drop the handful of rows that came from other mills.

Then he did the same for Tamarack and Deer Park, renamed the columns to match, and appended all three into a single table called FeedSales. [[close_and_load|Close & Load]] put it into the model. It was 11:40 p.m. Eli went home.

* * *

Friday night was [[modeling_phase|modeling]]. Dana had been thinking about the model's shape all day, and she drew it for Eli before he touched anything.

```tree
caption: Model view · the buying group's star schema
FeedSales (fact): Dealer ID, Product ID, Month, Pounds
  Dealers (dimension): Dealer ID [key], Dealer name, Town
  Products (dimension): Product ID [key], Product, Category
  Calendar (dimension): Month [key], Quarter, Year
```

It was a [[star_schema|star schema]]: one [[fact_table|fact table]] in the middle, a row for every dealer, product, and month, with the pounds, and a [[dimension_table|dimension table]] for each way the group would want to slice it. Each [[relationship|relationship]] joined a [[primary_key|primary key]] in a dimension table to the matching [[foreign_key|foreign key]] in FeedSales. The slides were blunt about the rule: the two fields had to match, with the same range of values, or the relationship would quietly fail.

It quietly failed. The Products table used Tamarack's item numbers, like 40817, as its key. Palmer's rows carried Gene's codes, like PAL-17, and Deer Park's carried Linda's. When Eli put a bar chart on the page, there was a bar labeled "(Blank)" holding 750 tons that belonged to products the model couldn't find. Fixing it meant going back to data preparation, which the slides also said would happen. Marcy built a small mapping table that night, matching every Palmer's and Deer Park code to a Tamarack item number, and Eli merged it into the two queries. The blank bar went away.

Then the calculations. Power BI used [[dax|DAX]], a formula language that started out looking like Excel's and went much further. The course's best practice was to write calculations from the [[data_view|Data view]], on the Modeling tab, and to let the pick-list fill in table and column names so nothing was misspelled. The first one was simple. The mill priced in tons, the files were in pounds, and every row needed converting.

```formula
caption: Power BI Desktop · Data view · FeedSales · New column
Tons = FeedSales[Pounds] / 2000
→ First row: 5,000 pounds of layer pellets becomes 2.5 tons.
```

That was a [[calculated_column|calculated column]]: a new value in every row, computed when the data refreshed. Eli wanted the grand total next, and he did what anyone fresh from Excel would do. He added another column.

```formula
caption: The first try at a total, also as a new column
TotalTons = SUM(FeedSales[Tons])
→ Every one of the 1,412 rows says 1,930.0.
```

The formula wasn't wrong. It was in the wrong place. A column calculated one value per row, so every row dutifully held the sum of the whole column, and the number couldn't change when anyone filtered by dealer or product. Dana pulled up the slide comparing the two. A total was an aggregate, and aggregates belonged in a [[calculated_measure|calculated measure]]: something that belonged to the whole model rather than a table and was computed on the fly inside each visual, adapting to whatever filters were applied.

Eli deleted the column and wrote it again from New Measure.

```formula
caption: Power BI Desktop · Modeling tab · New measure
Total Tons = SUM ( FeedSales[Tons] )
→ On a card: 1,930. On a bar chart by dealer: Tamarack 1,180, Palmer's 340, Deer Park 410.
Tons Over Break = [Total Tons] - 1500
→ 430
```

The second measure was the one Walt would care about, a [[kpi|KPI]] measuring the group against its one goal. It used the first measure inside it, which a column couldn't have done.

## The Second Meeting

The group met again the next Tuesday, and Eli brought the report up on the conference room screen. Before the meeting he had spent an hour on the [[report_canvas|report canvas]], dragging fields onto it and into the [[visual_details|visual details]] area under Visualizations, the axes and legend and values. Once, with the Total Tons card still selected, he had clicked the bar chart icon, and the card turned into a bar chart. The fix, he learned, was to click a blank part of the canvas first. Now the page held a card with Total Tons, a bar chart of tons by product, a line chart by month, and a [[slicer|slicer]] with the three dealers' names.

These were [[power_bi_reports|Power BI reports]] doing what they were for: letting the people who had to decide explore the data themselves. Gene clicked his own name on the slicer and watched every visual change to show only Palmer's. Then he clicked Linda's.

This was the [[evaluation_phase|evaluation]] phase, and Dana asked the question on the slide out loud: does the report satisfy the objective? Walt said yes; the card said 1,930, which was over 1,500 by a comfortable margin. Marcy said she wanted to see bag weights, so Eli dragged BagLbs onto a table, and it showed 68,623 pounds per bag. Power BI's default [[aggregation|aggregation]] for a number was sum. He changed it to average in the drop-down under Values, and it read 48.6, which was right. Nobody had been fooled, but it took the confidence out of the room for a minute.

Then Dana read the success criteria. A combined number the mill rep can trace back to each dealer's own records. She asked Linda about the 400,000-pound row from June.

Linda looked at it for a long time. "That's not a sale," she said. "That's our bin capacity. Somebody typed it in the wrong field."

```steps
caption: Dana's whiteboard, updated
Business Understanding
Data Understanding
> Data Preparation: remove Deer Park's June bin-capacity row, then refresh
Modeling
Evaluation
Deployment
```

Eli filtered the row out in the Deer Park query and refreshed. Deer Park dropped from 410 tons to 210. Total Tons dropped to 1,730. Tons Over Break dropped to 230. Still over, but no longer comfortable.

Gene, who had been quiet, asked to see the dealer bars again. Tamarack, 1,180. Palmer's, 340. Deer Park, 210.

* * *

[[deployment_phase|Deployment]] was the last phase, and the slides framed it as three questions: how the results would be used, who would use them, and how often. The answers were awkward.

The results would be used once a year in front of the mill, and monthly in between, so the group could watch whether it stayed over the line. The [[power_bi_service|Power BI service]], in the cloud, would have let all three dealers open the same live report from anywhere. It also needed a paid license for each person viewing it, and Gene said he wasn't paying for another subscription to look at a number he could be emailed. [[power_bi_mobile|Power BI Mobile]] would have put it on Walt's phone, which Walt wanted, for the same price. So the report stayed in [[power_bi_desktop|Power BI Desktop]] on Marcy's computer, on-premise, where Eli could refresh it on the first of each month and send each owner a PDF. For Gene's and Linda's copies, Eli used the [[filter_pane|Filters pane]] instead of the slicer, so the filter didn't show on the page and neither owner received the other's monthly detail.

Linda called Marcy two days later. She had looked at the bars again. Deer Park was twelve percent of the group's tons, and she had done the arithmetic on what the price break would save her, and on the hours she'd spend matching codes every month. She said she'd rather stay out and keep her own terms with the mill.

Without Deer Park, the group's total was 1,520 tons. Eli updated the slicer, and the card said 20 tons over the break, about one week of Tamarack's purchases from the mill. Marcy went to the December meeting with the report anyway. The mill rep asked for the dealer breakdown, traced Palmer's number back to Gene's invoices on the spot, and approved the break for next year on the condition that the group stay over 1,500 every quarter.
