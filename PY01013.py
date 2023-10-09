from math import *

def snt(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range (2 , int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def GCD(a,b):
    if a == 0 or b == 0:
        return a+b
    while b != 0:
        tmp = a%b
        a = b
        b = tmp
    return a

for t in range (int (input())):
    a,b = map(int,input().split())
    c = str(GCD(a,b))
    d = sum(int(i) for i in c)
    if snt(d):
        print("YES")
    else :
        print("NO")

