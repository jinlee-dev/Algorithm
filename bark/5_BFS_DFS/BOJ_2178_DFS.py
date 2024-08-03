# BFS 문제로 재귀 돌다가 메모리 초과남
# 그래도 DFS에 익숙해지기 위한 문제 풀이
import sys
sys.setrecursionlimit(10**6)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

x, y = map(int, sys.stdin.readline().split(" "))
g = []
for i in range (0, x):
    g.append(list(str(sys.stdin.readline().rstrip())))

vg = [[1e9 for col in range(y)] for row in range(x)]

def DFS(v, coord):
    global dx, dy, x, y, g
    cx = coord[0]
    cy = coord[1]
    if vg[cx][cy] == 1e9:
        vg[cx][cy] = v
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx >= 0 and ny >= 0 and nx < x and ny < y and g[nx][ny] == '1':
                nc = [nx, ny]
                DFS(vg[cx][cy] + 1, nc)

DFS(1, [0, 0])
print(vg[x - 1][y - 1])