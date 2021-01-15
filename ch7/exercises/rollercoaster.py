# using int() to accept numerical input
'''
When you use the input() function Python interperets everything the user enters as a string. 
When you need to cast from a string to an integer you can use int()
'''
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")

else:
    print("\nYou'll be able to ride when you're a little older.")