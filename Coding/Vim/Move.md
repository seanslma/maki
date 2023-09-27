# Move
Here’s a handy tip: prefacing a movement command with a number will execute that movement multiple times. So, if you want to move up 6 lines, enter 6k and Vim will move the cursor up 6 lines. If you want to move over 5 words, enter 5w. To move 10 words back, use 10b.

## char
```
h -> left
l -> right
k -> up
j -> down
```

## word
```
w  -> move forward one word
b  -> move backward one word
de -> move to end of current word
2w -> move to start of 2ed word
3e -> move to end of 3ed word
```

## line
```
0  -> moves to the beginning of the line
^  -> first non empty of the line
$  -> moves to the end of the line
```

## file
```
gg -> move to the beginning of the file
G  -> move to the end of the file
#G -> move to line#
`. -> move to the last edit
^G ->cursor location and file status
```
