# Captialize array

def capitalizearr(arr):
    arr1 = []
    if len(arr) == 0:
        return arr1
    arr1.append(arr[0][0].upper() + arr[0][1:])
    print(arr1)
    return arr1 + capitalizearr(arr[1:])

print(capitalizearr(['hi','hello']))