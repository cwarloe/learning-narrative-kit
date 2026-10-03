# Where the Twelfth Store Goes

*Tamarack Supply • MIS Module 8: Supporting Decisions and Processes • Hover over highlighted terms for course definitions.*

## Walt's Napkin

Walt Brandvold came back from a fishing trip with a napkin. On it, in his handwriting, was the word "Sandpoint" and an underline.

"Twelfth store," he told Ruth Halvorsen on Monday morning. "Jim Sorensen says there's nobody up there selling feed worth a damn. He's got a building he'd lease us."

Ruth had been asked to open a twelfth store within eighteen months, and she had a list of four candidate towns. Sandpoint was on it. So were Davenport, Newport, and Ritzville. She had not intended to decide by napkin.

She asked Dana Okafor to come up with a way to decide that Walt would accept, which Dana understood to mean a way that would let him keep the napkin if the answer turned out to be Sandpoint.

## Which Kind of Decision This Was

Dana started by sorting the decisions Tamarack made into the kinds she'd been taught, mostly so she could explain why this one was going to take longer than Walt wanted.

Reordering bagged feed was a [[structured_decisions|structured decision]]: there was a standard procedure — when stock fell below a reorder point, order a set quantity — and the system already did it automatically. Weekly staffing at the stores was a [[semistructured_decisions|semistructured decision]]. Part of it could be computed from sales history and the schedule, and part of it was a manager knowing that the high school's spring break meant two fewer clerks. Where to put a twelfth store was an [[unstructured_decisions|unstructured decision]]. It happened once, and there was no procedure for it.

"So there's no formula," Walt said.

"There's no formula for the whole thing. There are formulas for pieces of it."

## Looking Before Choosing

Ruth laid out the process in four phases, because the consultant she'd once worked with had, and because it kept people from skipping to the end.

The [[intelligence_phase|intelligence phase]] meant looking at the environment for the conditions that needed a decision and gathering data from inside and outside the company. Dana pulled loyalty customer addresses from all eleven stores, and Teo Vasquez loaded them into a [[geographic_information_system_gis|geographic information system]] along with county agricultural census data, competitor locations, and highway drive times. The map showed something nobody had expected: Tamarack already had more than four hundred loyalty customers in Lincoln County who drove past Davenport to shop in Spokane, an hour each way.

Sandpoint had fewer existing customers and more horse owners. Newport had a competitor already. Ritzville was mostly wheat farms with little livestock.

The [[design_phase|design phase]] meant defining criteria, generating alternatives, and connecting the two. Ruth's criteria were drive time from the DC, existing customer density, livestock numbers, competitor distance, and lease cost. The four towns were the alternatives, plus a fifth that Dana added — not opening a store, and adding a delivery route instead — which Walt found irritating.

## Building the Tool

To compare them, Ruth had the consultant set up a [[decision_support_system_dss|decision support system]]: an interactive system with data, models, and a user interface, built for one kind of problem. Its database held the map data and Tamarack's store sales. Its [[model_base|model base]] held a sales forecasting model that estimated a new store's first three years from the demographics around it and the performance of similar Tamarack stores.

Three people built it, and they kept getting in each other's way.

Ruth acted as the [[managerial_designer|managerial designer]]. She decided what management needed from the tool: comparing five alternatives on the same criteria, with first-year revenue and payback period. She didn't care how it was built.

Teo acted as the [[technical_designer|technical designer]]. He cared about exactly the things Ruth didn't: where the data was stored, who could log in, how fast it ran, and whether customer addresses were safe in a consultant's cloud account. He insisted the addresses be reduced to ZIP code counts before they left Tamarack's network, which made the map less precise.

The consultant, a former regional planner named Corinne, acted as the [[model_builder|model builder]]. Her job was to explain what the forecasting model did, what inputs it accepted, how to read its output, and what it assumed. Its biggest assumption was that a new store would perform like the most similar existing store. Davenport's most similar store was Colville. Sandpoint's most similar store didn't exist; Tamarack had never had a store in a town with that many weekend horse owners and vacation homes.

"So the Sandpoint number is weaker," Ruth said.

"The Sandpoint number is a guess with decimals," Corinne said. Dana wrote that one down.

## The Screen Walt Wanted

Walt did not want to run the DSS. He wanted to look at it.

Corinne built him a view in the company's [[executive_information_systems_eiss|executive information system]], which already showed him weekly sales. It had a [[digital_dashboard|digital dashboard]] up top, a single page of charts pulling from several sources: the five alternatives side by side, their projected first-year sales, and their payback periods. From there he could drill down: click Davenport, see the customer map; click the map, see the ZIP codes; click a ZIP code, see the livestock census.

Ruth told Dana afterward that the EIS, the DSS, and the reorder system were all one family of things, the [[management_support_systems_msss|management support systems]], each built to support one kind of decision. The trouble with the family, Ruth said, was that the one Walt saw most was the one with the least model behind it.

## The Answer Walt Didn't Want

The [[choice_phase|choice phase]] came on a Thursday. Davenport led on every criterion except lease cost. Its payback period was under three years. Sandpoint's was five, with the widest error range of the five. The delivery route came in second, which Walt said proved the model was broken.

He spent ten minutes drilling down on Sandpoint. Then he asked Corinne what would have to be true for Sandpoint to win. She ran it: Sandpoint's horse owners would have to spend like Colville's ranchers. Walt said that was possible. Corinne said it was possible.

Walt chose Davenport. He also asked that Sandpoint stay on the dashboard as a comparison, so that if Davenport underperformed, everyone would see what they'd passed up.

## Getting It Done

The [[implementation_phase|implementation phase]] meant turning the choice into a plan and getting the resources for it. It went wrong quickly.

The building in Davenport that had driven the lease-cost number belonged to an estate, and the estate's heirs took six weeks to agree on terms and then disagreed. The second site had a smaller lot with no room for a propane dock, which the model had assumed. Corinne reran the numbers without propane. Payback moved from under three years to almost four, and Sandpoint, still on Walt's dashboard, looked closer than it had.

Ruth signed the second lease anyway. Jim Sorensen called Walt to ask what happened to Sandpoint, and Walt told him to give it a year.
