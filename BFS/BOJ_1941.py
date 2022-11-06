import sys
from itertools import combinations
from collections import deque

def IsConnected(graph, startPnt):
    count = 0
    isVisited = [[False for col in range(5)] for row in range(5)]
    dirx = [-1,1,0,0]
    diry = [0,0,-1,1]
    q = deque()
    x = int(combi / 5)
    y = int(combi % 5)
    q.append([x, y])
    isVisited[x][y] = True
    count = count + 1
    while len(q):
        v = q.popleft()
        for i in range(4):
            nextX = v[0] + dirx[i]
            nextY = v[1] + diry[i]
            if nextX >= 0 and nextY >= 0 and nextX < 5 and nextY < 5 and isVisited[nextX][nextY] == False and graph[nextX][nextY] == True:
                q.append([nextX, nextY])
                isVisited[nextX][nextY] = True
                count = count + 1
    return count == 7

items = []
for i in range(25):
    items.append(i)

combiList = list(combinations(items, 7))

princessCount = 0
sevenPrincess = []
for i in range(5):
    sevenPrincess.append(list(sys.stdin.readline()))

for i in combiList:
    # 그래프 만들어줌
    graph = [[False for col in range(5)] for row in range(5)]
    curLeeDasomCnt = 0
    for combi in i:
        x = int(combi / 5)
        y = int(combi % 5)
        graph[x][y] = True
        if sevenPrincess[x][y] == 'S':
            curLeeDasomCnt = curLeeDasomCnt + 1
    
    if curLeeDasomCnt >= 4 and IsConnected(graph, i[0]):
        princessCount = princessCount + 1

print(princessCount)