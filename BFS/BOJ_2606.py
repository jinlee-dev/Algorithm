from collections import deque
import sys

def BFS(graph, start, visited):
    q = deque()
    visited[start] = True
    count = 0
    q.append(start)
    while 0 != len(q):
        v = q.popleft()
        for idx in graph[v]:
            if False == visited[idx]:
                q.append(idx)
                visited[idx] = True
                count = count + 1
    return count


computerCnt = int(input())
linkCnt = int(input())

graph = [[] for m in range(computerCnt + 1)]
isVisited = [False] * (computerCnt + 1)

for _ in range(linkCnt):
    s, e = map(int, sys.stdin.readline().split(' '))
    graph[s].append(e)
    graph[e].append(s)

ret = BFS(graph, 1, isVisited)
print(ret)
