# Greatest Common Factor

def gcd(a,b):
    if b == 0:
        return a
    print(b,a%b)
    return gcd(b,a%b)


print(gcd(40,16))