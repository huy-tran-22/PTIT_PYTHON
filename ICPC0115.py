for t in range (int(input())):
    n = int(input())
    s = str(n)
    tong = 0
    for i in s:
        tmp = 1
        for j in range (1,int(i)+1):
            tmp *= j
        tong += tmp
    if tong == n:
        print("Yes")
    else:
        print ("No")