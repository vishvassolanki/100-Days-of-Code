import random 
# import my_module

# random_integer = random.randint(1, 10)
# print(random_integer)

# print(my_module.favourite_number)

# random_number = random.random()  From 0 to 1
# random_number = random.random() * 10  From 0 to 10 not inclusive
# random_number = random.random() * 10 + 1 # From 1 to 10
# print(random_number)

# random_float = random.uniform(1, 10)
# print(random_float)

random_number = random.randint(0,1)

if (random_number == 0):
    print("Heads")
else:
    print("Tails")