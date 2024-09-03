'''
Puzzle URL: https://www.codingame.com/training/easy/horse-racing-duals
'''
import sys
import math

nums = []

n = int(input())
for i in range(n):
    pi = int(input())
    nums.append(pi)

nums.sort()
print(nums, file=sys.stderr, flush=True)

sDiff = 10000001
for x in range(len(nums)-1):
    cDiff = abs(nums[x]-nums[x+1])
    sDiff = cDiff if cDiff < sDiff else sDiff

print(sDiff)