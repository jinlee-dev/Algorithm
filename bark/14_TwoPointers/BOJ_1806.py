import sys

N, M = map(int, sys.stdin.readline().split(" "))
l = list(map(int, sys.stdin.readline().split(" ")))

st, et, v = 0, 0, 1e9
sum_ = 0
while True:
    if st == N and et == N:
        break
    
    if sum_ >= M:
        if (st == N): continue
        v = min(et-st, v)
        sum_ -= l[st]
        st += 1
        continue

    if sum_ < M:
        if (et == N): 
            st += 1 
            continue
        sum_ += l[et]
        et += 1
        continue

print(0) if 1e9 == v else print(v)
    