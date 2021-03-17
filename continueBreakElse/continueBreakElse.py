# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
#     if item == 'spam':
#         continue                        # Skipped over spam!
#         # break ends loop at spam, and removes spam and everything after spam.
#
#     print("Buy " + item)

# meal = ["egg", "bacon", "spam", "sausages"]
# nastyFoodItem = ''
#
# for item in meal:
#     if item == 'spam':
#         nasty_food_item = item
#         break
#
# if nastyFoodItem:
#     print("Can't I have anything without spam in it")
#
# else:
#     print("I'll have a plate of that then please")

#Exercise 1

for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break
#Exercise 2

for x in range(20):
    if x % 3 == 0 or x % 5 == 0:
        continue
    print(x)


