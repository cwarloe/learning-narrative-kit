# The Counter Assistant

*Tamarack Feed & Supply Co. • MIS Module 9: Artificial Intelligence and Automation • Hover over highlighted terms for course definitions.*

A woman came into the Chewelah store in May with a photo of a goat on her phone and asked the clerk which dewormer to buy. The clerk had worked at Tamarack for three weeks. He pointed her to the one with the most shelf space.

It was a cattle product. The dose for a forty-pound goat was not on the label, the woman guessed, and the goat was sick for two days. She came back to complain, and the Chewelah manager called Ruth Halvorsen, and Ruth called Dana Okafor into her office and closed the door.

"Arlo used to answer those," Ruth said. "Arlo retires in June. Half our counter people have been here less than a year. What do we do?"

Dana had a vendor pitch in her inbox that was exactly about this, and she had been ignoring it because it said "AI" eleven times on the first page.

## The Demo Call

The vendor's product was called Counter Assistant. Dana and Teo Vasquez took the demo call that Thursday from the small conference room, with the vendor's engineer sharing his screen. It was sold as [[artificial_intelligence_ai|artificial intelligence]] for farm-supply retail, which on the demo call turned out to mean several different technologies in one box.

The core was an [[expert_systems|expert system]]: software that mimicked a human expert in one well-defined area, in this case livestock health products. It had three main parts, and the vendor's engineer drew them on the shared screen.

The first box was the [[knowledge_base|knowledge base]].

"So it's a database of answers," Teo said. "The clerk types 'goat' and it looks up 'goat.'"

"A database would give you every dewormer that mentions goats," the engineer said. "This has the facts, product names and active ingredients and approved species, and it keeps rules on top of them." He typed one into the box: *if the animal is a goat and the product is labeled for cattle only, then do not recommend without a veterinarian's instruction.* "A lookup can't tell your clerk not to sell something. A rule can."

The second box was the [[inference_engine|inference engine]], the part that applied the rules to a question, the way a DSS's model base applied models to data. The third was the [[explanation_facility|explanation facility]], which told the clerk how the system had reached its recommendation, in plain language, so the clerk could tell the customer.

"That last part is the one I care about," Dana said. "If it just says 'buy this,' the clerk learns nothing and we're liable for whatever it says."

He ran two demos to show how the inference engine worked.

In the first, a clerk entered what they knew: goat, adult, about forty pounds, visible weight loss, pale gums. The engine used [[forward_chaining|forward chaining]], running through its if–then rules one condition at a time from the facts toward a conclusion. It ended at: possible barber pole worm; recommend a goat-labeled product from this list; recommend a fecal test through a vet; do not recommend the cattle product.

"Why would you ever run it backwards?" Dana asked. "That got the right answer."

"Because that's not how the question usually comes in," the engineer said. "Half your customers walk up already holding a bottle. They don't want a diagnosis. They want to know if this one is okay."

In the second demo the clerk started from the product: can this customer use this dewormer on her goat? The engine used [[backward_chaining|backward chaining]], starting from the goal and working back to see which facts would have to be true for the answer to be yes. It asked the clerk two questions, whether the goat was lactating and whether the customer had a vet's prescription for off-label use, and when both answers were no, it said no.

"The first one asked about everything," the engineer said. "This one only asked what it needed to answer the question she brought in."

The rules couldn't handle everything crisply. "Heavy" infestation, "young" animal, "thin" body condition were not yes-or-no facts. The system used [[fuzzy_logic|fuzzy logic]] for those, treating a goat as, say, seventy percent "thin" rather than forcing a yes or no, so the clerk could enter what they saw in ordinary words.

Teo's question was the one Dana hadn't thought to ask. "Who updates it when a product label changes?"

The vendor had two answers. A [[knowledge_base_management_system_kbms|knowledge base management system]] kept the knowledge base updated as facts and rules changed, the same way a DBMS kept a database updated. A [[knowledge_acquisition_facility|knowledge acquisition facility]] was how new rules got in: a veterinarian or the vendor's staff could add rules through a guided form, and the system would check them against the ones it already had.

The rules came from the vendor's veterinarians, who were in Iowa. Ruth wanted a local vet to review them. The vendor said that was fine and would cost extra.

The system also kept a [[case_based_reasoning_cbr|case-based reasoning]] library, a database of past questions and how they were resolved. When a new question came in, it looked for a similar solved case first. If it found no match, even after asking for more details, it told the clerk to call a person. Dana liked that it admitted when it didn't know.

## The Second Call

Walt Brandvold sat in on the second call, a week later. He wanted to know whether Counter Assistant meant he could hire fewer experienced counter people.

