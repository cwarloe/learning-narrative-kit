# The Count That Didn't Match

*Tamarack Supply • MIS Module 1: Information Systems in Business • Hover over highlighted terms for course definitions.*

## Forty Bags of Layer Pellets

The Colville store said it had forty bags of layer pellets. The register system said it had one hundred and twelve. Dana Okafor had the two numbers side by side on her laptop in the head-office break room, and neither of them was the number of bags on the pallet, which a clerk had just counted by hand and texted to her as fifty-three.

Walt Brandvold came in for coffee and looked over her shoulder. He had owned Tamarack Supply for twenty-two years and his father had owned it before that, and he did not like it when a screen disagreed with a pallet.

"That's the third store this month," he said. "I want a new inventory system. Teo says there's one the co-op in Moscow uses. Price it out."

Dana had been expecting this, and she had a half-finished answer. The register system wasn't really an inventory system at all. It was a [[transaction_processing_systems_tpss|transaction-processing system]]: it recorded each sale, each return, each receipt at the back door, and it was very good at that, which was why the company had bought it in the first place. It had replaced three part-time bookkeepers. It counted what people told it to count.

"The system isn't inventing the hundred and twelve," she said. "Somebody told it we received a pallet we didn't get, or sold bags under the wrong item number, or both. If we buy new software and feed it the same way, it'll be wrong in a nicer font."

Walt drank his coffee and said he would still like a price.

## What the Pallet Count Actually Is

Ruth Halvorsen, the chief operating officer, took Dana's side in the afternoon meeting, though not for Dana's reasons. Ruth's concern was the store managers' quarterly review, which used the register system's numbers to grade shrink, and three managers were about to be graded on a mistake.

"So what are we looking at, exactly?" Ruth asked. "Walk me through it like I don't know anything."

Dana pulled up the export. A row said that on March 4 a receipt of item 40817 posted at quantity 60 for the Colville store. Another row said a sale of item 40871 posted at quantity 1, twenty times that week.

"By itself this is just [[data|data]]," she said. "A row, a number, an item code. It doesn't mean anything until somebody puts it next to something else." She sorted by item, then filtered to the two codes that differed by one transposed digit. "When you compare the two item numbers and see that the clerks are scanning a shelf tag that's been mislabeled since February, now it's [[information|information]]. It tells you why the count is off."

What turned one into the other was the part Dana thought Walt kept skipping. The [[process|process]] step — the sorting, matching, and reporting that sits between the raw rows and the person making a decision — was where all of the value came from, and right now Dana was doing that step by hand, one store at a time.

"Then we need a system that does that step," Ruth said.

"We need a [[management_information_system_mis|management information system]]," Dana said. "Hardware and software, sure, but also the data, the process, and the people who scan the tags. The register system is one piece of it. The shelf tag is another piece."

Ruth asked who owned shelf tags. Nobody in the room knew.

## The Clerk Who Didn't Trust the Screen

On Thursday Dana drove the ninety minutes up to Colville. The store manager, a lean man named Curtis who had been there since the store opened, walked her to the feed aisle and showed her the tag. It was a pre-printed label from the vendor, and somebody had stuck it over the old one.

"I told the kid to scan the bag, not the shelf," Curtis said. "He says the bag barcode doesn't read half the time, so he scans the shelf."

The clerk, a nineteen-year-old named Jesse, was not apologetic. He could run the register fine. What he didn't have was [[computer_literacy|computer literacy]] past the register screen. He had never opened a spreadsheet, he didn't know the register data fed a report at head office, and he was surprised to hear that the report was graded.

The harder gap was in Curtis. Curtis could use every system the store had. What he didn't have was [[information_literacy|information literacy]]: he had stopped believing the numbers years ago, so he didn't look at them, so he didn't notice when they drifted. He kept the real count in a spiral notebook behind the counter. Dana asked to photograph it and he said no, then said yes, then asked whether this was going to show up in his review.

She told him the truth, which was that she didn't know.

## Pricing the Thing Walt Asked For

Back in Spokane Valley, Teo Vasquez had already priced the co-op's system. It was mostly cloud software and handheld scanners, and the scanners were the part Dana liked.

"The [[information_technologies|information technologies]] aren't the hard part," Teo said. "Handhelds, the network, a database, the point-of-sale lanes, maybe RFID on the pallets eventually. I can buy all of that. What I can't buy is somebody at Colville who scans the bag."

Walt wanted to know whether the new system would beat Northland Farm Supply, the chain that had opened two stores in his territory in the last eighteen months. Ruth had done a rough [[five_forces_model|Five Forces]] pass on Northland the previous fall and pulled it up. The threat of new entrants had turned out to be real: Northland had come in with private-label feed at a price Tamarack couldn't match. Rivalry was up. But buyer power was low in the ranching towns where Tamarack was the only store with a propane dock and a knowledgeable counter.

"We don't win on price," Ruth said. "We win where people need us to know what we have. If our counts are wrong, we lose the only thing Northland can't copy."

That reframed the purchase. A [[strategic_information_systems_siss|strategic information system]] was supposed to serve a long-term goal, and the goal Ruth had just named was being the store that knows. The inventory software was only strategic if it served that. If it was just a nicer register, it was a cost.

## The Feed Co-op Idea

Marcy Lund, the head buyer, raised the idea nobody had planned for. Three independent feed dealers in the region, Tamarack among them, had talked for years about pooling their purchasing to get better terms from the mills. The co-op's system could share inventory and orders across companies.

"If we're on the same platform as Palmer's and the Deer Park dealer, we could run as a [[virtual_organizations|virtual organization]] for feed," Marcy said. "Shared purchasing, shared delivery runs, each of us keeps our own stores and our own customers."

Walt didn't like the idea of Palmer's seeing his counts. Marcy pointed out that Palmer's counts were probably wrong too. Nobody laughed.

## What Got Decided

The decision came on the following Monday, and it was smaller than anyone wanted.

Walt approved a pilot of the handheld scanners in three stores, Colville first, and declined the full system until the pilot proved out. The feed partnership went on a list. Dana got the job of writing the receiving procedure the scanners would enforce, which was not the job she wanted: she had hoped to build the reporting.

The three store managers' shrink grades were held for a quarter, which Ruth had to defend to the board's finance committee. One committee member said that holding grades whenever the data was bad meant never grading anyone.

Curtis kept his notebook. When Dana called to tell him the pilot was coming, he said fine, and that he would believe the screen when it matched the book for three months running. She wrote the three months into the pilot plan, because it was as good a test as any she had.
