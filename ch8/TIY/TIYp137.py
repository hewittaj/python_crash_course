#8-3
# def make_shirt(size, text):
#     print(f"The size of the shirt is {size} and it will say '{text}'.")

# make_shirt('medium', 'hello there!')
# make_shirt(text = "I'm happy to see you!", size = 'small')
#8-4
# def make_shirt(text = 'I love Python', size = 'large'):
#     print(f"The size of the shirt is {size} and it will say '{text}'.")

# make_shirt()
# make_shirt(size='medium')
# make_shirt(size = 'extra large', text='i do not know what to say...')

#8-5

def describe_city(city, country = 'USA'):
    print(f"{city.title()} is in {country.title()}.")

describe_city('des moines')
describe_city('urbandale')
describe_city(country='france', city='paris')