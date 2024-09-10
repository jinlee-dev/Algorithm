import sys

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split(" ")))

v = 200000001
ret = 0

for i in range(len(A)):
    s = i + 1
    e = len(A) - 1

    while s <= e:
        m = (s + e) // 2
        curValue = A[i] + A[m]
        if abs(curValue) < v:
            v = abs(curValue)
            ret = A[i] + A[m]

            if v == 0:
                break

        if curValue < 0:
            s = m + 1

        else:
            e = m - 1

print(ret)
