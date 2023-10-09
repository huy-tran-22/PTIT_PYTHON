import math
def check(n):
    for i in range (2,int(math.sqrt(n))+1):
        while (n % i == 0):
            n/=i
    return n

for t in range (int(input())):
    n = int(input())
    if (check(n) <= 5):
        print(n)
    else:
        print("Not in sequence")