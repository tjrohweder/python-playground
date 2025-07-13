import random

random_num = random.randint(1, 10)

guess = None

while guess != random_num:
    guess = int(input("Try to guess the number: "))

    if guess > random_num:
        print("Too high")
    elif guess < random_num:
        print("Too low")

print("Congratulations... you guessed the number")
