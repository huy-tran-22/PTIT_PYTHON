n = int(input())
a = sorted([int(i) for i in input().split()])
if (a[0] > 1):
    print(a[0] - 1)
else:
    ok = 0
    for i in range (n-1):
        if (a[i] != a[i+1]-1):
            print(a[i]+1)
            ok = 1
            break
    if (ok == 0):
        print(a[n-1] + 1)