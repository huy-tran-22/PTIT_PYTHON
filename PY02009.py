t = int(input())
for i in range (t):
    m = int(input())
    lis = [0] * 1001
    for k in range (m):
        x = int(input())
        lis[x] += 1
    maxx = 0
    for j in range (1001):
        maxx = max(maxx,lis[j])
    for j in range (1001):
        if maxx == lis[j]:
            print(j)
            break
    
# 3
# 3
# 999
# 999
# 19