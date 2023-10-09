import math

def snt (n):
    if (n < 2):
        return False
    for i in range (2, int(math.sqrt(n))+1):
         if n % i == 0:
             return False
    return True

def solve (s):
    if (snt(len(s)) == False):
        return False
    nt = 0
    knt = 0
    for i in s:
        if snt(int(i)) == True:
            nt += 1
        else:
            knt += 1
    if nt < knt or nt == knt:
        return False
    return True

for t in range (int(input())):
    s = input()
    if solve (s) == True:
        print("YES")
    else:
        print("NO")
    
    