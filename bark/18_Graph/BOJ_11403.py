import sys
from collections import deque

cnt = int(sys.stdin.readline())

v = [[] for _ in range(cnt)]
for i in range(cnt):
    l = list(map(int, sys.stdin.readline().split(" ")))
    for j in range(cnt):
        if l[j] == 1:
            v[i].append(j)

ret = [[0 for _ in range(cnt)] for _ in range(cnt)]

for i in range(cnt):
    for j in range(cnt):
        isVisited = [False for _ in range(cnt)]
        deq = deque()
        deq.append(i)
        isFind = False
        while len(deq) != 0:
            t = deq.popleft()
            for k in v[t]:
                if isVisited[k] == False:
                    if k == j:
                        ret[i][j] = 1
                        isFind = True
                        break
                    else:
                        deq.append(k)
                        isVisited[k] = True
            if isFind == True:
                break


for i in range (cnt):
    for j in range(cnt):
        print(ret[i][j], end = " ")
    print()