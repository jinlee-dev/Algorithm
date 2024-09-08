import sys

def binary_search(l, target):
    s = 0
    e = len(l)
    while s < e:
        m = (s + e) // 2
        if l[m] >= target:
            e = m
        else:
            s = m + 1
    return s


universe, count = map(int, sys.stdin.readline().split(" "))
univList = []

for i in range(universe):
    univList.append(list(map(int, sys.stdin.readline().split(" "))))

copyUniv = []

for i in range(len(univList)):
    copyUniv.append(sorted(univList[i]))

ret = []
for i in range(len(univList)):
    r = []
    for j in range(len(univList[i])):
        r.append(binary_search(copyUniv[i], univList[i][j]))
    ret.append(r)

ret.sort()

count = 0
for i in range(len(ret) - 1):
    for j in range(i + 1, len(ret)):
        if ret[i] == ret[j]:
            count = count + 1

print(count)