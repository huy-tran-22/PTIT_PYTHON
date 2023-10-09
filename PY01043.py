def TN(n):
    res = str(n)
    if len(res) % 2 != 0:
        return 0
    for i in res:
        if int(i) % 2 != 0:
            return 0
    tmp = res[::-1]
    if res != tmp:
        return 0
    return 1

for t in range (int(input())):
    n = int(input())
    for i in range (22,n,2):
        if TN(i) == 1:
            print(i,end = " ")
    print()
    
        