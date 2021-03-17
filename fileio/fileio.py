# jabber = open("/users/root1/desktop/sample.txt", 'r')
# #
# # for line in jabber:
# #     if "jabberwock" in line.lower():
# #         print(line, end='') # using end='' prevents print from printing another new line character
# #
# # jabber.close() # MAKE SURE TO CLOSE THE FILE! OTHERWISE IT MAY BECOME CORRUPTED!

# with open("/users/root1/desktop/sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

# with open("/users/root1/desktop/sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

# with open("/users/root1/desktop/sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines:
#     print(line, end='')

with open("/users/root1/desktop/sample.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines[::-1]:
    print(line, end='')