# One Customer, Four Records

*Tamarack Supply • MIS Module 3: Data and Business Intelligence • Hover over highlighted terms for course definitions.*

## Four Envelopes in One Mailbox

Gordon Ashby ran cattle outside Republic and had been a Tamarack customer for thirty years. In April he walked into the Colville store holding four identical envelopes, each one a spring mailer with a twenty-dollar coupon for fencing supplies, each one addressed to him.

"Either you think I'm four people," he told the counter, "or somebody's going to try to use these."

The store manager scanned all four coupons into a photo and sent it to head office. By lunch it was on Marcy Lund's screen, and by one o'clock Marcy was in Dana Okafor's doorway.

The mailer was Marcy's project. It was the company's first real attempt at [[database_marketing|database marketing]]: using the loyalty program's list of customers to send each of them offers based on what they'd bought. Ranchers got fencing, backyard flocks got feed, people who'd bought a pressure washer in October got a coupon for a new one in April. It had cost eleven thousand dollars to print and mail, and Marcy now suspected some meaningful part of that had gone to Gordon's mailbox.

"How many Gordons do we have?" she asked.

## What a Customer Is, Physically

Dana pulled the loyalty export. It was a single [[database|database]] in the sense that it was a collection of related data in one place, but it had grown without anybody deciding what it should look like.

She walked Marcy through the [[data_hierarchy|data hierarchy]] because Marcy would have to defend the fix to Walt. A single piece of information, like a phone number, was a field. All the fields for one customer made a record. All the customer records together made the file. Gordon was four records in that file, with four slightly different spellings of the same ranch road and two different phone numbers.

"Why didn't the system catch it?" Marcy asked.

Because the system had never been told what made a customer unique. The loyalty software was built on the [[relational_model|relational model]]: tables of rows and columns, rows being records and columns being fields. In a relational design, every table needed a [[primary_key|primary key]], one field whose value was different for every record. The loyalty table's key was the loyalty card number, and every time a clerk couldn't find a customer at the register, they issued a new card. The key was unique. The customer wasn't.

The purchase table had the same problem from the other direction. Each purchase carried a [[foreign_key|foreign key]], the loyalty card number, which pointed back to one customer record. Gordon's fencing history was split across four cards, so the mailer logic saw four customers, each of whom had bought a moderate amount of fencing. All four qualified.

## The Old Program's Habits

Some of the mess was older than the current software. Teo Vasquez came by with the history.

Tamarack's first loyalty program, from 2009, had been run by a vendor that sent nightly files. It stored customers in a [[sequential_access_file_structure|sequential access file structure]]: records in the order they were entered, read from top to bottom. That was fine for printing a list once a month. It was terrible for a cashier trying to find one customer, so the vendor added an index and moved to an [[indexed_sequential_access_method_isam|indexed sequential access method]], which went straight to a record when you looked up one person and read in order when you ran a batch. The current system used a [[random_access_file_structure|random access file structure]] for the lookups, which was why the register could find a card number instantly.

The duplicates came from the migration. The 2009 vendor's export had been arranged in a [[hierarchical_model|hierarchical model]]: each store at the top, customers underneath as children, purchases underneath them. Every record had one parent. A rancher who shopped in both Colville and Kettle Falls had to appear twice, once under each store. The current system was relational and could have had one Gordon linked to two stores, but the migration had simply loaded every child it found.

"The [[network_model|network model]] would have fixed that," Teo said, "if anybody had used it in 2014. One customer record, multiple parent stores." He shrugged. "Nobody did."

## Who Gets to Delete a Person

The obvious fix was to merge duplicates. The less obvious question was who was allowed to.

Tamarack had no [[database_administrator_dba|database administrator]]. In a larger company a DBA would have designed the tables, set security, owned the recovery procedures, and decided what the stores could change. At Tamarack, Teo did those things when nothing else was on fire.

Dana opened the permissions screen in the [[database_management_system_dbms|database management system]], the software that actually stored and served the tables. Store clerks had full [[create_read_update_and_delete_crud|CRUD]] rights on customers: create, read, update, and delete. They could merge records, and they could also delete them, and the log showed a handful of deletions every week with no explanation.

"So we take away delete," Marcy said.

"And update?" Dana asked. "Half the duplicates are a clerk who couldn't find someone, so they made a new card. If they can't update an address, they'll make a new card every time somebody moves."

They settled on create and read for the stores, update with a supervisor's PIN, and delete reserved for head office. Two store managers called within a day to say this was slower.

Dana also wrote the first real [[data_dictionary|data dictionary]] for the loyalty tables: what each field was, its data type, its default, and its validation rules. Phone numbers would be ten digits, no dashes. The ranch-road field would get a pick list for the twelve roads that accounted for most of the misspellings. Nobody would read the dictionary, Teo said, but the validation rules would read it for them.

## Finding the Duplicates

Marcy wanted a list of every probable duplicate by Friday. Dana wrote it in [[structured_query_language_sql|SQL]]: select customers grouped by last name and phone number where the count was more than one, then a second pass on last name and street.

Marcy didn't read SQL. She built her own version in the reporting tool using [[query_by_example_qbe|query by example]], clicking fields into a grid and adding an OR row for "same phone or same address." Hers found 212 more possible matches than Dana's. Most were real. Eleven were families: a father and son with the same name on the same ranch, a mother and daughter-in-law sharing a phone.

