def check(n):
    for i in range(0,len(n)-1):
        if n[i] > n[i+1]:
            return False
    return True

for t in range(int(input())):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")