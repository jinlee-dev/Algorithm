import sys
from collections import deque

v, e = map(int, sys.stdin.readline().split(" "))

l = [[] for i in range(v + 1)]

for i in range(e):
    s, e = map(int, sys.stdin.readline().split(" "))
    l[s].append(e)
    l[e].append(s)

isVisited = [0 for i in range(v + 1)]
ret = 0
bfs = deque()
for i in range(1, v + 1):
    if isVisited[i] == False:
        bfs.append(i)
        isVisited[i] = True
        while len(bfs) != 0:
            pv = bfs.popleft()
            for j in l[pv]:
                if isVisited[j] == False:
                    bfs.append(j)
                    isVisited[j] = True
        ret += 1

print(ret)