Dana had prepared for that question. The vendor's own contract said the product was [[augmented_intelligence|augmented intelligence]]: it was there to support the clerk's decision, not make it. Every recommendation had to be confirmed by a person, and the explanation had to be shown to the customer. Hank Pruitt, who had read the liability section, said that was the only reason their insurer would allow it.

Walt said he'd been hoping for the other kind.

The vendor's sales rep, sensing a big customer, pitched everything else in the catalog.

For the web store, a chat assistant using [[natural_language_processing_nlp|natural-language processing]], so customers could type "what do I feed ducklings" and get an answer in ordinary language. Marcy Lund liked the idea and asked who would review its answers.

For forecasting, the rep had a demand model built on [[machine_learning|machine learning]].

"Who writes its rules?" Hank asked. The expert system's rules came from veterinarians in Iowa, and Ruth had already asked for a local vet to read them. Hank wanted to know who would be reading these.

"Nobody writes them," the rep said. "It learns them from your sales history. Three years of it." Underneath were [[artificial_neural_networks_anns|artificial neural networks]], networks that learned patterns conventional programs struggled with, including seasonal ones a spreadsheet would miss.

"Then what does the vet read?"

The rep said the model checked itself against what actually sold. Teo ran a trial on chick-starter sales. It did well until a late May cold snap, which wasn't anywhere in the three years, and then badly for three weeks. There was no rule to correct, because nobody had written one.

For propane delivery routes, the rep had a route optimizer built on [[genetic_algorithms_gas|genetic algorithms]].

"So it works out the best route," Walt said. "Checks them all and picks one."

"Nobody checks them all," the rep said. "Forty stops can go in more orders than there are seconds left in the century. It starts with a few hundred routes, most of them bad, keeps the shortest, and builds the next batch from those. Half of one good route spliced onto half of another. And now and then it swaps two stops at random."

"Why random?" Teo asked. "You'd think you'd want it to stick with what's working."

"That's how it gets stuck. If it only ever combines the routes it already has, it polishes one idea forever. Most random swaps make a route worse and get thrown out. Once in a while one finds a shortcut nobody would have tried, and that one gets bred."

Her slide named the three steps: selection, crossover, mutation. After a few hundred generations the routes stopped getting shorter, and on last winter's tickets they beat the ones the dispatcher built by hand on most days.

Teo had asked the propane dispatcher to listen in. He hadn't said anything yet.

"Does it know Wolfe Road washes out in March?"

The rep said it used the distances in the map data.

"Then it doesn't," the dispatcher said. "In March the shortest route has me pulling a truck out of the ditch."

For the DC, the rep had a video of a palletizing [[robots|robot]] stacking feed bags, the kind of repetitive, heavy work that injured people's backs. Eli Mendez, the DC's shift lead, watched it twice. He said his crew could use it on the forty-pound bags and that it would never handle the torn ones. The rep had an answer for that too: a [[soft_robot|soft robot]] gripper made of elastomer, cheaper and gentler than a metal one, that could pick up a bag that had started to split. The price was not cheap.

* * *

Dana's report to Ruth included a section the vendor hadn't asked for, because while she was researching, she realized Tamarack was already running AI and hadn't called it that.

[[intelligent_agents|Intelligent agents]] — software that reasoned and followed rules on someone's behalf — were all over the company. The new NAS sent alerts from [[monitoring_and_surveillance_agents|monitoring and surveillance agents]] that watched disk health and network traffic to predict failures before they happened. Marcy used [[shopping_and_information_agents|shopping and information agents]] that crawled competitors' websites every morning and told her where Northland had cut prices.

And every employee's email client had a [[personal_agents|personal agent]] that remembered addresses and finished them after the first few letters. After the payment fraud in March, Teo found that Hank's email client still suggested the attacker's look-alike address first when he typed the seed company's name, because Hank had replied to it twice. Teo deleted it from the suggestion list on every machine in accounting.

Ruth approved Counter Assistant for livestock health products only, in three stores, with a local vet reviewing the rules first. The vet's review took six weeks and found nineteen rules she disagreed with, mostly about sheep. The vendor accepted fourteen of the changes and said the other five were consistent with label guidance. The vet said label guidance was the problem. That argument was still going on when the pilot started.

The demand forecasting stayed a trial. The route optimizer was approved for one truck so the dispatcher could compare. The palletizing robot went into the capital request for next year, and the soft gripper was cut from it.

The Chewelah clerk who had pointed the woman at the cattle dewormer was the first to be trained on Counter Assistant. In his first week he overrode it twice, both times correctly, and both times the system logged his override as an error.
