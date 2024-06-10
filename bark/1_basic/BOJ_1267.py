import sys

def YG(time, min, money):
    c = int(time / min)
    v = money * c
    if time % (min - 1) != 0:
        v = v + money
    return v


count = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(" ")))
ysV = 0
msV = 0
for i in arr:
    ysV = ysV + YG(i, 30, 10)
    msV = msV + YG(i, 60, 15)

if ysV < msV:
    print("Y %d" % (ysV))
elif ysV > msV:
    print("M %d" % (msV))
else:
    print("Y M %d" % (msV))