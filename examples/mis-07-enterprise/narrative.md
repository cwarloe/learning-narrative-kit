# Chick Days

*Tamarack Feed & Supply Co. • MIS Module 7: Enterprise Systems • Hover over highlighted terms for course definitions.*

Every spring, for four weeks, Tamarack Feed & Supply sold baby chicks. They came from a hatchery in the Willamette Valley by overnight truck every Tuesday, in ventilated boxes of fifty, and they could not wait. A box of chicks that arrived at a store with nobody ready for it had perhaps a day.

Chick Days was also the busiest four weeks of the year for feed, heat lamps, waterers, and brooder bedding, which meant it was the four weeks when every weakness in how Tamarack ordered things showed up at once.

The second Tuesday of this year's Chick Days, the Republic store received four hundred chicks it had not ordered and the Spokane Valley store received a hundred it had ordered three hundred of. The hatchery had swapped the two stores' order lines. The driver had unloaded what the manifest said.

Dana Okafor spent the morning on the phone with both store managers while Ruth Halvorsen tried to find a van.

* * *

That afternoon, Ruth asked Dana to draw how a chick got from the hatchery to a customer's backyard, with every handoff. Dana drew it on the conference-room whiteboard and kept running out of room.

The [[supply_chain|supply chain]] for Chick Days was the hatchery, a trucking company, the DC, eleven stores, the feed mill that made chick starter, two heat-lamp suppliers, and a bedding wholesaler. Every one of them was a separate company, and they were coordinated by phone calls, emails, a fax machine at the hatchery, and Marcy Lund's memory.

[[supply_chain_management_scm|Supply chain management]] was supposed to be the practice of working with those partners to improve how goods got delivered. At Tamarack, it was mostly reacting.

The feed mill was the exception. Tamarack and the mill had exchanged orders, confirmations, and invoices through [[electronic_data_interchange_edi|electronic data interchange]] for five years, computer to computer, in a standard format, with nobody retyping anything. Feed orders never got swapped between stores. Chick orders did, because the hatchery took them by fax.

While Dana was still drawing, the feed mill's account manager called Ruth. She had been pushing an idea for a year, and Chick Days gave her an opening. She proposed [[collaborative_planning_forecasting_and_r|collaborative planning, forecasting, and replenishment]]: Tamarack would share its point-of-sale data for chick starter and grower feed with the mill daily, and the two companies would plan production together. The mill would see sell-through as it happened instead of guessing from Tamarack's orders, and would stop making too much or too little.

Marcy didn't like sharing sales data with a supplier who also sold to Northland. Ruth asked what the alternative was. Marcy said the alternative was the mill running out of chick starter in week three, as it had last year. They agreed to a pilot on chick feed only.

Teo Vasquez added one piece. The DC had started a small trial of [[radio_frequency_identification_rfid|RFID]] tags on feed pallets: a chip and an antenna on each pallet that gave it a unique ID a reader could pick up without line of sight. If the pallets of chick starter were tagged, the mill could see when they left the DC, not just when they sold.

Walt Brandvold came into the conference room at four, looked at the whiteboard, and asked the question Dana had been hoping someone would ask.

"Why do we have six systems for this?"

Because Tamarack had bought a register system for selling, an accounting package for paying, a spreadsheet for ordering, and a loyalty program for marketing, at different times and from different vendors, and none of them knew about the others. What Walt was asking for was an [[enterprise_system|enterprise system]]: one application that served every function in the business and supported decisions across all of it.

The specific kind every consultant would sell him was [[enterprise_resource_planning_erp|enterprise resource planning]]. An ERP would collect and process data and coordinate resources across purchasing, inventory, sales, accounting, and HR in one integrated system with one database. When the hatchery's order was entered, the store, the DC, and accounting would all see the same thing.

"Then let's buy one," Walt said.

Ruth asked Dana to get three quotes and a realistic timeline. Dana had already looked at timelines for companies Tamarack's size. They ran twelve to eighteen months.

The swapped order had a second set of victims: the customers. Republic sold out of the chicks it did get by ten in the morning, and the store manager estimated he had turned away forty families, some of whom had driven an hour.

