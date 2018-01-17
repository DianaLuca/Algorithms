# map function: applies a function to all items in the input list
squares = list(map(lambda x: x**2, range(10)))
print(squares)

squares2 = [x**2 for x in range(10)]
print(squares2)


