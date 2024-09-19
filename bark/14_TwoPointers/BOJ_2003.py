import sys

N, M = map(int, sys.stdin.readline().split(" "))
l = list(map(int, sys.stdin.readline().split(" ")))


e = 0

curRet = 0
cnt = 0
for s in range(N):
    while e < N and curRet < M:
        curRet = curRet + l[e]
        e = e + 1
    
    if curRet == M:
        cnt = cnt + 1
    
    curRet = curRet - l[s]
    


print(cnt)