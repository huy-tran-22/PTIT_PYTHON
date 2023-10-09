n = int(input())
lis = [int(i) for i in input().split()]

i,cnt = 1,0
while (i < n):
    if (lis[i] != lis[i-1]):
        cnt += 1
    i += 1
print(cnt)
    