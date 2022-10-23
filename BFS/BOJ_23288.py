import sys
from collections import deque

#east : 0, west : 1, south : 2, north : 3
def UpdateDice(jusawi, direction):
    dice = jusawi.copy()
    if direction == 0:
        dice[1] = jusawi[4]
        dice[4] = jusawi[6]
        dice[6] = jusawi[3]
        dice[3] = jusawi[1]
    elif direction == 1:
        dice[1] = jusawi[3]
        dice[3] = jusawi[6]
        dice[6] = jusawi[4]
        dice[4] = jusawi[1]
    elif direction == 2:
        dice[1] = jusawi[2]
        dice[2] = jusawi[6]
        dice[6] = jusawi[5]
        dice[5] = jusawi[1]
    elif direction == 3:
        dice[1] = jusawi[5]
        dice[5] = jusawi[6]
        dice[6] = jusawi[2]
        dice[2] = jusawi[1]   
    
    return dice

def BFS(graph, startPos, width, height):
    q = deque()
    val = graph[startPos[0]][startPos[1]]
    isVisited = [[False] * (height + 1) for _ in range(width + 1)]
    isVisited[startPos[0]][startPos[1]] = True
    count = 1
    q.append(startPos)
    bw = [
        [0, -1],
        [0, 1],
        [1, 0],
        [-1, 0],
    ]

    while 0 != len(q):
        v = q.popleft()
        for i in bw:
            curDir = [0] * 2
            curDir[0] = i[0] + v[0]
            curDir[1] = i[1] + v[1]
            if curDir[0] > 0 and curDir[1] > 0 and curDir[0] <= width and curDir[1] <= height:    
                if False == isVisited[curDir[0]][curDir[1]]:
                    isVisited[curDir[0]][curDir[1]] = True
                    if graph[curDir[0]][curDir[1]] == val:
                        q.append(curDir)
                        count = count + 1
    return count


def GetScore(startPos, jusawi, scoreBoard, width, height):
    score = scoreBoard[startPos[0]][startPos[1]]
    
    return score * count

def GetLocation(dir, location, mW, mH, retDir, jusawi):
    retDir = dir
    if dir == 2:
        location[0] = location[0] + 1
        if location[0] > mW:
            location[0] = location[0] - 2
            retDir = 3
    elif dir == 3:
        location[0] = location[0] - 1
        if location[0] <= 0:
            location[0] = location[0] + 2
            retDir = 2
    elif dir == 1:
        location[1] = location[1] - 1
        if location[1] <= 0:
            location[1] = location[1] + 2
            retDir = 0
    elif dir == 0:
        location[1] = location[1] + 1
        if location[1] > mH:
            location[1] = location[1] - 2
            retDir = 1
    jusawi = UpdateDice(jusawi, retDir)
    return [location, jusawi, retDir]

def GetDirection(scoreBoard, dir, startPos, value):
    if scoreBoard[startPos[0]][startPos[1]] < value:
        if dir == 0:
            dir = 2
        elif dir == 1:
            dir = 3
        elif dir == 2:
            dir = 1
        elif dir == 3:
            dir = 0

    elif scoreBoard[startPos[0]][startPos[1]] > value:
        if dir == 0:
            dir = 3
        elif dir == 1:
            dir = 2
        elif dir == 2:
            dir = 0
        elif dir == 3:
            dir = 1
    return dir

def solution(count, scoreBoard, board, mW, mH):
    startPos = [1, 1]
    score = 0
    direction = 1
    #1:아래, 2:뒤 3:오른 4:왼 5:앞 6: 위
    jusawi = [0, 1, 2, 3, 4, 5, 6]
    #east
    direction = 0
    for _ in range(count):
        ret = GetLocation(direction, startPos, mW, mH, direction, jusawi)
        startPost = ret[0]
        jusawi = ret[1]
        direction = ret[2]
        score = score + board[startPos[0]][startPos[1]]
        direction = GetDirection(scoreBoard, direction, startPos, jusawi[6])
    return score


col, row, count = map(int, sys.stdin.readline().split(" "))
scoreBoard = [[] for _ in range(col + 1)]
board = [[0] * (row + 1) for _ in range(col + 1)]

for i in range(1, col + 1):
    scoreBoard[i] = list(map(int, sys.stdin.readline().split(" ")))
    scoreBoard[i].insert(0, 0)

for i in range(1, col + 1):
    for j in range(1, row + 1):
        board[i][j] = scoreBoard[i][j] * BFS(scoreBoard, [i, j], col, row)

print(solution(count, scoreBoard, board, col, row))