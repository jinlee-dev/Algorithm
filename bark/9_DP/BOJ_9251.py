import sys

l1 = list(str(sys.stdin.readline().rstrip()))
l2 = list(str(sys.stdin.readline().rstrip()))

cl1 = len(l1)
cl2 = len(l2)

dp = [[0 for i in range(cl2)] for _ in range(cl1)]

for i in range (cl1):
    if l1[i] == l2[0]:
        dp[i][0] = 1
        for j in range(i, cl1):
            dp[j][0] = 1
        break

for i in range (cl2):
    if l1[0] == l2[i]:
        dp[0][i] = 1
        for j in range(i, cl2):
            dp[0][j] = 1
        break
        

for i in range(1, cl1):
    for j in range (1, cl2):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        if l1[i] == l2[j]:
            dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i][j])

print(dp[cl1 - 1][cl2 - 1])