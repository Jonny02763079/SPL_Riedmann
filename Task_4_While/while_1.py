import random;
boolean = True;
sum = 0;

while boolean:
    random_Int = random.randint(10, 30)
    print(random_Int);
    if random_Int == 15 or random_Int == 25:
        boolean = False
        print(sum)
        break;
    sum += random_Int

print(sum)