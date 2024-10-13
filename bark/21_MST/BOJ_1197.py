import sys
import heapq

V, E = map(int, sys.stdin.readline().split(" "))
graph = []
g = [[] for _ in range(V + 1)]
isVisited = [False for _ in range(V + 1)]
minVal = (0, 0, 0)
for i in range(E):
    s, e, d = map(int, sys.stdin.readline().split(" "))
    g[s].append((e, d))
    g[e].append((s, d))
    if minVal[1] == 0:
        minVal = (d, s, e)
    elif d < minVal[0]:
        minVal = (d, s, e)

for i in g[minVal[1]]:
    heapq.heappush(graph, (i[1], minVal[1], i[0]))

ret = 0
while 0 != len(graph):
    v = heapq.heappop(graph)
    if isVisited[v[1]] == True and isVisited[v[2]] == True:
        continue
    isVisited[v[1]] = True
    isVisited[v[2]] = True
    ret += v[0]
    for i in g[v[2]]:
        if isVisited[i[0]] == False:
            heapq.heappush(graph, (i[1], v[2], i[0]))

print(ret)

