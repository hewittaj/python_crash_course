#7-8 & 7-9
# Create our orders list
sandwich_orders = ['ham', 'bologna','pastrami', 'cheese', 'blt', 'pastrami', 'turkey', 'pastrami']
finished_sandwiches = []

# Deli is out of pastrami, so we will remove all pastrami orders.
print("\nThe deli is out of pastrami sandwiches.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Loop through the orders and make them
for sandwich in sandwich_orders:
    print(f"I finished your {sandwich} sandwich. \n")
    finished_sandwiches.append(sandwich)


print(finished_sandwiches)


#7-10 Polling users about dream vacations

# Set a flag so we can break when flag is False
flag = True

# Dictionary to store users name and dream vacation location
dream_vacations = {}

while flag:
    name = input("\nWhat is your name? ")
    destination = input("Where is your dream vacation location? ")

    dream_vacations[name] = destination

    poll_again = input("Would you like to poll another person? (yes/no)")
    if poll_again == 'no':
        flag = False

print("- - - Results - - -")
for name, location in dream_vacations.items():
    print(f"{name.title()} would go to {location}.")