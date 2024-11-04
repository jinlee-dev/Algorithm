import sys
import heapq

N = int(sys.stdin.readline())
v = [int(sys.stdin.readline()) for _ in range(N)]
isVisited = [False for _ in range(N)]
W = []
minVal = v[0]
minIdx = 0

q = []
# 직접 뚫어보자
for i in range(N):
    tl = list(map(int, sys.stdin.readline().split(" ")))
    W.append(tl)
    heapq.heappush(q, (v[i], i, i))

count = 0
ret = 0
while count < N:
    v = heapq.heappop(q)
    if  isVisited[v[1]] == True and  isVisited[v[2]] == True:
        continue
    isVisited[v[1]] = True
    isVisited[v[2]] = True
    ret += v[0]
    count += 1
    for i in range(N):
        if isVisited[i] == False:
            heapq.heappush(q, (W[v[2]][i], v[2], i))

print(ret)