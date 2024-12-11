import sys
from collections import deque
def convStrToInt(a):
    return ord(a) - ord('A')

def convIntToStr(a):
    return chr(a + chr('A'))

count = int(sys.stdin.readline())
l = [[] for _ in range(count + 1)]
for _ in range(count):
    tp, tc1, tc2 = map(str, sys.stdin.readline().rstrip().split(" "))
    p = convStrToInt(tp)
    if tc1 != '.':
        c1 = convStrToInt(tc1)
        l[p].append(c1)
        l[c1].append(p)
    if tc2 != '.':
        c2 = convStrToInt(tc2)
        l[p].append(c2)
        l[c2].append(p)

def bfs(l):
    isVisited = [0 for _ in range(27)]
    s = 'A'
    d = deque()
    d.append(0)
    isVisited[0] = 1
    while(len(d)):
        v = d.popleft()
        for i in l[v]:
            if isVisited[i] == 0:
                isVisited[i] = 1
                s += convIntToStr(i)
                d.append(i)
    return s

def dfs(idx, isVisited, l, s):
    for t in l[idx]:
        if isVisited[t] == 1:
            continue
        else:
            isVisited[t] = 1
            dfs(t, isVisited, l, s)
            s += convIntToStr(t)

def dfs2(idx, isVisited, l, s):
    for t in l[idx]:
        if isVisited[t] == 1:
            continue
        else:
            isVisited[t] = 1
            dfs(t, isVisited, l, s)
            s += convIntToStr(t)

print(bfs(l))
s = ""
dfs(0)
print(s)
s = ""
dfs(0)
print(s)
