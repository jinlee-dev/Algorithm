import sys
INPUT = sys.stdin.readline

def cond(arr, target):
    ret = 0
    st = 0
    curAnswer = 0

    for i in range(0, len(arr)):
        if st > i:
            continue
        else:
            curAnswer = 0
            for j in range(st, len(arr)):
                curAnswer += arr[j]
                if curAnswer > target:
                    st = j
                    ret += 1
                    break
    
    if curAnswer == 0:
        ret += 1
    return ret
        
            

N, M = map(int, INPUT().split(" "))
arr = list(map(int, INPUT().split(" ")))

acc = []
acc.append(arr[0])

length = 0
for i in range(0, len(arr)):
    length += arr[i] 

s, e = 0, length

while s < e:
    mm = (s + e) // 2
    cnt = cond(arr, mm)
    if cnt < M:
        e = mm
    else:
        s = mm + 1
    
print(s)
