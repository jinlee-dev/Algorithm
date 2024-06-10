import sys

v = 1
for i in range(3):
    v = v * int(sys.stdin.readline())

arr = [0] * 10
div = 10
while ( v != 0 ):
    curVal = v%10
    arr[curVal] = arr[curVal] + 1
    v = v//10

for i in range(10):
    print(arr[i])