#3-4
# invited = ['michael scott', 'professor layton', 'jim halpert']
# for name in invited:
#     print(f"{name.title()}, you are invited to my party!")

#3-5
# invited = ['michael scott', 'professor layton', 'jim halpert']
# for name in invited:
#     print(f"{name.title()}, you are invited to my party!")
# print(f"Unfortunately {invited[1]} can't make it.")

# invited[1] = 'toby macguire'
# print("\n")

# for name in invited:
#     print(f"{name.title()}, you are invited to my party!")

#3-6
# invited = ['michael scott', 'professor layton', 'jim halpert']
# for name in invited:
#     print(f"{name.title()}, you are invited to my party!")

# print("I've found a bigger table so more people are invited now!\n")

# invited.insert(0,'mom')
# invited.insert(2, 'dad')
# invited.append('keaton')

# for name in invited:
#     print(f"{name.title()}, you are invited to my party!")

#3-7
invited = ['michael scott', 'professor layton', 'jim halpert']
for name in invited:
    print(f"{name.title()}, you are invited to my party!")

print("I've found a bigger table so more people are invited now!\n")

invited.insert(0,'mom')
invited.insert(2, 'dad')
invited.append('keaton')

for name in invited:
    print(f"{name.title()}, you are invited to my party!")

print("Nevermind, I can only invite two people now...\n")

for name in range(len(invited) - 2):
    invited.pop(-1)

for name in invited:
    print(f"You are still invited, {name.title()}")

del(invited[0])
del(invited[0])
print(invited)