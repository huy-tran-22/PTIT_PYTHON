for t in range (int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    if n == 1:
        print(a[0])
    else :
        res,m,ans = {},1,a[0]
        for i in a:
            if i in res:
                res[i] += 1
                if res[i] > m:
                    m = res[i]
                    ans = i
            else:
                res[i] = 1
        if 2 * m > n:
            print(ans)
        else:
            print("NO")
        