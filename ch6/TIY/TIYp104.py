#6-4 ignoring because I skipped over exercise 6-3 which this is dependent on

#6-5
# rivers = {
#     'nile': 'egypt',
#     'mississippi': 'usa',
#     'euphrates': 'africa'
# }

# for river, country in rivers.items():
#     print(f"The {river.title()} runs through {country.title()}")

#6-6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

users_to_poll = ['alex', 'sarah', 'phil', 'adam']

for name in users_to_poll:
    if name in favorite_languages:
        print(f"Thank you for taking the survery {name.title()}")
    
    else:
        print(f"{name.title()}, would you like to take our survey?")