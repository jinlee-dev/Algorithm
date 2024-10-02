import sys
import heapq

cnt = int(sys.stdin.readline())

for i in range(cnt):
    tCnt = int(sys.stdin.readline())
    l = list(map(int, sys.stdin.readline().split(" ")))
    heapq.heapify(l)
    ret = 0
    while(len(l) > 1):
        v1 = heapq.heappop(l)
        v2 = heapq.heappop(l)
        curRet = v1 + v2
        heapq.heappush(l, curRet)
        ret += curRet
    print(ret)