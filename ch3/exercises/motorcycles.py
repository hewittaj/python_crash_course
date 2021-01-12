motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# # Modify at a specified index 
# motorcycles[0] = 'ducati'
# print(motorcycles)


# # Append to the list
# motorcycles.append('honda')
# print(motorcycles)

# # Insert a new value at a specified location, doesn't overwrite what is at index 0
# motorcycles.insert(0, 'test insert')
# print(motorcycles)

# # Delete a specific value
# del(motorcycles[0])
# print(motorcycles)

# # Using the .pop() method
# print(motorcycles)
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)

# # Popping from any index
# first_owned = motorcycles.pop(0)
# print(f"The first motorcycle I owned was a {first_owned}")

# # Removing a value based off of knowing the value
# motorcycles.remove('honda')
# print(motorcycles)

# Removing and printing a reason
too_expensive = 'suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"A {too_expensive.title()} is too expensive for me.")
