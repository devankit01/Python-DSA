# Sum of Digit

def Sum(n):
    if n<=0:
        return 0
    else:
        return int(n%10) + Sum(int(n/10))

print(Sum(637))