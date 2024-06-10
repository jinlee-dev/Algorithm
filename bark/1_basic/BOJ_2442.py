import sys

count = int(sys.stdin.readline())
allCnt = count * 2 - 1
for i in range (0, count):
    curStarCnt = allCnt - (i * 2)
    curBlankCnt = int((allCnt - curStarCnt) / 2)
    for j in range(0, curBlankCnt):
        print(" ", end="")
    for j in range(0, curStarCnt):
        print("*", end="")
    print("")    

for i in range(1, count):
    curStarCnt = (i) * 2 + 1
    curBlankCnt = int((allCnt - curStarCnt) / 2)
    for j in range(0, curBlankCnt):
        print(" ", end="")
    for j in range(0, curStarCnt):
        print("*", end="")
    print("")
