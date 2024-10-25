import sys
from collections import deque

N = int(sys.stdin.readline())
nodeList = list(map(int, sys.stdin.readline().split(" ")))
deleteNode = int(sys.stdin.readline())
l = [[] for _ in range(N)]


rootNode = -1
for i in range(N):
    if nodeList[i] != deleteNode and i != deleteNode:
        if nodeList[i] == -1:
            rootNode = i
        else:
            l[nodeList[i]].append(i)

if rootNode == -1:
    print(0)
else:
    isVisited = [False for _ in range(N)]
    q = deque()
    q.append(rootNode)
    isVisited[rootNode] = True
    while q:
        v = q.popleft()
        for i in l[v]:
            if isVisited[i] == False:
                isVisited[i] = True
                q.append(i)

    count = 0    
    for i in range(N):
        if len(l[i]) == 0 and isVisited[i] == True:
            count += 1
    
    print(count)
