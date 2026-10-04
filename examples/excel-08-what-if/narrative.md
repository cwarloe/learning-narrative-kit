# What Davenport Has to Sell

*Tamarack Feed & Supply Co. • Excel Module 8: Performing What-If Analyses • Hover over highlighted terms for course definitions.*

## The Number Ruth Didn't Have

The lease for the Davenport store was signed. The building had no propane dock, and the forecasting model had already been rerun once because of it. Now the bank that was financing the fixtures wanted to see one more number before it released the money: how much the store had to sell each month to stop losing money.

Ruth Halvorsen had a rough idea. Hank Pruitt had a better one, but he was closing the year. So in February Ruth asked Eli Mendez, whose eighth SAM module was what-if analysis, and whose workbooks Hank had started trusting.

## Sorting the Costs

[[what_if_analysis|What-if analysis]] meant changing inputs to see how they affected the results. Before Eli could change anything, he needed a model that showed how Davenport's costs behaved.

Hank gave him the budget lines, and the module gave him three kinds of expense.

A [[fixed_expense|fixed expense]] had to be paid no matter how much the store sold: the lease at $6,500 a month, the manager's and three full-time clerks' salaries, insurance, and the loan payment on the fixtures. Together they came to $34,000 a month.

[[variable_expenses|Variable expenses]] changed in proportion to sales. The biggest was the cost of the goods themselves. Across Tamarack's product mix, goods cost about 70 cents of every sales dollar, which left 30 cents.

A [[mixed_expense|mixed expense]] was part fixed and part variable. Utilities were the clearest one: a base of about $1,200 a month to heat and light the building, plus more as the store got busier and the doors stayed open later. Hank estimated that part at 1 percent of sales. Card processing fees were all variable. Part-time labor was mixed.

## Guessing

Eli built the profit formula: sales, minus variable costs, minus the variable part of mixed costs, minus fixed costs. Then he started typing numbers into the sales cell to see what happened. At $100,000, the store lost $6,200. At $150,000, it made $8,300. At $120,000, it lost $400.

That was [[trial_and_error|trial and error]]: change an input, watch the output, change it again. It worked, but every new question meant another round of guessing.

## Working Backward

[[goal_seek|Goal Seek]] reversed the process. Instead of trying sales numbers until profit came out to zero, Eli told Goal Seek to set the profit cell to 0 by changing the sales cell, and it worked backward to the answer: $121,379 a month.

That was the core of a [[cost_volume_profit_cvp_analysis|Cost-Volume-Profit (CVP) analysis]], which studied how expenses, sales volume, and profit related to each other. Hank called the same thing a [[break_even_analysis|break-even analysis]], because the question everyone actually asked was where the store broke even.

For the bank, Eli drew a [[cost_volume_profit_cvp_chart|CVP chart]]. Monthly sales ran across the bottom. One line showed total costs, starting at $35,200 for the fixed part even at zero sales and rising slowly. Another line showed revenue, starting at zero and rising faster. Where they crossed was the break-even point. To the left was a shaded area labeled "loss" and to the right "profit."

## A Table of Answers

The bank's loan officer asked the follow-up Eli had expected: what if margins were worse than 30 percent? Davenport would sell more feed than Tamarack's average store, and feed had thin margins.

Eli built a [[data_table|data table]], a range of cells showing the formula's results as one or more inputs varied. Down the left side he listed monthly sales from $90,000 to $160,000. Across the top he listed gross margins from 24 to 32 percent. Each cell in the grid showed the monthly profit for that combination. At a 26 percent margin, which was closer to a feed-heavy store, break-even moved to about $141,000 a month.

The forecast from the site-selection model, after the propane dock was cut, put Davenport's first-year sales at about $118,000 a month.

Ruth looked at the grid for a long time. "So we lose money the first year," she said.

"At most margins, yes. A little at 30 percent. More at 26."

"The bank's going to see that."

"The bank asked for it," Eli said.

