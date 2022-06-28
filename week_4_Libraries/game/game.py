import random as r
from sys import exit

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

game_number = r.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess > game_number:
                print("Too large!")
            elif guess < game_number:
                print("Too small!")
            else:
                print("Just right!")
                exit()
    except ValueError:
        pass
