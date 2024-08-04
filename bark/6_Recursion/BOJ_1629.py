import sys

a, b, c = map(int, sys.stdin.readline().split(" "))

def MOD(x, y, m):
    if y == 1:
        return x % m
    else:
        # 나머지 연산값을 리턴한다
        v = MOD(x, y//2, m)
        # 나머지 연산을 나눌 때 값이 짝수라면 
        if y%2 == 0:
            # 나머지 분배법칙의 결과대로 mod 결과를 곱해준 다음 다시 또 mod를 해준다
            return v * v % m
        else:
            # 홀수면 x 한번 더 곱해준다
            return v * v * x % m

r = MOD(a, b, c)
print(r)