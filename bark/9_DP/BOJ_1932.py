import sys

count = int(sys.stdin.readline())
l = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(count)]

dp = []
for i in range (count):
    dp.append([0 for _ in range (i + 1)])

dp[0][0] = l[0][0]

for i in range(1, count):
    for j in range(0, i + 1):
        left = 0 if j - 1 < 0 else dp[i - 1][j-1]
        right = 0 if j >= i else dp[i - 1][j]
        dp[i][j] = max(left, right) + l[i][j]

answer = 0
for i in range(count):
    answer = max(answer, dp[count - 1][i])

print(answer)