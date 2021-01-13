# squares = []
# for value in range(1, 11):
#     square = value ** 2
#     squares.append(square)

# print(squares)

# we can create a list using list comprehensions which is a bit more condensed, though sometimes more convoluted
squares = [value ** 2 for value in range(1, 11)]
print(squares)