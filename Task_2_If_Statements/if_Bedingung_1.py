import random

random_Int = random.randint(0,100);
print(random_Int)

if random_Int < 20:
    print("Mini")
elif random_Int >= 20 and random_Int <= 50:
    print("Medium");
else:
    print("Large");