'''
Puzzle URL: https://www.codingame.com/training/easy/gdq---binary-coded-decimal-clock
'''

import sys
import math

def makeAns(num):
    bZero = "_"*5
    bOne  = "#"*5
    l4 = bOne if num % 2 == 1 else bZero
    l3 = bOne if num in [2,3,6,7] else bZero
    l2 = bOne if 3 < num < 8 else bZero
    l1 = bOne if num > 7 else bZero
    return [l1, l2, l3 ,l4]

_input = input()

binArr = []

for numS in str(_input).replace(":", ""):
    print(numS, file=sys.stderr, flush=True)
    binArr.append(makeAns(int(numS)))

for i in range(4):
    line =  "|" + str(binArr[1][i])  
    line += "|" + str(binArr[2][i])  
    line += "|" + str(binArr[3][i]) 
    line += "|" + str(binArr[4][i])
    line += "|" + str(binArr[5][i])
    line += "|" + str(binArr[6][i])
    line += "|"

    print(line)
