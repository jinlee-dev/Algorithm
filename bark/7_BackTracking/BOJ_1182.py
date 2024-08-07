import sys

c, sum = map(int, sys.stdin.readline().split(" "))
seq = list(map(int, sys.stdin.readline().split(" ")))


isVisit = [False for i in range (c)]
count = 0

def BackTracking(selectCnt, curSum, index):
    global c, sum, isVisit, count, seq
    if selectCnt == c:
        if curSum == sum:
            count = count + 1
        return 0
    else:
        if curSum == sum:
            count = count + 1
        for i in range(index, c):
            if isVisit[i] == False:
                curSum = curSum + seq[i]
                isVisit[i] = True
                BackTracking(selectCnt + 1, curSum, i)
                isVisit[i] = False
                curSum = curSum - seq[i]

if sum == 0:
    count = count - 1
        
BackTracking(0, 0, 0)
print(count)