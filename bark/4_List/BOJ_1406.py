import sys

left = list(str(sys.stdin.readline().rstrip()))
count = int(sys.stdin.readline())
right = list()

for i in range(count):
    s = str(sys.stdin.readline().rstrip())

    if len(s) > 2:
        lstr = s.split(" ")
        ip = lstr[1]
        s = lstr[0]
    else:
        ip = ""
    if s == 'L':
        if len(left) != 0:
            right.append(left.pop())
    elif s == 'D':
        if len(right) != 0:
            left.append(right.pop())
    elif s == 'B':
        if len(left) != 0:
            left.pop()
    elif s == 'P':
        left.append(ip)

print("".join(left+right[::-1]))