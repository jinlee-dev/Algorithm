import sys

arr = []
for i in range(21):
    arr.append(i)

for i in range(10):
    s, e = map(int, sys.stdin.readline().split(' '))
    s = s
    e = e + 1
    v = arr[s:e]
    v.reverse()
    idx = 0
    for i in range(s, e):
        arr[i] = v[idx]
        idx = idx + 1
for i in arr:
    if i != 0:
        print(i, end=" ")