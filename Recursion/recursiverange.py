# Add from 0 to n

def recursive(n):
    if n == 0:
        return 0
    return n + recursive(n-1)


print(recursive(6))