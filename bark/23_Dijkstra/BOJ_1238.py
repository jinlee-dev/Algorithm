import sys
import heapq

N, M, X = map(int, sys.stdin.readline().split(" "))

g = [[] for _ in range(N + 1)]

for i in range(M):
    s, e, c = map(int, sys.stdin.readline().split(" "))
    g[s].append((e, c))

def dijkstra(N, g, start, end):
    dist = [1e9 for _ in range(N + 1)] 
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while len(q):
        v = heapq.heappop(q)
        if dist[v[1]] < v[0]:
            continue
        for i in g[v[1]]:
            cost = dist[v[1]] + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (i[1], i[0]))
    
    return dist[end]

maxVal = 0
for start in range(1, N + 1):
    ret = dijkstra(N, g, start, X)
    ret += dijkstra(N, g, X, start)
    if ret > maxVal:
        maxVal = ret
    
print(maxVal)

