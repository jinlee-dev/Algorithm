import sys
import heapq
n, m = map(int, sys.stdin.readline().split(" "))
v = []
for i in range(n):
    v.append(list(map(int, sys.stdin.readline().split(" "))))
    heapq.heapify(v[i])

hp = []

maxVal = 0
maxIdx = 0
for i in range(n):
    cv = heapq.heappop(v[i])
    heapq.heappush(hp, (cv, i))
    if cv > maxVal:
        maxVal = cv
        maxIdx = i

minVal = hp[0]
answer = 1e11
popCnt = [0 for _ in range(n)]
while hp:
    val, idx = heapq.heappop(hp)
    if popCnt[minVal[1]] < m:
        minVal = (val, idx)
    popCnt[idx] += 1
    answer = min(answer, maxVal - minVal[0])
    if len(v[idx]):
        cv = heapq.heappop(v[idx])
        if cv > maxVal:
            maxVal = cv
            maxIdx = i
        heapq.heappush(hp, (cv, idx))

print(answer)