import sys

v = int(sys.stdin.readline())
ret = v
for i in range (2, v):
    d = i * i
    if d > ret:
        break
    else:
        while v % i == 0:
            v = v / i
            print(i)

if v != 1.0:
    print(int(v))