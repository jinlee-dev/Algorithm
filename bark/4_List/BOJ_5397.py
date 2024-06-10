import sys

count = int(sys.stdin.readline())

for i in range(count):
    left = list()
    right = list()
    input = str(sys.stdin.readline()).rstrip()
    for j in input:
        if j == '<':
            if left:
                right.append(left.pop())
        elif j == '>':
            if right:
                left.append(right.pop())
        elif j == '-':
            if left:
                left.pop()
        else:
            left.append(j)
    
    print("".join(left + right[::-1]))
    