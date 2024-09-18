import sys
count, excludeCnt = map(int, sys.stdin.readline().split(" "))
l = list(map(int, sys.stdin.readline().split(" ")))

ans = 0
cnt = 0
curExcCnt = 0
s, e = 0 , 0

while(e < count):
    # 제외한 개수가 최대개수보다 더 크다면, 제외개수를 낮출 때까지 count를 낮춰준다
    if curExcCnt > excludeCnt:
        if l[s] % 2 == 0:
            cnt -= 1
        else:
            curExcCnt -= 1
        s += 1

    # 개수가 같거나 적다면, 개수를 올리고, e를 올려준다
    elif l[e] % 2 == 0: 
        cnt += 1
        e += 1
    # 홀수 찾으면 홀수 개수를 올려준다
    else:
        curExcCnt += 1
        e += 1
    
    # 최대개수 업데이트
    ans = max(ans,cnt)
    
print(ans)