import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split(" ")))

A.sort()
ret = 0

for i in range(len(A)):
    num = A[i]
    for j in range(0, i - 1):
        curVal = A[j]
        s = 0
        e = i
        
        curRet = False
        while s <= e:
            m = (s + e) // 2

            pv = (curVal + A[m])
            if num == pv:
                curRet = True
                break
                
            else:
                if pv < num:
                    s = m + 1
                else:
                    e = m - 1
        
        if curRet == True:
            ret = ret + 1
            break

print(ret)