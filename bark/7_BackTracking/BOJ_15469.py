import sys

x, y = map(int, sys.stdin.readline().split(" "))

isUsed = [0 for i in range(9)]
value = [0 for i in range(9)]

# n 자연수 개수, m 선택 개수, c 현재 고른 개수
def Backtracking(n, m, c, v):
    global isUsed
    global value
    if c == m:
        for i in range(m):
            print(value[i], end=' ')
        print("")
    else:
        for i in range(1, n + 1):
            if False == isUsed[i]:
                isUsed[i] = True
                value[c] = i
                Backtracking(n, m, c + 1, i)
                isUsed[i] = False

Backtracking(x, y, 0, 1)