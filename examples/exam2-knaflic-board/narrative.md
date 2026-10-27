# What Eli Left Out

*Tamarack Feed & Supply Co. • ITM 310 Exam 2 review: Knaflic Ch. 1 and Power BI • Hover over highlighted terms for definitions.*

The board met on the first Thursday of October, and Ruth Halvorsen put Eli Mendez on the agenda for twenty minutes. By the Monday before, he had a nine-page Power BI report and no idea which page to open first.

He had spent three evenings in September finding things. He split sales by store, then by month, then by week, and the report showed a jump in Davenport's August sales, two propane tanks the dispatcher had missed, and a carrier whose damage rate climbed every Friday. Dana Okafor, who had stopped by the day supervisor's office to return a stapler, looked over his shoulder and called it [[exploratory_analysis|exploratory analysis]]. He had gone in without a question, to see what turned up. Her book on presenting data, which she'd kept since school, described it as opening a hundred oysters to find two pearls.

"That's the right way to find them," she said. "Who's it for?"

"The board."

"Which part of the board?"

Eli said all of it. The store managers would see it too, since they got the PDFs, so they'd want—

"They aren't deciding anything," Dana said. She asked him to pick a smaller [[audience|audience]], because a report built for everyone would give nobody what they needed. The one that mattered was Walt, who decided on instinct, and who had never wanted a Power BI license. Kip Andersen came second. Kip read the packet in advance and would ask about every number in parentheses.

She wrote three questions on the whiteboard and left them there. Who is the audience? What do they need to know or do? How can the data show it? Together they made up the [[presentation_context|context]] for the talk, and Eli had answered none of them. He had been stuck on the third.

The second question took twenty minutes. The board did not need to know that Davenport had a good August. It needed to decide next year's Davenport budget, and the August number was about to anchor it. When Eli drilled into the week of the jump, he had seen that a competitor in Ritzville was closed for a remodel. Some of Davenport's sales had been borrowed from a store that wasn't open, and would go back.

That made it [[explanatory_analysis|explanatory analysis]]: one finding, already in hand, for one audience. Dana made him say it as a single sentence, and the first three tries failed. "Davenport sales" was a topic. "Davenport had a strong August" was true and cost nobody anything. The fourth one stuck: Davenport's August spike came from a competitor's remodel in Ritzville, so budgeting next year at August's pace would plan for sales that won't return.

Dana said that was a [[big_idea|Big Idea]]: a complete sentence with a point of view and something at stake. She did not say it was good. She said it was long.

* * *

They built the talk on sticky notes before touching the report. This was [[storyboarding|storyboarding]]: one note per slide, moved around on the whiteboard until the order held. Eli's first board had eleven notes. The final one had four: the August jump, the Ritzville week, the same weeks without it, and the budget ask. Propane went into an email for the dispatcher. The Friday carrier problem went into a note to himself. Drill mode, which Ruth loved, stayed in the report, because there was no good way to click through it in front of a room without losing the room.

The packet raised a different question. The report lived in the Power BI service, and Walt could not open it. The board read paper. Dana called that choosing the [[communication_method|communication method]], and the two choices pulled in opposite directions. A page in the packet had to explain itself, because Kip would read it alone at his kitchen table. In the room, Eli could say the rest out loud, so the slides could carry less.

So he made both: one printed page that stood on its own and three slides that did not. To keep the printed page clean, he rebuilt the August chart in a new file with nothing else in it. The empty canvas wouldn't do anything until he chose [[get_data|Get data]], so he started there.

Kip called on Tuesday, after the packet went out. He wanted to know whether the Total Sales figure on the page was typed in or calculated.

Eli read it to him off the formula bar. The [[calculated_measure|measure]] was named Total Sales. It began with an equals sign and called the [[dax_function|DAX function]] SUM, which added up numbers. Inside the parentheses was a single [[argument|argument]], the SalesAmount column in the Sales table. The function needed that argument to know what to add.

"One," Kip said. Eli heard him write it down.

On Thursday, Walt read the Big Idea aloud from the packet, said Davenport would be fine regardless—he said it twice—and approved the lower budget anyway. Then he asked Eli to put August's pace back into the forecast as an upside case. Eli did it that afternoon. It took four minutes.

Ruth caught him in the hall afterward. She asked why he hadn't shown the drill-down, since it was the best thing in the report. Eli said it wouldn't have fit, and went to check on the dock.


## Study cards: Knaflic Ch. 1

These are the Knaflic chapter 1 cards from the Exam 2 study deck. Click a card to flip it.

```lnk-deck
title: Red · Knaflic Ch. 1 · recall
meta: 2 cards · definition on the front, term on the back
size: 3x5
band: red
---
tag: KNAFLIC CH. 1
Q: A single complete sentence that states your point of view and what is at stake.
A: Big Idea
hint: Name the term
---
tag: KNAFLIC CH. 1
Q: Sketching the outline of a presentation, one note per slide, and rearranging it before building anything.
A: Storyboarding
hint: Name the term
```

```lnk-deck
title: Knaflic Ch. 1 · concepts
meta: 5 cards · answer before you flip
size: 4x6
band: green
---
tag: KNAFLIC CH. 1
Q: Presentation context: what three questions does Knaflic say to answer before building anything?
A: Who is the audience? What do you need them to know or do? How can the data help make your point?
band: green
---
tag: KNAFLIC CH. 1
Q: Exploratory vs explanatory analysis?
A: Exploratory: looking through data to find what might be worth telling (opening many oysters). Explanatory: communicating one finding to a specific audience (the pearl).
band: yellow
---
tag: KNAFLIC CH. 1
Q: Present to the widest possible audience, or a specific one?
A: A specific one. A report built for everyone gives nobody what they need.
why: Review deck slide 42.
band: yellow
---
tag: KNAFLIC CH. 1
Q: Live presentation vs a document read alone: which one has to stand on its own?
A: The document. In a live talk the speaker carries part of the message, so the slides can hold less.
band: yellow
---
tag: KNAFLIC CH. 1
Q: Planning a data talk: put these in order. Storyboard · answer the three context questions · write the Big Idea · build the visuals.
A: Context questions → Big Idea → storyboard → visuals.
why: Knaflic: settle who, what, and how before touching the data tool.
band: blue
```
