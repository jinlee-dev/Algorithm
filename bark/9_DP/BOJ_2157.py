import sys
from collections import deque
cityCnt, meetCnt, flight = map(int, sys.stdin.readline().split())
g = [[] for _ in range(cityCnt + 1)]
for i in range(flight):
    x, y, z = map(int, sys.stdin.readline().split())
    if x < y:
        g[x].append((y, z))

dp = [[0 for _ in range(meetCnt  + 1)] for _ in range(cityCnt + 1)]

# 도시, 방문횟수
dp[1][1] = 0
q = deque()
q.append((1, 1))
while q:
    v = q.popleft()
    for next, score in g[v[0]]:
        nextScore  = dp[v[0]][v[1]] + score
        if (v[1]) < meetCnt and dp[next][v[1] + 1] < nextScore:
            dp[next][v[1]+ 1] = nextScore
            q.append((next, v[1] + 1))

print(max(dp[cityCnt]))