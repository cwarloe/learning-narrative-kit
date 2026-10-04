# Hank's Year-End

*Tamarack Feed & Supply Co. • Excel Module 9: Exploring Financial Tools and Functions • Hover over highlighted terms for course definitions.*

## Four Questions in One Week

In the second week of March, Hank Pruitt was closing Tamarack's fiscal year, preparing for the auditors, and answering Walt Brandvold's questions about Davenport, all at once. He borrowed Eli Mendez from the DC for three afternoons. Ruth Halvorsen agreed on the condition that Eli would be back on the night shift by Thursday.

Eli's ninth SAM module was financial tools and functions. Hank had four questions, and Eli wrote them on a sticky note: what does the new forklift cost us each year, how much of the loan have we paid, is Davenport worth it, and how much propane do we buy for next winter.

## The Statement Everything Lands On

Hank started by showing Eli where all four answers would end up. The [[income_statement|income statement]] summarized Tamarack's income and expenses over the fiscal year. Hank called it the [[profit_and_loss_p_l_statement|profit and loss statement]], or the P&L, which was the same document under another name.

Near the top was sales. Below it was the cost of the goods sold. The difference was [[gross_profit|gross profit]], what was left of each sales dollar after paying for the merchandise, before rent, salaries, or anything else. Tamarack's gross profit was about 30 cents on the dollar. Below that came operating expenses, including depreciation and interest, and at the bottom, net profit.

"Everything you calculate this week lands on one line of this," Hank said. "If it's wrong, the line's wrong."

## What the Forklift Costs Each Year

The new forklift had been delivered in December for $34,000. It was one of Tamarack's [[tangible_assets|tangible assets]], physical noncash things like equipment, land, buildings, and vehicles. The company didn't expense its whole cost in one year; it spread the cost over the forklift's useful life through depreciation. Hank estimated eight years and a $4,000 salvage value at the end.

[[straight_line_depreciation|Straight-line depreciation]] took the same amount each year until the asset reached its salvage value. The SLN function did it in one step: =SLN(34000, 4000, 8) returned $3,750 a year.

[[declining_balance_depreciation|Declining balance depreciation]] took the same percentage each year instead, so the dollar amount was largest in year one and shrank after that. The DB function, =DB(34000, 4000, 8, 1), returned $7,990 for the first year.

Eli asked which was right. Hank said both were legitimate methods and the question was what Tamarack wanted its P&L to show. Declining balance put more expense in the early years, when a forklift actually lost value fastest, and lowered this year's reported profit. Straight-line was simpler and matched how Tamarack had always done it. The auditors would want the same method used consistently. Hank chose straight-line and said he'd think about the other one next year, which Eli was learning was how Hank said no.

## How Much of the Loan Was Paid

The forklift loan was $34,000 at 7.5 percent for five years. The board had approved one forklift, not two. The payment was $681.29 a month. Hank wanted the first twelve payments split into interest and principal, because only interest was an expense. Principal just reduced the debt.

The [[cumipmt_function|CUMIPMT function]] added up the interest across a range of payments: =CUMIPMT(7.5%/12, 60, 34000, 1, 12, 0) returned about -$2,353 of interest for the first twelve payments, negative because it was money going out. The [[cumprinc_function|CUMPRINC function]] did the same for principal: about -$5,823. Added together, they equaled twelve payments.

Eli noticed that interest was large at the start and shrank as the balance fell. Hank said that was why paying a loan off early saved more than people expected.

## Is Davenport Worth It

Walt's question was the one Hank cared about most. Davenport would open in May. Walt wanted to know, in one number, whether the store was a good investment.

The answer started with the [[time_value_of_money|time value of money]]: a dollar received today was worth more than a dollar received in five years, because today's dollar could be invested or used to pay down debt in the meantime. A store that cost $260,000 now and paid back $260,000 over eight years had not broken even. It had lost money.

Hank had projected Davenport's [[cash_flow|cash flow]], the money moving in and out, by year. There was $260,000 out on March 15 for fixtures, the build-out, and opening inventory. Another $18,000 out by December, the first-year loss Eli's break-even model had predicted. Then money coming in each December: $42,000, $64,000, $78,000, and up to about $92,000 by year eight.

The dates weren't evenly spaced, because the build-out money went out in March and the fiscal year ended in December. The [[xnpv_function|XNPV function]] calculated the net present value of cash flows at specific dates, discounting each one by how far in the future it fell. At a 9 percent discount rate, about what Tamarack paid to borrow, XNPV returned about $72,000. That meant the store was worth more than it cost, in today's dollars.

The [[xirr_function|XIRR function]] calculated the internal rate of return for the same dated cash flows, the rate at which the store's net present value would be exactly zero. It came out to 14.5 percent.

Walt had a rule, older than Hank's time at the company, that a new store should return 15 percent. Hank said the rule was something Walt's father had made up in 1979. Walt said that it had worked since 1979.

## How Much Propane

The last question was propane. Tamarack pre-bought propane each summer for the winter, at a contract price, to protect customers from price spikes. Buying too much meant paying for gas nobody used. Buying too little meant buying the rest on the spot market in January.

Eli pulled five years of monthly propane gallons. It was [[seasonal_data|seasonal data]] — values that followed a pattern through the year — high in December and January, nearly nothing in July.

He made a [[forecast_sheets|forecast sheet]], Excel's tool for modeling data and projecting it forward. It drew the history and a forecast line for the next twelve months that kept the seasonal pattern. Above and below the line were [[confidence_bounds|confidence bounds]], the upper and lower edges of the range the forecast expected the real values to fall in. For next January, the forecast was 184,000 gallons, with bounds from 151,000 to 217,000.

"That's a sixty-six-thousand-gallon range," Hank said. "That's the whole question."

Eli tried another angle. He made a chart of yearly totals and added a [[trendline|trendline]], a line showing the general direction of the data. The trend was up about 3 percent a year as Tamarack added customers. The chart also showed the [[r_statistic|R² statistic]], how much of the variation the trendline explained. It was 0.41. Less than half of the year-to-year change was the trend; the rest was mostly how cold the winter was, which nobody could forecast in June.

Hank also wanted to see how big a typical delivery was, for planning the new delivery truck's route. Eli made a [[histogram|histogram]], a column chart showing how values from one series were distributed. He divided delivery sizes into [[bins|bins]] of 100 gallons each: 0–100, 100–200, and so on. Most deliveries landed in the 200–300 bin. A long tail of big ranch deliveries ran out past 1,000 gallons.

## What Hank Took to Walt

Hank presented Thursday morning. The forklift went on the books at straight-line. The loan interest went on the P&L. Davenport's XIRR went on a slide by itself.

Walt looked at 14.5 percent and said it was half a point short. Hank said the cash flows were estimates, the half point was well inside the error, and the store was already leased. Walt said he knew it was already leased.

For propane, Hank contracted for 170,000 gallons, below the forecast and above the low bound, and planned to buy the rest on the spot market if it was a hard winter. If it was a hard winter, the spot price would be high too. Hank said so in the meeting, so that nobody could say later that he hadn't.

Eli was back on the night shift Thursday, as promised. He had missed two SAM deadlines that week and asked the instructor for an extension. The instructor gave him four days on one and none on the other.
