# Bot script: The Crew Bonus (Excel 3)

Generated from `steps.yaml` by `build_workbook.py`. Edit the YAML, not this file.
Every value under **Check** was verified against the answer key when this file was built.

This file has two parts. **Part A is for you**, the person setting up. **Part B is the
prompt**: paste it into the computer-use agent (Claude, ChatGPT, Grok, or another), one
clip at a time.

## Part A: before you hand over control

1. **Use a clean screen.** Close email, the browser, chat apps, password managers, and
   anything with personal or work data. Turn on Do Not Disturb. Better still, use a
   separate user account or a virtual machine that only has Excel.
2. **Work on a copy.** Copy `crew-bonus-start.xlsx` to a local folder (Desktop or
   Documents, not inside OneDrive or a synced folder) and open the copy. If Excel opens
   it in **Protected View** (a yellow bar), click **Enable Editing** yourself.
3. **Set up Excel.** Desktop Excel for Microsoft 365 or 2021, maximized, zoom 120%. Make
   sure the **Bonus** sheet tab is visible and the window is on your main display.
4. **Start the screen recorder yourself**, recording **the Excel window only** (not the
   whole display), so the agent's own chat window and overlay stay out of the video.
   Don't ask the agent to start or stop the recording.
5. **Give the agent access to Excel only**, if your tool asks which apps it may control.
6. **Run one clip per message.** Paste the rules plus Clip 1. When it reports done, check
   the screen, then paste Clip 2. A wrong turn then costs one clip, not the whole take.
7. **Stay at the keyboard.** If the agent wanders out of Excel, take over the mouse;
   most tools stop when you do.

## Part B: paste this to the agent

### Rules (paste these first, with Clip 1)

You are operating Microsoft Excel on my computer to record a training video. The
workbook `crew-bonus-start.xlsx` is already open in Excel.

- **Work only inside Excel.** Do not open, click, or type into any other application,
  browser, file, or website. Do not use the File menu, Save, Share, or any sign-in.
- **Follow the actions exactly, in order.** Type text exactly as given, character for
  character, including quotation marks, dollar signs, and parentheses. Do not fix,
  improve, or reformat anything.
- **Prefer the keyboard.** To go to a cell or range, press Ctrl+G, type the reference,
  and press Enter. Do not click cells or drag. Do not use the fill handle; use the
  `fill` action instead.
- **Never press Tab** while typing a formula. It accepts Excel's autocomplete suggestion
  and can change the formula.
- **Go slowly.** This is a video. After each `enter` action, wait about one second.
  Obey every `pause`.
- **Check, then stop if wrong.** After each **Check** or **Look**, compare what the cell
  shows. If it does not match, **stop**, do not try to repair it, and tell me the cell,
  what you expected, and what you see.
- **Dialogs.** If an unexpected dialog appears (a security warning, sign-in, update,
  anything not in these steps), stop and tell me. Do not click through it.
- When the clip is done, say "Clip N done" and wait for my next message.

**Action meanings:**

- *Tab* NAME: click the sheet tab with that name at the bottom of the window.
- *Go to* REF: press Ctrl+G, type REF, press Enter.
- *Enter* TEXT: type TEXT exactly, then press Enter.
- *Type* TEXT: type TEXT exactly, without pressing Enter.
- *Fill* RANGE: press Ctrl+G, type RANGE, press Enter, then press Ctrl+D.
- *Press* KEYS: press that key or key combination.
- *Pause* N: wait N seconds without touching anything.
- *Check* / *Look*: read the cell on screen and compare.

### Clip 1: Hours that cross midnight

*Pause 3* (hold still: this marks the start of the clip)

