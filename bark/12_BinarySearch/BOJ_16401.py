import sys

M, N = map(int, sys.stdin.readline().split(" "))
snack = list(map(int, sys.stdin.readline().split(" ")))

s = 0
e = 1000000000
snack.sort()

while s < e:
    mid = (s + e + 1) // 2
    snackCnt = 0
    for i in snack:
        snackCnt = snackCnt + (i // mid)

    if snackCnt < M:
        e = mid - 1
    else:
        s = mid

print(s)

