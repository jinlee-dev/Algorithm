import sys
from collections import deque

def bfs(jimin, bro):
    if jimin == bro:
        return 0
    isVisited = {}
    time = 0
    q = deque()
    q.append((jimin, 0))
    isVisited[jimin] = True
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
                return depth + 1
            elif i > 100000:
                continue
            elif False == (i in isVisited):
                isVisited[i] = True
                q.append((i, depth + 1))


jimin, bro = map(int, sys.stdin.readline().split(" "))
print(bfs(jimin, bro))