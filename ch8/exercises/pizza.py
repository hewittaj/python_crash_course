# passing an arbitrary number of arguments

def make_pizza(size, *toppings):
    """Summarize pizza."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

#make_pizza(12, 'pepperoni')
#make_pizza(13, 'mushrooms', 'green peppers', 'extra cheese')

# if you want to mix positional and arbitrary arguments then you need to put the *whatever at the end 
# ex. make_pizza(size, *toppings)