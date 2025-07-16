while True:
    number = int(input('Please enter a number: '))
    result = number % 2

    try:
        if result == 0:
            print(f'The number {number} is pair')
        else:
            print(f'The number {number} is odd')
    except Exception as e:
        print(f'{e}')
