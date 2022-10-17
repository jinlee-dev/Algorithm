import sys
import heapq

global inf
inf = 1e9

def dijkstra(start, end):
    q = []
    dist = [inf] * 100001
    heapq.heappush(q, (0, start))
    while q:
        time, index = map(int, heapq.heappop(q))
        if index == end:
            return time
        if dist[index] < time:
            continue
        else:
            add = []
            add.append([index + 1, 1])
            add.append([index - 1, 1])
            add.append([index * 2, 0])
            for i in add:
                if i[0] > 100000:
                    continue
                elif i[0] < 0:
                    continue
                else:
                    cost = time + i[1]
                    if cost < dist[i[0]] :
                        dist[i[0]] = cost
                        heapq.heappush(q,(cost,i[0]))



subin, bro = map(int, sys.stdin.readline().split(" "))
print(dijkstra(subin, bro))