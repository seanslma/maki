# Scrollbar

## horizontal scrollbar
Changing `flex-direction: column` will get vertical scrollbar.
```css
.horizontal-scrollbar {
  flex-direction: row; }
  .horizontal-scrollba > div {
    overflow: auto !important; }
  .horizontal-scrollbar > div::-webkit-scrollbar {
    width: 8px;
    height: 8px; }
  .horizontal-scrollbar > div::-webkit-scrollbar-corner {
    background: transparent; }
  .horizontal-scrollbar > div::-webkit-scrollbar-track {
    background: transparent;
    border-radius: 8px; }
  .horizontal-scrollbar > div::-webkit-scrollbar-thumb {
    background: #5e6b73;
    border-radius: 8px; }
  .horizontal-scrollbar > div::-webkit-scrollbar-thumb:hover {
    background: #535e65; }
  .horizontal-scrollbar > div::-webkit-scrollbar-thumb:active {
    background: #475157; } 
```
