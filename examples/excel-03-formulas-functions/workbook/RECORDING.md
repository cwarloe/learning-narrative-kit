# Recording script: The Crew Bonus (Excel 3)

Generated from `steps.yaml` by `build_workbook.py`. Edit the YAML, not this file.

## Before you start

- **Excel:** desktop Excel for Microsoft 365, or Excel 2021. Excel 2019 lacks some
  functions used here.
- **File:** open a fresh copy of `crew-bonus-start.xlsx` each time you record.
- **Screen:** 1920×1080 if you can, Excel maximized, zoom 120% (bottom-right slider).
  Turn off notifications.
- **Privacy:** your name or email shows in Excel's title bar and on the account button.
  Crop or blur it later, or record only the grid area.
- **Recording on Windows:** Win+Alt+R (Xbox Game Bar) records the Excel window; OBS
  works too. **On a Mac:** Cmd+Shift+5.
- **Clips:** either record each clip as its own file (`clip-01.mp4`, `clip-02.mp4`…),
  or record one long take and **hold still for three seconds** before each clip so it
  can be cut apart later.
- **Pace:** type at normal speed and pause about a second after each Enter, so the
  result is on screen long enough to see.
- **Mistakes:** if you mistype, just fix it and keep going. Real fumbles are fine.

## Clip 1: Hours that cross midnight

*Story passage:* "The first thing he needed was hours."

1. Click the Timeclock sheet tab. Click cell G2.
2. Type =(D2-C2)*24 and press Enter.
   - **You should see:** G2 shows -12.50. The night shift crossed midnight, so clock-out is smaller than clock-in.
3. Click G2 again. Type =IF(D2<C2,D2+1-C2,D2-C2)*24 and press Enter.
   - **You should see:** G2 shows 11.50.
4. Click H2. Type =MAX(0,G2-8) and press Enter.
   - **You should see:** H2 shows 3.50, the overtime past eight hours.
5. Select G2:H2 and double-click the fill handle (the small square at the lower right of the selection).
   - **You should see:** Both columns fill to the bottom of the export.

## Clip 2: Who qualified

*Story passage:* "Ruth's eligibility rule had two parts…"

1. Click the Bonus sheet tab. Click F2. Type =COUNTIF(Timeclock!A:A,A2) and press Enter.
   - **You should see:** Days worked for employee 1101.
2. In G2, type =COUNTIF(Safety!B:B,A2) and press Enter.
   - **You should see:** G2 shows 0 incidents.
3. In I2, type =AND(F2>=60,G2=0) and press Enter.
   - **You should see:** TRUE.
4. Click I2. Type =OR(AND(F2>=60,G2=0),H2=Leave) and press Enter. (The quotation marks are left out on purpose.)
   - **You should see:** #NAME? appears.
5. Click I2. Type =OR(AND(F2>=60,G2=0),H2="Light duty",H2="Leave") and press Enter.
   - **You should see:** TRUE. Column H is still empty; it fills in during clip 5.

## Clip 3: What normal looks like

*Story passage:* "Eli started with the AVERAGE function…"

1. Click the Checks sheet tab. In B2, type =AVERAGE(WMS!D:D) and press Enter.
   - **You should see:** 41.3
2. In B3, type =MEDIAN(WMS!D:D) and press Enter.
   - **You should see:** 44
3. In B4, type =MODE.MULT(WMS!D:D) and press Enter.
   - **You should see:** 45

## Clip 4: Totals by crew and month

*Story passage:* "Two nights later Hank called down from head office."

1. In B6, type =SUMIF(Timeclock!E:E,"Night",Timeclock!H:H) and press Enter.
   - **You should see:** Total night-crew overtime for the quarter.
2. In B7, type =COUNTIF(Timeclock!G:G,">10") and press Enter.
   - **You should see:** Number of shifts over ten hours.
3. In B8, type =AVERAGEIF(Timeclock!E:E,"Night",Timeclock!G:G) and press Enter.
   - **You should see:** Average night shift length.
4. In B9, type =SUMIFS(Timeclock!H:H,Timeclock!E:E,"Night",Timeclock!F:F,"Sep") and press Enter.
   - **You should see:** 1103.0, night overtime in September. Note the order: in SUMIFS the range to add comes first.
5. In B10, type =COUNTIFS(Timeclock!E:E,"Night",Timeclock!F:F,"Sep",Timeclock!G:G,">10") and press Enter.
6. In B11, type =AVERAGEIFS(Timeclock!G:G,Timeclock!E:E,"Night",Timeclock!F:F,"Sep") and press Enter.
7. In B12, type =MAXIFS(Timeclock!G:G,Timeclock!E:E,"Night",Timeclock!F:F,"Sep") and press Enter.
   - **You should see:** 11.50, the longest night shift in September.
8. In B13, type =MINIFS(Timeclock!G:G,Timeclock!E:E,"Night",Timeclock!F:F,"Aug") and press Enter.
   - **You should see:** 3.00, the week the forklift was down.

## Clip 5: The lookups

*Story passage:* "Each employee's tier came from their pallets per hour…"

1. Click the Bonus sheet tab. In B2, type =VLOOKUP(A2,HR!$A:$F,2,FALSE) and press Enter.
   - **You should see:** Dale Ostrander
