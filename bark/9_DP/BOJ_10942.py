import sys
c = int(sys.stdin.readline())

v = list(map(int, sys.stdin.readline().split(" ")))
dp = [[0 for _ in range(c)] for _ in range(c)]

for i in range(c):
    odd = True
    even = True
    sIdx = i + 1
    eIdx = i 
    
    for j in range(c):
        if j % 2 == 0:
            sIdx -= 1
        else:
            eIdx += 1
        if sIdx < 0 or eIdx >= c:
            break

        if v[sIdx] == v[eIdx]:
            if j - 2 >= 0 and dp[i][j - 2] == True:
                dp[i][j] = 1
            else:
                if j - 2 < 0:
                    dp[i][j] = 1
    
        

qc = int(sys.stdin.readline())
for i in range(qc):
    s, e = map(int, sys.stdin.readline().split(" "))
    idx = ((s + e) // 2) - 1
    endIdx = e - s
    print(dp[idx][endIdx])
    