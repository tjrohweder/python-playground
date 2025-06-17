from datetime import date

current_date = date.today()
current_year = current_date.year

birth = int(input("Please enter the year of your bithday: "))

age = current_year - birth

try:
    if age >= 18:
        print("Ok, you are old enought to watch those ladies")

    else:
        print("Go talk to your mama")

except ValueError as e:
    print(f"Error: {e}")
