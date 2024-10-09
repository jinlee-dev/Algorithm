import sys
from collections import deque

friendCnt = int(sys.stdin.readline())
edgeCnt = int(sys.stdin.readline())

graph = [[] for _ in range(friendCnt + 1)]
ret = 0
isVisited = [False for _ in range(friendCnt + 1)]
for i in range(edgeCnt):
    st, et = map(int,sys.stdin.readline().split(" "))
    graph[st].append(et)
    graph[et].append(st)

isVisited[1] = True
deq = deque()
deq.append((1, 0))

while len(deq) != 0:
    t = deq.popleft()
    for i in graph[t[0]]:
        if isVisited[i] == False and t[1] < 2:
            isVisited[i] = True
            ret += 1
            deq.append((i, t[1] + 1))

print(ret)