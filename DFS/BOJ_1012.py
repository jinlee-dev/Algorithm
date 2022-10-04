import sys
sys.setrecursionlimit(10 ** 6)

def DFS(g, isVisited, lrtb, x, y, xMax, yMax):
    if x >= 0 and y >= 0 and x < xMax and y < yMax and 0 < graph[x].count(y) and False == isVisited[x][y]:
        isVisited[x][y] = True
        for i in lrtb:
            ax = x + i[0]
            ay = y + i[1]
            DFS(g, isVisited, lrtb, ax, ay, xMax, yMax)
        return 1
    else:
        return 0

tc = int(sys.stdin.readline())
lrtb = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

ret = []
for i in range(tc):
    w, h, count = map(int,sys.stdin.readline().split())
    isVisited = [[False] * (h + 1) for m in range(w + 1)]
    graph = [[] for m in range(w + 1)]
    curRet = 0
    for c in range(count):
        x, y = map(int,sys.stdin.readline().split())
        graph[x].append(y)
    for cx in range(w):
        for cy in range(h):
            curRet = curRet + DFS(graph, isVisited, lrtb, cx, cy, w, h)
    ret.append(curRet)

for i in ret:
    print(i)