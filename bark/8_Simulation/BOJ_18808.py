import sys

n, m, k = map(int, sys.stdin.readline().split(" "))
inputStiker = []
for i in range(k):
    nn, mm = map(int, sys.stdin.readline().split(" "))
    inputStiker.append([list(map(int, input().rstrip().split(" "))) for _ in range(nn)])

stikerList = []
for stiker in inputStiker:
    rotatedStikerList = []
    sizeX, sizeY = len(stiker[0]), len(stiker)
    # 90, 180, 270을 계산한다
    prevStiker = stiker
    for angleIdx in range(3):
        # 이전 X, Y를 뒤집어준다
        tmp = sizeY
        sizeY = sizeX
        sizeX = tmp
        # 뒤집어준 만큼 할당을 한다
        rotateStiker = [[0 for j in range (sizeX)] for _ in range (sizeY)]
        # 값을 뒤집어서 넣어준다
        for k in range(sizeX):
            for t in range(sizeY):
                prevX = t
                prevY = k
                rotateStiker[sizeY - t - 1][k] = prevStiker[k][t]
        
        rotatedStikerList.append(rotateStiker)
        prevStiker = rotateStiker
    
    rotatedStikerList.reverse()
    stikerList.append(rotatedStikerList)

def IsStikable(stiker, lStartX, lStartY, lapTop):
    global n, m
    stikerX = len(stiker)
    stikerY = len(stiker[0])
    for i in range(lStartX, lStartX + stikerX):
        for j in range(lStartY, lStartY + stikerY):
            sXIndex = i - lStartX
            sYIndex = j - lStartY
            if i >= n or j >= m:
                return False
            elif stiker[sXIndex][sYIndex] == 1 and lapTop[i][j] == 1:
                return False
    return True

def SetStiker(stiker, lStartX, lStartY, lapTop):
    global n, m
    stikerX = len(stiker)
    stikerY = len(stiker[0])
    for i in range(lStartX, lStartX + stikerX):
        for j in range(lStartY, lStartY + stikerY):
            sXIndex = i - lStartX
            sYIndex = j - lStartY
            lapTop[i][j] = max(stiker[sXIndex][sYIndex], lapTop[i][j])


lapTop = [[0 for i in range(m)] for j in range(n)]
# 스티커 개수만큼 돌려준다
for stiker in range(len(inputStiker)):
    # 일단 회전없이 붙일 수 있는지 확인한다
    stikerX = len(inputStiker[stiker])
    stikerY = len(inputStiker[stiker][0])   
    ret = False 
    for j in range(0, n):
        for k in range(0, m):
            if True == IsStikable(inputStiker[stiker], j, k, lapTop):
                SetStiker(inputStiker[stiker], j, k, lapTop)
                ret = True
                break
        if ret == True:
            break

    if ret == False:
        # 로테이션한 스티커리스트를 확인한다.
        for rotation in stikerList[stiker]:
            for xCoord in range(n):
                for yCoord in range(m):
                    # 스티커 사이즈 확인
                    stikerX = len(rotation)
                    stikerY = len(rotation[0])
                    if True == IsStikable(rotation, xCoord, yCoord, lapTop):
                        SetStiker(rotation, xCoord, yCoord, lapTop)
                        ret = True
                        break
                if ret == True:
                    break
            if ret == True:
                break


count = 0
for i in range (n):
    for j in range (m):
        if lapTop[i][j] == 1:
            count = count + 1

print(count)