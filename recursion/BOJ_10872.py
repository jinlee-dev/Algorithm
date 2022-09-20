def Factorial(i):
    if i <= 1:
        return 1
    else:
        return i * Factorial(i - 1)

x = int(input())
ret = Factorial(x)
print(ret)