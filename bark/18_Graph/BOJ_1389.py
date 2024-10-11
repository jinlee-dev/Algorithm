import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split(" "))
bacon = [[(0) for _ in range(N + 1)] for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]

for i in range(M):
    s, e = map(int, sys.stdin.readline().split(" "))
    graph[s].append(e)
    graph[e].append(s)


for i in range(1, N + 1):
    d = deque()
    d.append((i, 0))
    while len(d) != 0:
        t = d.popleft()
        depth = t[1] + 1
        for v in graph[t[0]]:
            if bacon[i][v] == 0:
                bacon[i][v] = depth
                d.append((v, depth))

baconRet = [0]
minVal = 1e9
minIdx = 0
for i in range(1, N + 1):
    baconSum = 0
    for j in range(1, N + 1):
        baconSum += bacon[j][i]
    baconRet.append(baconSum)
    if baconSum < minVal:
        minVal = baconSum
        minIdx = i

print(minIdx)
