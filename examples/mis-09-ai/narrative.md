# The Counter Assistant

*Tamarack Supply • MIS Module 9: Artificial Intelligence and Automation • Hover over highlighted terms for course definitions.*

## The Question at the Counter

A woman came into the Chewelah store in May with a photo of a goat on her phone and asked the clerk which dewormer to buy. The clerk had worked at Tamarack for three weeks. He pointed her to the one with the most shelf space.

It was a cattle product. The dose for a forty-pound goat was not on the label, the woman guessed, and the goat was sick for two days. She came back to complain, and the Chewelah manager called Ruth Halvorsen, and Ruth called Dana Okafor into her office and closed the door.

"Arlo used to answer those," Ruth said. "Arlo's gone. Half our counter people have been here less than a year. What do we do?"

Dana had a vendor pitch in her inbox that was exactly about this, and she had been ignoring it because it said "AI" eleven times on the first page.

## What the Vendor Was Selling

The vendor's product was called Counter Assistant. It was sold as [[artificial_intelligence_ai|artificial intelligence]] for farm-supply retail, which on the demo call turned out to mean several different technologies in one box.

The core was an [[expert_systems|expert system]]: software that mimicked a human expert in one well-defined area, in this case livestock health products. It had three main parts, and the vendor's engineer drew them for Dana and Teo Vasquez on a shared screen.

The [[knowledge_base|knowledge base]] was like a database, but besides facts — product names, active ingredients, approved species — it held rules: if the animal is a goat, and the product is labeled for cattle only, then do not recommend without a veterinarian's instruction. The [[inference_engine|inference engine]] was the part that applied the rules to a question, the way a DSS's model base applied models to data. And the [[explanation_facility|explanation facility]] told the clerk why it had recommended what it did, in plain language, so the clerk could tell the customer.

"That last part is the one I care about," Dana said. "If it just says 'buy this,' the clerk learns nothing and we're liable for whatever it says."

## Two Ways to Reason

The engineer ran two demos to show how the inference engine worked.

In the first, a clerk entered what they knew: goat, adult, about forty pounds, visible weight loss, pale gums. The engine used [[forward_chaining|forward chaining]], running through its if–then rules one condition at a time from the facts toward a conclusion. It ended at: possible barber pole worm; recommend a goat-labeled product from this list; recommend a fecal test through a vet; do not recommend the cattle product.

In the second, the clerk started from a product: can this customer use this dewormer on her goat? The engine used [[backward_chaining|backward chaining]], starting from the goal and working back to see which facts would have to be true for the answer to be yes. It asked the clerk two questions — is the goat lactating, and does the customer have a vet's prescription for off-label use — and when both answers were no, it said no.

The rules couldn't handle everything crisply. "Heavy" infestation, "young" animal, "thin" body condition were not yes-or-no facts. The system used [[fuzzy_logic|fuzzy logic]] for those, treating a goat as, say, seventy percent "thin" rather than forcing a yes or no, so the clerk could enter what they saw in ordinary words.

## Who Keeps the Rules Right

Teo's question was the one Dana hadn't thought to ask. "Who updates it when a product label changes?"

The vendor had two answers. A [[knowledge_base_management_system_kbms|knowledge base management system]] kept the knowledge base updated as facts and rules changed, the same way a DBMS kept a database updated. A [[knowledge_acquisition_facility|knowledge acquisition facility]] was how new rules got in: a veterinarian or the vendor's staff could add rules through a guided form, and the system would check them against the ones it already had.

The rules came from the vendor's veterinarians, who were in Iowa. Ruth wanted a local vet to review them. The vendor said that was fine and would cost extra.

The system also kept a [[case_based_reasoning_cbr|case-based reasoning]] library, a database of past questions and how they were resolved. When a new question came in, it looked for a similar solved case first. If it found no match, even after asking for more details, it told the clerk to call a person. Dana liked that it admitted when it didn't know.

## Assist, Don't Replace

Walt Brandvold sat in on the second call. He wanted to know whether Counter Assistant meant he could hire fewer experienced counter people.

Dana had prepared for that question. The vendor's own contract said the product was [[augmented_intelligence|augmented intelligence]]: it was there to support the clerk's decision, not make it. Every recommendation had to be confirmed by a person, and the explanation had to be shown to the customer. Hank Pruitt, who had read the liability section, said that was the only reason their insurer would allow it.

Walt said he'd been hoping for the other kind.

## The Rest of the Pitch

The vendor's sales rep, sensing a big customer, pitched everything else in the catalog.

For the web store, a chat assistant using [[natural_language_processing_nlp|natural-language processing]], so customers could type "what do I feed ducklings" and get an answer in ordinary language. Marcy Lund liked the idea and asked who would review its answers.

For forecasting, a demand model built on [[machine_learning|machine learning]], which learned from three years of sales history without anyone writing the rules. Underneath, it used [[artificial_neural_networks_anns|artificial neural networks]], networks that learned patterns conventional programs struggled with, including seasonal ones a spreadsheet would miss. Teo ran a trial on chick-starter sales. It did well until a late May cold snap, which wasn't in the history, and then badly for three weeks.

For propane delivery routes, a route optimizer using [[genetic_algorithms_gas|genetic algorithms]]: it generated hundreds of possible routes, kept the best, combined and mutated them over many generations, and converged on routes that were shorter than the ones the dispatcher built by hand. The dispatcher said the optimizer didn't know which roads washed out in March.

For the DC, the rep had a video of a palletizing [[robots|robot]] stacking feed bags, the kind of repetitive, heavy work that injured people's backs. Eli Mendez, the DC's shift lead, watched it twice. He said his crew could use it on the forty-pound bags and that it would never handle the torn ones. The rep had an answer for that too: a [[soft_robot|soft robot]] gripper made of elastomer, cheaper and gentler than a metal one, that could pick up a bag that had started to split. The price was not cheap.

## The Agents Already Running

Dana's report to Ruth included a section the vendor hadn't asked for, because while she was researching, she realized Tamarack was already running AI and hadn't called it that.

[[intelligent_agents|Intelligent agents]] — software that reasoned and followed rules on someone's behalf — were all over the company. The new NAS sent alerts from [[monitoring_and_surveillance_agents|monitoring and surveillance agents]] that watched disk health and network traffic to predict failures before they happened. Marcy used [[shopping_and_information_agents|shopping and information agents]] that crawled competitors' websites every morning and told her where Northland had cut prices.

And every employee's email client had a [[personal_agents|personal agent]] that remembered addresses and finished them after the first few letters. After the payment fraud in March, Teo found that Hank's email client still suggested the attacker's look-alike address first when he typed the seed company's name, because Hank had replied to it twice. Teo deleted it from the suggestion list on every machine in accounting.

## What They Bought

Ruth approved Counter Assistant for livestock health products only, in three stores, with a local vet reviewing the rules first. The vet's review took six weeks and found nineteen rules she disagreed with, mostly about sheep. The vendor accepted fourteen of the changes and said the other five were consistent with label guidance. The vet said label guidance was the problem. That argument was still going on when the pilot started.

The demand forecasting stayed a trial. The route optimizer was approved for one truck so the dispatcher could compare. The palletizing robot went into the capital request for next year, and the soft gripper was cut from it.

The Chewelah clerk who had pointed the woman at the cattle dewormer was the first to be trained on Counter Assistant. In his first week he overrode it twice, both times correctly, and both times the system logged his override as an error.
