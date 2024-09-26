import sys
import heapq

problemCnt = int(sys.stdin.readline())

for i in range(problemCnt):
    problemList = []
    bstMin = []
    bstMax = []
    num = int(sys.stdin.readline())
    isVisited =  [False for i in range(num + 1)]
    heapCnt = 0    

    for j in range(num):
        func, value = map(str, sys.stdin.readline().rstrip().split(" "))
        value = int(value)
        if func == 'I':
            heapCnt += 1
            heapq.heappush(bstMin, (value, j))
            heapq.heappush(bstMax, (-value, j))
            isVisited[j] = True
        elif func == 'D':
            if heapCnt != 0:
                if value == 1:
                    while len(bstMax):
                        ret = heapq.heappop(bstMax)
                        if isVisited[ret[1]] == True:
                            isVisited[ret[1]] = False
                            heapCnt -= 1
                            break
                                         
                else:
                    while len(bstMin):
                        ret = heapq.heappop(bstMin)
                        if isVisited[ret[1]] == True:
                            isVisited[ret[1]] = False
                            heapCnt -= 1
                            break
    
    minValRet = False
    maxValRet = False
    minVal = 0
    maxVal = 0
    while len(bstMax):
        maxheap = heapq.heappop(bstMax)
        if isVisited[maxheap[1]] == True:
            maxValRet = True
            maxVal = -maxheap[0]
            break

    while len(bstMin):
        minHeap = heapq.heappop(bstMin)
        if isVisited[minHeap[1]] == True:
            minValRet = True
            minVal = minHeap[0]
            break
    
    if minValRet and maxValRet:
        print(maxVal, minVal)
    elif minValRet:
        print(minVal, minVal)
    elif maxValRet:
        print(maxVal, maxVal)
    else:
        print("EMPTY")