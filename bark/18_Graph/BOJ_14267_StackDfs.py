import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split(" "))

praise = [0 for _ in range(n + 1)]

g = [[] for _ in range(n + 1)]
l = list(map(int, sys.stdin.readline().split(" ")))
dp = [0 for _ in range(n + 1)]

for cur, sangsa in enumerate(l):
    if sangsa != -1:
        g[sangsa].append(cur + 1)

for i in range(m):
    s, p = map(int, sys.stdin.readline().split(" "))
    praise[s] += p


def dfs(g, isVisited, idx, score):
    isVisited[idx] = True
    
v = [0 for _ in range(n + 1)]
stack = []  
stack.append((1, 0))
v[1] = True

while stack:
    t, s = stack.pop()
    v[t] = True
    print(t, s)
    for i in range(len(g[t])-1, -1, -1):
        index = g[t][i]
        if v[index] == False:
            stack.append((g[t][i], s + praise[index]))

for i in range(1, n + 1):
    print(dp[i], end=' ')