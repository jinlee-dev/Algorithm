import sys

count = int(sys.stdin.readline())
l = [int(sys.stdin.readline().rstrip()) for _ in range(count)]

dp = [0 for _ in range(11)]
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i-3]

for i in l:
    print(dp[i])
