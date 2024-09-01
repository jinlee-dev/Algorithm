import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split(" ")))
M = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(" ")))

A.sort()

def binarySearch(sortedArr, value):
    b = 0
    e = len(sortedArr) - 1
    
    while b <= e:
        m = (b + e) // 2

        if sortedArr[m] == value:
            return 1
        elif value > sortedArr[m]:
            b = m + 1
        else:
            e = m - 1
    
    return 0

for i in arr:
    print(binarySearch(A, i))

