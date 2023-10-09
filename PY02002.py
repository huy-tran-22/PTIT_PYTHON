fibo = []
fibo.append(1)
fibo.append(1)
for i in range (2,93):
    fibo.append(fibo[i-1] + fibo[i-2])

for t in range (int(input())):
    a,b = [int(i) for i in input().split()]
    for i in range (a,b+1):
        print(fibo[i-1], end = " ")
    print(  )