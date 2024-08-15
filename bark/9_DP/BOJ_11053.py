import sys

count = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split(" ")))

dp = [1 for i in range(count + 1)]

for i in range(1, count):
    for j in range(i - 1, -1, -1):
        if l[j] < l[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))