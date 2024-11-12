import sys
from collections import deque
sys.setrecursionlimit(10**5)

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
    for i in g[idx]:
        if isVisited[i] == False:
            score += praise[i]
            dp[i] = score
            dfs(g, isVisited, i, score)
            score -= praise[i]

v = [0 for _ in range(n + 1)]
dfs(g, v, 1, 0)
for i in range(1, n + 1):
    print(dp[i], end=' ')