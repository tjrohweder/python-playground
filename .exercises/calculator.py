def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y

print('Select operation: ')
print('1.Add')
print('2.Substract')
print('3.Multiply')

choice = input('Enter choice: 1/2/3\n')

if choice in ('1', '2', '3'):
    try:
        number1 = int(input('Enter the first number: '))
        number2 = int(input('Enter the second number: '))

        if choice == '1':
            print(f'Result: {add(number1, number2)}')
        elif choice == '2':
            print(f'Result: {subtract(number1, number2)}')
        elif choice == '3':
            print(f'Result: {multiply(number1, number2)}')

    except ValueError:
        print('Invalid input')

else:
    print(f'{choice} is an invalid operation')
