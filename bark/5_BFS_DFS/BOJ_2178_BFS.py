import sys
from collections import deque

g = []
x, y = map(int, sys.stdin.readline().split(" "))
for i in range(x):
    g.append(list(str(sys.stdin.readline().rstrip())))

v = [[1e9 for i in range(y)] for j in range(x)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque()
v[0][0] = 1
q.append([0, 0])

while(len(q) != 0):
    c = q.popleft()
    for i in range(4):
        nx = c[0] + dx[i]
        ny = c[1] + dy[i]
        if 0 <= nx < x and 0 <= ny < y and g[nx][ny] == '1' and v[nx][ny] == 1e9:
            q.append([nx, ny])
            v[nx][ny] = v[c[0]][c[1]] + 1

print(v[x - 1][y - 1])
