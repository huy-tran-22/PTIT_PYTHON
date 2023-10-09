import math
while (True):
    a = [int(i) for i in input().split()]
    if (a.count(0) == 4):
        break
    
    cnt = 0
    while (a[0] != a[1]  or a[1] != a[2] or a[2] != a[3] or a[3] != a[1]):
        tmp = a.copy()
        for i in range (0,3):
            a[i] = abs(tmp[i] - tmp[i+1])
        a[3] = abs(tmp[3] - tmp[0])
        cnt += 1
    print(cnt)