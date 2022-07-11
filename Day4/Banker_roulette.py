import random


import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
print(names)
choice = random.randint(0, len(names)-1)
person = names[choice]
print(f"{random.choice(names)} is gonna make the reservation for us !")
print(f"{person} is gonna buy the dinner today!")
