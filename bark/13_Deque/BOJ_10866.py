import sys
from collections import deque

count = int(sys.stdin.readline())

d = deque([])
for i in range(count):
    st1 = str(sys.stdin.readline().rstrip())
    if st1 == 'front':
        if len(d) != 0:
            print(d[0])
        else:
            print(-1)
    elif st1 == 'back':
        if len(d) != 0:
            print(d[len(d) - 1])
        else:
            print(-1)
    elif st1 == 'size':
        print(len(d))
    elif st1 == 'empty':
        if(len(d) == 0):
            print(1)
        else:
            print(0)
    elif st1 == 'pop_front':
        if len(d):
            print(d.popleft())
        else:
            print(-1)
    elif st1 == 'pop_back':
        if len(d):
            print(d.pop())
        else:
            print(-1)
    else:
        v, t = st1.split(" ")
        num = int(t)
        if v == 'push_back':
            d.append(t)
        else:
            d.appendleft(t)

