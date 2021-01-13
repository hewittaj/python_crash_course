# working with tuples in this exercise
dimensions = (200,50) # parentheses dictate that this is a tuple

# print(dimensions[0])
# print(dimensions[1])

#try to change tuple will result in an error
# dimensions[0] = 251

# loop through a tuple
# for dimension in dimensions:
#     print(dimension)

# how to modify a tuple then? by assigning a new value to a variable that represents a tuple
# this is valid because reassigning a variable is acceptable!
print("Original dimensions: ")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)