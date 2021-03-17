import shelve

with shelve.open('ShelfTest') as fruit:
    fruit['Orange'] = "A sweet, orange, citrus fruit."
    fruit['Apple'] = "Good for making cider."
    fruit['Lemon'] = "A sour, yellow citrus fruit."
    fruit['Grape'] = "A small, sweet fruit that grows in bunches."
    fruit['Lime'] = "A sour, green citrus fruit."

    print(fruit['Orange'])
    print(fruit['Grape'])