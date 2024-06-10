import sys

l = []
for i in range(5):
    l.append(int(sys.stdin.readline()))
l.sort()
av = 0
for i in range(5):
    av = av + l[i]
av = av / 5

print(int(av))
print(l[2])