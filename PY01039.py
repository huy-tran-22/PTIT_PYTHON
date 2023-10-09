def check(s):
    for i in range(0,len(s)-2):
        if s[i] != s[i+2] or s[i] == s[i+1]:
            return 0
    return 1

for t in range (int(input())):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")