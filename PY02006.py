def check(a,b,n):
    for i in range (n):
        if (a[i] > b[i]):
            return 0
    return 1

for t in range (int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    b = [int(i) for i in input().split()]
    b.sort()
    if (check(a,b,n) == 1):
        print("YES")
    else:
        print("NO")
    
