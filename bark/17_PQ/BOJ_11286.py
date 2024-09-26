import heapq
import sys

ic = int(sys.stdin.readline())

l = []
for i in range(ic):
    ic = int(sys.stdin.readline())
    if ic != 0:
        heapq.heappush(l, (abs(ic), ic))
    else:
        if len(l) != 0:
            v = heapq.heappop(l)
            print(v[1])
        else:
            print(0)