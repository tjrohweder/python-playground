import random

number = random.randint(1, 10)

guess = None

while guess != number:
    guess = int(input("Try to guess the number(1-10): "))
    print(f"{guess} is not the correct number")

print("You guessed the number :)")
