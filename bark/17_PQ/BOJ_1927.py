import sys
import heapq

v = int(sys.stdin.readline())
l = []

for i in range(v):
    t = int(sys.stdin.readline())
    if t == 0:
        if len(l) == 0:
            print(0)
        else:
            print(heapq.heappop(l))
    else:
        heapq.heappush(l, t)