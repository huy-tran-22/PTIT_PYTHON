P = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ_.")
while (True):
    inp = input()
    if (inp == '0'): 
        break
    k,s = inp.split()
    k = int(k)
    res = ""
    for i in s:
        tmp = P.index(i)
        res += P[(tmp+k) % 28]
    print(res[::-1])