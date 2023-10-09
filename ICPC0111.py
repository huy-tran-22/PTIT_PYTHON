t = int (input())
while ( t > 0):
    n,a = map(int,input().split())
    l = [int(i) for i in input().split()]
    print(*(l[a:] + l[:a]))
    t -= 1
    