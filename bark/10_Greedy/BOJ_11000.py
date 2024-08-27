import sys
import heapq

count = int(sys.stdin.readline())
timeTables = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(count)]

timeTables.sort()

classList = []
heapq.heappush(classList, (timeTables[0][1], timeTables[0][0] - timeTables[0][1]))
prevIdx = 0
for i in range(1, count):
    minEndTime = heapq.heappop(classList)
    if minEndTime[0] <= timeTables[i][0]:
        heapq.heappush(classList, (timeTables[i][1], timeTables[i][0] - timeTables[i][1]))
    else:
        heapq.heappush(classList, minEndTime)
        heapq.heappush(classList, (timeTables[i][1], timeTables[i][0] - timeTables[i][1]))

print(len(classList))