import sys

nodeCnt, linkCnt = map(int, sys.stdin.readline().split(" "))

dist = [[1e9 for _ in range(nodeCnt + 1)] for _ in range(nodeCnt + 1)]
startPnt = [[0 for _ in range(nodeCnt + 1)] for _ in range(nodeCnt + 1)]

for i in range(linkCnt):
    s, e, v = map(int, sys.stdin.readline().split(" "))
    dist[s][e] = v
    dist[e][s] = v
    startPnt[s][e] = e
    startPnt[e][s] = s

for i in range(1, nodeCnt + 1):
    for j in range(1, nodeCnt + 1):
        for k in range(1, nodeCnt + 1):
            if j != k:
                v = dist[j][i] + dist[i][k]
                if dist[j][k] > v:
                    dist[j][k] = v
                    startPnt[j][k] = startPnt[j][i]

for i in range(1, nodeCnt + 1):
    for j in range(1, nodeCnt + 1):
        if i == j:
            print("-", end=" ")
        else:
            if 0 != startPnt[i][j]:
                print(startPnt[i][j], end=" ")
            else:
                print("-", end=" ")
    
    print()