import sys
from collections import deque

global ind
ind = 1
def bfs(start, graph, order):
    global ind
    q = deque()
    q.append(start)
    isVisited[start] = True
    while q:
        cur = q.popleft()
        order[cur] = ind
        ind = ind + 1
        for i in graph[cur]:
            if isVisited[i] == 0:
                isVisited[i] = 1
                q.append(i)


import sys
n, m, start = map(int, sys.stdin.readline().split(" "))
isVisited = [False] * (n + 1)
graph = [[]  for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split(" "))
    graph[s].append(e)
    graph[e].append(s)

for i in graph:
    i.sort(reverse=True)
order = [0] * (n + 1)
bfs(start, graph, order)

for i in range(1,n+1):
    print(order[i])
