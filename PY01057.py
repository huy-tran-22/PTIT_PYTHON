import math

def snt(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return n > 1

def solve(s):
    for i in range(len(s)):
        if (snt(i) and not snt(int(s[i]))) or (not snt(i) and snt(int(s[i]))):
            return False
    return True

for t in range (int(input())):
    s = input()
    if solve(s):
        print("YES")
    else:
        print("NO")