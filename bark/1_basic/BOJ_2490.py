import sys
t = []
for i in range(3):
    t.append(list(map(int, input().split())))

play = ['E','A', 'B', 'C', 'D']
for i in t:
    f = 0
    for y in i:
        if y == 0:
            f = f + 1
    print(play[f])
