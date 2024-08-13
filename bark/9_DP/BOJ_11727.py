import sys

count = int(sys.stdin.readline())
dp = [0 for i in range (count + 1)]

dp[0] = 0
dp[1] = 1

if count >= 2:
    dp[2] = 3
    for i in range (3, count + 1):
        dp[i] = ((dp[i - 1]) % 10007 + (dp[i - 2]) % 10007 + (dp[i - 2]) % 10007)%10007


print(dp[count])