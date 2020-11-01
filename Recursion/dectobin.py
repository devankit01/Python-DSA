# Decimal To Binary

def DecimalToBinary(n):
    if n == 0:
        return 0
    return n%2 + 10*(DecimalToBinary(int(n/2)))


print(DecimalToBinary(13))