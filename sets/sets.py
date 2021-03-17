# farm_animals = {"sheep", "cow", "hen"}
# print(farm_animals)
#
# for animal in farm_animals:
#     print(animal)
#
# print("-" * 48)
#
# wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
# print(wild_animals)
#
# for animal in wild_animals:
#     print(animal)
#
# farm_animals.add("horse")
# wild_animals.add("horse")
# print(farm_animals)
# print(wild_animals)

# empty_set = set()
# empty_set_2 = {}
# empty_set.add("a")
# # empty_set_2.add("a")  # generates an error because the set() method was not utilized, dicts are immutable!
#
# even = set(range(0, 40, 2))
# print(even)
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)


# even = set(range(0, 40, 2))
# print(even)
# print(len(even))
#
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)
# print(len(squares))
#
# print(even.union(squares))
# print(len(even.union(squares)))
#
# print(squares.union(even))
#
# print("-" * 48)
#
# print(even.intersection(squares))
# print(even & squares)
# print(squares.intersection(even))
# print(squares & even)

# even = set(range(0, 40, 2))
# print(sorted(even))
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(sorted(squares))
#
# print("even more squares")
# print(sorted(even.difference(squares)))
# print(sorted(even - squares))
#
# print("squares minus even")
# print(squares.difference(even))
# print(squares - even)
#
# print("-" * 48)
# print(sorted(even))
# even.difference_update(squares)
# print(sorted(even))

# even = set(range(0, 40, 2))
# print(sorted(even))
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(sorted(squares))
#
# # print("symmetric even minus squares")
# # print(sorted(even.symmetric_difference(squares)))
# #
# # print("symmetric squares minus even")
# # print(sorted(squares.symmetric_difference(even)))
#
# squares.discard(4)
# squares.remove(16)  # works because item is in the set
# squares.discard(8)  # no error, does nothing
# print(squares)
# # squares.remove(8)  # item must be in set, will not work
# try:  # attempt the following operation
#     squares.remove(8)
# except KeyError:  # if error occurs, execute the following:
#     print("The item 8 is not a member of the set.")

# even = set(range(0, 40, 2))
# print(sorted(even))
# squares_tuple = (4, 6, 16)
# squares = set(squares_tuple)
# print(sorted(squares))
#
# if(squares.issubset(even)):  # subset means that squares is contained within even
#     print("squares is a subset of even")
#
# if even.issuperset(squares):  # superset means that all of even contains of all the items in squares
#     print("even is a superset of squares")

even = frozenset(range(0, 100, 2))  # immutable set

print(even)
even.add(3)





