import sys

count = int(sys.stdin.readline())
dp = [ [0 for i in range (count + 1)] for _ in range(2) ]
dp[0][0] = 0
dp[0][1] = 0

dp[1][0] = 1
dp[1][1] = 1

for i in range(2, count + 1):
    dp[0][i] = dp[0 ][i - 1] + dp[1][i - 1]
    dp[1][i] = dp[0][ i - 1]

print(dp[0 ][count] + dp[1][count])