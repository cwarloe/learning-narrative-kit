# Where the Twelfth Store Goes

*Tamarack Feed & Supply Co. • MIS Module 8: Supporting Decisions and Processes • Hover over highlighted terms for course definitions.*

Walt Brandvold came back from a fishing trip with a napkin. On it, in his handwriting, was the word "Sandpoint" and an underline.

"Twelfth store," he told Ruth Halvorsen on Monday morning. "Jim Sorensen says there's nobody up there selling feed worth a damn. He's got a building he'd lease us."

Ruth had been asked to open a twelfth store within eighteen months, and she had a list of four candidate towns. Sandpoint was on it. So were Davenport, Newport, and Ritzville. She had not intended to decide by napkin.

She asked Dana Okafor to come up with a way to decide that Walt would accept, which Dana understood to mean a way that would let him keep the napkin if the answer turned out to be Sandpoint.

Walt's first idea was that the computer should decide. "Teo's system orders feed by itself," he said. "Give it the four towns and let it pick."

Dana pulled up the reorder screen, because Walt trusted things he had seen work. Reordering bagged feed was a [[structured_decisions|structured decision]]: it came up every week, and it had a standard procedure. When stock fell below a reorder point, the system ordered a set quantity. Someone had written that rule once, and it had run ever since.

"So write one for stores," Walt said.

"From what? We've never had to pick a town twice."

"Ruth's staffing sheet does clerks."

"Half of it does," Dana said. The sheet worked out each store's clerks from sales history, and then every manager changed it, because the sheet didn't know the high school's spring break took two clerks away. Staffing was a [[semistructured_decisions|semistructured decision]]: a part the computer could calculate and a part somebody had to know. Where to put a twelfth store was an [[unstructured_decisions|unstructured decision]]. It happened once, and there was no procedure for it at all.

Walt thought about that. "So the computer does the pieces."

"The pieces it has numbers for."

Ruth laid out the process in four phases, because the consultant she'd once worked with had, and because it kept people from skipping to the end.

The [[intelligence_phase|intelligence phase]] meant looking at the environment for the conditions that needed a decision and gathering data from inside and outside the company. Dana pulled loyalty customer addresses from all eleven stores, and Teo Vasquez loaded them into a [[geographic_information_system_gis|geographic information system]] along with county agricultural census data, competitor locations, and highway drive times. The map showed something nobody had expected: Tamarack already had more than four hundred loyalty customers in Lincoln County who drove past Davenport to shop in Spokane, an hour each way.

Sandpoint had fewer existing customers and more horse owners. Newport had a competitor already. Ritzville was mostly wheat farms with little livestock.

The [[design_phase|design phase]] meant defining criteria, generating alternatives, and connecting the two. Ruth's criteria were drive time from the DC, existing customer density, livestock numbers, competitor distance, and lease cost. The four towns were the alternatives, plus a fifth that Dana added — not opening a store, and adding a delivery route instead — which Walt found irritating.

## The Tool Three People Built

Over the next three weeks, Ruth had a consultant set up a [[decision_support_system_dss|decision support system]]: an interactive system with data, models, and a user interface, built for one kind of problem. Its database held the map data and Tamarack's store sales. Its [[model_base|model base]] held a sales forecasting model that estimated a new store's first three years from the demographics around it and the performance of similar Tamarack stores.

Three people built it, and they kept getting in each other's way.

Ruth acted as the [[managerial_designer|managerial designer]]. She decided what management needed from the tool: comparing five alternatives on the same criteria, with first-year revenue and payback period. She didn't care how it was built.

Teo acted as the [[technical_designer|technical designer]]. He cared about exactly the things Ruth didn't: where the data was stored, who could log in, how fast it ran, and whether customer addresses were safe in a consultant's cloud account. That was where they collided.

"I need the addresses," Ruth said. "That's how we found the people driving past Davenport."

"You need to know how many people drive past Davenport," Teo said. "You don't need to know which ones. If Corinne's account gets breached, I don't want four hundred customers' home addresses in it."

"That's a technical question."

"That's why it's mine."

They settled on ZIP code counts. The addresses stayed on Tamarack's network, and the map got less precise.

The consultant, a former regional planner named Corinne, acted as the [[model_builder|model builder]]. Her job was to explain what the forecasting model did, what inputs it accepted, how to read its output, and what it assumed. Its biggest assumption was that a new store would perform like the most similar existing store. Davenport's most similar store was Colville. Sandpoint's most similar store didn't exist; Tamarack had never had a store in a town with that many weekend horse owners and vacation homes.

"So the Sandpoint number is weaker," Ruth said.

"The Sandpoint number is a guess with decimals," Corinne said. Dana wrote that one down.

Walt did not want to run the DSS. He wanted to look at it.

Corinne built him a view in the company's [[executive_information_systems_eiss|executive information system]], which already showed him weekly sales. It had a [[digital_dashboard|digital dashboard]] up top, a single page of charts pulling from several sources: the five alternatives side by side, their projected first-year sales, and their payback periods. From there he could drill down: click Davenport, see the customer map; click the map, see the ZIP codes; click a ZIP code, see the livestock census.

Walt clicked through it for twenty minutes and came out convinced. "Sandpoint holds up," he said. "I went all the way down to the ZIP codes."

"Those are the census numbers," Corinne said. "They're real. The dashboard shows you what the model concluded and the data underneath it. It doesn't show you what the model assumed."

"Which is?"

"That Sandpoint will sell like whatever store it most resembles. And it doesn't resemble any of them." The assumption lived in the model base, two layers below anything Walt could click.

Ruth told Dana afterward that the EIS, the DSS, and the reorder system were all one family of things, the [[management_support_systems_msss|management support systems]], each built to support one kind of decision. The trouble with the family, Ruth said, was that the one Walt saw most was the one with the least model behind it.

* * *

The [[choice_phase|choice phase]] came on a Thursday. Davenport led on every criterion except lease cost. Its payback period was under three years. Sandpoint's was five, with the widest error range of the five. The delivery route came in second, which Walt said proved the model was broken.

He went back to Sandpoint one more time. Then he asked Corinne what would have to be true for Sandpoint to win. She ran it: Sandpoint's horse owners would have to spend like Colville's ranchers. Walt said that was possible. Corinne said it was possible.

Walt chose Davenport. He also asked that Sandpoint stay on the dashboard as a comparison, so that if Davenport underperformed, everyone would see what they'd passed up.

The [[implementation_phase|implementation phase]] meant turning the choice into a plan and getting the resources for it. It went wrong quickly.

The building in Davenport that had driven the lease-cost number belonged to an estate, and the estate's heirs took six weeks to agree on terms and then disagreed. The second site had a smaller lot with no room for a propane dock, which the model had assumed. Corinne reran the numbers without propane. Payback moved from under three years to almost four, and Sandpoint, still on Walt's dashboard, looked closer than it had.

Ruth signed the second lease anyway. Jim Sorensen called Walt to ask what happened to Sandpoint, and Walt told him to give it a year.