1. *Tab* **Timeclock**
2. *Go to* `G2`
3. *Enter* `=(D2-C2)*24`
4. *Pause* 2
5. **Look:** `G2` shows -12.50
6. *Go to* `G2`
7. *Enter* `=IF(D2<C2,D2+1-C2,D2-C2)*24`
8. *Pause* 2
9. **Check:** `Timeclock!G2` shows **11.50**
10. *Go to* `H2`
11. *Enter* `=MAX(0,G2-8)`
12. *Pause* 1
13. **Check:** `Timeclock!H2` shows **3.50**
14. *Fill* `G2:H3460`
15. *Pause* 2
16. *Go to* `G2`
17. *Pause 3*, then say "Clip 1 done".

### Clip 2: Who qualified

*Pause 3* (hold still: this marks the start of the clip)

1. *Tab* **Bonus**
2. *Go to* `F2`
3. *Enter* `=COUNTIF(Timeclock!A:A,A2)`
4. *Pause* 1
5. **Check:** `Bonus!F2` shows **61**
6. *Go to* `G2`
7. *Enter* `=COUNTIF(Safety!B:B,A2)`
8. *Pause* 1
9. **Check:** `Bonus!G2` shows **0**
10. *Go to* `I2`
11. *Enter* `=AND(F2>=60,G2=0)`
12. *Pause* 2
13. **Look:** `I2` shows TRUE
14. *Go to* `I2`
15. *Enter* `=OR(AND(F2>=60,G2=0),H2=Leave)`
16. *Pause* 2
17. **Look:** `I2` shows #NAME?
18. *Go to* `I2`
19. *Enter* `=OR(AND(F2>=60,G2=0),H2="Light duty",H2="Leave")`
20. *Pause* 2
21. **Check:** `Bonus!I2` shows **TRUE**
22. *Pause 3*, then say "Clip 2 done".

### Clip 3: What normal looks like

*Pause 3* (hold still: this marks the start of the clip)

1. *Tab* **Checks**
2. *Go to* `B2`
3. *Enter* `=AVERAGE(WMS!D:D)`
4. *Pause* 2
5. **Check:** `Checks!B2` shows **41.3**
6. *Go to* `B3`
7. *Enter* `=MEDIAN(WMS!D:D)`
8. *Pause* 2
9. **Check:** `Checks!B3` shows **44**
10. *Go to* `B4`
11. *Enter* `=MODE.MULT(WMS!D:D)`
12. *Pause* 2
13. **Check:** `Checks!B4` shows **45**
14. *Pause 3*, then say "Clip 3 done".

### Clip 4: Totals by crew and month

*Pause 3* (hold still: this marks the start of the clip)

1. *Go to* `B6`
2. *Enter* `=SUMIF(Timeclock!E:E,"Night",Timeclock!H:H)`
3. *Pause* 1
4. **Check:** `Checks!B6` shows **3016.5**
5. *Go to* `B7`
6. *Enter* `=COUNTIF(Timeclock!G:G,">10")`
7. *Pause* 1
8. **Check:** `Checks!B7` shows **616**
9. *Go to* `B8`
10. *Enter* `=AVERAGEIF(Timeclock!E:E,"Night",Timeclock!G:G)`
11. *Pause* 1
12. **Check:** `Checks!B8` shows **9.02**
13. *Go to* `B9`
14. *Enter* `=SUMIFS(Timeclock!H:H,Timeclock!E:E,"Night",Timeclock!F:F,"Sep")`
15. *Pause* 2
16. **Check:** `Checks!B9` shows **1103.0**
17. *Go to* `B10`
18. *Enter* `=COUNTIFS(Timeclock!E:E,"Night",Timeclock!F:F,"Sep",Timeclock!G:G,">10")`
19. *Pause* 1
20. **Check:** `Checks!B10` shows **220**
21. *Go to* `B11`
22. *Enter* `=AVERAGEIFS(Timeclock!G:G,Timeclock!E:E,"Night",Timeclock!F:F,"Sep")`
23. *Pause* 1
24. **Check:** `Checks!B11` shows **9.47**
25. *Go to* `B12`
26. *Enter* `=MAXIFS(Timeclock!G:G,Timeclock!E:E,"Night",Timeclock!F:F,"Sep")`
27. *Pause* 1
28. **Check:** `Checks!B12` shows **11.50**
29. *Go to* `B13`
30. *Enter* `=MINIFS(Timeclock!G:G,Timeclock!E:E,"Night",Timeclock!F:F,"Aug")`
31. *Pause* 2
32. **Check:** `Checks!B13` shows **3.00**
33. *Pause 3*, then say "Clip 4 done".

