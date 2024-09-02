import sys

c = int(sys.stdin.readline())
l = []

for i in range(c):
    l.append(int(sys.stdin.readline()))


l.sort()
l2 = []

for i in range(c):
    for j in range(i + 1, c):
        l2.append(l[i] + l[j])

def binSearch(arr, target):
    s = 0
    e = len(arr)
    while s < e:
        mid = (s + e) // 2
        if arr[mid] < target:
            s = mid + 1
        elif arr[mid] > target:
            e = mid - 1
        else:
            return mid    
    return -1

l2.sort()
ret = 0
for i in range(len(l) - 1, 0, -1):
    for j in range(0, i):
        binIdx = binSearch(l2, l[i] - l[j])
        if binIdx != -1:
            ret = l[i]
            break
    if ret != 0:
        break

print(ret)
