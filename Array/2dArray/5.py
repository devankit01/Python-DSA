# Traversal


import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(arr)


def traverse(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

    
traverse(arr)