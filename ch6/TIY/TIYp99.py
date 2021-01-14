#6-1
# person = {
#     'first_name': 'kristen',
#     'last_name': 'hewitt',
#     'age': 23,
# }

# for info in person:
#     print(person.get(info))

#6-2
fav_nums = {
    'kristen': 9,
    'will':8, 
    'jacob': 7,
    'adam': 6
}

for person in fav_nums:
    print(f"{person.title()}'s favorite number is: {fav_nums[person]}.")
