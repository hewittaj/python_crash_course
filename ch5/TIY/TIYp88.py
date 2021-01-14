#5-8 & 5-9 looping through a list and checking if name is a certain one we specify
# usernames = ['jake', 'admin', 'test','bob', 'sally']
# print("\n")
# if len(usernames) == 0:
#     print("We need to find some users.")
# for name in usernames:
#     if(name == 'admin'):
#         print("Hello admin, would you like to see a status report?")
#     else:
#         print(f"Hello {name}, thank you for logging in again")



#5-10
# current_users = ['test', 'alex', 'jacob', 'will', 'adam']
# new_users = ['Jacob', 'adaM', 'bill', 'bob', 'chris']

# lowercase_all_users = current_users[:]
# for user in new_users:
#     if user.lower() in lowercase_all_users:
#         print("Select a new username please.")
#     else:
#         print("Username is available.")

#5-11
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in numbers:
    if num != 1 and num != 2 and num != 3:
        print(f"{num}th")
    elif num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")