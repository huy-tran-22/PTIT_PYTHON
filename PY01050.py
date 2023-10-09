def solve(s,n,a,b,c):
    if (len(s) == n and a > 0 and b >= a and c >= b):
        print(s)
    if (len(s) < n):
        solve(s + "A", n,a+1,b,c)
        solve(s + "B", n,a,b+1,c)
        solve(s + "C", n,a,b,c+1)


n = int(input())
for i in range (3,n+1):
    solve("",i,0,0,0)

    