import sys
sys.setrecursionlimit(10 ** 6)

d = [(-1, 0), (1, 0), (0, 1), (0, -1) ]
n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

def DFS(x, y, graph):
    if x >= n or x < 0 or y >= m or y < 0:
        return False
    else:
        if graph[x][y] == 0:
            graph[x][y] = 1
            for i in d:
                DFS(x + i[0], y + i[1], graph)
            return True
        else:
            return False


count = 0
for i in range(n):
    for j in  range(m):
        if True == DFS(i, j, graph):
            count = count + 1

print(count)