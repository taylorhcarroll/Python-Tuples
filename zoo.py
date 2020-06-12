zoo = ("red panda", "cod", "salmon", "pufferfish", "cow",
       "pig", "sheep", "parrot", "rabbit", "spider")

pigIndex = zoo.index("pig")

animal_to_find = "spider"
if animal_to_find in zoo:
    print(f"{animal_to_find} was found!")

(first_animal, second_animal, third_animal, fourth_animal, fifth_animal,
 sixth_animal, seventh_animal, eight_animal, ninth_animal, tenth_animal) = zoo
print(first_animal)
print(second_animal)
print(third_animal)
print(fourth_animal)
print(fifth_animal)
print(sixth_animal)
print(seventh_animal)
print(eight_animal)
print(ninth_animal)
print(tenth_animal)

zooList = list(zoo)
zooList.extend(["turtle", "armadillo", "donkey"])
print("List of Animals", zooList)

zooTuple = tuple(zooList)
print("tuple returned check out what's been added", zooTuple)
