import sys
import heapq

i = int(sys.stdin.readline())
l = []
popCnt = 0
min = 1e9
pPopCnt = (i * i) - i + 1
for t in range(i):
    min = 1e9
    v = list(map(int, sys.stdin.readline().split(" ")))
    for j in v:
        heapq.heappush(l, j)
        if min > j:
            min = j
        
    while popCnt != pPopCnt:
        p = heapq.heappop(l)
        popCnt += 1
        if p == min:
            break

while popCnt != pPopCnt:
    min = heapq.heappop(l)
    popCnt += 1 

print(min)