import sys
import heapq

n, m, f, t, budget = map(int, sys.stdin.readline().split(" "))

g = [[] for _ in range(n + 1)]

for i in range(m):
    s, e, v = map(int, sys.stdin.readline().split(" "))
    g[s].append((e, v))
    g[e].append((s, v))

dist = [[-1, 0] for _ in range(n + 1)]
pq = []

# 수치심, 현재 인덱스, 예산
heapq.heappush(pq, (0, f, budget))

# 수치심, 남은 예산
dist[f] = [-1, budget]

while pq:
    s, f, bud = heapq.heappop(pq)
    if dist[f][0] != 0 and dist[f][0] < s and dist[f][1] > bud :
        continue
    for idx, value in g[f]:
        curBud = bud - value
        suchi = max(s, value)
        if curBud >= 0 and ((dist[idx][0] == -1) or (suchi < dist[idx][0])):
            dist[idx][0] = suchi
            dist[idx][1] = curBud
            
            heapq.heappush(pq, (suchi, idx, curBud))

print(dist[t][0])