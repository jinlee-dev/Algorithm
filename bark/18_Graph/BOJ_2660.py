import sys
from collections import deque

def bfs(graph, length, start, isVisited):
    deq = deque()
    deq.append((start, 0))
    while len(deq) != 0:
        t = deq.popleft()
        depth = t[1] + 1
        for i in graph[t[0]]:
            if isVisited[start][i] > depth:
                isVisited[start][i] = depth
                deq.append((i, depth))


v = int(sys.stdin.readline())
graph = [[] for i in range(v + 1)]
isVisited = [[v + 1 for k in range(v + 1)] for j in range(v + 1)]
isVisited[0][0] = v
while 1:
    st, et = map(int, sys.stdin.readline().split(" "))
    if st == -1 and et == -1:
        break
    graph[st].append(et)
    graph[et].append(st)

for i in range(1, v + 1):
    bfs(graph, v, i, isVisited)
    isVisited[i][i] = 0


cnt = 0
hubo = []
minVal = 1e9
isVisitedRet = [0]

for i in range(1, v + 1):
    maxVal = -1e9
    for j in range(1, v + 1):
        maxVal = max(maxVal, isVisited[j][i])
    isVisitedRet.append(maxVal)
    if minVal > maxVal:
        minVal = maxVal

for i in range(1, v + 1):
    if isVisitedRet[i] == minVal:
        cnt += 1
        hubo.append(i)

print(minVal, cnt)
for i in hubo:
    print(i, end=" ")