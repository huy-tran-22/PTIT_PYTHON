for t in range(int(input())):
    p,q = input().split()
    ip = input().split()
    if len(ip) == 1:
        x1 = ip[0]
        x2 = input()
    else:
        x1,x2 = ip
    t1 = int(x1.replace(p,q)) + int(x2.replace(p,q))
    t2 = int(x1.replace(q,p)) + int(x2.replace(q,p))
    print(min(t1,t2), max(t1,t2))
