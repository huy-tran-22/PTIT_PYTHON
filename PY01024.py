def check(s):
    t = 0
    for i in range (0, len(s)-1):
        t += int(s[i])
        if abs(int(s[i]) - int(s[i+1])) != 2:
            return 0
    t += int(s[len(s)-1])   
    if t % 10 != 0:
        return 0
    return 1

for t in range(int(input())):
    s = input()
    if check(s) == 0:
        print("NO")
    else :
        print("YES")

