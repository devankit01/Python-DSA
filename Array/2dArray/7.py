# Deleting row and column


import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(arr)


newarr = np.delete(arr, 0, axis = 0)
print(newarr)

'''
Output :

[[ 5,  6,  7,  8],
[ 9, 10, 11, 12],
[13, 14, 15, 16]]

'''