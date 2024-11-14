import sys
import heapq
import math

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]
 
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def GetCost(x1, y1, x2, y2):
    x = x2 - x1
    y = y2 - y1
    return math.sqrt(pow(x, 2) + pow(y, 2))

shin, link = map(int, sys.stdin.readline().split(" "))
coord = []
coord.append((0, 0))
for i in range(shin):
    x, y = map(int, sys.stdin.readline().split(" "))
    coord.append((x, y))
 
p = [0 for _ in range(shin + 1)]
for i in range(1, shin + 1):
    p[i] = i

pq = []
ll = []
for _ in range(link):
    a, b = map(int, sys.stdin.readline().split(" "))
    if a > b:
        tmp = a
        a = b
        b = tmp
    ll.append((a, b))

ll.sort()
for i, j in ll:
    union_parent(p, i, j)

for i in range(1, shin + 1):
    for j in range(i + 1, shin + 1):
        heapq.heappush(pq, (GetCost(coord[i][0], coord[i][1], coord[j][0], coord[j][1]), i, j))
 
maxCnt = shin - 1
curLinkCnt = link
minLength = 0.0
while pq:
    cost, x, y = heapq.heappop(pq)
    if find_parent(p, x) != find_parent(p, y):
        union_parent(p, x, y)
        minLength += cost
        curLinkCnt += 1


formatted_number = f"{minLength:.2f}"
print(formatted_number)