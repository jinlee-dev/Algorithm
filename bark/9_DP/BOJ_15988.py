import sys

count = int(sys.stdin.readline())
l = [int(sys.stdin.readline()) for i in range (count)]
m = max(l)
dp = [0 for i in range (m + 1)]
dp[1] = 1
dp[2] = 2
dp[3] = 4
div =  1000000009
for i in range(4, m + 1):
    dp[i] = (dp[i - 1] % div + dp[i - 2] % div + dp[i - 3] % div) % div

for i in l:
    print(dp[i])