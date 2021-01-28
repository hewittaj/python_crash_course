# creatinga and using a class
class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attreibutes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

'''
- Capitalized names generally refer to classes in Python.
- The __init__() method.
    - A function that's part of a class is a method.
    - A special method that Python runs automatically whenever we create a new instance based on the Dog class.
'''
# making an instance from a class
my_dog = Dog('willie', 6)
print(f"My dog's name is {my_dog.name}")
print(f"My dog's age is {my_dog.age}")

my_dog.sit()
my_dog.roll_over()