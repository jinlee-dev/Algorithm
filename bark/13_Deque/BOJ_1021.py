import sys
from collections import deque

qSize, count = map(int, sys.stdin.readline().split(" "))
li = list(map(int, sys.stdin.readline().split(" ")))

cq = deque()
for i in range(1, qSize + 1):
    cq.append(i)

ret = 0
for i in range(len(li)):
    lf = deque()
    rf = deque()
    size = len(cq)
    lfc = 0
    rfc = 0
    for j in range(size):
        if cq[j] == li[i]:
            lfc = j
            break
    for j in range(size):
        if cq[size - j - 1] == li[i]:
            rfc = j + 1
            break
    ret += min(lfc, rfc)

    if lfc < rfc:
        for i in range(lfc):
            v = cq.popleft()
            cq.append(v)
    else:
        for i in range(rfc):
            v = cq.pop()
            cq.appendleft(v)
    
    cq.popleft()

print(ret)