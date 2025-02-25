Fruit = input("Enter a fruit: ").casefold()

Fruits_list = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapes": 90,
    "sweet cherries": 100,
}

if Fruit in Fruits_list:
    print("calories:", Fruits_list[Fruit])
else:
    print("Fruit not found")