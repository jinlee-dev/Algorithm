import sys
mapSize, selectChickCnt = map(int, sys.stdin.readline().split(" "))
chickenMap = [ list(map(int, sys.stdin.readline().split(" "))) for _ in range (mapSize)]

homeList = []
chickList = []

for i in range(mapSize):
    for j in range(mapSize):
        if chickenMap[i][j] == 1:
            homeList.append([i, j])
        elif chickenMap[i][j] == 2:
            chickList.append([i, j])

isVisited = [False for i in range(len(chickList))]

minDist = 1e9
def backtracking(index, selectChickList):
    global homeList, selectChickCnt, minDist, chickList
    if len(selectChickList) == selectChickCnt:
        curDist = 0
        for i in homeList:
            homeX = i[0]
            homeY = i[1]
            dist = 1e9
            for j in selectChickList:
                x = j[0]
                y = j[1]
                dist = min(dist, abs(homeX - x) + abs(homeY- y))
            curDist = dist + curDist
        minDist = min(minDist, curDist)
        return
    else:
        for i in range(index, len(isVisited)):
            if isVisited[i] == False:
                isVisited[i] = True
                selectChickList.append(chickList[i])
                backtracking(i, selectChickList)
                selectChickList.pop()
                isVisited[i] = False

s = []
backtracking(0, s)
print(minDist)