import sys
count = int(sys.stdin.readline())

l = [list(map(int, sys.stdin.readline().split(" "))) for _ in range (count)]

l.sort()

startDay = (3, 1)
idx = 0
answer = 0
ret = False

while idx < count:
    start = (l[idx][0], l[idx][1])
    end = (l[idx][2], l[idx][3])
    if start <= startDay < end:
        maxEnd = end
        while idx < count - 1:
            curStart = (l[idx + 1][0],l[idx + 1][1])
            curEnd = (l[idx + 1][2],l[idx + 1][3])
            if startDay < curStart:
                break
            if maxEnd < curEnd:
                maxEnd = curEnd
            idx = idx + 1
    
        answer = answer + 1
        startDay = maxEnd
            
        if maxEnd > (11, 30):
            print(answer)
            ret = True
            break
    idx = idx + 1

if ret == False:
    print(0)