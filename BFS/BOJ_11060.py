import sys
from collections import deque
def BFS(graph, count):
    if count == 1:
        return 0
    q = deque()
    q.append([0, 0])
    isVisited = [False] * count
    while len(q):
        v = q.popleft()
        if v[0] == count - 1:
            return v[1]
        for i in range(1, graph[v[0]] + 1):
            curValue = v[0] + i
            if curValue < count and isVisited[curValue] == False:
                q.append([curValue, v[1] + 1])
                isVisited[curValue] = True
    return -1


count = int(input())
graph = list(map(int, sys.stdin.readline().split(" ")))
print(BFS(graph, count))

