#4-3
# # print from 1 to 20 the end=' ' tells Python to print each number followed by a space rather than a newline
# for num in range (1,21):
#     print(num, end=' ')

# print("\n")


#4-4
# # print from 1 to 1,000,000
# numbers = list(range(1,1000001))

# for number in numbers:
#     print(number)

#4-5
# numbers = list(range(1,1000001))
# print(f"Min: {min(numbers)}")
# print(f"Max: {max(numbers)}")
# print(sum(numbers))

#4-6
# # prints all the odd numbers from 1 to 20
# odds = []
# for num in range(1,21,2):
#     odds.append(num)
# print(odds)

#4-7
# # prints numbers from 3 to 30 using a list comprehension and for loops
# threes = [num for num in range(3,31,3)]
# for num in threes:
#     print(num)

#4-8 and 4-9
# prints the cubed numbers from 1 to 10
cubes = [num ** 3 for num in range(1,11)]
for num in cubes:
    print(num)


#4-9