2. In C2, type =VLOOKUP(A2,HR!$A:$F,4,FALSE) and press Enter.
   - **You should see:** $330.15
3. In H2, type =VLOOKUP(A2,HR!$A:$F,6,FALSE)&"" and press Enter.
   - **You should see:** Blank. Dale has no special status. (The &"" turns an empty cell into blank text instead of 0.)
4. In D2, type =ROUND(AVERAGEIF(WMS!A:A,A2,WMS!D:D),0) and press Enter.
   - **You should see:** 44
5. In J2, type =VLOOKUP(D2,Tiers!$A$2:$C$5,2,TRUE) and press Enter.
   - **You should see:** 2. An approximate match: 44 is at least the 44 cutoff and under 52.
6. In E2, type =IFS(J2=3,"Gold",J2=2,"Silver",J2=1,"Bronze",J2=0,"Base") and press Enter.
   - **You should see:** Silver

## Clip 6: Rounding

*Story passage:* "The bonus came out in odd amounts…"

1. In K2, type =C2*VLOOKUP(D2,Tiers!$A$2:$C$5,3,TRUE) and press Enter.
   - **You should see:** $412.6875
2. Click the Checks sheet tab. In B15, type =ROUND(Bonus!K2,2) and press Enter.
   - **You should see:** $412.69
3. In B16, type =ROUNDDOWN(Bonus!K2,0) and press Enter.
   - **You should see:** $412.00
4. In B18, type =ROUNDDOWN(-1.9,0). In B19, type =INT(-1.9).
   - **You should see:** -1 and -2. ROUNDDOWN moves toward zero; INT goes to the next lowest integer.
5. In B17, type =MROUND(Bonus!K2,5) and press Enter.
   - **You should see:** $415.00
6. Click the Bonus sheet tab. In L2, type =MROUND(K2,5). In N2, type =INT(F2/5).
   - **You should see:** L2 shows $415. N2 shows full weeks worked.

## Clip 7: Dates

*Story passage:* "The payout date came from Ruth's rule…"

1. Click the Checks sheet tab. In B22, type =WORKDAY(B21,10) and press Enter.
   - **You should see:** 10/14/2026
2. In B23, type =NETWORKDAYS(HR!E7,B21). In B24, type =NETWORKDAYS(HR!E27,B21). In B25, type =NETWORKDAYS(HR!E28,B21).
   - **You should see:** 53, 63 and 43: the most days each new hire could have worked. Only Kyle Banks could reach 60.
3. In B26, type =TODAY() and press Enter.
   - **You should see:** Today's date. It will change every time the file is opened, which is the problem.
4. Click B26 and type 10/6/2026, then press Enter. In C26, type: Typed, not TODAY().
5. In B27, type =CELL("filename",A1) and press Enter.
   - **You should see:** The file's full path and the sheet name.

## Clip 8: One formula for the total

*Story passage:* "The last number Hank wanted was the total payout…"

1. Click the Bonus sheet tab. In M2, type =IF(I2,1,0) and press Enter.
   - **You should see:** 1
2. Select B2:N2 and double-click the fill handle.
   - **You should see:** Every row fills. Row 6 (employee 1147) shows #N/A in several columns.
3. Click L40. Type =SUM(L2:L38*M2:M38) and press Enter. (In Excel 2019 or earlier, press Ctrl+Shift+Enter.)
   - **You should see:** #N/A. One bad row breaks the total.

## Clip 9: The IFERROR that hid a person

*Story passage:* "Eli's first try at the total…"

1. Click B2. Change the formula to =IFERROR(VLOOKUP(A2,HR!$A:$F,2,FALSE),0) and press Enter.
2. Click C2. Change it to =IFERROR(VLOOKUP(A2,HR!$A:$F,4,FALSE),0). Click H2. Change it to =IFERROR(VLOOKUP(A2,HR!$A:$F,6,FALSE)&"",0).
3. Select B2:C2, double-click the fill handle. Select H2, double-click the fill handle.
   - **You should see:** Row 6 now shows 0 instead of #N/A. L40 shows $9,840. The sheet looks clean.

## Clip 10: Marco's pay stub

*Story passage:* "On payday, a forklift driver named Marco Reyes…"

1. Click the HR sheet tab. Press Ctrl+F, search for 1147, and press Find Next.
   - **You should see:** Excel can't find it.
2. Search for Marco instead.
   - **You should see:** Marco Reyes, row 6, with Emp ID 1174: two digits swapped.
3. Close Find. Click A6 on the HR sheet, type 1147, press Enter.
4. Click the Bonus sheet tab.
   - **You should see:** Row 6 shows Marco Reyes, $330.15, and a $415 bonus. L40 shows $10,255.
5. Click B2. Change it to =IFERROR(VLOOKUP(A2,HR!$A:$F,2,FALSE),"ID NOT FOUND") and fill down. Click C2 and remove the IFERROR: =VLOOKUP(A2,HR!$A:$F,4,FALSE), and fill down.
   - **You should see:** A missing ID will now show ID NOT FOUND, and the total will break loudly instead of quietly coming up short.

