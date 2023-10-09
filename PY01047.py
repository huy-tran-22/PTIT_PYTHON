import math

def snt(n):
    if n < 2:
        return False
    for i in range (2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

for t in range (int(input())):
    s = input()
    tmp = int(s[len(s)-4 : len(s)])
    if snt(tmp):
        print("YES")
        
    else:
        print("NO")