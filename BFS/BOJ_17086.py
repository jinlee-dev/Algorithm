from collections import deque
import sys

def BFS(graph, isVisited, startIdx, n, m):
    if graph[startIdx[0]][startIdx[1]] == True:
        return 0

    q = deque()
    depth = 0
    q.append([[startIdx], depth])
    isVisited[startIdx[0]][startIdx[1]] = True
    dir = [
        [-1, 0],[1, 0],[-1, -1],[1, -1],
        [0, -1],[0, 1],[-1, 1],[1, 1] 
    ]

    minDepth = 0
    while q:
        v = q.popleft()
        for vt in v[0]:
            ret = [[], v[1] + 1]
            for d in dir:
                curLoc = [0, 0]
                curLoc[0] = vt[0] + d[0]
                curLoc[1] = vt[1] + d[1]
                lastDepth = v[1]
                if curLoc[0] >= 0 and curLoc[0] < n and curLoc[1] >= 0 and curLoc[1] < m:
                    if False == isVisited[curLoc[0]][curLoc[1]]:
                        ret[0].append(curLoc)
                        isVisited[curLoc[0]][curLoc[1]] = True
                        if graph[curLoc[0]][curLoc[1]] == 1:
                            return v[1] + 1
            q.append(ret)
            
    return minDepth

n, m = map(int, sys.stdin.readline().split(" "))
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split(" "))))

maxVal = 0
for i in range(n):
    for j in range(m):
        isVisited = [[False for col in range(m)] for row in range(n)]
        maxVal = max(maxVal, BFS(graph, isVisited, [i, j], n, m))

print(maxVal)