import sys
from collections import deque

def bfs(subin, bro):
    if subin == bro:
        return [0, str(subin)]
    isVisited = {}
    time = 0
    q = deque()
    q.append((subin, 0, str(subin)))
    isVisited[subin] = True
    while q:
        nextNode = q.popleft()
        depth = nextNode[1]
        cases = [
            nextNode[0] + 1,
            nextNode[0] - 1,
            nextNode[0] * 2
        ]
        for i in cases:
            if i == bro:
                ret = nextNode[2] + " " + str(i)
                return [depth + 1, ret]
            elif i > 100000:
                continue
            elif False == (i in isVisited):
                isVisited[i] = True
                path = nextNode[2]
                path = path + " " + str(i)
                q.append((i, depth + 1, path))


subin, bro = map(int, sys.stdin.readline().split(" "))
ret = bfs(subin, bro)
print(ret[0])
print(ret[1])