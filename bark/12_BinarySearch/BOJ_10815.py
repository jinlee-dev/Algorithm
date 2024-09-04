import sys

c = int(sys.stdin.readline())
l1 = list(map(int, sys.stdin.readline().split(" ")))

c2 = int(sys.stdin.readline())
l2 = list(map(int, sys.stdin.readline().split(" ")))

l1.sort()

def binSearch(l, target):
    s = 0
    e = len(l) - 1
    while s <= e:
        m = (s + e) // 2
        if target < l[m]:
            e = m - 1
        elif target > l[m]:
            s = m + 1
        else:
            return 1
    
    return 0

for i in l2:
    print(binSearch(l1, i), end=" ")