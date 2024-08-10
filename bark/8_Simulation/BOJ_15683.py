import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))
# 반복횟수 하면서 리스트에 값 할당.
t = [list(map(int, input().rstrip().split(" "))) for _ in range(n)]



# 각각 오른쪽/하단/왼쪽/위쪽
def CCTV1(pos, angle, index):
    global t, m, n
    posX = pos[0]
    posY = pos[1]
    if angle == 0:
        for i in range(posY + 1, m):
            if t[posX][i] == 0:
                t[posX][i] = index
            elif t[posX][i] == 6:
                break
    elif angle == 1:
        for i in range(posX + 1, n):
            if t[i][posY] == 0:
                t[i][posY] = index
            elif t[i][posY] == 6:
                break
                
    elif angle == 2:
        for i in range(posY - 1, -1, -1):
            if t[posX][i] == 0:
                t[posX][i] = index
            elif t[posX][i] == 6:
                break        

    elif angle == 3:
        for i in range(posX - 1, -1, -1):
            if t[i][posY] == 0:
                t[i][posY] = index
            elif t[i][posY] == 6:
                break

cctvCase = [ [],
            [[0], [1], [2], [3]],
            [[0, 2], [1, 3]],
            [[0, 1], [1, 2], [2, 3], [3, 0]],
            [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
            [[0, 1, 2, 3]]
            ]

cctvCaseCnt = [
    0, 4, 2, 4, 4, 1
]

def reset(index):
    global t, n, m
    for i in range(n):
        for j in range(m):
            if index == t[i][j]:
                t[i][j] = 0

l = []
isVisited = []
for i in range(n):
    for j in range(m):
        if 0 < t[i][j] <= 5:
            l.append([i, j, t[i][j]])
            isVisited.append([False for i in range(len(cctvCase[t[i][j]]))])


answer = 1e9

uniq = 6
def Backtracking(cameraCnt, cctvCnt):
    cctv = 6
    global answer, t, l, isVisited, cctvCaseCnt, cctvCase, uniq
    count = 0
    if cameraCnt == cctvCnt:
        for i in range(n):
            for j in range(m):
                if 0 == t[i][j]:
                    count = count + 1
        answer = min(count, answer)
        return
    else:
        cctvType = l[cameraCnt][2]
        # 현 CCTV의 가능한 경우의 수
        for j in range(cctvCaseCnt[cctvType]):
            # 카메라의 가능한 경우의 수에 접근하였으면
            if False == isVisited[cameraCnt][j]:
                isVisited[cameraCnt][j] = True
                uniq = uniq + 1
                uniqValue = uniq
                for a in cctvCase[cctvType][j]:
                    CCTV1(l[cameraCnt], a, uniqValue)
                Backtracking(cameraCnt + 1, cctvCnt)
                reset(uniqValue)
                isVisited[cameraCnt][j] = False
                                    
Backtracking(0, len(l))
print(answer)