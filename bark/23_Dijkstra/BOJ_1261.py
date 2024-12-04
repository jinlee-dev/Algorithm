import sys
import heapq

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

x, y = map(int, sys.stdin.readline().split(" "))
l = [[] for _ in range(y)]
for i in range(y):
    v = str(sys.stdin.readline().rstrip())
    for j in str(v):
        l[i].append(int(j))

q = []
dist = [[1e9 for _ in range(x)] for _ in range(y)]
heapq.heappush(q, (0, (0, 0)))
dist[0][0] = 0
while len(q):
    pop = heapq.heappop(q)
    c, coord = pop[0], pop[1]
    if dist[coord[0]][coord[1]] < c:
        continue
    else:
        for k in range(4):
            cx, cy = (coord[0] + dx[k], coord[1] + dy[k])
            if cy >= 0 and cy < x and cx >= 0 and cx < y:
                cost = l[cx][cy] + dist[coord[0]][coord[1]]
                if cost < dist[cx][cy]:
                    dist[cx][cy] = cost
                    heapq.heappush(q, (l[cx][cy], (cx, cy)))

print(dist[y - 1][x - 1])