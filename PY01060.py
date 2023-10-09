for t in range (int(input())):
    s = input()
    c = 0
    l = 1
    ok = 0
    for i in range (0,len(s)):
        if i % 2 == 1:
            c += int(s[i])
        else:
            if s[i] != "0":
                l *= int(s[i])
                ok = 1
    
    print(l,end = " ")
    if ok == 1:
        print(c)
    else:
        print("0")