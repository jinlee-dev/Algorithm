import sys
from collections import deque
sushiCnt, sushiKind, eatCnt, coupon = map(int,sys.stdin.readline().split())
sushi = [int(sys.stdin.readline()) for _ in range(sushiCnt)]

l = deque()
ans = 0
# 한 번에 넣는 스시 개수
v = min(sushiCnt,eatCnt)

for j in range(v): 
    l.append(sushi[j])
l.append(coupon)
ans = len(set(l))
l.pop()

for i in range(sushiCnt):
    sIdx = (i + v)% sushiCnt
    l.append(sushi[sIdx])
    l.popleft()
    l.append(coupon)
    ans = max(ans, len(set(l)))
    l.pop()

print(ans)


