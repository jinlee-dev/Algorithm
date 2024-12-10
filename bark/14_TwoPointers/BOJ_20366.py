import sys

c = int(sys.stdin.readline())
v = list(map(int, sys.stdin.readline().split(" ")))
v.sort()

minVal = abs((v[0] + v[1]) - (v[2] + v[3]))
for i in range(c - 3):
    for j in range(i + 3, c):
        #print(i, j)
        babySum = v[i] + v[j]
        e1 = i + 1
        e2 = j - 1
        while e1 < e2:
            sum = v[e1] + v[e2]
            minVal = min(abs(sum - babySum), minVal)
            if sum > babySum:
                e2 -= 1
            elif sum < babySum:
                e1 += 1

print(minVal)