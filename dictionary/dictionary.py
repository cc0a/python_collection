# dictionaries are accessed via key

fruit = {"orange": "a sweet, orange, citrus fruit",
         "lemon": "a sour, yellow, citrus fruit",
         "grape": "a small, sweet fruit, growing in bunches",
         "lime": "a sour, green, citrus fruit",
         "apple": "round and crunchy"}

print(fruit)

# print(fruit["lemon"])  # key is lemon, description of lemon is printed
# fruit["pear"] = "an odd-shaped apple"
# print(fruit)
# fruit["lime"] = "great with tequila"
# print(fruit)
# # del fruit["lemon"]  # deletes lemon
# fruit.clear()  # contents of fruit are now cleared out
# print(fruit)

# while True:  # while loop
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":  # enter quit to exit program
#         break
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("We don't have any " + dict_key)

# for snack in fruit:
#     print(fruit[snack])

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()

# ordered_keys = sorted(list(fruit.keys()))  # same as lines 34 + 35
# for f in ordered_keys:
#     print(f + " - " + fruit[f])

# for f in sorted(fruit.keys()):  # same as 37 - 39, .keys is being used to call in the keys to be sorted
#  print(f + " - " + fruit[f])

# fruit_keys = fruit.keys()  # view object, like a list
# print(fruit_keys)
#
# fruit["tomato"] = "Not nice with ice cream"  # added item to dictionary, only way to update dictionary
# print(fruit_keys)
print(fruit)
print(fruit.items())
f_tuple = tuple(fruit.items())  # tuple created from dictionary
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + "is" + description)

print(dict(f_tuple))

