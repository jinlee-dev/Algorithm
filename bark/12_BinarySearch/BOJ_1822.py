import sys

ac, bc = map(int, sys.stdin.readline().split(" "))

al = list(map(int, sys.stdin.readline().split(" ")))
bl = list(map(int, sys.stdin.readline().split(" ")))

al.sort()
bl.sort()

def binSearch(arr, target):
    s = 0
    e = len(arr)

    while s < e:
        m = (s + e) // 2
        if arr[m] == target:
            return True
        elif arr[m] < target:
            s = m + 1
        else:
            e = m
    
    return False

ret = []
for i in al:
    if False == binSearch(bl, i):
        ret.append(i)

print(len(ret))
for i in range(len(ret)):
    print(ret[i], end=" ")