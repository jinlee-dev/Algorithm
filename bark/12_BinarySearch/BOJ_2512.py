import sys

N = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split(" ")))
M = int(sys.stdin.readline())

s = 1
e = 1000000000
l.sort()
answer = 0
lenL = len(l)
if sum(l) <= M:
    print(l[lenL - 1])
else:
    while s <= e:
        mid = (s + e) // 2
        ret = 0
        for i in l:
            ret = ret + min(mid, i)
        if ret <= M:
            answer = mid
            s = mid + 1
        else:
            e = mid - 1

    print(answer)