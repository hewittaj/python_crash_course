# looping through all key-value pairs
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

#looping through all the keys in a dictionary, technically default when looping through a dictionary
for key in user_0.keys():
    print(key)

    