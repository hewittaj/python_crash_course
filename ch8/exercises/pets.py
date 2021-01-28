# using positional arguments, the way you call the function matters
# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name.title()}")

#describe_pet('hamster', 'harry')

# using keyword arguments the function call matters less
# describe_pet(animal_type='hamster', pet_name='harry')
# describe_pet(pet_name = 'harry', animal_type = 'hamster')
# these will be the same because we've called them in a concrete way

# using default values by declaring it in the function arguments
# order matters, our default values have to be at the end and explicitly declared in the function call

def describe_pet(pet_name, animal_type = 'dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet(pet_name='willie')