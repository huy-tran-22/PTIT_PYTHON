def GCD(a,b):
    if a == 0 or b == 0:
        return a+b
    while (b != 0):
        tmp = a % b
        a = b
        b = tmp
    return a

for t in range (int(input())):
    s = input()
    s2 = s[::-1]
    if (GCD(int(s),int(s2)) == 1):
        print("YES")
    else:
        print("NO")