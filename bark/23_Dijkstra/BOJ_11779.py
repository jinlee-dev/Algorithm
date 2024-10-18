import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

g = [[] for _ in range(N + 1)]
dist = [1e9 for _ in range(N + 1)]
prev = [0 for _ in range(N + 1)]

for i in range(M):
    s, e, c = map(int, sys.stdin.readline().split(" "))
    g[s].append((e, c))

start, end = map(int, sys.stdin.readline().split(" "))
q = []

heapq.heappush(q, (0, start))
prev[start] = 0
dist[start] = 0

while len(q):
    v = heapq.heappop(q)
    if dist[v[1]] < v[0]:
        continue
    else:
        for i in g[v[1]]:
            cost = i[1] + dist[v[1]]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                prev[i[0]] = v[1]
                heapq.heappush(q, (i[1], i[0]))

print(dist[end])
ret = []
idx = end

while idx != 0:
    ret.append(idx)
    idx = prev[idx]

print(len(ret))
for i in range(len(ret) - 1, -1, -1):
    print(ret[i], end = " ")