import sys

count = int(sys.stdin.readline())
cardNumber = list(map(int, sys.stdin.readline().split(" ")))
reqCnt = int(sys.stdin.readline())
cardList = list(map(int, sys.stdin.readline().split(" ")))

cardNumber.sort()

def binarySearch_st(sArr, target):
    s = 0
    e = len(sArr)
    while s < e:
        m = (s + e) // 2

        if sArr[m] >= target:
            e = m
        else:
            s = m + 1
    return s

def binarySearch_et(sArr, target):
    s = 0
    e = len(sArr)
    while s < e:
        m = (s + e) // 2

        if target < sArr[m]:
            e = m
        else:
            s = m + 1
    
    return s


for i in cardList:
    print(binarySearch_et(cardNumber, i) - binarySearch_st(cardNumber, i))