def bmi (x, y):
    return x / (y ** 2)

weight = float(input('Type your weight: '))
height = float(input('Type your height: '))

print(f'Your BMI is {bmi(weight, height):.2f}')
