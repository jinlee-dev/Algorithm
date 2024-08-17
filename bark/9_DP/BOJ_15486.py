import sys

count = int(sys.stdin.readline())
l = []
for i in range(count):
    tmpList = list(map(int, sys.stdin.readline().split(" ")))
    l.append(tmpList)

dp = [0 for i in range(count + 1)]
# 걸리는 시간 / 비용

for i in range(count):
    day = l[i][0]
    endDay = day + i
    dp[i] = max(dp[i], dp[i - 1])
    if endDay <= count:
        dp[endDay] = max(dp[endDay], dp[i] + l[i][1])
    #print(dp)

print(max(dp))