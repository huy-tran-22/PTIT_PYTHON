t = int(input())
while (t > 0):
    n = int(input())
    l = sorted([int (i) for i in  input().split()])
    res = 0 
    for i in range(n-2):
        left = i+1; right= n-1
        while (left < right):
            tong = l[i] + l[left] + l[right]
            if tong == 0:
                res += 1
                left += 1
            elif tong < 0:
                left += 1
            else:
                right -= 1
                
    t -= 1
    print(res)
            
    