import sys
from collections import deque

tc = int(sys.stdin.readline())
retList = []
for i in range(tc):
    f = list(str(sys.stdin.readline()).rstrip())
    numCnt = int(sys.stdin.readline())
    s = str(sys.stdin.readline().rstrip())

    curList = deque()
    if numCnt > 0:
        curList = deque(list(map(int, s[1:len(s) - 1].split(","))))

    ret = True
    isReversed = False
    for j in f:
        if j == 'D':
            if len(curList) > 0:
                if isReversed == True:
                    curList.pop()
                else:
                    curList.popleft()
            else:
                ret = False
                break
        elif j == 'R':
            if isReversed == True: 
                isReversed = False
            else:
                isReversed = True

    curRetStr = ""    
    if ret == False:
        curRetStr = "error"
    else:
        retStr = ""
        if isReversed == True:
            cLen = len(curList)
            for j in range(cLen - 1, -1, -1):
                retStr += str(curList[j]) + ','
        else:            
            for j in curList:
                retStr += str(j) + ','
        
        curRetStr = '[' + retStr.rstrip(',') +']'

    retList.append(curRetStr)
        
for i in retList:
    print(i)