That was the thing about [[normalization|normalization]] that Dana found hardest to explain. Normalizing the customer table meant every fact lived in exactly one place, with no redundant copies to drift apart. But to do that you first had to decide what the facts were. Was the ranch the customer? The person? The household? The tables couldn't tell you that.

They also couldn't tell you how the data looked to the person using it. Marcy's [[logical_view|logical view]] was a list of customers with their history. The [[physical_view|physical view]] was a set of tables, index files, and a log on the server's disks. Most of the fight over Gordon happened because the two views didn't match.

## Walt Wants a Dashboard

Walt's interest arrived on Thursday, by way of a conference. He had sat through a session on [[business_intelligence_bi|business intelligence]] and come back wanting to see, on one screen, what had happened, what was happening, and what was going to happen, by store.

Dana drew it on the whiteboard for him and Ruth.

On the left were the systems that ran the business minute to minute. The register lanes were [[online_transaction_processing_oltp|online transaction processing]]: fast, real-time, internal, one sale at a time. The web store was a [[data_driven_web_site|data-driven Web site]], a front end that read from and wrote to a database every time a customer browsed or checked out. The loyalty tables sat alongside.

In the middle she drew [[extraction_transformation_and_loading_et|ETL]]: pull data out of each source every night, clean it, reshape it so a "store" meant the same thing everywhere, and load it.

On the right she drew the [[data_warehouse|data warehouse]], one place where all of it came together for decision-making instead of for running the registers. Hanging off it she drew a smaller box: a [[data_mart|data mart]] just for merchandising, which was all Marcy actually needed.

"And then what?" Walt asked.

Then [[online_analytical_processing_olap|OLAP]], which would let Marcy turn the data like a cube: fencing sales by store, by month, by product line, without writing a new report each time. Then a visualization tool. Teo had a trial of [[tableau|Tableau]] and had already built a map of feed sales by ZIP code that Walt liked so much he asked for a printout.

Ruth asked about the comment cards. Every store had a box of them, plus the web reviews. Dana suggested a [[data_lake|data lake]], a cheaper bucket that kept data in its raw form, structured or not, so they could ask questions of it later. [[text_mining_analysis|Text-mining analysis]] could pull themes out of thousands of comments. The free trial had already found that "propane" and "wait" showed up together a lot.

## What the Patterns Said

The trial ran for three weeks. [[data_mining_analysis|Data-mining analysis]] on the merged purchase history found a pattern Marcy hadn't known: customers who bought T-posts in March bought mineral feed within six weeks at almost twice the normal rate. The vendor's [[data_mining_agents|data-mining agents]], small programs that ran against the warehouse looking for relationships nobody had asked about, flagged it on their own.

Marcy wanted to act on it. That was the step from BI to [[business_analytics_ba|business analytics]]: not just seeing what happened, but using statistics to decide what to do. She built a test: a mineral coupon in the bag with every T-post order in two stores, none in two others.

## The Parts Nobody Asked About

Three other decisions got made that month because the warehouse forced them.

The stores lost internet a few times a year, usually in winter. Teo proposed a [[distributed_database_management_system_d|distributed database]] so each store kept working on its own server and synced later. The question was how. Full [[replication|replication]] put a copy of everything at every store, which was simple and used a lot of disk. [[fragmentation|Fragmentation]] split the tables, so the Colville server held only Colville's rows. Teo picked [[allocation|allocation]], a mix of the two: each store kept its own customers and transactions plus a copy of the product catalog, which it used constantly.

The web store's vendor ran an [[object_oriented_databases|object-oriented database]]. In it, a product was an [[object|object]] that held its own data and its own procedures, like how to calculate its shipping weight. Every product came from a [[class|class]] that defined its format and behavior. A propane tank was a new class built from the general product class through [[inheritance|inheritance]], with a few extra attributes for hazmat rules. All of it was bundled together through [[encapsulation|encapsulation]], which was why the vendor could add product photos and spec sheets without touching anything else. It also meant Dana couldn't query it with SQL, and the nightly ETL job had to go through the vendor's export.

A different vendor pitched a [[graph_database|graph database]] for household relationships, with customers as nodes and "same household" or "same ranch" as edges. It would have solved the Gordon problem properly. It cost more than the mailer.

Finally, because the warehouse vendor would hold customer names, addresses, and phone numbers, Hank insisted on [[data_encryption|data encryption]] in transit and at rest. The vendor charged extra for it.

## What It Cost

The merge ran on a Saturday. It collapsed 1,940 duplicate cards into 811 customers, including Gordon, who went from four cards to one and was mailed a single apology letter with one coupon.

It also merged Dale Hollister Sr. and Dale Hollister Jr., who ran different operations from the same mailing address and did not speak to each other. Dale Jr. found out when his points balance doubled. Splitting them back apart took Dana most of a day, because the [[data_model|data model]] had no way to say "same address, different customer" and she had to add a field to do it.

Walt approved the merchandising data mart and declined the full warehouse until next fiscal year. Marcy's mineral-feed test was still running. The spring mailer went out again to the corrected list, two weeks late, after most of the fencing season had started.
