global vs,n,str

def solve (s):
    if len(s) == n:
        print(s)
        return
    for i in range (n):
        if vs[i] == 0:
            vs[i] = 1
            solve(s + str[i])
            vs[i] = 0

str = input()
n = len(str)
vs = [0] * n
solve("")