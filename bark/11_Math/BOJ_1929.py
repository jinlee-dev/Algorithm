import sys

f, t = map(int, sys.stdin.readline().split(" "))

eratos = [True for _ in range(t + 1)]

eratos[1] = False
for i in range(2, t + 1):
    d = i * i
    if d >= (t + 1):
        break

    for j in range(d, t + 1, i):
        eratos[j] = False

for i in range(f, t + 1):
    if eratos[i] == True:
        print(i)