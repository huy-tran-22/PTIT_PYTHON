import math
def solve (n):
    t = 0
    for i in n:
        t += int(i)
    if t % 3 == 0:
        return True
    return False


for t in range (int(input())):
    s = input()
    if solve(s):
        print("YES")
    else:
        print("NO")