# Recursive Program

# Factorial
def Factorial(n):
    assert n>=0 and int(n) == n , "The number should be Positive and Integer"
    if n<=0:
        return 1
    return n*Factorial(n-1)

print(Factorial(10))