''' Linear or Sequential Search '''

searchList = [1,4,6,8,4,3]
find = int(input())
for i in searchList:
    if i == find:
        print('Element catched')
        break
else:
    print('Not Found')