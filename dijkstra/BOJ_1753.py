import sys
import heapq

global inf
inf = 1e9

def Dijkstra( graph, dist, start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        distance, cur = heapq.heappop(q)
        if dist[cur] < distance:
            continue
        for i in graph[cur]:
            cost = distance + i[1]
            if cost < dist[i[0]] :
                dist[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

vertexCnt, linkCnt = map(int, sys.stdin.readline().split(" "))
start = int(sys.stdin.readline())

dist = [inf] * (vertexCnt + 1)
graph = [[] for m in range(vertexCnt + 1)]

for i in range(linkCnt):
    fromIdx, toIndx, distance = map(int, sys.stdin.readline().split(" "))
    graph[fromIdx].append((toIndx, distance))

Dijkstra( graph, dist, start)
for i in dist[1:]:
    if i == inf:
        print("INF")
    else:
        print(i)

