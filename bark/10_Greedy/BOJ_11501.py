import sys

count = int(sys.stdin.readline())

l = []
for i in range(count):
    sys.stdin.readline()
    l.append(list(map(int, sys.stdin.readline().split(" "))))


for i in range(count):
    jusik = []
    for j in range (len(l[i])):
        jusik.append(l[i][j])

    money = 0
    curIdx = 0
    while (curIdx < len(jusik)):
        curJusik = []
        maxIdx = 0
        maxVal = 0
        for k in range(curIdx, len(jusik)):
            if maxVal <= jusik[k]:
                maxIdx = k
                maxVal = jusik[k]

        for k in range(curIdx, maxIdx):
            curJusik.append(l[i][k])
            if curIdx >= len(jusik):
                break
            curIdx += 1

        for k in range(len(curJusik)):
            money = money + (jusik[maxIdx] - curJusik[k])
        curIdx += 1

    print(money)