for t in range (int(input())):
    n = int(input())
    t = 0
    for i in range (2 - n%2 , n+1 , 2):
        t += 1/i
    print("{:.6f}".format(t))