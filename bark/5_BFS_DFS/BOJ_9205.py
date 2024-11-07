import sys
from collections import deque
tc = int(sys.stdin.readline())
beer = 1000
for k in range(tc):
    conviCnt = int(sys.stdin.readline())
    # 집, 편, 편, 펜
    coord = [[] for _ in range(conviCnt + 2)]
    isVisited = [False for _ in range(conviCnt + 2)]

    for i in range(conviCnt + 2):
        coord[i] = list(map(int, sys.stdin.readline().split(" ")))

    q = deque()
    q.append(0)
    isVisited[0] = False
    while q:
        index = q.popleft()
        for i in range(conviCnt + 2):
            if isVisited[i] == False:
                dist = abs(coord[index][0] - coord[i][0]) + abs(coord[index][1] - coord[i][1])
                if dist <= beer:
                    isVisited[i] = True
                    q.append(i)
    
    if isVisited[conviCnt + 1] == False:
        print("sad")
    else:
        print("happy")