import sys
import heapq

N = int(sys.stdin.readline())
l = [[] for _ in range(N)]
minVal = [1e9, 0, 0]

for i in range(N):
    tl = list(map(int, sys.stdin.readline().split(" ")))
    for j in range(N):
        if i != j:
            l[i].append((j, tl[j]))
            if minVal[0] > tl[j]:
                minVal[0] = tl[j]
                minVal[1] = i
                minVal[2] = j

q = []
startIdx = minVal[1]
for i in range(len(l[startIdx])):
    heapq.heappush(q, [l[startIdx][i][1], minVal[1], l[startIdx][i][0]])

isVisited = [False for _ in range(N)]

ret = 0
count = 0
while count < (N - 1):
    v = heapq.heappop(q)
    if isVisited[v[1]] == True and isVisited[v[2]] == True:
        continue
    isVisited[v[1]] = True
    isVisited[v[2]] = True
    count += 1
    ret += v[0]

    for i in l[v[2]]:
        if isVisited[i[0]] == False:
            heapq.heappush(q,[i[1], v[2], i[0]])

print(ret)