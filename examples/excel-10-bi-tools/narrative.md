# Davenport's First Month

*Tamarack Feed & Supply Co. • Excel Module 10: Analyzing Data with Business Intelligence Tools • Hover over highlighted terms for course definitions.*

## A Target on the Wall

The Davenport store opened on May 4. On May 5, Walt Brandvold asked how it was doing.

Ruth Halvorsen wanted a single workbook she could open every Monday that answered Walt's question the same way every time. She asked Eli Mendez to build it. He was ten weeks from finishing his course, and his tenth SAM module was on Excel's business intelligence tools.

## Tables That Fit Together

The data lived in four places. Sales came from the register system. Store information — address, square footage, opening date — was in a list Marcy Lund kept. Each store's lease terms were in a separate list Hank Pruitt kept, because Hank did not want lease terms in the same file as anything Marcy shared. Loyalty customers and their ZIP codes came from the loyalty system.

Copying them all into one sheet would mean the same store name typed four thousand times. Instead, Eli loaded the four tables into Excel's Data Model with Power Pivot and connected them, so the workbook behaved like one of the [[relational_databases|relational databases]] Dana Okafor had described in the spring: separate tables, each about one subject, joined through a common field.

In [[data_view|Data view]], Power Pivot showed each table on its own tab, row by row, so he could check that the data had loaded correctly. It mostly had. Republic was spelled two different ways in the sales table, and he fixed it at the source.

In [[diagram_view|Diagram view]], Power Pivot showed each table as a box with its field names and drew the connections between them as lines. Eli dragged Store ID from the sales table onto Store ID in Marcy's store list. Every sale belonged to one store, and every store had many sales.

The connection between Marcy's store list and Hank's lease list was different. Each store had exactly one lease, and each lease belonged to exactly one store. That was a [[one_to_one_relationship|one-to-one relationship]]. Eli asked Hank why the two lists weren't one table, since they matched row for row. Hank said they matched because he kept them separate, and he would like to keep it that way.

## The Number That Mattered

Ruth's question for Davenport was simple: was the store on pace to break even by the end of its first year? Eli's what-if model from February had put break-even at about $121,000 a month in sales, and the site model expected about $118,000.

He set up a [[key_performance_indicator|key performance indicator]] in Power Pivot, a measurement tied to a specific goal. The KPI compared Davenport's sales to date against a monthly target that ramped up toward $121,000 by month twelve, with a status icon: green if ahead, yellow if within 10 percent, red if further behind.

Davenport's first month came in at $94,000 against a month-one target of $98,000. Yellow.

## Where the Customers Were

Walt wanted to see where Davenport's customers came from. Eli used map charts, which drew counties on a map and colored them from the data.

A [[value_map|value map]] colored each region on a gradient by a number. Eli mapped Davenport's first-month sales by the customer's county. Lincoln County was dark, as expected. Spokane County was also darker than anyone expected: a lot of Davenport's first-month customers were people who had been driving into Spokane for years and lived closer to Davenport.

That raised a question for Ruth, and Eli made a second map. A [[category_map|category map]] colored regions by category instead of value, every region in the same category getting the same color. He colored each county by which Tamarack store had the most loyalty customers there. Before May, the western half of Lincoln County was the Spokane Valley store's color. In the May data, it had switched to Davenport's.

"So some of those sales are ours already," Ruth said. "They just moved."

Eli checked. About a fifth of Davenport's first-month sales came from loyalty customers who had shopped at Spokane Valley the year before. Spokane Valley's May sales were down about the same amount.

## The Wrong Republic

Walt also asked for sales per person in each county, which needed population. Eli tried [[linked_data_types|linked data types]], which connected a cell to information online. He typed each county and town name and converted them to the Geography data type. Excel looked them up and returned fields he could pull into the sheet: population, area, and more.

It worked for counties. For towns, it got Republic, Washington, confused with Republic, Missouri, which had many times as many people, and Eli only noticed because sales per person in Republic came out absurdly low. He selected the right Republic from the list of matches, then checked the other ten towns by hand. Davenport itself had matched the one in Iowa.

## Monday

Ruth opened the workbook on the first Monday in June and showed Walt the yellow KPI, the two maps, and the one-fifth that had moved from Spokane Valley.

Walt asked whether Davenport was growing the business or just moving it. Ruth said both, and that it was too early to say in what proportion. Walt said he wanted the KPI to show only sales from customers who were new to Tamarack. Eli said that would make it red. Walt said then it should be red.

Eli rebuilt the KPI that week to count only new customers. It turned red.
