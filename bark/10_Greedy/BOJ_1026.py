import sys

count = int(sys.stdin.readline())
l1 = list(map(int, sys.stdin.readline().split(" ")))
l2 = list(map(int, sys.stdin.readline().split(" ")))

l1.sort()
l2.sort(reverse=True)

v = 0
for i in range(count):
    v = v + (l1[i] * l2[i])

print(v)