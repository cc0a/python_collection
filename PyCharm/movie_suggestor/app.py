import random


def movie_choice_output():

    for choice in movie_choice:

        if choice == '0':
            break
        else:
            if choice == '1':
                print(random.choice(Selections))
                new_movie = input("Press enter to see another choice.")
            if choice == '2':
                print(random.choice(Selections))
            if choice == '3':
                print(random.choice(Selections))
            if choice == '4':
                print(random.choice(Selections))
            if choice == '5':
                print(random.choice(Selections))
            if choice == '6':
                print(random.choice(Selections))
            if choice == '7':
                print(random.choice(Selections))
            if choice == '8':
                print(random.choice(Selections))
            if choice == '9':
                print(random.choice(Selections))
            if choice == '10':
                print(random.choice(Selections))


movies = ['1. A Nightmare on Elm Street',
          '2. Friday the 13th',
          '3. The Thing',
          '4. The Shining',
          '5. The Void',
          '6. Event Horizon',
          '7. Alien',
          '8. Gremlins',
          '9. Ghostbusers',
          '10. Hellraiser \n']

Selections = ["FIlm 1", "Film 2", "Film 3", "Film 4", "Film 5"]

for movie in movies:
    print(movie)

movie_choice = input("Please choose from the preceding list (by number) and some suggestions will be made available: ")

movie_choice_output()





# complaint = input("Call me a bitch if you dare!")
#
# if complaint == "bitch":
#     print("Fuck you, too.")










































suggestions_1 = ['Insidious',
                 'Nightmare Documentary',
                 'Scream',
                 'The Cell',
                 '28 Days Later']

suggestions_2 = ['Splinter',
                 'Cabin in the Woods',
                 'The Ritual',
                 'Halloween',
                 'Black Christmas']

suggestions_3 = ['']

suggestions_4 = ['Splinter',
                 'Cabin in the Woods',
                 'The Ritual',
                 'Halloween',
                 'Black Christmas']

suggestions_5 = ['Splinter',
                 'Cabin in the Woods',
                 'The Ritual',
                 'Halloween',
                 'Black Christmas']

suggestions_6 = ['Splinter',
                 'Cabin in the Woods',
                 'The Ritual',
                 'Halloween',
                 'Black Christmas']

suggestions_7 = ['Splinter',
                 'Cabin in the Woods',
                 'The Ritual',
                 'Halloween',
                 'Black Christmas']

suggestions_8 = ['Splinter',
                 'Cabin in the Woods',
                 'The Ritual',
                 'Halloween',
                 'Black Christmas']

suggestions_9 = ['Splinter',
                 'Cabin in the Woods',
                 'The Ritual',
                 'Halloween',
                 'Black Christmas']

suggestions_10 = ['Splinter',
                 'Cabin in the Woods',
                 'The Ritual',
                 'Halloween',
                 'Black Christmas']




