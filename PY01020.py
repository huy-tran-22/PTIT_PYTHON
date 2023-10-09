for t in range (int(input())):
    s = input()
    if (s[:len(s)-3:-1] == "68"):
        print("YES")
    else:
        print("NO")