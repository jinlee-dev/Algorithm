import sys
sys.setrecursionlimit(10 ** 6)

global order
order = 0

def DFS(g, isVisited, start, ret):
    global order
    isVisited[start] = True
    order = order + 1
    ret[start] = order
    for i in g[start]:
        if False == isVisited[i]:
            isVisited[i] = True
            DFS(g, isVisited, i, ret)

vertexCnt, linkCnt, start = map(int, sys.stdin.readline().split(' '))

isVisited = [False] * (vertexCnt + 1)
graph = [[] for m in range(vertexCnt + 1)]
for i in range(linkCnt):
    a, b = map(int, sys.stdin.readline().split(' '))
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

ret = {}
for i in range(1, vertexCnt + 1):
    ret[i] = 0

DFS(graph, isVisited, start, ret)

for i in ret.values():
    print(i, end="\n")