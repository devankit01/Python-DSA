# Extend array extend()

from array import *
arr1 = array('i',[1,2,3,4,5])
arr2 = array('i',[6,7,8,9,10])

arr1.extend(arr2)
print(arr1)