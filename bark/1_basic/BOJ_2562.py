import sys
count = 1
maxCnt = 1
maxVal = 0
for i in range(9):
    v = int(sys.stdin.readline())
    if maxVal < v:
        maxVal = v
        maxCnt = count
    count = count + 1

print(maxVal)
print(maxCnt)