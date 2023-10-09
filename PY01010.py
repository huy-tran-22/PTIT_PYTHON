for t in range (int(input())):
    s = input()
    if s[0:2] == s[len(s)-2:]:
        print("YES")
    else:
        print("NO")