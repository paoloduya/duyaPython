numberOfTerms = int(input('Input Limit: '))

number0 = 0
number1 = 1
count = 0

if numberOfTerms <= 0:
    print('Please input a positive number: ')
else:
    print('Fibonacci sequence:')
    while count < numberOfTerms:
        print(number0)
        total = number0 + number1
        number0 = number1
        number1 = total
        count += 1