import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

puyo = []
for i in range(12):
    puyo.append(list(str(sys.stdin.readline().rstrip())))

def bfs(x, y, isVisited):
    q = deque()
    color = puyo[x][y]
    isVisited[x][y] = 1
    q.append((x, y))    
    dic = {}
    dic[y] = [x, x]
    count = 1
    while q:
        v = q.popleft()
        for i in range(4):
            cx = v[0] + dx[i]
            cy = v[1] + dy[i]
            if 0 <= cx < 12 and 0 <= cy < 6 and isVisited[cx][cy] == 0 and puyo[cx][cy] == color:
                q.append((cx, cy))
                isVisited[cx][cy] = 1
                if cy in dic:
                    mm = dic[cy]
                    if mm[0] < cx:
                        mm[0] = cx
                    elif mm[1] > cx:
                        mm[1] = cx
                else:
                    dic[cy] = [cx, cx]
                count += 1
    return count, dic

answer = 0
while 1:
    pop = []
    isVisited = [[0 for _ in range(6)] for _ in range(12)]

    for i in range(12):
        for j in range(6):
            if '.' != puyo[i][j] and isVisited[i][j] == False:
                count, ret = bfs(i, j, isVisited)
                if count >= 4:
                    pop.append((puyo[i][j], ret))
    
    if len(pop) == 0:
        print(answer)
        break
    else:
        answer += 1
        for i in pop:
            for cx, cy in i[1].items():
                for k in range(cy[1], cy[0] + 1):
                    if puyo[k][cx] == i[0]:
                        puyo[k][cx] = '.'
    
        for i in range(6):
            for j in range(12):
                if puyo[j][i] == '.':
                    for k in range(j, 0, -1):
                        puyo[k][i] = puyo[k - 1][i]
                    puyo[0][i] = '.'
