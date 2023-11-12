# Example

## code 1
The `html.Div` component is being created with a list containing a `metric_tab` element as its child. 
The `style` attribute is used to apply specific styling to this `html.Div` component. Let's break down the style:
```py
style={
    'flex': '1 1 75%',
    'display': 'flex',
    'flexDirection': 'column',
    'marginTop': '-18px',
    'padding': '1px',
}
```

1. **`'flex': '1 1 75%'`**: This is setting the flex property of the element.
   The `flex` property is shorthand for three individual properties: `flex-grow`, `flex-shrink`, and `flex-basis`.
   In this case, it is set to `'1 1 75%'`, which means:
    - `flex-grow`: 1 (the element can grow to fill the available space)
    - `flex-shrink`: 1 (the element can shrink if there is not enough space)
    - `flex-basis`: 75% (initial size of the element before growing or shrinking)

3. **`'display': 'flex'`**: This specifies that the element should be treated as a flex container.
   Flex containers can be used to control the layout and alignment of their children.

4. **`'flexDirection': 'column'`**: This sets the direction of the flex container's main axis.
   In this case, it's set to 'column', which means the children of the flex container will be placed in a column (top to bottom) layout.

5. **`'marginTop': '-18px'`**: This sets the top margin of the element to -18 pixels.
   A negative margin can be used to adjust the spacing above the element.

6. **`'padding': '1px'`**: This property sets the padding of the element to 1 pixel on all sides.
   Padding is the space between the content of an element and its border.   

So, in summary, this piece of code is styling a `html.Div` to be a flex container with a vertical column layout for its children (`metric_tab`).
It has a flexible width of 75% of its parent container, can grow or shrink as needed, and has a negative top margin of 18 pixels.
