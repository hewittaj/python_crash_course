# using slices to print subsects of a list, end number is exclusive
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# # if you omit the first index, python automatically starts slice at beginning of the list
# print(players[:4])

# # this also works the other way around
# print(players[2:])

# # or with negative numbers, this prints the last three names of the players
# print(players[-3:])

print("\nHere are the first three players on my team:")
for player in players[:3]:
    print(player.title())