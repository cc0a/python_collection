def python_food():  # Defining the function/parameters
    width = 80
    text = "Spam and Eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)

def center_text(*args, sep=' '):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text


with open("menu", 'w') as menu:  # creates a file titled centered that contains text
    s1 = center_text("spam and eggs")
    print(s1, file=menu)
    s2 = center_text("spam, spam and eggs")
    print(s2, file=menu)
    print(center_text(12), file=menu)
    print(center_text("spam, spam, spam and spam"), file=menu)
    s5 = center_text("first", "second", 3, 4, "spam", sep=":")
    print(s5, file=menu)






