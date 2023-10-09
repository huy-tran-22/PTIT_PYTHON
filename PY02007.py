check = [0] * 43
cnt = 0
n = 10
while (n != 0):
    a = [int(i) for i in input().split()]
    n -= len(a)
    for i in a:
        if check[i % 42] == 0:
            cnt += 1
            check[i % 42] = 1
print(cnt)

