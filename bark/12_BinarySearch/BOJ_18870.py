import sys

c = int(sys.stdin.readline())
v = list(map(int, sys.stdin.readline().split(" ")))

dup = sorted(list(set(v)))

def binary_search(arr, target):
    s = 0
    e = len(arr)

    while s < e:
        m = (s + e) // 2

        if arr[m] >= target:
            e = m
        else:
            s = m + 1
        
    return s

for i in v:
    print(binary_search(dup, i), end=" ")