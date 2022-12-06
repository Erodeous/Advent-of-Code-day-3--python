import sys
s = [x.strip() for x in sys.stdin]
score=0
def getSame(s):
    for i in s:
        firstpart  = s[:len(s)//2]
        secondpart = s[len(s)//2 if len(s)%2 == 0 else ((len(s)//2)+1):]
        if i in firstpart and i in secondpart:
            if i==(i.upper()): return ord(i)-64+26
            else:
                return ord(i)-96
for j in range(len(s)):
    score+=(getSame(s[j]))
print(score)