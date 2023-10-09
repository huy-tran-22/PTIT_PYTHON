global a,k,n

def sinh():
    i = k
    while (i > 1 and a[i] == n-k+i):
        i -= 1
    if i == 1:
        return
    a[i] += 1
    for i in range (i+1 , n+1):
        a[i] = a[i-1] + 1

l,k = [int(i) for i in input().split()]
for i in range (1,l+1):
    a[i] = int(input())  