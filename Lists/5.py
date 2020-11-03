# Search

shop = ['bread','egg','butter','sauce','fish']
print(shop)

class Search:
    def MethodOne(list,item):
        if item in list:
            print('Element is found')
        else:
            print('Element is not Found')


    def MethodTwo(list,item):
        for i in list:
            if i == item:
                print('Element is found')
            else:
                print('Element is not Found')


Search.MethodOne(shop,'egg')
# Search.MethodTwo(shop,'bread')
