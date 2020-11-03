# append

import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(arr)



# np.append(arrayname, 2darray, at row/column))
# axis = 1 for column and axis = 0 for row
newarr1 = np.append(arr, [[1,1,1,1]],axis =0)


print(newarr1)
'''
Output :

[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]
 [13 14 15 16]]

[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]
 [13 14 15 16]
 [ 1  1  1  1]]

 '''