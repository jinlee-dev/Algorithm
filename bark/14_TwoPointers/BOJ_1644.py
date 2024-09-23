import sys

num = int(sys.stdin.readline())
eratos = [True for _ in range(num + 1)]

eratos[1] = False
l = []
for i in range(2, num + 1):
    d = i * i
    if d >= (num + 1):
        break

    for j in range(d, num + 1, i):
        eratos[j] = False

for i in range(2, num + 1):
    if eratos[i] == True:
        l.append(i)

ssCnt = len(l)
e = 0
ret = 0
answer = 0
for s in range(ssCnt):
    while e < ssCnt and ret < num:
        ret += l[e]
        e = e + 1
    
    if ret == num:
        answer += 1
    
    ret -= l[s]

print(answer)
