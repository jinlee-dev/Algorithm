import sys
N, M = map(int, sys.stdin.readline().split(" "))
l = [int(sys.stdin.readline()) for i in range(N)]

l.sort()

minDist = 2000000001

for i in range(1, N):
    comp = i - 1
    s = i
    e = len(l) - 1
    while s < e:
        mid = (s + e) // 2

        if l[mid] - l[comp] >= M:
            e = mid
        else:
            s = mid + 1
    
    ret = l[s] - l[comp]
    if ret >= M and ret < minDist:
            minDist = ret

print(minDist)