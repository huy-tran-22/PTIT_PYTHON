from math import sqrt


def snt(n):
    if int(n) < 2:
        return False
    for i in range (2, int(sqrt(int(n)))+1):
        if (int(n) % i == 0):
            return False
    return True

for t in range (int(input())):
    n = int(input())
    s = str(n)
    if (snt(n) == False or snt(int(s[::-1])) == False):
        print("No")
    else :
        tong = sum(int(i) for i in s)
        ok = 1
        for i in s:
            if snt(i) == False:
                ok = 0
                break
        if ok == 0 or snt(tong) == False:
            print("No")
        else:
            print("Yes")