import random

num = random.randint(1, 100)

tries = 0
while True:
    guessed = int(input("Guess a number between 1 & 100: "))
    tries += 1
    
    if guessed == num:
        print(f"Congratulations! You guessed the number in {tries} tries.")
        break
    elif guessed < num:
        print("Sorry, your guess is too low than the number. Try again\n.")
    elif guessed > num:
        print("Sorry, your guess is too high than the number. Try again\n.")