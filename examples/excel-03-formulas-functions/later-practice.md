# Later problem: replacement filters

Open this roughly 7–14 days after [the initial practice](practice.md). Allow about 15 minutes. Record the actual gap and any related practice. Start without the chapter, walkthrough, earlier answers, search, or AI assistance. If you need help, save what you have first, then use it and note what helped. This is a learning check, not a pass/fail test.

A workshop orders replacement filters. Its reorder rule is: **order enough to reach the target stock, with a minimum order quantity of zero**. A missing count or target must be resolved before that item's order can be released. Verified items can be released separately. The item register supplies the target and unit price by exact item ID. Quantities are whole filters; costs are in dollars.

| Count record item ID | Stock counted |
|---|---:|
| F10 | 2 |
| F20 | 8 |
| F30 | 1 |
| F40 | missing |

| Register item ID | Target stock | Unit price |
|---|---:|---:|
| F10 | 10 | $3 |
| F20 | 6 | $4 |
| F40 | 5 | $2 |

Prepare the order recommendation. State the quantity and cost wherever determinable, which items you can release, and what you need for the others. Explain how the sheet should handle incomplete records. Save your first answer before reading below.

<details>
<summary>Feedback: open after saving your recommendation</summary>

F10 needs 8 filters, costing $24. F20 needs zero: stock already exceeds the target, so an order of −2 is inappropriate. F30's target and price are unknown; request a verified register entry. F40's target and price are known, but its count is missing; request the count. Neither missing value should become zero automatically.

Release F10 for $24 under the supplied policy; record F20 as no order needed and hold F30 and F40. **$24 is the releasable amount, not a complete total for all four items.** The remaining quantities and costs cannot yet be calculated. An amount of $10 for F40 would assume its stock is zero, which was not observed.

A suitable calculation for complete records is maximum of zero and target minus counted stock, followed by quantity times price. Keep a separate visible status for missing inputs and prevent those rows from being treated as cleared. Do not require one particular formula or sheet layout.

Compare the first and revised recommendation. Could you distinguish a legitimate zero from unknown information without the bonus story's names and wording? That is useful evidence from this task, not proof of workplace performance or a causal training effect.

</details>
