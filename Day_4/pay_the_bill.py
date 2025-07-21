import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Option 1
# random_num = random.randint(1, 5)
# print(friends[random_num - 1])
# print(random_num)

# Option 2
# random_num = random.randint(0, 4)
# print(friends[random_num])


# Option 3
random_int = random.choice(friends)
print(random_int)