import sys

count = int(sys.stdin.readline())
ret = []
for i in range(count):
    s, f = map(str, sys.stdin.readline().split(" "))
    f = f.replace("\n", "")
    ls = list(s)
    lf = list(f)

    ls.sort()
    lf.sort()
    if str(ls) == str(lf):
        ret.append("Possible")
    else:
        ret.append("Impossible")

for i in ret:
    print(i)