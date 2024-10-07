import sys
from collections import deque

v, e, s = map(int, sys.stdin.readline().split(" "))

def bfs(graph, length, start):
    isVisited = [0 for i in range(length + 1)]
    deq = deque()
    deq.append(start)
    print(start, end = " ")
    isVisited[start] = True
    while len(deq) != 0:
        t = deq.popleft()
        for i in graph[t]:
            if isVisited[i] == False:
                isVisited[i] = True
                print(i, end = " ")
                deq.append(i)

def dfs(graph, length, start, isVisited):
    if isVisited[start] == False:
        isVisited[start] = True
        print(start, end = " ")
        for i in graph[start]:
            if isVisited[i] == False:
                dfs(graph, length, i, isVisited)
                isVisited[i] = True

graph = [[] for i in range(v + 1)]
for i in range(e):
    st, et = map(int, sys.stdin.readline().split(" "))
    graph[st].append(et)
    graph[et].append(st)
for i in range(1, v + 1):
    graph[i].sort()

isVisited = [False for i in range(v + 1)]
dfs(graph, v, s, isVisited)
print()
bfs(graph, v, s)
