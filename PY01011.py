def So_Thuan_Nghich(n):
    s = str(n)
    if (s != s[::-1] or len(s) % 2 == 1):
        return False
    for i in s:
        if int(i) % 2 != 0:
            return False
    return True

for t in range(int(input())):
    for i in range (22, int(input()), 2):
        if So_Thuan_Nghich(i):
            print(i, end = " ")
    print()