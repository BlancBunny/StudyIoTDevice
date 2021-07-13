m = 0
n = 1

def func():
    global m
    m = m + 1
    global n
    n = n + 1

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))


