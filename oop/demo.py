a_string = "This is\na string\t\t and tabbed."
print(a_string)

raw_string = r"This is\na string\t\t and tabbed."  # using r at the beginning of the string disabled escapes
print(raw_string)

b_string = "This is" + chr(10) + "a string split" + chr(9) + chr(9) + "and tabbed"
print(b_string)

r"""" chr(10) and chr(9) are the characters from ASCII for \n and \t respectively """

backslash_string = "This is a backslash \followed by some text."
print(backslash_string)

backslash_string = "This is a backslash \\followed by some text."
print(backslash_string)

error_string = r"This string ends with \\"  # When ending a string with a backslash, you MUST use TWO







