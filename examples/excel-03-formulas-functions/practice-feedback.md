# The Crew Bonus: feedback

Save your first response to [the practice](practice.md) before reading this file. Equivalent formulas and clear formats are welcome; the explanation matters more than a particular layout.

## Partly finished check

- P01: $100 × 1.00 = $100.
- P02: $100 × 1.10 = $110. The boundary value 40 enters the second tier.
- P03: the rule-based amount is $100 × 1.25 = $125, but the missing HR record prevents payment authorization. Ask the HR record owner to reconcile the ID. Do not turn it into zero or guess a nearby ID.

Employee identity needs an exact match. A productivity tier uses the interval containing the value; with an approximate VLOOKUP, sort the lower cutoffs ascending. Other methods that implement the same intervals are acceptable. The $5 rule happens not to change these three amounts.

## Supplier reimbursement

| Claim | Calculated amount | Decision |
|---|---:|---|
| C01 | $40 | Can release to verified Account A |
| C02 | $0 | Verified zero; nothing payable |
| C03 | $40 | Hold: S30 has no registered payment account |
| C04 | $60 | Can release to verified Account D |

The releasable total is **$100**. The unresolved amount is **$40**. The full calculated amount is **$140**. The original sheet could also show $100; that does not make it a complete account of the claims.

Preserve the calculated amount separately from account status. Make missing accounts visible and list held claims. Ask the supplier-register owner to verify S30 through the approved process; do not copy an account from a similar ID. This policy permits separate release of verified claims, so holding the entire batch is not required.

If you marked C02 as an error because it is zero, revisit the distinction between a known value and a failed lookup. If you rounded to $5, revisit which rules belong to which task. If you found $140 but would release all of it, revisit the account requirement.

Name one decision you changed after feedback and the evidence that changed it. If none changed, explain how you checked your first answer.
