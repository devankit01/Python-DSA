# Accessing and traverse

shop = ['bread','egg','butter','sauce']
print(shop[1])

# 'in' operator
print('bread' in shop)  # return boolean

# reverse Indexing
print(shop[-1])

#traverse
for item in shop:
    print(item)

# traverse and update   
for item in range(len(shop)):
    shop[item] = '👉' + shop[item]
    print(shop[item])