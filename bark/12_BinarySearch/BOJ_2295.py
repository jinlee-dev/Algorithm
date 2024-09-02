import sys

n = int(sys.stdin.readline().rstrip())
u = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

arr = []
res = 0
for i in range(n):
    for j in range(i, n):
        arr.append(u[i] + u[j])
arr.sort()

def bin_search(target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
    return False

for i in range(n):
    for j in range(i, n):
        target = u[j] - u[i]
        if bin_search(target):
            res = max(res, u[j])

print(res)