import sys

count = int(sys.stdin.readline())
l = []
for i in range (count):
    l.append(int(sys.stdin.readline()))

dp = [0 for i in range(count + 1)]
dp[0] = l[0]

if count > 1:
    dp[1] = l[0] + l[1]

if count > 2:
    dp[2] = max(dp[1], l[0] + l[2], l[1]+l[2])
    
for i in range(3, count):
    dp[i] = max(dp[i - 1], dp[i - 2] + l[i],  dp[i - 3] + l[i - 1] + l[i])


print(dp[count - 1])