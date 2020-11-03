# Array to string

from array import *
arr1 = array('i',[1,2,1,3,4,5,6,6,7,8,9,8,9,0,8])

strTemp = arr1.tostring()
print(arr1 , strTemp)
ints = array('i')
ints.fromstring(strTemp)
print(ints)