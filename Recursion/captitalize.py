# Captialize array

def capitalizearr(arr):
    arr1 = []
    if len(arr) == 0:
        return arr[0].upper()
    arr1.append(arr[0].upper())
    return arr1 + capitalize(arr[1:])

print(capitalizearr['hi','hillo'])