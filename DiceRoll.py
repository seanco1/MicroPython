import random
sides = input("How many sides do your dice have? : ")
sides = int(sides)
roll_again = "yes"
while roll_again == "yes" or roll_again == "y":
    print("Dice rolling...")
    dice1 = random.randint(1, sides)
    dice2 = random.randint(1, sides)
    if dice1 == dice2:
        print(f"You rolled double =",dice1)
    else:
        print(f"Dice 1 =",dice1)
        print(f"Dice 2 =",dice2)
    roll_again = input("Roll again? (yes / y) : ")