### Clip 5: The lookups

*Pause 3* (hold still: this marks the start of the clip)

1. *Tab* **Bonus**
2. *Go to* `B2`
3. *Enter* `=VLOOKUP(A2,HR!$A:$F,2,FALSE)`
4. *Pause* 1
5. **Check:** `Bonus!B2` shows **Dale Ostrander**
6. *Go to* `C2`
7. *Enter* `=VLOOKUP(A2,HR!$A:$F,4,FALSE)`
8. *Pause* 1
9. **Check:** `Bonus!C2` shows **330.15**
10. *Go to* `H2`
11. *Enter* `=VLOOKUP(A2,HR!$A:$F,6,FALSE)&""`
12. *Pause* 1
13. **Look:** `H2` shows (blank)
14. *Go to* `D2`
15. *Enter* `=ROUND(AVERAGEIF(WMS!A:A,A2,WMS!D:D),0)`
16. *Pause* 1
17. **Check:** `Bonus!D2` shows **44**
18. *Go to* `J2`
19. *Enter* `=VLOOKUP(D2,Tiers!$A$2:$C$5,2,TRUE)`
20. *Pause* 2
21. **Check:** `Bonus!J2` shows **2**
22. *Go to* `E2`
23. *Enter* `=IFS(J2=3,"Gold",J2=2,"Silver",J2=1,"Bronze",J2=0,"Base")`
24. *Pause* 2
25. **Check:** `Bonus!E2` shows **Silver**
26. *Pause 3*, then say "Clip 5 done".

### Clip 6: Rounding

*Pause 3* (hold still: this marks the start of the clip)

1. *Go to* `K2`
2. *Enter* `=C2*VLOOKUP(D2,Tiers!$A$2:$C$5,3,TRUE)`
3. *Pause* 2
4. **Check:** `Bonus!K2` shows **412.6875**
5. *Tab* **Checks**
6. *Go to* `B15`
7. *Enter* `=ROUND(Bonus!K2,2)`
8. *Pause* 1
9. **Check:** `Checks!B15` shows **412.69**
10. *Go to* `B16`
11. *Enter* `=ROUNDDOWN(Bonus!K2,0)`
12. *Pause* 1
13. **Check:** `Checks!B16` shows **412.00**
14. *Go to* `B18`
15. *Enter* `=ROUNDDOWN(-1.9,0)`
16. *Go to* `B19`
17. *Enter* `=INT(-1.9)`
18. *Pause* 2
19. **Check:** `Checks!B18` shows **-1**
20. **Check:** `Checks!B19` shows **-2**
21. *Go to* `B17`
22. *Enter* `=MROUND(Bonus!K2,5)`
23. *Pause* 2
24. **Check:** `Checks!B17` shows **415.00**
25. *Tab* **Bonus**
26. *Go to* `L2`
27. *Enter* `=MROUND(K2,5)`
28. *Go to* `N2`
29. *Enter* `=INT(F2/5)`
30. *Pause* 1
31. **Check:** `Bonus!L2` shows **415**
32. **Check:** `Bonus!N2` shows **12**
33. *Pause 3*, then say "Clip 6 done".

### Clip 7: Dates

*Pause 3* (hold still: this marks the start of the clip)

