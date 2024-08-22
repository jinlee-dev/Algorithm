import sys

count = int(sys.stdin.readline())
l = [int(sys.stdin.readline()) for _ in range(count)]

l.sort(reverse=True)

maxWeight = 0
curWeight = 0
for i in range(count):
    curWeight = l[i] * (i + 1)
    if curWeight > maxWeight:
        maxWeight = curWeight

print(maxWeight)
