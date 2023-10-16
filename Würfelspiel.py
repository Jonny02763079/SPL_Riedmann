import random;

player_Count = 0;
computer_Count = 0;

for i in range(6):
    player_Count += random.randint(0,5) + 1;
    computer_Count += random.randint(0,5) + 1;

print("Playercount: \n" + str(player_Count), "\nComputercount: \n" + str(computer_Count))

if player_Count > computer_Count:
    print("You won! Gratulations")

elif player_Count < computer_Count:
    print("You lost! Sucker")

elif player_Count == computer_Count:
    print("Draw! You are both loosers")