1. *Tab* **Checks**
2. *Go to* `B22`
3. *Enter* `=WORKDAY(B21,10)`
4. *Pause* 2
5. **Check:** `Checks!B22` shows **10/14/2026**
6. *Go to* `B23`
7. *Enter* `=NETWORKDAYS(HR!E7,B21)`
8. *Enter* `=NETWORKDAYS(HR!E27,B21)`
9. *Enter* `=NETWORKDAYS(HR!E28,B21)`
10. *Pause* 2
11. **Check:** `Checks!B23` shows **53**
12. **Check:** `Checks!B24` shows **63**
13. **Check:** `Checks!B25` shows **43**
14. *Go to* `B26`
15. *Enter* `=TODAY()`
16. *Pause* 2
17. **Look:** `B26` shows today's date
18. *Go to* `B26`
19. *Enter* `10/6/2026`
20. *Go to* `C26`
21. *Enter* `Typed, not TODAY()`
22. *Pause* 1
23. **Check:** `Checks!B26` shows **10/06/2026**
24. *Go to* `B27`
25. *Enter* `=CELL("filename",A1)`
26. *Pause* 2
27. **Look:** `B27` shows the file's path, ending in [crew-bonus-…]Checks
28. *Pause 3*, then say "Clip 7 done".

### Clip 8: One formula for the total

*Pause 3* (hold still: this marks the start of the clip)

1. *Tab* **Bonus**
2. *Go to* `M2`
3. *Enter* `=IF(I2,1,0)`
4. *Pause* 1
5. **Check:** `Bonus!M2` shows **1**
6. *Fill* `B2:N38`
7. *Pause* 2
8. *Go to* `B6`
9. *Pause* 2
10. **Look:** `B6` shows #N/A
11. *Go to* `L40`
12. *Enter* `=SUM(L2:L38*M2:M38)`
13. *Pause* 3
14. **Look:** `L40` shows #N/A
15. *Pause 3*, then say "Clip 8 done".

### Clip 9: The IFERROR that hid a person

*Pause 3* (hold still: this marks the start of the clip)

1. *Go to* `B2`
2. *Enter* `=IFERROR(VLOOKUP(A2,HR!$A:$F,2,FALSE),0)`
3. *Go to* `C2`
4. *Enter* `=IFERROR(VLOOKUP(A2,HR!$A:$F,4,FALSE),0)`
5. *Go to* `H2`
6. *Enter* `=IFERROR(VLOOKUP(A2,HR!$A:$F,6,FALSE)&"",0)`
7. *Fill* `B2:C38`
8. *Fill* `H2:H38`
9. *Go to* `L40`
10. *Pause* 3
11. **Check:** `Bonus!B6` shows **0**
12. **Check:** `Bonus!L40` shows **9840**
13. *Pause 3*, then say "Clip 9 done".

### Clip 10: Marco's pay stub

*Pause 3* (hold still: this marks the start of the clip)

1. *Tab* **HR**
2. *Press* **Ctrl+F**
3. *Type* `1147`
4. *Press* **Enter**
5. *Pause* 2
6. **Look:** a message says Excel couldn't find what you were looking for
7. *Press* **Enter**
8. *Press* **Ctrl+A**
9. *Type* `Marco`
10. *Press* **Enter**
11. *Pause* 2
12. *Press* **Esc**
13. **Look:** `HR!A6` shows 1174
14. *Go to* `A6`
15. *Enter* `1147`
16. *Tab* **Bonus**
17. *Go to* `B6`
18. *Pause* 2
19. **Look:** `B6` shows Marco Reyes
20. *Go to* `L40`
21. *Pause* 3
22. **Look:** `L40` shows $10,255
23. *Go to* `B2`
24. *Enter* `=IFERROR(VLOOKUP(A2,HR!$A:$F,2,FALSE),"ID NOT FOUND")`
25. *Go to* `C2`
26. *Enter* `=VLOOKUP(A2,HR!$A:$F,4,FALSE)`
27. *Fill* `B2:C38`
28. *Go to* `L40`
29. *Pause* 3
30. **Look:** `L40` shows $10,255
31. *Pause 3*, then say "Clip 10 done".

