from collections import deque
import sys

def BFS(graph, start, visited, order):
    queue = deque()
    visited[start] = True
    queue.append(start)
    o = 1
    while queue:
        v = queue.popleft()
        order[v] = o
        o = o + 1
        for i in graph[v]:
            if False == visited[i]:
                queue.append(i)
                visited[i] = True


node, link, start = map(int, sys.stdin.readline().split(' '))

isVisited = [False] * (node + 1)

graph = [[] for m in range(node + 1)]
for i in range(link):
    a, b = map(int, sys.stdin.readline().split(' '))
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

order = [0] * (node + 1)
BFS(graph, start, isVisited, order)

for i in order[1:]:
    print(i, end="\n")