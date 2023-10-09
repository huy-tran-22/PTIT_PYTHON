for t in range (int(input())):
    s = input() + '!'
    cnt,tmp = 0,s[0]
    res = ""
    for i in s:
        if i == tmp:
            cnt += 1
        else:
            res = res + str(cnt) + tmp
            cnt,tmp = 1,i 
    print(res)
