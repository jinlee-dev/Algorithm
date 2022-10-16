from cmath import inf
import heapq
import sys

global inf
inf = 1e9

def dijksta(start, end, graph):
    global inf
    q = []
    dist= [inf] * 101
    jusawi = [1, 2, 3, 4, 5, 6]
    # cost, index
    heapq.heappush(q, (0, 1))

    while(q):
        c = heapq.heappop(q)
        index = c[1]
        curDist = c[0]
        for i in jusawi:
            cost = curDist + 1
            jusawiValue = index + i
            if jusawiValue > 100:
                continue
            if 0 != len(graph[jusawiValue]):
                for j in graph[jusawiValue]:
                    if cost < dist[j]:
                        dist[j] = cost
                        heapq.heappush(q, (cost,  j))
            else:
                if cost < dist[jusawiValue]:
                        dist[jusawiValue] = cost
                        heapq.heappush(q, (cost,jusawiValue))
    return dist[100]

graph = [[] for _ in range(101)]
sadari, bam = map(int, sys.stdin.readline().split(" "))
for _ in range(sadari):
    s, e = map(int,sys.stdin.readline().split(" "))
    graph[s].append(e)

for _ in range(bam):
     s, e = map(int,sys.stdin.readline().split(" "))
     graph[s].append(e)

print(dijksta(1, 100, graph))