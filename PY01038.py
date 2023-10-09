def solve(n):
    if n % 7 == 0:
        return n
    for i in range (0,1000):
        tmp = str(n)
        n += int(tmp[::-1])
        if (n % 7 == 0):
            return n
    return -1

for t in range (int(input())):
    n = int(input())
    print(solve(n))