import sys
from collections import deque

x, y = map(int, sys.stdin.readline().split(" "))
l = list()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range (0, x):
    t = list(map(int, sys.stdin.readline().split(" ")))
    l.append(t)

a = [[0 for col in range(y)] for row in range(x)]
match = 0
max = 0
for i in range (0, x):
    for j in range(0, y):
        deq = deque()
        if a[i][j] == 0 and l[i][j] == 1:
            match = match + 1
            deq.append((i, j))
            neru = 0
            while (len(deq) != 0):
                v = deq.pop()
                if a[v[0]][v[1]] == 0:
                    neru = neru + 1
                    a[v[0]][v[1]] = 1
                for k in range(4):
                    cx = v[0] + dx[k]
                    cy = v[1] + dy[k]
                    if 0 <= cx < x and 0 <= cy < y and l[cx][cy] == 1 and a[cx][cy] == 0:
                        deq.append((cx, cy))
                        
                        
            if max < neru:
                max = neru
            
print(match)
print(max)