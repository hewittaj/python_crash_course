# # 8-12
# def make_sandwich(*ingredients):
#     print("\nThis is what you would like on your sandwich:")
#     for ingredient in ingredients:
#         print(f"- {ingredient}")

# make_sandwich('salami', 'turkey', 'tomato', 'sardines')

# # 8-13
# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user."""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info

# user_profile = build_profile('alex', 'hewitt', age = 23, degree = 'computer science')
# print(user_profile)

# 8-14
def make_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car_1 = make_car('subaru', 'impreza', year = 2003, mileage = 23000, color = 'red')
print(car_1)