import sys

cityCnt = int(sys.stdin.readline())
busCnt = int(sys.stdin.readline())

l = [[] for _ in range(cityCnt)]
dist = [[1e9 for _ in range(cityCnt)] for _ in range(cityCnt)]

for i in range(busCnt):
    s, e, c = map(int, sys.stdin.readline().split(" "))
    s -= 1
    e -= 1
    l[s].append([e, c])

# 전처리
for i in range(cityCnt):
    for j in l[i]:
        dist[i][j[0]] = min(dist[i][j[0]], j[1])
    dist[i][i] = 0

for k in range(cityCnt):
    for i in range(cityCnt):
        for j in range(cityCnt):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(cityCnt):
    for j in range(cityCnt):
        if dist[i][j] == 1e9:
            print(0, end=" ")
        else:
            print(dist[i][j], end=" ")
    
    print()