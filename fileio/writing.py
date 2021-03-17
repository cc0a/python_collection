# cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]
#
# with open("cities.txt", 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file)  # there's no space after the = sign because it is NOT var assignment

# Double-Checking output Below

# cities = []
#
# with open("cities.txt", 'r') as city_file:
#     for city in city_file:
#         cities.append(city.strip('\n'))
#
# print(cities)
# for city in cities:
#     print(city)

# Any text can be recorded in a file as plain text, but output will vary:

# imelda = "More Mayhem", "Imelda May", 2011, ((1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"))
#
# with open("imelda3.txt", 'w') as imelda_file:
#     print(imelda, file=imelda_file)

# Convert file BACK into readable code with eval()

with open("imelda3.txt", 'r') as imelda_file:
    contents = imelda_file.readline() # reads a single line from the file, \n left at the end of a string

imelda = eval(contents)  # runs python code within a plain text file

print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)




