import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split(" "))
l = [[] for _ in range(N + 1)]
indegree = [0 for _ in range(N + 1)]
for i in range(M):
    tl = list(map(int, sys.stdin.readline().split(" ")))
    for i in range(1, tl[0]):
        l[tl[i]].append(tl[i + 1])
        indegree[tl[i + 1]] += 1

q = deque()
answer = []
for i in range (1, N + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    s = q.popleft()
    answer.append(s)
    for i in l[s]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

if len(answer) != N:
    print(0)
else:
    print('\n'.join(map(str, answer)))
