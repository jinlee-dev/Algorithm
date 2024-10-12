import sys
from collections import deque

count = int(sys.stdin.readline())
l = [[] for _ in range(count + 1)]
isVisited = [-1 for _ in range(count + 1)]
for i in range(count - 1):
    s, e = map(int,sys.stdin.readline().split(" "))
    l[s].append(e)
    l[e].append(s)

d = deque()
d.append(1)

while(len(d)):
    v = d.popleft()
    for t in l[v]:
        if isVisited[t] == -1:
            isVisited[t] = v
            d.append(t)

for i in range(2, count + 1):
    print(isVisited[i])