'''
unfinished
https://www.codingame.com/training/easy/unary
'''

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()
print(ord("z"), file=sys.stderr, flush=True)
print(message, file=sys.stderr, flush=True)
print("---", file=sys.stderr, flush=True)

ans = []
full_ans = ""
br = ""
for letter in message:
    
    lav = ord(letter)
    
    br += "1" if lav > 64 else "0" # 64
    br += "1" if (lav % 64) > 32 else "0" # 32
    br += "1" if (lav % 32) >= 16 else "0" # 16
    br += "1" if (lav % 16) >= 8 else "0" # 8
    br += "1" if (lav % 8) >= 4 else "0" # 4
    br += "1" if (lav % 4) >= 2 else "0" # 2
    br += "1" if (lav % 2) >= 1 else "0" # 1

    print("BR: "+br+"\nletter: "+letter, file=sys.stderr, flush=True)
print("BR: "+br, file=sys.stderr, flush=True)

savedSymbol = "z"
savedSymbolNum = 1
curSymbol = "zz"

for x in range(len(br)):
    if savedSymbol != br[x]:
        curSymbol = "0" if br[x] == "1" else "00"
        
        if x != 0 or x == (len(br)-1):
            ans.append("0"*savedSymbolNum)
            savedSymbolNum = 1
        ans.append(curSymbol)
        savedSymbol = br[x]
        savedSymbolNum = 1

        if x == (len(br)-1):
            ans.append("0"*savedSymbolNum)
        continue
        
    if savedSymbol == br[x]:
        savedSymbolNum += 1
        if x == (len(br)-1):
            ans.append("0"*savedSymbolNum)

print(" ".join(ans))