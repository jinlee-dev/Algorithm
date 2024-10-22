import sys

problemCnt = int(sys.stdin.readline())

for i in range(problemCnt):
    coinCnt = int(sys.stdin.readline())
    coinList = list(map(int, sys.stdin.readline().split(" ")))
    money = int(sys.stdin.readline())
    dp = [0 for _ in range(money + 1)]
    dp[0] = 1
    for j in range(coinCnt):
        for k in range(1, money + 1):
            if j == 0:
                dp[k] += 1 if k % coinList[j] == 0 else 0
            if j > 0 and k - coinList[j] >= 0:
                dp[k] += dp[k - coinList[j]]

    
    print(dp[money])