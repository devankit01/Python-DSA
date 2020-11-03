# insertion

import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(arr)



# np.insert(arrayname, index(row/column, array, at row/column))
# axis = 1 for column and axis = 0 for row
newarr1 = np.insert(arr ,0, [1,1,1,1],axis =1)
newarr2 = np.insert(arr ,0, [8,8,8,8],axis=0)

print(newarr1,newarr2)


'''
Output :

[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]
 [13 14 15 16]]

[[ 1  1  2  3  4]
 [ 1  5  6  7  8]
 [ 1  9 10 11 12]
 [ 1 13 14 15 16]] 

 [[ 8  8  8  8]
 [ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]
 [13 14 15 16]]

 '''