Those customers had reserved chicks by phone, and the reservations were written on a clipboard. Tamarack's [[customer_relationship_management_crm|customer relationship management]] was the loyalty program plus that clipboard. A proper CRM would track every contact with a customer — the reservation, the call when the order went wrong, the coupon to make up for it — and use that history to serve them and market to them.

Marcy wanted something more specific for the web store. Online, customers could already choose their own mix of breeds and add a starter kit, a kind of [[customization|customization]] where the customer modified the standard offering themselves. What Marcy wanted was [[personalization|personalization]]: the store designing what it offered around each customer's preferences and history, so a returning customer who raised meat birds saw meat-bird breeds and broiler feed first.

The web store vendor's way of doing that was [[collaborative_filtering_cf|collaborative filtering]]: grouping customers by shared interests and recommending what others in the group had bought. Customers who bought chicks bought heat lamps. Customers who bought ducklings bought a particular waterer. The vendor could also pull in data from partners, including the hatchery's breed sales.

Teo raised notifications. Customers currently had to check the website or call the store to find out whether chicks had arrived, which was [[pull_technology|pull technology]]: the customer had to ask first. He proposed [[push_technology|push technology]] instead: customers who signed up would get a text the moment their store's shipment was checked in. Marcy liked it. Hank Pruitt asked what it cost per text.

## The Man Who Knew How Many Ducks

When Chick Days ended, Ruth drove up to Republic to see the store manager, Arlo Nygaard, who was retiring in June after thirty-one years. Arlo was the one person at Tamarack who knew, without looking, how many of each breed to order for his store, which ones sold out first, which week the ducklings should come, and which local 4-H families would want what.

None of that was written down. Ruth wanted it to be before he left.

That was [[knowledge_management_km|knowledge management]]: converting the tacit knowledge in Arlo's head into explicit knowledge the next manager could use, and building a culture where people shared what they knew instead of guarding it. Arlo was willing. He was also busy, and what he knew came out as stories, not rules.

Dana set up the tools for it, mostly ones Tamarack already paid for and didn't use. Their [[collaboration_system_or_collaboration_so|collaboration software]] gave every store manager one shared workspace for Chick Days. Its [[communication_software|communication software]] ran a fifteen-minute video call every Tuesday morning before the truck came in. A [[document_and_content_management_software|document and content management]] library held one shared order sheet instead of eleven versions in eleven inboxes. [[task_management_software|Task management software]] tracked the hatchery's cutoff dates and assigned each one to a person.

Arlo recorded two video calls about his ordering before he said he didn't have time for a third.

Back at head office, heat lamps were the other bottleneck. Two suppliers had shorted Tamarack in week one.

Marcy tried something new for next year's order. She posted the specification on a [[reverse_auctions|reverse auction]] platform: one buyer, many sellers, each seller bidding down, with Tamarack free to choose the lowest acceptable price. Seven suppliers bid. The lowest bid was from a company nobody had heard of, and Marcy picked the third-lowest, from a supplier she'd used before, and explained to Hank why.

She also joined an agricultural [[e_marketplace|e-marketplace]], a third-party exchange where farm-supply buyers and sellers traded online, mostly to find a backup bedding supplier.

And the eighty brooder kits left over from a supplier's overshipment last year finally left the DC through an [[online_auction|online auction]], which reached buyers in four states and sold them for more than Marcy had expected.

* * *

The swapped order never fully recovered. Ruth found a van, but by the time it reached Republic, the store had already sold some of the extra chicks at walk-in prices, and the Spokane Valley store was left with a short supply for its reservations. Spokane Valley called its reservation customers one by one to apologize. Sixty chicks that nobody had reserved were sold at a discount to a small farm near Cheney.

The hatchery agreed to take Tamarack's orders through the feed mill's EDI connection next year, for a setup fee. The CPFR pilot with the mill started in May. The push notifications went into next year's budget.

Walt approved an ERP selection project and gave it a twelve-month deadline, which nobody who had read Dana's timeline believed. Arlo retired in June. His replacement watched both of the recorded calls and then called him at home in July to ask about ducklings.
