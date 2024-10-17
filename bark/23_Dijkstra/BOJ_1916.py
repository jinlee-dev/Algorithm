import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

g = [[] for _ in range(N + 1)]
dist = [1e9 for _ in range(N + 1)]

for i in range(M):
    s, e, c = map(int, sys.stdin.readline().split(" "))
    g[s].append((e, c))

start, end = map(int, sys.stdin.readline().split(" "))
q = []

# index, cost
heapq.heappush(q, (start, 0))
dist[start] = 0
while len(q):
    v = heapq.heappop(q)
    if dist[v[0]] < v[1]:
        continue
    for i in g[v[0]]:
        e, c = i[0], i[1]
        cost = c + dist[v[0]]
        if cost < dist[e]:
            dist[e] = cost
            heapq.heappush(q, (e, c))

print(dist[end])