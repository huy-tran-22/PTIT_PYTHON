from math import gcd

n,k = [int(i) for i in input().split()]
cnt = 1
for i in range(pow(10,k-1), pow(10,k)-1):
    if (gcd(n,i) == 1):
        print(i,end = " ")
        if cnt % 10 == 0:
            print()
        cnt += 1
        