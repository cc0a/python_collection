import shelve

locations = shelve.open('locations')
vocabulary = shelve.open('vocabulary')

loc = '1'
while True:
    availableExits = ", ".join(locations[loc]["exits"].keys())

    print(locations[loc]["desc"])

    if loc == 0:
        break
    else:
        allExits = locations[loc]["exits"].copy()
        allExits.update(locations[loc]["namedExits"])

    direction = input("Available exits are " + availableExits).upper()
    print()

    # Parse the user input, using our vocabular dictionary if necessary
    if len(direction) > 1:  # More than one letter, so check vocab
        words = direction.split()
        for word in words:
            if word in vocabulary:  # Does it contain a known word?
                direction = vocabulary[word]
                break

    if direction in allExits:
        loc = allExits[direction]
    else:
        print("You cannot go there...")

locations.close()
vocabulary.close()

