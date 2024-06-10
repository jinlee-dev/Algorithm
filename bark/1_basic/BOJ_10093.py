import sys
n, m = map(int, sys.stdin.readline().split(' '))
minn = min(n, m)
maxx = max(n, m)
dif = (int)(maxx - minn - 1)
diff = max(0, dif)
print(diff)

for i in range(minn + 1, maxx):
    print(i, end=' ')