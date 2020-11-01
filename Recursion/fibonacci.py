# Fibonacci

def Fibonacci(n):
    if n in [0,1]:
        return n
    return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(7))