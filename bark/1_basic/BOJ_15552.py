import sys

c = int(sys.stdin.readline())
arr = []
for i in range(c):
    add1, add2 = map(int, sys.stdin.readline().split(' '))
    arr.append(add1 + add2)

for i in arr:
    print(i)