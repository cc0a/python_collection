fruit = {"orange": "a sweet, orange, citrus fruit",
         "lemon": "a sour, yellow, citrus fruit",
         "grape": "a small, sweet fruit, growing in bunches",
         "lime": "a sour, green, citrus fruit",
         "apple": "round and crunchy"}

print(fruit)

veg = {"cabbage": "Every child's favorite",
       "Sprouts": "Mmmm, lovely",
       "Spinach": "Can I have some more fruit please?"}

print(veg)

# veg.update(fruit)  # combines fruit and veggies
# print(veg)

nice_and_nasty = fruit.copy()  # calling in fruit
nice_and_nasty.update(veg)  # calling in veg
print(nice_and_nasty)
print(veg)
print(fruit)
