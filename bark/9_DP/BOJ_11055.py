import sys

count = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split(" ")))

# count = 5
# l = [5, 4, 3, 4, 5]

dp = l[:]

for i in range(1, count):
    for j in range(i - 1, -1, -1):
        #print(i, j)
        if l[j] < l[i]:
            dp[i] = max(dp[i], dp[j] + l[i])

print(dp)
print(max(dp))
