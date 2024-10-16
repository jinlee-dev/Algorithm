import sys
from collections import deque

c = int(sys.stdin.readline())
l = sorted(list(map(str, sys.stdin.readline().rstrip().split(" "))))
parent = [[] for _ in range(c)]
child = [[] for _ in range(c)]
answer = [[] for _ in range(c)]

indegree = [0 for _ in range(c)]
dic = {}
for i in range(len(l)):
    dic[l[i]] = i

linkCnt = int(sys.stdin.readline())
for _ in range(linkCnt):
    s, e = map(str, sys.stdin.readline().rstrip().split(" "))
    sIdx, eIdx = dic[s], dic[e]
    parent[sIdx].append(eIdx)
    child[eIdx].append(sIdx)
    indegree[sIdx] += 1

boss = []
for i in range(c):
    if len(parent[i]) == 0:
        boss.append(i)

for i in boss:
    q = deque()
    q.append(i)

    while(len(q) != 0):
        v = q.popleft()
        for j in child[v]:
            indegree[j] -= 1
            if indegree[j] == 0:
                answer[v].append(j)
                q.append(j)

print(len(boss))
for _ in range(len(boss)):
    print(l[boss[_]], end=" ")
print()

for i in range(c):
    print(l[i], len(answer[i]), end=" ")
    answer[i].sort()
    for j in answer[i]:
        print(l[j], end=" ")
    print()