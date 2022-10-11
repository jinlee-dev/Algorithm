from collections import deque
import sys

subin,bro = map(int, sys.stdin.readline().split(" "))
check=[0 for _ in range(100001)]

cnt = 0
queue=deque()

if subin != bro:
    queue.append(subin)
else:
    cnt = 1

while queue:
    point = queue.popleft()

    if point == bro:
        cnt += 1

    for i in [point - 1,point + 1,point * 2]:
        if 0<=i<=100000:
            if check[i] == 0 or check[i] >= check[point] + 1:
                check[i] = check[point] + 1
                queue.append(i)


print(check[bro])
print(cnt)