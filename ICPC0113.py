MAX = int(1e6+1)
SNT = [1] * MAX

SNT[0] = 0
SNT[1] = 0
for i in range (1000):
    if (SNT[i]):
        for j in range(i*i, MAX, i):
            SNT[j] = 0

for t in range (int(input())):
    vs = [1] * MAX
    n = int(input())
    for i in range(n):
        if SNT[i]:
            tmp = str(i)
            s = tmp[::-1]
            if(SNT[int(s)] and s != tmp and vs[i] and vs[int(s)] and int(s) < n):
                print(i, s, end = " ")
                vs[i] = 0
                vs[int(s)] = 0
    print()
            
            