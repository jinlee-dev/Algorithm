import sys

N = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split(" ")))
tmp = [0 for i in range(100001)]

count = 0
e = 0
for s in range(N):
    while e < N:
        hasSameNumber = tmp[l[e]] >= 1
        if hasSameNumber:
            tmp[l[s]] = 0
            break
        else:
            count = count + (e - s + 1)
            tmp[l[e]] = 1
            e = e + 1


print(count)