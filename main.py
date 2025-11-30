print('PyCalculator')

history_of_calculations = []

while True:
    number_one = int(input('Enter number 1: '))
    number_two = int(input('Enter number 2: '))
    print('+ - addition\n- - subtraction\n/ - division\n* - multiplication\n** - exponentiation\n// - Division without remainder')
    operator = input('Select operator (Or quit to exit): ')

    if operator == '+':
        print(f'Calculation result: {number_one + number_two}')
        history_of_calculations.append(f'{number_one} + {number_two} = {number_one + number_two}')
    elif operator == '-':
        print(f'Calculation result: {number_one - number_two}')
        history_of_calculations.append(f'{number_one} - {number_two} = {number_one - number_two}')
    elif operator == '/':
        if number_two != 0:
            print(f'Calculation result: {number_one / number_two}')
            history_of_calculations.append(f'{number_one} / {number_two} = {number_one / number_two}')
        else:
            print(f'Error: Division by zero!')
    elif operator == '*':
        print(f'Calculation result: {number_one * number_two}')
        history_of_calculations.append(f'{number_one} * {number_two} = {number_one * number_two}')
    elif operator == '**':
        print(f'Calculation result: {number_one ** number_two}')
        history_of_calculations.append(f'{number_one} ** {number_two} = {number_one ** number_two}')
    elif operator == '//':
        print(f'Calculation result: {number_one // number_two}')
        history_of_calculations.append(f'{number_one} // {number_two} = {number_one // number_two}')
    elif operator == 'quit':
        break
    else:
        print('Incorrect operator!')

for i, calc in enumerate(history_of_calculations, start=1):
    print(f'{i}. {calc}') 