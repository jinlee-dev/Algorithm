import sys

c = int(sys.stdin.readline())
l = []

for i in range(c):
    s, w = map(int, sys.stdin.readline().split(" "))
    l.append([s, w])

ng = []
for i in range (c):
    ng.append(l[i][0])

answer = 0
def bt(idx, brokenCnt):
    global c, answer, ng, l
    if idx == c:
        answer = max(brokenCnt, answer)
        return
    elif ng[idx] <= 0 or brokenCnt == c - 1:
        bt(idx + 1, brokenCnt)
    else:
        nCnt = brokenCnt
        for i in range(c):
            if i == idx:
                continue
            if ng[i] <= 0:
                continue
            else:
                ng[idx] = ng[idx] - l[i][1]
                if ng[idx] <= 0:
                    brokenCnt = brokenCnt + 1

                ng[i] = ng[i] - l[idx][1]
                if ng[i] <= 0:
                    brokenCnt = brokenCnt + 1

                bt(idx + 1, brokenCnt)
                ng[idx] = ng[idx] + l[i][1]
                ng[i] = ng[i] + l[idx][1]
                brokenCnt = nCnt

bt(0, 0)
print(answer)