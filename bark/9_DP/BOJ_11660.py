import sys

N, M = map(int, sys.stdin.readline().split(" "))
g = []
dp = [[0 for _ in range(N)] for _ in range (N)]
for i in range (N):
    g.append(list(map(int, sys.stdin.readline().split(" "))))

# 초기화
for i in range(N):
    for j in range (N):
        dp[i][j] = g[i][j]

# dp 그래프 채우기
for i in range(N):
    for j in range(1, N):
        dp[i][j] += dp[i][j - 1]

for i in range(M):
    ss, se, es, ee = map(int, sys.stdin.readline().split(" "))
    answer = 0
    for j in range(ss - 1, es):
        minus = dp[j][se - 2] if (se - 1) > 0 else 0
        answer += (dp[j][ee - 1] - minus)
    
    print(answer)
