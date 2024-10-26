import sys

# 북 동 남 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]


N, M = map(int, sys.stdin.readline().split(" "))
room = []

X, Y, pos = map(int, sys.stdin.readline().split(" "))

for i in range(N):
    room.append(list(map(int, sys.stdin.readline().split(" "))))

def ClockWise(startDir):
    if startDir == 0:
        return 3
    elif startDir == 1:
        return 0
    elif startDir == 2:
        return 1
    else:
        return 2
    
cursor = [X, Y, pos]
while 1:
    ret = False
    dir = cursor[2]
    # 현재 자리가 청소되어 있지 않다면 현재 자리를 청소한다
    if room[cursor[0]][cursor[1]] == 0:
        room[cursor[0]][cursor[1]] = 2
    else:
        # 청소되지 않은 빈칸이 있는지 확인한다
        for i in range(4):
            dir = ClockWise(dir)
            cw = [cursor[0] + dx[dir], cursor[1] + dy[dir], dir]
            if cw[0] < 0 or cw[1] < 0 or cw[0] >= N or cw[1] >= M:
                continue
            else:
                nextPos = room[cw[0]][cw[1]]
                # 청소해야 하는 자리가 있을 경우 청소를 한다
                if nextPos == 0:
                    room[cw[0]][cw[1]] = 2
                    ret = True
                    cursor = cw
                    break
        # 청소를 못했을 경우
        if ret == False:
            dir = cursor[2]
            # 한칸 뒤로 땡긴다
            nextPos = [cursor[0] - dx[dir], cursor[1] - dy[dir]]
            # 더 갈 수 있는 곳이 없거나, 벽이면 중지한다
            if nextPos[0] < 0 or nextPos[1] < 0 or nextPos[0] >= N or nextPos[1] >= M or room[nextPos[0]][nextPos[1]] == 1:
                break
            else:
                cursor = [nextPos[0], nextPos[1], cursor[2]]


answer = 0
for i in range(N):
    for j in range(M):
        if room[i][j] == 2:
            answer += 1

print(answer)