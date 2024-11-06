import sys
import heapq

def dijkstra(meetRoom, l, N, dist):
    q = []
    for i in meetRoom:
        heapq.heappush(q, (0, i))
        dist[i] = 0

    while len(q):
        v = heapq.heappop(q)
        if dist[v[1]] < v[0]:
            continue
        else:
            for end, c in l[v[1]]:
                cost = dist[v[1]] + c
                if cost < dist[end]:
                    dist[end] = cost
                    heapq.heappush(q, (cost, end))

N, M, K = map(int,sys.stdin.readline().split(" "))
l = [[] for _ in range(N + 1)]

for i in range(M):
    st, et, ct = map(int,sys.stdin.readline().split(" "))
    l[et].append((st, ct))

meetingRoom = list(map(int,sys.stdin.readline().split(" ")))

dist = [1e11 for _ in range(N + 1)]
dijkstra(meetingRoom, l, N, dist)
max_start, max_cost = 0, 0

for i, r in enumerate(dist):
    if r > max_cost and r != int(1e11):
        max_start, max_cost = i, r
print(max_start)
print(max_cost)