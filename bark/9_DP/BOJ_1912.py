import sys

count = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split(" ")))

dp = [-1001 for i in range(count + 1)]

dp[0] = l[0]

maxVal = dp[0]
for i in range(1, count):
    dp[i] = max(dp[i - 1] + l[i], l[i])
    if dp[i] > maxVal:
        maxVal = dp[i]

print(maxVal)