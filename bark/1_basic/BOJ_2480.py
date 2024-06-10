import sys
s = list(map(int, input().split()))
b = [0] * 7
for i in s:
    b[i] = b[i] + 1

money = 0
for i in range(6, 0, - 1):
    if b[i] != 0:
        if b[i] == 3:
            money = max(10000 + (i * 1000), money)
        elif b[i] == 2:
            money = max(1000 + (i * 100), money)
        else:
            money = max(money, (i * 100))

print(money)