''' Linear or Sequential Search '''
# Method 1
searchList = [1,4,6,8,4,3]
find = int(input())
for i in searchList:
    if i == find:
        print('Element catched')
        break
else:
    print('Not Found')
    
 
# Method 2
pos = 0
while pos < len(searchList):
    if searchList[pos] == find:
        print(pos)
    pos +=1
print("-1")
    
