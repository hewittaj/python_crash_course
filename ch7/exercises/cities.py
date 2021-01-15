# using break to exit a loop

prompt = "\nPlease enter the name of a city you've visited: "
prompt += "\n(Enter 'quit' when you're finished.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}")