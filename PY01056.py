import math
def snt (n):
    if (n < 2):
        return False
    for i in range (2, int(math.sqrt(n)) + 1):
        if n % 2 == 0:
            return False
    return True

def solve (s):
    t = 0
    for i in range (0,len(s)):
        t += int(s[i])
        if (i % 2 == 0 and int(s[i]) % 2 != 0):
            return False
        elif (i % 2 != 0 and int(s[i]) % 2 == 0):
            return False
    if (snt(t) == True):
        return True
    return False

for t in range (int(input())):
    s = input()
    if solve (s):
        print("YES")
    else :
        print("NO")