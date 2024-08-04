import sys
x, y, z = map(int, sys.stdin.readline().split(" "))

def Z(n, r, c):
    if n == 0: 
        return 0
    else:
        half = 1 << (n - 1)
        if r < half:
            if c < half: return Z(n - 1, r, c)
            else: return (half * half) + Z(n - 1, r, c - half)
        else:
            if c < half: return (2 * half * half) + Z(n - 1, r - half, c)
            else: return (half * half * 3) + Z(n - 1, r - half, c - half)

print(Z(x, y, z))