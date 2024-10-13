import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split(" "))
d = deque()
l = [[] for _ in range(N + 1)]
indegree = [0 for _ in range (N + 1)]
for i in range(M):
    s, e = map(int, sys.stdin.readline().split(" "))
    l[s].append(e)
    indegree[e] += 1

for i in range(1, N + 1):
    if indegree[i] == 0:
        d.append(i)

while len(d) != 0:
    s = d.popleft()
    print(s, end=" ")

    for i in l[s]:
        indegree[i] -= 1
        if indegree[i] == 0:
            d.append(i)