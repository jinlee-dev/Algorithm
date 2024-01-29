import sys

ret = []
loop = int(sys.stdin.readline())
for a in range(0, loop):
    row = int(sys.stdin.readline())
    stiker = []
    for a in range(2):
        value = list(map(int, sys.stdin.readline().split(" ")))
        stiker.append(value)

    dp = [[ 0 for col in range(row)] for j in range(2)]
    dp[0][0] = stiker[0][0]
    dp[1][0] = stiker[1][0]
    for a in range(1, row):
        if a == 1:
            dp[0][a] = dp[1][a-1] + stiker[0][a]
            dp[1][a] = dp[0][a-1] + stiker[1][a]
        else:
            dp[0][a] = max(dp[1][a-1] , dp[0][a-2], dp[1][a-2]) + stiker[0][a]
            dp[1][a] = max(dp[0][a-1] , dp[1][a-2], dp[0][a-2]) + stiker[1][a]
    
    print(max(dp[0][row - 1], dp[1][row - 1]))