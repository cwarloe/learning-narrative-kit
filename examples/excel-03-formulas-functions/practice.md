# The Crew Bonus: try the work

Read [The Crew Bonus](narrative.md) first. Allow about 30 minutes for this companion. The chapter stays complete; these exercises contain no extra story events.

## 1. Follow the worked example

Use the existing [starting workbook](workbook/crew-bonus-start.xlsx) and [step-by-step walkthrough](workbook/RECORDING.md). The starting workbook has no formulas yet, so follow clips 2, 5, 6, 8, 9 and 10, in that order. Clip 2 sets who is eligible. Clip 5 builds the exact ID lookup and the tier lookup. Clip 6 does the rounding. Clip 8 fills the rows down and builds the total. Clip 9 hides the error, and clip 10 corrects it. Clips 1, 3, 4 and 7 do not feed the total; they are there if you want them.

Watch these two different outcomes in the same incident:

- An exact lookup for Marco's ID, 1147, fails because HR contains 1174. Replacing the error with zero makes a missing record look like a legitimate zero payment.
- Correcting the ID after checking the source restores the $415 payment. The visible total rises from $9,840 to $10,255. A missing-ID message you can't miss, and a total that shows an error until the ID is fixed, prevent a quiet repeat.

Explain in your own words why a clean-looking total was insufficient. Then close the walkthrough.

Keep this page for later: [Zero or unknown? A one-page check](handout.md).

## 2. Complete a partly finished check

This small practice dataset is fictional and separate from the chapter's payroll. All quantities below are supplied facts. Every person meets the eligibility rule. The base amount is $100; the multiplier is 1.00 below 40 pallets/hour, 1.10 from 40 through less than 50, and 1.25 from 50 upward. Round each payment to the nearest $5.

| Employee ID in work record | Pallets/hour | Matching HR ID |
|---|---:|---|
| P01 | 39 | P01 |
| P02 | 40 | P02 |
| P03 | 50 | absent |

The first row is finished: P01 receives $100. Finish P02. For P03, state what is unresolved and what source you need before authorizing payment. Do not invent an ID correction.

Write the formula or calculation you used, and identify which lookup needs an exact match and which uses cutoffs. If stuck, consult the worked example, then record what help you used.

## 3. Solve one different problem

A supplier reimbursement file has a total that looks ready to send. This is a standalone practice company, with no connection to Tamarack's cast or timeline.

| Claim | Supplier ID | Approved units | Rate per unit |
|---|---|---:|---:|
| C01 | S10 | 10 | $4 |
| C02 | S20 | 0 | $6 |
| C03 | S30 | 5 | $8 |
| C04 | S40 | 12 | $5 |

| Supplier register ID | Payment account |
|---|---|
| S10 | Account A |
| S20 | Account B |
| S40 | Account D |

The current sheet uses an exact supplier lookup wrapped in `IFERROR(...,0)`. Missing accounts cause that row's payment to become zero. Policy requires an approved amount AND a verified payment account. It permits paying verified claims separately if unresolved claims are clearly listed for follow-up. Amounts are paid to the cent, with no $5 rounding.

Prepare a short payment note, using a table or any clear format:

1. State each claim's calculated amount and whether it can be released.
2. Separate a legitimate zero from missing information.
3. State the releasable total, unresolved amount, and full calculated amount.
4. Explain what you would change in the sheet and who must supply the missing evidence.

Save your first answer before opening [feedback](practice-feedback.md). Compare the reasoning, then save corrections separately. A matching total with the wrong explanation still needs attention.

## Come back later

Ask someone to give you the [later problem](later-practice.md) roughly 7–14 days after this session. That interval is a convenient pilot choice, not a research-established optimum. Record the actual gap and any practice in between. If working alone, leave that file unopened until then.

## For the person trying this with a learner

Before starting, agree on available time, access to Excel or another suitable spreadsheet tool, and who can discuss the learner's work. If using a real workplace task afterward, use an authorized copy with sensitive data removed and have the task owner review it before any operational use. A course assignment is not evidence of workplace application.

Keep the first and revised work, note where help was needed, and ask whether the learner could explain the difference between zero and unknown in a new setting. The later problem is a small learning check, not a validated assessment or proof that the narrative caused improvement.

The design draws cautiously on the [October 29, 2026 classroom practice meta-analysis](https://doi.org/10.1007/s10648-026-10225-5), the [October 27 workplace transfer meta-analysis](https://doi.org/10.1108/EBHRM-03-2025-0117), and the [October 30 workplace work-product trial](https://doi.org/10.1186/s13063-026-10057-2). The classroom findings do not establish workplace transfer or validate narrative instruction. Only the workplace meta-analysis abstract was available during the research review; causal effects and its measurement quality were not verified. The randomized work-product trial was small and inconclusive. These exercises are a design to try, not an outcome claim.
