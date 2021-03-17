# Ranges

# o = range(0, 100, 4)
# print(o)
# p = o [::5]
# print(p)
# for i in o:
#     print(i)

# Tuples

# t = "a", "b", "c"
# print(t)
#
# print ("a", "b", "c")
#
# print (("a", "b", "c"))

# imelda = imelda[0], "Imelda May", imelda[2] # Proper way to append a tuple!!!
# print(imelda)
#
# metallica2 = ["Ride the Lightning", "Metallica", 1984]
# print(metallica2)
# metallica2[0] = "Master of Puppets"
# print(metallica2)
#
# a = b = c = d = 12
# print(c)
#
# a, b = 12, 13
# print(a, b)
#
# a, b = b, a
# print("a is {}".format(a))
# print("b is {}".format(b))

# welcome = "Welcome to My Nightmare", "Alice Cooper", 1975
# bad = "Bad Company", "Bad Company", 1974
# budgie = "Nightflight", "Budgie", 1981
# imelda = "More Mayhem", "Imelda May", 2011, (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")
#
#
# print(imelda)
#
# title, artist, year, track1, track2, track3, track4 = imelda
# print(title)
# print(artist)
# print(year)
# print(track1)
# print(track2)
# print(track3)
# print(track4)

# imelda = "More Mayhem", "Imelda May", 2011, (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
#
# title, artist, year, tracks = imelda
# print(title)
# print(artist)
# print(year)
# for song in tracks:
#     track, title = song
#     print("\tTrack number {}, Title {}".format(track, title))

# Dictionaries

# fruit = {"orange": "a sweet, orange, citrus fruit",
#          "apple": "good for making cider",
#          "lemon": "a sour, yellow citrus fruit",
#          "grape": "a small, sweet fruit growing in bunches",
#          "lime": "a sour, green citrus fruit"}
#
# print(fruit)
# print(fruit["lemon"])

# locations = {0: {"desc": "You are sitting in front of a computer learning Python",
#                  "exits": {},
#                  "namedExits": {}},
#              1: {"desc": "You are standing at the end of a road before a small brick building",
#                  "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
#                  "namedExits": {"2": 2, "3": 3, "5": 5, "4": 4}},
#              2: {"desc": "You are at the top of a hill",
#                  "exits": {"N": 5, "Q": 0},
#                  "namedExits": {"5": 5}},
#              3: {"desc": "You are inside a building, a well house for a small stream",
#                  "exits": {"W": 1, "Q": 0},
#                  "namedExits": {"1": 1}},
#              4: {"desc": "You are in a valley beside a stream",
#                  "exits": {"N": 1, "W": 2, "Q": 0},
#                  "namedExits": {"1": 1, "2": 2}},
#              5: {"desc": "You are in the forest",
#                  "exits": {"W": 2, "S": 1, "Q": 0},
#                  "namedExits": {"2": 2, "1": 1}}
#              }
#
# vocabulary = {"QUIT": "Q",
#               "NORTH": "N",
#               "SOUTH": "S",
#               "EAST": "E",
#               "WEST": "W",
#               "ROAD": "1",
#               "HILL": "2",
#               "BUILDING": "3",
#               "VALLEY": "4",
#               "FOREST": "5"}
#
# loc = 1
# while True:
#     availableExits = ", ".join(locations[loc]["exits"].keys())  # W E N S Q IF 1
#
#     print(locations[loc]["desc"])
#
#     if loc == 0:
#         break
#     else:
#         allExits = locations[loc]["exits"].copy() # note the use of the copy() function
#         allExits.update(locations[loc]["namedExits"]) # note the use of the update() function
#
#     direction = input("Available exits are " + availableExits).upper()
#     print()
#
#     # Parse the user input, using our vocabulary dictionary if necessary
#     if len(direction) > 1:  # more than 1 letter, so check vocab
#         words = direction.split() # note use of split function
#         for word in words:
#             if word in vocabulary:   # does it contain a word we know?
#                 direction = vocabulary[word]
#                 break
#
#     if direction in allExits:
#         loc = allExits[direction]
#     else:
#         print("You cannot go in that direction")

# Sets

# farm_animals = {"sheep", "cow", "hen"}
# print(farm_animals)
#
# for animal in farm_animals:
#     print(animal)
#
# print("=" * 40)
#
# wild_animals = set(("Lion", "Tiger", "Panther", "Elephant", "hare"))
# print(wild_animals)
#
# for animal in wild_animals:
#     print(animal)
#
# farm_animals.add("horse")
# wild_animals.add("horse")
# print(farm_animals)
# print(wild_animals)

empty_set = set()
empty_set_2 = {}
empty_set.add("a")

even = set(range(0, 40, 2))
print(even)
print(len(even))

squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(squares)
print(len(squares))

print("Even minus squares")
print(sorted(even.difference(squares)))
print(sorted(even - squares))

print("squares minus even")
print(squares.difference(even))
print(squares - even)