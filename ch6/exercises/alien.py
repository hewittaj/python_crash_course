# # simple dictionary 
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])

# new_points = alien_0['points']
# print(f"You just earned {new_points} points!")

# # to add new key-value pairs looks something like below
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# # how to create an empty dictionary
# alien_0 = {}

# alien_0['color'] = 'green'
# alien_0['points'] = 5

# print(alien_0)

# # modifying values in a dictionary
# alien_0 = {}
# alien_0['color'] = 'green'
# print(f"\nThe alien is {alien_0['color']}")

# alien_0['color'] = 'yellow'
# print(f"\nThe alien is now {alien_0['color']}")

# advanced example tracking position of an alien that moves at different speeds
alien_0 = {'x_position': 25, 'speed': 'medium', 'points': 5}
print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1

elif alien_0['speed'] == 'medium':
    x_increment = 2

else:
    # This must be a fast alien
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

# removing key-value pairs
del alien_0['points']
print(alien_0)