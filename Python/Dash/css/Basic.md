# Basic

## syntax
```css
selector {
  property: value;
  property: value;
}
```

## types
In CSS (Cascading Style Sheets), selectors are used to target and style HTML elements. 
There are different types of selectors, and they serve various purposes. 

Here are explanations of three common types: type selectors, class selectors, and ID selectors:

1. **Type Selectors:**
   - **Syntax:** `elementName { /* styles */ }`
   - **Example:** `p { color: blue; }`
   - **Explanation:** Type selectors target HTML elements based on their tag names.
     In the example, all `<p>` (paragraph) elements will have a blue text color.

2. **Class Selectors:**
   - **Syntax:** `.className { /* styles */ }`
   - **Example:** `.highlight { background-color: yellow; }`
   - **Explanation:** Class selectors target elements with a specific class attribute.
     In the example, all elements with the class "highlight" will have a yellow background color.
     You apply a class to an HTML element using the `class` attribute: `<div class="highlight">...</div>`.

3. **ID Selectors:**
   - **Syntax:** `#idName { /* styles */ }`
   - **Example:** `#header { font-size: 24px; }`
   - **Explanation:** ID selectors target a specific element with a unique ID attribute.
     In the example, the element with the ID "header" will have a font size of 24 pixels.
     You apply an ID to an HTML element using the `id` attribute: `<div id="header">...</div>`.
     It's important to note that an ID must be unique within a page, whereas a class can be used on multiple elements.

Examples of usage in HTML:

```html
<!-- Type Selector -->
<p>This is a paragraph.</p>

<!-- Class Selector -->
<div class="highlight">This element has a yellow background.</div>

<!-- ID Selector -->
<div id="header">This is a header.</div>
```

Selectors can also be combined and used in more complex ways to target specific elements or groups of elements. 
Understanding and using CSS selectors effectively is crucial for styling web pages efficiently 
and maintaining a clear separation of structure and presentation.
