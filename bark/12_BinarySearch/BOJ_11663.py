import sys
INPUT = sys.stdin.readline

def bin_search_upper(target, arr):
    s, e = 0, len(arr)
    while s < e:
        m = (s + e) // 2
        if arr[m] <= target:
            s = m+1
        else:
            e = m
    
    return s

def bin_search_lower(target, arr):
    s, e = 0, len(arr)
    while s < e:
        m = (s + e) // 2
        if arr[m] < target:
            s = m+1
        else:
            e = m
    
    return s

N, M = map(int, INPUT().split(" "))
l = list(map(int, INPUT().split(" ")))
l.sort()
for i in range(M):
    st, et = map(int, INPUT().split(" "))
    stIdx = bin_search_lower(st, l)
    etIdx = bin_search_upper(et, l)
    print(etIdx-stIdx)