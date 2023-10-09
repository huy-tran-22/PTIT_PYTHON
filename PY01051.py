def solve (n):
    t = 0
    for i in n:
        t += int(i)
    s = str(t)
    if (len(s) == 1):
        return False
    if s != s[::-1]:
        return False
    return True


for t in range (int(input())):
    s = input()
    if solve(s):
        print("YES")
    else:
        print("NO")