import sys
import heapq

cnt = int(sys.stdin.readline())

l = []
for i in range (cnt):
    heapq.heappush(l, int(sys.stdin.readline()))

ret = 0
if len(l) == 1:
    print(0)
else:
    while len(l):
        v1 = heapq.heappop(l)
        v2 = heapq.heappop(l)
        ret += (v1 + v2)
        if len(l):
            heapq.heappush(l, (v1 + v2))
    print(ret)