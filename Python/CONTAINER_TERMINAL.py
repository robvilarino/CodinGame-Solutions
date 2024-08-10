import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
cs = []
for i in range(n):
    line = input()
    print(line, file=sys.stderr, flush=True)
    cs.append(line)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
print(cs, file=sys.stderr, flush=True)

for order in cs:
    
    ans = 0
    con_stks = []
    
    print("\n"+order+"\n---", file=sys.stderr, flush=True)

    for i in range(len(order)):
        #print(i, file=sys.stderr, flush=True)
        if i == 0:
            con_stks.append(ord(order[i]))
            ans += 1
        else:
            orderVal = ord(order[i])
            #print(max(con_stks), file=sys.stderr, flush=True)
            if(orderVal > int(max(con_stks))):
                ans+=1
                con_stks.append(ord(order[i]))
            else:
                lowestIndex = 0
                lowestDiff = 1000
                for j in range(len(con_stks)):
                    currDiff = con_stks[j] - orderVal
                    if  lowestDiff > currDiff >= 0 : 
                        lowestDiff = con_stks[j] - orderVal
                        lowestIndex = j
                        print(lowestDiff, file=sys.stderr, flush=True)
                con_stks[lowestIndex] = orderVal
            
    print(con_stks, file=sys.stderr, flush=True)
    print(ans)
