import sys
count = int(sys.stdin.readline().rstrip())
problem = [int(sys.stdin.readline().rstrip()) for _ in range(count)]


dp0 = [0 for i in range(41)]
dp1 = [0 for i in range(41)]

dp0[0] = 1
dp0[1] = 0

dp1[0] = 0
dp1[1] = 1

minVal = 2
for i in problem:
    for j in range(minVal, i + 1):
        dp0[j] = dp0[j - 1] + dp0[j - 2]
        dp1[j] = dp1[j - 1] + dp1[j - 2]
    minVal = max(i, minVal)
    print(str(dp0[i]) + " " + str(dp1[i]))
    