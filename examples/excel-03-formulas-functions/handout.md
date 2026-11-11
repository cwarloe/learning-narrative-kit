# Zero or unknown? A one-page check

Keep this page from [The Crew Bonus](narrative.md) and its [practice](practice.md). Use it when you are about to send a total that was built with lookups. It is a list of questions to ask. It does not check your sheet for you.

## 1. Zero or unknown?

Look at every 0 and every blank that feeds the total, and ask which kind it is.

- **A known zero** has a source behind it. Someone approved 0 units. Stock is already at the target, so the order is 0. Keep it and pay or order nothing.
- **An unknown** has no source yet. The ID did not match, the record is not in the list, or nobody took the count. Do not let it become 0. Label the row, hold it, and go find the fact.

Excel treats an empty cell as 0 in arithmetic. A blank will give you a tidy number and no warning, so a blank alone never tells you which kind you have.

## 2. Exact match, or cutoffs?

- **Which one?** A person, a supplier, an item ID. Use an exact match (in VLOOKUP, `FALSE` as the last argument). Employee 1047 is not employee 1046, and a near miss is the wrong one.
- **Which band?** A number that falls between cutoffs, like pallets per hour into a bonus tier. An approximate match is fine here (in VLOOKUP, `TRUE` as the last argument). Sort the cutoffs from smallest to largest, or the lookup returns the wrong band.

## 3. What `IFERROR(...,0)` can hide

IFERROR replaces any error with whatever you choose. If you choose 0, a lookup that failed to find someone looks the same as a person who is owed nothing. The total adds up, the sheet looks clean, and one person is missing from it. That is how Marco's $415 dropped out of a total that looked finished.

If you wrap a lookup of a name or an ID, have it return a message you cannot miss, such as "ID NOT FOUND". Leave the amount lookup unwrapped, so the total shows an error until the record is fixed.

## 4. Three checks before you send a total

1. **Look for rows that came back empty.** Is there an error, a "not found" message, or a 0 where a name or an amount should be?
2. **Question the zeros.** For each row that pays or orders 0, can you point to the source that says zero?
3. **Say what the total covers.** If any rows are held, send three numbers: what can be released, what is held, and the full calculated amount. Never send the released amount as if it were the whole.

## 5. When a record is missing

Do not guess, and do not copy from an ID that looks close. Ask the person who owns the list (HR for employee records, the register owner for suppliers or items) and tell them:

- which ID or item you looked for, and where you looked;
- what you found instead, if anything (for example, the same name under a different ID);
- which row is on hold, and what is waiting on their answer.

When the owner has corrected the source record, check that the total changes the way you expect.
