'''
Puzzle URL: https://www.codingame.com/training/easy/temperatures
'''
import sys
import math

n = int(input())  # the number of temperatures to analyse
absLow = 5527

for i in input().split():
    
    t = int(i) # t: a temperature expressed as an integer ranging from -273 to 5526
    
    # Check if we have gone through all given temps
    if n > 0:
        # Double Ternary:
        # Use the new Temp if it is closer to zero
        # Use the absoltue value of the current lowest temp if they have equal absolute values and one or both are positive
        # Use the value of the lowest temp if the absolute values of both are equal but they are both negative
        absLow = t if abs(t) < abs(absLow) else abs(absLow) if abs(t) == abs(absLow) and (t > 0 or absLow > 0) else absLow

    # Decrement counter
    n -=1

# If the counter is zero and the temp has not changed from default send 0
if n == 0 and absLow == 5527:
        absLow = 0

print(int(absLow))
