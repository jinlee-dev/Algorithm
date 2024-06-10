import sys

v = int(sys.stdin.readline())
for i in range(0, v):
    for j in range(0, i):
        print(" ", end="")
    for j in range(i, v):
        print("*", end="")
    print("")
