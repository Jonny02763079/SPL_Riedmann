import random;

random_IntOne = random.randint(0, 100);
random_IntTwo = random.randint(0, 100);

print(random_IntOne, random_IntTwo)

if random_IntOne <= random_IntTwo and random_IntOne <= 50:
    print("Die Zahl 1:" + str(random_IntOne) + " ist kleiner wie die Zahl 2:" + str(random_IntTwo) + " Mini")

if random_IntOne <= 30 or random_IntTwo <= 30:
    print("Einer der beiden Zahlen ist kleiner wie 30")

if random_IntOne <= 50 and random_IntTwo != 50:
    print("Erste Zahl klein, zweite Zahl kein 50iger")