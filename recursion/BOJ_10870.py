def Fibonacci(i):
    if i < 2:
        return i
    else:
        return Fibonacci(i - 1) + Fibonacci(i - 2)

x = int(input())
ret = Fibonacci(x)
print(ret)