# using get() to access values
alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points']) # this will throw an error!

# using get() will access the dictionary by key and use a default value if none was found

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)