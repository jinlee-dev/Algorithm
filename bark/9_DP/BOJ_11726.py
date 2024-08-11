import sys

count = int(sys.stdin.readline())

dp = [False for _ in range (1001)]
dp[0] = 0
dp[1] = 1
dp[2] = 2

for i in range (3, count + 1):
    dp[i] = ((dp[i - 1] % 10007) + (dp[i - 2] % 10007) ) % 10007

print(dp[count] % 10007)