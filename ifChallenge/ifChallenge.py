print("To qualify for this holiday, you must be over 18 and under 31.")
name = input("Please enter your name.")
age = int(input("How old are you, {0}?".format(name)))

if age >=18 and age <=31:
    print("Welcome to your Holiday.")
else:
    print("No holiday for you.")
