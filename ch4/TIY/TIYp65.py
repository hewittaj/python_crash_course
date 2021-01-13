#4-10 testing slice functionality
# test_list = ['test', 'hungry', 'food', 'milk', 'apples', 'kristen']

# print(f"\nThe first three items in the list are:")
# for item in test_list[:3]:
#     print(item.title())

# print(f"\nThe items from the middle of the list are:")
# for item in test_list[1:4]:
#     print(item.title())

# print("\nThe last three items in the list are:")
# for item in test_list[-3:]:
#     print(item)

#4-11 testing copied slices
pizzas = ['pepperoni', 'cheese', 'black olive']
friend_pizzas = pizzas[:]

pizzas.insert(2, 'pineapple')
friend_pizzas.append('sausage')

print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(f"{pizza}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)