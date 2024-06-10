import sys

count = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split(" ")))
v = int(sys.stdin.readline())
ret = 0
for i in l:
    if i == v:
        ret = ret + 1
        
print(ret)