import sys

N = list(str(sys.stdin.readline().rstrip()))
dp = [0 for _ in range(len(N) + 1)]
dp[0] = 1
dp[1] = 1
ret = True
if N[0] == '0':
    ret = False
for i in range(2, len(N)+ 1):
    curValue =  int(N[i - 2] + N[i - 1])
    if N[i - 2] == '0':
        if N[i - 1] == '0':
            ret = False
            break
        else:
            dp[i] = (dp[i - 1]) % 1000000        
    elif curValue > 26:
        if N[i - 1] == '0':
            ret = False
            break
        else:
            dp[i] = (dp[i - 1]) % 1000000
    elif N[i - 1] == '0':
        dp[i] = (dp[i - 2]) % 1000000   
    else:
        dp[i] = ((dp[i - 1] % 1000000) + (dp[i - 2] % 1000000)) % 1000000
if ret == True:
    print(dp[len(N)] % 1000000)
else:
    print(0)