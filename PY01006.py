def So_May_Man(s):
    for i in range(len(s)):
        if s[i] != '4' and s[i] != '7':
            return 'NO'
    return 'YES'


for t in range(int(input())):
    s = input()
    print(So_May_Man(s))