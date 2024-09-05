import sys

k, n = map(int, sys.stdin.readline().split(" "))
lan = [ int(sys.stdin.readline()) for _ in range (k)]

s = 1
e = (2**31) - 1
m = 0

while s < e:
    m = (s + e + 1) // 2
    cnt = 0
    for i in lan:
        cnt = cnt + (i // m)
    
    if cnt < n:
        e = m - 1
    else:
        s = m


print(s)