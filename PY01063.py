import re
for t in range (int(input())):
    s = input()
    k = input()
    tmp = re.findall(k,s)
    print(len(tmp))
