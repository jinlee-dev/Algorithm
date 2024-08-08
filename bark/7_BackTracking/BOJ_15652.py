import sys

n, m = map(int, sys.stdin.readline().split(" "))

def BT(cnt, l, prevIdx):
    global n, m
    if cnt == m:
        for i in range(cnt):
            print(l[i], end=" ")
        print()
        return

    for i in range(prevIdx, n + 1):
        l[cnt] = i
        BT(cnt + 1, l, i)

l = [0 for i in range(m)]
BT(0, l, 1)