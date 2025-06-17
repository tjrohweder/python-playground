from datetime import date

current_date = date.today()
current_year = int(current_date.year)

name = str(input("Enter your name: \n"))
birth_year = int(input("Inform the year of your birthday\n"))

age = current_year - birth_year

if age >= 150:
    print("Sorry dude, it can't be")

elif age >= 100 and age < 150:
    print("Time is running out...Enjoy")

elif age >= 1:
    print(f"Your name is {name} and you are {age} years old")

else:
    print("Looks like you're not born yet")
