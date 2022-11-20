import sys

count = int(sys.stdin.readline())
l = []
for i in range(count):
    l.append(list(map(int, sys.stdin.readline().split(" "))))

dp = [[0 for _ in range(count)] for _ in range(count)]
dp[0][0] = 1
for i in range(count):
    for j in range(count):
        pathCnt = 0
        for left in range(j, -1, -1):
            if l[left][i] == j - left:
                pathCnt = dp[left][i] + pathCnt
        for right in range(i,-1, -1):
            if l[j][right] == i - right:
                pathCnt = dp[j][right] + pathCnt
        dp[j][i] = dp[j][i] + pathCnt

print (dp[count - 1][count - 1])
