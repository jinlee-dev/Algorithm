import sys

count, move = map(int, sys.stdin.readline().split(" "))
plum = [int(sys.stdin.readline()) for i in range(count)]

dp = [[[0 for k in range(2)] for j in range(move + 1)] for i in range(count + 1)]

# 첫번째 index 처리
curPlumIdx = plum[0] - 1
# 현재 plum이 1번 나무에서 떨어질 경우 1 아님 0
dp[0][0][0] = 1 if curPlumIdx == 0 else 0  

# 현재 plum이 2번 나무에서 떨어질 경우 1 아님 0
dp[0][1][1] = 1 if curPlumIdx == 1 else 0  

maxVal = 1

for i in range(1, len(plum)):
    plumFall = plum[i] - 1
    revPlumIdx = 1 if plumFall == 0 else 0        
    # [자두인덱스][움직임횟수][이전 자두가 어디였는지]
    for j in range(move + 1):
        dp[i][j][plumFall] = dp[i - 1][j][plumFall] + 1
        if maxVal < dp[i][j][plumFall]:
            maxVal = dp[i][j][plumFall]

    
    # 이번에 움직인다면?
    for j in range(move):
        dp[i][j + 1][plumFall] = max(dp[i - 1][j][revPlumIdx] + 1, dp[i][j + 1][plumFall])
        if maxVal <  dp[i][j + 1][plumFall] :
            maxVal =  dp[i][j + 1][plumFall] 

    for j in range(move + 1):
        dp[i][j][revPlumIdx] = max(dp[i][j][revPlumIdx], dp[i - 1][j][revPlumIdx])
        if maxVal <  dp[i][j][revPlumIdx] :
            maxVal =  dp[i][j][revPlumIdx]

print(maxVal)