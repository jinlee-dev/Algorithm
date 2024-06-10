import sys

i = str(sys.stdin.readline())
i = i.replace('\n', '')
j = str(sys.stdin.readline())
j = j.replace('\n', '')
start = int(ord("a"))
li = list(i)
lj = list(j)

arr1 = [0] * 26
arr2 = [0] * 26

for k in i:
    v = ord(k) - start
    arr1[v] = arr1[v] + 1
for k in j:
    v = ord(k) - start
    arr2[v] = arr2[v] + 1

ret = 0
for i in range(26):
    if arr1[i] != arr2[i]:
        ret = ret + abs(arr1[i] - arr2[i])

print(ret)