import sys

count = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split(" ")))

l.sort()
value = int(sys.stdin.readline())
ret = 0
for i in range (count - 1):
    for j in range(i + 1, count):
        if l[i] + l[j] == value:
            ret = ret + 1
        elif l[i] + l[j] > value:
            break

print(ret)