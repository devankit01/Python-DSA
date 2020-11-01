# Reverse

def rev(n):
    if len(n) <=1:
        return n
    return n[len(n)-1] + rev(n[0:len(n)-1])

print(rev('123'))