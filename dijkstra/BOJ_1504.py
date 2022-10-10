import sys
import heapq

global INF
INF = int(1e9)

def Dijkstra(startIdx, endIdx, graph):
    dist = [INF] * (vertexCnt + 1)
    q = []
    dist[startIdx] = 0
    heapq.heappush(q, (0, startIdx))
    while q:
        distance, curIdx = map(int, heapq.heappop(q))
        if distance > dist[curIdx]:
            continue
        else:
            for i in graph[curIdx]:
                curDist = i[1]
                nextIdx = i[0]
                cost = curDist + distance
                if cost < dist[nextIdx]:
                    dist[nextIdx] = cost
                    heapq.heappush(q, (cost, nextIdx))
    return dist[endIdx]

vertexCnt, linkCnt = map(int, sys.stdin.readline().split(" "))
graph = [[] for _ in range(vertexCnt + 1)]


for _ in range(linkCnt):
    s, e, cost = map(int, sys.stdin.readline().split(" "))
    graph[s].append((e, cost))
    graph[e].append((s, cost))

distSum = -1
interDest1, interDest2 = map(int, sys.stdin.readline().split(" "))

result = min( Dijkstra(1, interDest1, graph) + Dijkstra(interDest1, interDest2, graph) + Dijkstra(interDest2, vertexCnt, graph),
             Dijkstra(1, interDest2, graph) + Dijkstra(interDest2, interDest1, graph) + Dijkstra(interDest1, vertexCnt, graph) )
print("-1" if result >= INF else result)
