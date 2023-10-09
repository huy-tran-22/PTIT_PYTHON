def check(s):
    if len(s) < 3:
        return "NO"
    for i in range (s.index(max(s)), 0,-1):
        if int(s[i]) <= int(s[i-1]):
            return "NO"
    for i in range (s.index(max(s)), len(s)-1):
        if int(s[i]) <= int(s[i+1]):
            return "NO"
    return "YES"

for t in range (int(input())):
    s = input()
    print(check(s))