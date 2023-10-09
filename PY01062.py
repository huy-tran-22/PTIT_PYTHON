import math

def snt (n):
    if n < 2: 
        return 0
    for i in range (2, int(math.sqrt(n))+1):
        if n % i == 0:
            return 0
    return 1

def solve(s):
    if (snt(len(s)) == 0):
        return 0
    cnt = 0    
    for i in range (len(s)):
        if s[i] == '2' or s[i] == '3' or s[i] == '5' or s[i] == '7':
            cnt += 1
    if cnt <= len(s) - cnt:
        return 0
    return 1

for t in range (int(input())):
    s = input()
    if solve(s) == 1:
        print("YES")
    else:
        print("NO")
             
    