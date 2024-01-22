import random;
num1 = int(input("Gib hier die Coder Zahl 1 ein\n"))
num2 = int(input("Gib hier die Coder Zahl 2 ein\n"))

string_array = ["Apfel", "Affe", "Wall"]

def add(num1, num2):
    sum = num1 + num2
    return sum;

print(add(num1, num2))

def randomInt():
    random_Int = random.randint(100, 200)
    return random_Int

print(randomInt())

def getArray():
    random_Int = random.randint(0,2)
    print(random_Int)
    word = string_array[random_Int];
    return word;

print(getArray())