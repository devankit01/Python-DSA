# Captialize all in array

def capitalizearr(arr):
    arr1 = []
    if len(arr) == 0:
        return arr1
    arr1.append(arr[0].upper())
    print(arr1)
    return arr1 + capitalizearr(arr[1:])

print(capitalizearr(['hi','hello']))