import sys
input = sys.stdin.readline

tc = int(input())
for i in range(tc):
    cnt = input()
    v1 = list(map(int, input().split(" ")))
    cnt = input()
    v2 = list(map(int, input().split(" ")))
    v1.sort()


    for j in range(len(v2)):
        ret = False
        s = 0
        e = len(v1) - 1
        while s <= e:
            m = (s + e) // 2
            if v1[m] < v2[j]:
                s = m + 1
            elif v1[m] > v2[j]:
                e = m - 1
            else:
                ret = True
                break
        
        if ret == True:
            print(1)
        else:
            print(0)