## The Opening Shelves

The second job was smaller and harder. Davenport had about 6,000 square feet of sales floor and a $210,000 budget for opening inventory. Marcy Lund wanted to know how to split the floor and the money among eight product categories to get the most gross margin out of the opening stock.

That was a job for Solver, which looked for the best value of a target cell by changing other cells within limits. Eli set the target to maximize total gross margin. The changing cells were the square feet assigned to each category. The constraints were total floor space under 6,000, total inventory cost under $210,000, and minimums Marcy insisted on: no store opened without feed, fencing, and work clothes.

The model was linear. Each square foot of a category added the same amount of margin and the same inventory cost no matter how many square feet there were. So Eli used the [[simplex_lp_method|Simplex LP method]], Solver's method for simple linear problems. It found an answer in under a second.

## What the Reports Said

Solver offered three reports on a successful solution, and Eli generated all of them because Hank would ask.

The [[answer_report|answer report]] summarized the result: the original and final values of the target cell and changing cells, and the status of each constraint. It put a lot of floor space into generators and chainsaws, a modest amount into feed, and the minimum into work clothes.

Among the constraints, floor space was a [[binding_constraint|binding constraint]]: the solution used all 6,000 square feet, and floor space was what stopped it from finding more margin. The budget was a [[nonbinding_constraint|nonbinding constraint]]. The solution only spent $187,000 of the $210,000. The difference, $23,000, was the [[slack|slack]]: how far the solution was from hitting that limit.

The [[sensitivity_report|sensitivity report]] showed how the solution would change as the constraints changed. Each additional square foot of floor space would add about $41 of gross margin, and each additional dollar of budget would add nothing, because the budget wasn't binding. The [[limits_report|limits report]] showed the range each changing cell could move within while the other constraints still held.

Ruth read the sensitivity report and asked what more shelving would cost. Taller gondolas in the back half of the store would add the equivalent of 400 square feet. They cost $9,000.

## When It Wasn't Linear

Marcy didn't believe the linear model. Generators didn't sell in a straight line. The first twenty in a store would sell; the fortieth would sit there until next winter. Each additional square foot of a category was worth less than the one before.

Eli rewrote the margin formula with a curve that flattened as space grew. Simplex LP refused it, because the problem was no longer linear. He switched to the [[grg_nonlinear_method|GRG Nonlinear method]], for problems with nonlinear functions.

GRG used an [[iterative_process|iterative process]]: it started from an initial solution, the floor plan Eli typed in, and calculated better ones from there, step by step, until it couldn't improve. When Eli started it from Marcy's draft floor plan, it found a solution worth $612,000 in annual margin. When he started from an even split across categories, it found one worth $634,000.

The SAM module had warned about this. The first answer was a [[local_optimum|local optimum]], the best solution near where Solver started, not the best possible one. The [[global_optimum|global optimum]] was the overall best, and GRG couldn't promise to find it. Eli turned on Solver's Multistart option, which ran it from many different starting points, and the best answer came out at $637,000.

The vendors added one more wrinkle. Prairie Wire gave volume discounts in steps: below a certain number of rolls, one price, and above it, a lower one. The jump made the cost formula discontinuous, and GRG choked on it. Solver's [[evolutionary_method|Evolutionary method]], built for problems with discontinuous functions, handled it. It took four minutes and gave a slightly different answer every time Eli ran it.

## What Opened

The bank released the fixture money. The loan officer noted that the store would likely lose money in its first year and that Tamarack had disclosed it. Walt Brandvold said that was what the first year was for.

Ruth approved the taller gondolas. Marcy took the Solver's floor plan and changed it anyway, moving a third of the generator space to feed and animal health. Ranchers who came in for feed, she said, would come back for chainsaws, and ranchers who found the store full of generators wouldn't come back at all. Eli reran the model with her floor plan. It came in about $19,000 a year below the optimum.

He showed Marcy the number. She said she knew, and that the model didn't know Davenport.
