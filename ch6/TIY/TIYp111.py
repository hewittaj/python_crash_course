#6-7
person_0 = {
    'first_name': 'kristen',
    'last_name': 'hewitt',
    'age': 23,
}

person_1 = {
    'first_name': 'keaton',
    'last_name': 'hewitt',
    'age':20,
}

people = [person_0, person_1]

for person in people:
    print(f"User Info:")
    for key, value in person.items():
        print(f"\t{key}: {value}")
    print("\n")

# skipped the rest of the exercises as they are somewhat repetitive, and I've gone through this book like 3 times already...