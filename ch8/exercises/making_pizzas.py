# importing an ENTIRE module - need dot notation ie. pizza.make_pizza(...)
# import pizza


# importing SPECIFIC functions - don't need to use dot notation
# we can use an alias using keyword AS for repeated module names or function names
import pizza as p 
from pizza import make_pizza as mp
p.make_pizza(16, 'pepperoni')
mp(16, 'none')

# import all functions in a module using *    -     from pizza import * 