''' Binary  Search '''
''' Note : Only works if arrat is sorted '''

import math
def BinarySearch(array, value):
    start = 0
    end = len(array)-1
    middle = math.floor((start+end)/2)
    # print(start,end,middle)
    while not array[middle] == value:
        if value < array[middle] :
            end = middle-1
        else:
            start = middle+1
        
        middle = math.floor((start+end)/2)
    return middle



array = [1,6,4,8,11,16,20,20,36]
print(BinarySearch(array,1))


