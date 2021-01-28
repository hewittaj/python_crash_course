# #9-1
# class Restaurant:

#     """This class represents a basic restaurant."""

#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         """Describes the restaurant name and cuisine type."""
#         print(f"\nThe restaurant '{self.restaurant_name}' serves {self.cuisine_type}-style food.")

#     def open_restaurant(self):
#         print(f"{self.restaurant_name} is open and ready to serve!")

# restaurant_1 = Restaurant('alex\'s place', 'american')

# restaurant_1.describe_restaurant()
# restaurant_1.open_restaurant()

# 9-2
class User:
    
    """This class represents a simple user profile."""

    def __init__(self, first_name, last_name, *other_info):
        self.first_name = first_name
        self.last_name = last_name
        self.other_info = other_info

    def describe_user(self):
        """Describes the current user."""
        print(f"\nHere is a summary of this person's info:")
        print(f"{self.first_name} {self.last_name}")
        for info in self.other_info:
            print(info)

    def greet_user(self):
        """Greets the user."""
        print(f"Hello, {self.first_name} {self.last_name}!")

user_1 = User('alex', 'hewitt', 'age 23', 'height of 5\'10"')
user_1.describe_user()
user_1.greet_user()