import math
def snt(n):
    if n < 2:
        return 0
    for i in range (2 , int(math.sqrt(n)) +1):
        if (n % i == 0):
            return 0
    return 1

lis = [0,2,3]
tmp = 5
n,k = [int(i) for i in input().split()]
while (len(lis) <= n+1):
    if (snt(tmp) == 1):
        lis += [tmp]
    tmp += 2
res = [k]
for i in range(1,n+1):
    res += [res[i-1] + lis[i]]
for i in res:
    print(i,end = " ")
