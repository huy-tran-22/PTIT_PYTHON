import math
def solve (n):
    t = 0
    for i in n:
        t += int(i)
    if (t < 2):
        return False
    for i in range (2, int(math.sqrt(t))+1):
         if t % i == 0:
             return False
    return True


for t in range (int(input())):
    s = input()
    if solve(s):
        print("YES")
    else:
        print("NO")