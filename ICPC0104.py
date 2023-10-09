n = int(input())
while (n > 0):
    s = input()
    i = 0; a = 0; min = 100000
    while (i < len(s)):
        if (s[i].isdigit()):
            a = a * 10 + int(s[i])
        else:
            if (a != 0 and a < min):
                min = a
            a = 0
        i += 1
    print(min)
    n -= 1
    
            