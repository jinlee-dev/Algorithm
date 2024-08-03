import sys
from collections import deque

x, y, rc = map(int, sys.stdin.readline().split(" "))

m = [[0 for i in range(y)] for j in range(x)]
v = [[0 for i in range(y)] for j in range(x)]

t = []
for i in range(rc):
    sx, sy, ex, ey = map(int, sys.stdin.readline().split(" "))
    t.append([sx, sy, ex, ey])


for i in range(rc):
    sx, sy, ex, ey = t[i][0], t[i][2], t[i][1], t[i][3]
    for j in range(sx, sy):
        for k in range(ex, ey):
            m[k][j] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(c):
    global v, m, x, y
    cx = c[0]
    cy = c[1]
    if v[cx][cy] == 0 and m[cx][cy] == 0:
        v[cx][cy] = 1
        dq = deque()
        nb = 1
        dq.append([cx, cy])
        while (len(dq) != 0):
            n = dq.popleft()
            for i in range (4):
                nx = n[0] + dx[i]
                ny = n[1] + dy[i]
                if 0 <= nx < x and 0 <= ny < y and v[nx][ny] == 0 and m[nx][ny] == 0 and v[nx][ny] == 0:
                    v[nx][ny] = 1
                    dq.append([nx, ny])
                    nb = nb + 1
        return nb
    return 0

r = []
for i in range(x):
    for j in range(y):
        ret = BFS([i, j])
        if ret != 0:
            r.append(ret)

print(len(r))
r.sort()
strRet = ""
for i in range(len(r)):
    strRet = strRet + str(r[i])
    strRet = strRet + " "

strRet.rstrip()
print(strRet)