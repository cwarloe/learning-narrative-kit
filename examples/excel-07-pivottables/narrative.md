# Did the Coupon Work?

*Tamarack Feed & Supply Co. • Excel Module 7: Summarizing Data with PivotTables • Hover over highlighted terms for course definitions.*

## Walt's One Question

In the spring, Marcy Lund had started a test: a coupon for mineral feed went into the bag with every T-post order at two stores, and two other stores got no coupon. In January, Walt Brandvold remembered it and asked her one question in the hallway. "Did it work?"

Marcy had the data: every sale at all four stores from March through September, about 61,000 rows, in an Excel table. She asked Eli Mendez to help her answer Walt by Friday, because Eli's seventh SAM module was on PivotTables and she had never built one.

## Building the Summary

Eli built a [[standard_pivottable|standard PivotTable]], a PivotTable summarizing data from an Excel table. He dragged Store into the rows, Product Category into the columns, and Sales into the values. Sixty-one thousand rows collapsed into a grid of four stores and twelve categories.

Marcy wanted to see the test the way she'd designed it. Eli added a Region field above Store in the rows: "Coupon" for the two test stores, "No coupon" for the two control stores. At the top level, the PivotTable showed just two rows. Mineral sales in the coupon stores were up 14 percent over the previous year. In the no-coupon stores, they were up 9 percent.

"So it worked," Marcy said. "Five points."

## Going Down and Back Up

Eli had learned to distrust a number that came that easily. He expanded the "Coupon" row, [[drilling_down|drilling down]] from the general view to the specific one, to see each store separately. Colville was up 22 percent. Chewelah was up 5. The average had hidden that the coupon worked very well in one store and barely at all in the other.

He drilled down again, from Colville to Colville's individual products. Almost all of Colville's mineral gain was one product, a loose mineral the store had started carrying in April. It had nothing to do with the coupon.

Then he went back the other way, [[drill_up|drilling up]] from products to stores to regions, so Marcy could see how the details summed to the headline number. The headline stayed the same. What it meant had changed.

## Narrowing It

Marcy wanted to see the result without the new loose mineral, to be fair to the test.

The PivotTable's filters could do that in several ways. [[manual_filters|Manual filters]] showed a check box for every unique value in a field, so Eli opened the Product filter and unchecked the loose mineral. It was one product out of 340, so check boxes worked.

For a broader cut, he used [[label_filters|label filters]], which filtered by the items' names. Marcy wanted every product with "mineral" in its name and nothing else. A label filter of "contains mineral" found all 23 of them.

Then [[date_filters|date filters]], which selected data by dates or date ranges. The coupon had only been in the bags from April 1 to June 30. Eli set a date filter for that range, so sales in March and the summer wouldn't dilute the comparison.

Last, Marcy asked which of the stores' customers had bought the most mineral. Eli put Customer in the rows and used [[value_filters|value filters]], which filtered on a numeric value elsewhere in the PivotTable. Top 10 customers by sum of sales. Eight of the top ten in the coupon stores had used the coupon.

With the loose mineral out and the dates narrowed, the coupon stores were up 8 percent and the others up 7.

## The Screenshot

On Wednesday night Marcy took a screenshot of the first version, the five-point gap, and sent it to Walt before Eli had finished. She wanted Walt to have something.

On Thursday Hank Pruitt noticed that the sales table was missing the last two weeks of September, which the stores had sent late. Marcy pasted them into the bottom of the table. The PivotTable didn't change. Eli had to [[refresh|refresh]] it, which updated the PivotTable to reflect changes to the underlying data. A PivotTable didn't recalculate on its own the way a formula did. After the refresh, the gap with the new mineral and dates excluded was still about one point.

## Friday

Marcy brought both versions to Walt on Friday: the screenshot from Wednesday, with its five points, and the refreshed, filtered one with its one point.

Walt asked which one was true. Marcy said the second one. Walt said that a one-point lift on a coupon that cost forty cents a bag was not nothing, and also not something he'd print another 20,000 of. He had already told two store managers about the five-point result. Marcy said she'd call them.

The coupon test was extended to all eleven stores for the spring, with the date filter set before the season started this time. Marcy asked Eli to build the PivotTable before the data came in, so she would only have to refresh it.
