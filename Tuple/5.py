# Tuple Operations

# Concatenate
tuple1 = ('1', '2', '3', '4')
tuple2 = ('5', '6', '7', '8')
print(tuple1 + tuple2)


# * Operator
print(tuple1*2)


# in operator
print("2" in tuple1)  # return boolean


# Count()
tuple3 = ('1', '2', '3', '3', '1', '1')
print(tuple3.count('3'))


# index
print(tuple3.index('2'))

# max
print(max(tuple3))

# min
print(min(tuple3))
