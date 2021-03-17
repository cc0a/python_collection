# create a program that returns a list of all the characters in the text that are not vowels,
# sorted in alphabetical order


phrase = "i'm going to kc after i get this money"

vowels = frozenset("aeiou")  # creates immutable set containing aeiou
finalSet = set(phrase).difference(vowels)  # changing string var to a set, pulling vowels with .difference + vowels frozenset
print(finalSet)

finalList = sorted(finalSet)  # piping in sorted version of finalSet into new var: finalList
print(finalList)