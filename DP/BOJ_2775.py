import sys

tc = int(input())
answer = []
for _ in range(tc):
    floor = int(input())
    ho = int(input())
    apart = [[col for col in range(ho + 1)] for j in range(floor + 1)]
    for f in range(1,floor + 1):
        for h in range(1,ho + 1):
            count = 0
            for j in range(1,h + 1):
                count = count + apart[f-1][j]
            apart[f][h] = count
    answer.append(apart[floor][ho])

for _ in answer:
    print(_)