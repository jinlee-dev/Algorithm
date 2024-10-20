import sys
from collections import deque
v = int(sys.stdin.readline())
dp = deque()

dp.append(1)
dp.append(2)

for i in range(3, v + 1):
    dp.append((dp[0] + dp[1]) % 15746)
    dp.popleft()

if v == 1:
    print(dp[0])
else:
    print(dp[1] % 15746)