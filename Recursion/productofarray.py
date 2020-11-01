# Product of Array

def prodarr(arr):
    if len(arr) == 0:
        return 1

    return arr[0]*prodarr(arr[1:])


print(prodarr([1,2,3,4]))