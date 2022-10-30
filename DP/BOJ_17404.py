import sys
global INF
INF = int(1e9)

count = int(sys.stdin.readline())
expense = []
for _ in range(count):
   expense.append(list(map(int, sys.stdin.readline().split(" "))))

red = 0
green = 1
blue = 2

ret = INF
dp = [[[INF for _ in range(3)] for _ in range(count)]  for _ in range(3)]

for c in range(3):
    dp[c][0][c] = expense[0][c]

    for i in range(1,count):
        dp[c][i][red] = min(dp[c][i - 1][green], dp[c][i - 1][blue]) + expense[i][red]
        dp[c][i][green] = min(dp[c][i - 1][red], dp[c][i - 1][blue]) + expense[i][green]
        dp[c][i][blue] = min(dp[c][i - 1][red], dp[c][i - 1][green]) + expense[i][blue]

dp[0][count - 1][0] = INF
dp[1][count - 1][1] = INF
dp[2][count - 1][2] = INF

answer = INF
for i in range(3):
    answer = min(answer, dp[i][count - 1][red], dp[i][count - 1][green], dp[i][count - 1][blue])

print(answer)