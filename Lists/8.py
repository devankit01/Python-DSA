# List pitfalls

lst = [1, 3, 9, 8, 7, 5]

# print(sorted(lst))  also works

lst.sort()
print(lst)

lst = lst.sort() # return None
print(lst)
