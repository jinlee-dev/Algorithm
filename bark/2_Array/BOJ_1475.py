import sys
l = [0] * 10

roomNum = int(sys.stdin.readline())
while roomNum != 0:
    num = roomNum%10
    if num == 9:
        num = 6
    l[num] = l[num] + 1
    roomNum = roomNum //10
    
l[6] = l[6] % 2 + int(l[6] / 2)

max = 0
for i in l:
    if max < i:
        max = i

print(max)