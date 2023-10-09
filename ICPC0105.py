import re
for t in range (int(input())):
    s = input()
    l = re.findall('\d+',s)
    max = 0
    for i in l:
        if int(i) > max:
            max = int(i)
    print(max)
