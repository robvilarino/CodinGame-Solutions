'''
Puzzle URL: https://www.codingame.com/ide/puzzle/the-broken-editor
'''

import sys
import math

# Input
typed_keys = input()

# x = Length of new String
# y = Offset of index for operations
x,y = -1,0

# List for the Answer, will be made a string
myStr = []

# Iterate through characters in the typed keys
for char in typed_keys:
    
    if char == "<":
        # Cursor is set back once 
        # Offset is decremented as long as cursor 
        # is not at begining of the new string (index 0)
        if x+y>-1:
            y -= 1
    
    elif char == ">":
        # Cursor is forwarded once 
        # Offset is incremented as long as cursor 
        # is not at the end of the new string (index = len(myStr))
        if y!=0:
            y += 1

    elif char == "-":
        # One character is backspaced 
        # Remove whatever the cursor is right infront and 
        # Decrement the cursors position
        if x > -1:
            myStr.pop(x+y)
            x -= 1
    else:
        # A new character is typed
        # Increment cursor and 
        # add character where the cursor is
        x += 1
        myStr.insert(x+y,char)
        
# Print the list of characters joined into a string
print("".join(myStr))