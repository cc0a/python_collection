locations = {0: "You are sitting in front of a computer learning Python",  # VALUES
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}  # End dictionary

exits = { 0:  {"Q": 0},  # Exits available for each location, each of these items corresponds to the items above in position
          1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},  # west takes you to the hill, east building, south valley, north forest
          2: {"N": 5, "Q": 0},
          3: {"W": 1, "Q": 0},  # KEYS
          4: {"N": 1, "W": 2, "Q": 0},
          5: {"W": 2, "S": 1, "Q": 0} }  # End dictionary utilizing list

vocabulary = {"QUIT":  "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST":  "E",
              "WEST":  "W"}

loc = 1  # Determines starting point of game
while True:  # While loop is run until quit is utilized to exit
    availableExits = ", ".join(exits[loc].keys())  # retrieving the dictionary from locations

    # below is less efficient
    # availableExits = ""  # Creates string for available exits to be populated in
    # for direction in exits[loc].keys():  #
    #     availableExits += direction + ", "

    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are " + availableExits + " ").upper()  # .upper allows players to type upper/lower case without consequence, players are allowed to choose from available exits only
    print()
    # parse the user input, using our vocabulary dictionary if necessary
    if len(direction) > 1:  # more than 1 letter, so check vocab
        for word in vocabulary:  # does it contain a word we know?
            if word in direction:
                direction = vocabulary[word]

    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")

