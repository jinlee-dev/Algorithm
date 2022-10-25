global dpCount
def fibonacci(count, f):
    global dpCount
    dpCount = 0
    f[1] = 1
    f[2] = 1
    for i in range(3, (count + 1)):
        f[i] = f[i - 1] + f[i - 2]
        dpCount = dpCount + 1

global rCount
rCount = 0
def fibonacciR(count):
    global rCount
    if count == 1 or count == 2:
        rCount = rCount + 1
        return 1
    else:
        return fibonacciR(count - 1) + fibonacciR(count - 2)

number = int(input())
f = [0] * (number + 1)
fibonacci(number, f)
fibonacciR(number)

print(rCount, dpCount)
