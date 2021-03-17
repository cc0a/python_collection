# for i in range (1, 20):
#     print("i is now{}".format(i))
#
# number = "9,122,232,132,434"
# for i in range(0, len(number)):
#     print(number[i])

# number = "9,122,232,132,434"
# cleanedNumber = ''
#                 ''
# for i in range(0, len(number)):
#     if number[i] in '0123456789': #Boolean statement due to the use of in, note that if i corresponds to 0-9, returns true
#         cleanedNumber = cleanedNumber + number[i]#'' creates a string for the number to go into, horizontal rather than vertical
#
#         newNumber = int(cleanedNumber)
#
# newNumber = int(cleanedNumber)
#
# print("The number is {}".format(newNumber))

# for i in range (10):
#     print(i)

number = "9,122,232,132,434"
cleanedNumber = ''

for char in number:
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))

for state in ["not pinin'", "no more", "a stiff", "bereft of life"]: #Iteration example!!!
    print("This parrot is "+ state)

for i in range(0, 100, 5): #Start Stop Step!!
    print("i is {}".format(i))

for i in range(1, 13):
    for j in range(1,3):
        print("{1} times {0} is {2}".format(i, j, i*j))
    print("===============")

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

for i in quote:
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ": # Note that it is CASE-SENSITIVE!
        print(i, end='')

for i in range(0, 100, 7): # Prints all numbers in this range that are divisible by 7
    print(i)