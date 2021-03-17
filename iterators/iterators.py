string = "1234567890"

# for char in string:
#     print(char)

# Example of how a for loop works below:

# my_iterator = iter(string)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

# for char in string:
#     print(char)
#
# for char in iter(string):
#     print(char)

####################################################

colors = ["blue", "green", "red", "yellow", "orange"]

my_iterator = iter(colors)

for i in range(0, len(colors)):
    next_item = next(my_iterator)
    print(next_item)