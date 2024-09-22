import sys
from collections import deque

N, P, Q = map(int, sys.stdin.readline().split(" "))
v = deque()
t = {}
v.append(N)
l = []
while len(v) != 0:
    tmp = v.pop()
    t[tmp] = 0
    
    ll = [tmp // P, tmp // Q]
    for i in ll:
        if i != 0:
            if i in t:
                continue
            else:
                t[i] = 0
                v.append(i)
t[0] = 1

sortDic = sorted(t.items(), key=lambda x:x[0])
for i in range(len(sortDic)):
    index = sortDic[i][0]
    if index != 0:
        t[index] = t[index // P] + t[index // Q]

print(t[N])
