import sys

a = [[0 for col in range(7)] for row in range(2)]
count, max = map(int, sys.stdin.readline().split(" "))

for i in range(count):
    sex, grade = map(int, sys.stdin.readline().split(" "))
    a[sex][grade] = a[sex][grade] + 1

roomCnt = 0
for i in range(2):
    for j in range(7):
        curRoomCnt = int(a[i][j] / max)
        if a[i][j] % max != 0:
            curRoomCnt = curRoomCnt + 1
        roomCnt = curRoomCnt + roomCnt

print(roomCnt)
