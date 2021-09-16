import random
number = random.randint(1, 100)
tries = 0

name = input("What is your name?")

guess = input("Guess a number: ")
guess = int(guess)
tries += 1
if guess == number:
    print("You win!")
    exit()
if guess < 1:
    print("Invalid Input, guess higher than 1")
if guess > 100:
    print("Invalid Input, guess a number lower than 100")
if guess > number:
    print("Your guess is too high")
if guess < number:
    print("Your guess is too low")
while guess != number and tries < 5:
    guess = input("Try again: ")
    guess = int(guess)
    tries += 1

    if guess > number:
        print("Your guess is too high")
    if guess < number:
        print("Your guess is too low")
if guess > number:
    print("Your guess is too high")
if guess < number:
    print("Your guess is too low")
if tries == 5:
    print("You lose")
