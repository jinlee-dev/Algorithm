import sys

N, M = map(int, sys.stdin.readline().split(" "))
tree = list(map(int, sys.stdin.readline().split(" ")))

s = 0
e = 1000000000

tree.sort()

while s < e:
    mid = (s + e + 1) // 2
    ret = 0
    for i in tree:
        ret = ret + max(0, i - mid)
    if ret < M:
        e = mid - 1
    else:
        s = mid

print(s)