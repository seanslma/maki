# Button

## spin button
https://support.microsoft.com/en-au/office/add-a-scroll-bar-or-spin-button-to-a-worksheet-f8443be3-ff00-4cad-bb2f-bf0f88ebf5bb
- Developer > Insert > Form Controls > Scroll bar
- Developer > Controls ? Properties > Min/max value
- copy C:I based on Row number in A4: `=INDEX(mysheet!$C$1:$I$1000, A4, COLUMN(C1:I1)-2)`
