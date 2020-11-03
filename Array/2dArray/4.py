# accessing


import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(arr)


def access(array, rowIndex, columnIndex):
    if rowIndex >= len(array) and columnIndex >= len(array[0]):
        print('Incorrect Index')
    else:
        print(array[rowIndex][columnIndex])
    
    
access(arr,1,2)