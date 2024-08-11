import sys

n, m = map(int, sys.stdin.readline().split(" "))
l = list(map(int, sys.stdin.readline().split(" ")))
problem = [list(map(int, sys.stdin.readline().split(" "))) for _ in range (m)]

dp = [0 for _ in range(n + 1)]

minVal = 1e9
maxVal = 0
for i in problem:
    if i[0] < minVal:
        minVal = i[0]
    if i[1] > maxVal:
        maxVal = i[1]

for i in range(minVal, maxVal + 1):
    dp[i] = dp[i - 1] + l[i - 1]

for i in problem:
    print(dp[i[1]] - dp[i[0] - 1])
