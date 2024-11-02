import sys

purpose, inputCnt = map(int, sys.stdin.readline().split(" "))
dp = [[0 for _ in range(purpose + 1)] for _ in range(inputCnt)]
bag = []
for i in range(inputCnt):
    bag.append((list(map(int, sys.stdin.readline().split(" ")))))
bag.sort()

# 18원을 들여서 6명의 고객
for i in range(1, purpose + 1):
    # 필요한 개수
    c = (i // bag[0][1]) + ((i % bag[0][1]) != 0)
    dp[0][i] = bag[0][0] * c

for i in range(1, inputCnt):
    for j in range(1, purpose + 1):
        if j - bag[i][1] >= 0:
            nap = dp[i - 1][j - bag[i][1]]
            dp[i][j] = min(dp[i - 1][j],  (nap + bag[i][0]),  dp[i][j - bag[i][1]] + bag[i][0])
        else:
            dp[i][j] = dp[i - 1][j]

minVal = 1e9
for i in range(inputCnt):
    minVal = min(minVal, dp[i][purpose])

print(minVal)