from datetime import date

current_date = date.today()
current_year = current_date.year

birth = int(input('Please enter the year of your bithday: '))

age = current_year - birth

try:
    if age >= 18:
        print("You're old enough")

    else:
        print('Go talk to your mama')

except Exception as e:
    print(f'Error calculating your age: {e}')
