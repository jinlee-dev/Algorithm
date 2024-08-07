import sys

n, m = map(int, sys.stdin.readline().split(" "))

v = [0 for i in range(8)]

def BT(c):
    global v, n, m
    if c == m:
        for i in range(c):
            print(v[i], end=" ")
        print("")
    else:
        for i in range (1, n + 1):
            v[c] = i
            BT(c + 1)

BT(0)