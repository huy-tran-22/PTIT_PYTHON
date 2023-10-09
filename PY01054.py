def solve(s):
    res = 1
    for i in s:
        if i != "0":
            res *= int(i)
    return res

for t in range (int(input())):
    s = input()
    print(solve(s))
