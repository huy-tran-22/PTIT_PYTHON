from math import *
MAX = int(1e6)

for t in range (int(input())):
    lis = [0]*MAX
    n = int(input())
    idm = 0
    ans = "1"
    for i in range (2 , int(sqrt(n)) + 1):
        if (n % i == 0):
            cnt = 0
            while (n % i == 0):
                cnt += 1
                n /= i
            ans += " * " + str(i) + "^" + str(cnt)
        if n == 1:
            break
    if n > 1:
        n = int(n)
        ans += " * " + str(n) + "^" + "1"
    print(ans)


