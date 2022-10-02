from collections import deque
import sys

def BFS(count, graph, x, y, isVisited, dir):
    dCnt = 0
    if False == isVisited[x][y] and 1 == graph[x][y]:
        q = deque()
        q.append((x, y))
        dCnt = 1
        isVisited[x][y] = True
        while 0 != len(q):
            v = q.popleft()
            qx = v[0]
            qy = v[1]
            for i in dir:
                ax = qx + i[0]
                ay = qy + i[1]
                if ax >= 0 and ay >= 0 and ax < count and ay < count and False == isVisited[ax][ay] and 1 == graph[ax][ay]:
                    isVisited[ax][ay] = True
                    q.append((ax, ay))
                    dCnt = dCnt + 1
    return dCnt

count = int(input())
isVisited = [[]  for m in range(count + 1)]
graph = [[] for m in range(count + 1)]

for i in range(count):
    n = list(sys.stdin.readline().rstrip())
    for j in n:
        graph[i].append(int(j))
        isVisited[i].append(False)

direction = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
]

houseCnt = []
for x in range(count):
    for y in range(count):
        ret = BFS(count, graph, x, y, isVisited, direction)
        if 0 != ret:
            houseCnt.append(ret)

houseCnt.sort()
print(len(houseCnt))
for i in houseCnt:
    print(i)