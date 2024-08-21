import sys

count = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split(" ")))


dp = [1 for i in range(count + 1)]
nextIdx = [-1 for i in range(count + 1)]
maxIdx = 0
maxVal = 0
for i in range (count):
    for j in range(i - 1, -1, -1):
        if l[i] > l[j]:
            if dp[i] < (dp[j] + 1):
                dp[i] = dp[j] + 1
                nextIdx[i] = j
    if dp[i] > maxVal:
        maxVal = dp[i]
        maxIdx = i

answer = []
curIdx = maxIdx
for i in range(maxVal):
    answer.insert(0, l[curIdx])
    curIdx = nextIdx[curIdx]


s = ""
for i in answer:
    s = s + (str(i))
    s= s + (" ")
print(maxVal)
print(s.rstrip())