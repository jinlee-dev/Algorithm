import sys
from collections import deque

N, M = map(int, (sys.stdin.readline().split(" ")))
g = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(isVisited, x, y):
    maxDepth = 0
    isCurrentVisited = [[False for _ in range(N)] for _ in range(N)]
    q = deque()
    isVisited[x][y] = 0
    isCurrentVisited[x][y] = 1
    q.append(((x, y), 0))
    
    while q:
        v = q.popleft()
        vx, vy = v[0][0], v[0][1]
        depth = v[1]
        for i in range(4):
            cx = vx + dx[i]
            cy = vy + dy[i]
            if 0 <= cx < N and 0 <= cy < N and (g[cx][cy] == 0 or g[cx][cy] == 2) and isCurrentVisited[cx][cy] == False:
                isCurrentVisited[cx][cy] = True
                isVisited[cx][cy] = min(isVisited[cx][cy], depth + 1)
                q.append(((cx, cy), depth + 1))

def AllVisited(isVisited):
    depth = 0
    for i in range(N):
        for j in range(N):
            if (g[i][j] == 0 or g[i][j] == 2) and isVisited[i][j] == 3000:
                return -1
            elif isVisited[i][j] == 3000:
                continue
            else:
                depth = max(isVisited[i][j], depth)
    return depth
    


answer = 3000
def dfs(virus, x, y, isVisited):
    global answer
    if len(virus) == M:
        isVirusVisited = [[3000 for _ in range(N)] for _ in range(N)]
        for i in range(M):
            bfs(isVirusVisited, virus[i][0], virus[i][1])

        ret = AllVisited(isVirusVisited)
        if ret != -1:
            answer = min(answer, ret)

    else:
        for i in range(x, N):
            startIdx = y if i == x else 0
            for j in range(startIdx, N):
                if 0 <= i < N and 0 <= j < N and isVisited[i][j] == 0 and g[i][j] == 2:
                    isVisited[i][j] = 1
                    virus.append((i, j))
                    dfs(virus, i, j, isVisited)
                    virus.pop()
                    isVisited[i][j] = 0

isVisited = [[0 for _ in range(N)] for _ in range(N)]
dfs([], 0, 0, isVisited)
if answer == 3000:
    print(-1)
else:
    print(answer)