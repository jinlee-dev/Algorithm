import sys
num = int(sys.stdin.readline())
v = list(map(int, sys.stdin.readline().split(" ")))
v.sort()

def bs(startIdx, endIdx, target):
    while startIdx < endIdx:
        mid = ((startIdx + endIdx) // 2)
        if v[mid] < target:
            startIdx = mid + 1
        else:
            endIdx = mid
    return startIdx


ans = 0
for i in range(num- 2):
    start = i + 1
    end = num - 1
    t = num
    while start < end:
        sum = v[start] + v[end] + v[i]
        if sum > 0:
            end -= 1
        elif sum == 0:
            if v[start] == v[end]:
                ans += (end-start)
            else:
                if t > end:
                    t = end
                    while t >= 0 and v[end] == v[t-1]:
                        t -= 1
                ans += end - t + 1
            start += 1
        else:
            start += 1
print(ans)