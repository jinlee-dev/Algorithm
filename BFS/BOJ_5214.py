import sys
from collections import deque
N, C, M = map(int, sys.stdin.readline().split(" "))
g = [[] for _ in range(N + 1)]
isVisited = [100001 for _ in range(N + 1)]
tube = []
for i in range(M):
    l = list(map(int, sys.stdin.readline().split(" ")))
    tube.append(l)
    for j in range(C):
        start = l[j]
        g[start].append(i)

dq = deque()
dq.append(1)
isVisited[1] = 1
while dq:
    v = dq.popleft()
    for j in g[v]:
        for i in tube[j]:
            if i != v and isVisited[i] == 100001:
                isVisited[i] = isVisited[v] + 1
                dq.append(i)

print(-1 if isVisited[N] == 100001 else isVisited[N])