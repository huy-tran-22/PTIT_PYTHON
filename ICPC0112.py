MAX = int(1e6 + 1)
snt = [1] * MAX

snt[0] = 0
snt[1] = 0
for i in range (1000):
    if (snt[i]):
        for j in range(i*i, MAX, i):
            snt[j] = 0

for t in range (int(input())):
    cnt = 0
    for i in range (int(input()) - 5):
        if snt[i] and snt[i+6]:
            if snt[i+2] or snt[i+4]:
                cnt += 1
    print(cnt)