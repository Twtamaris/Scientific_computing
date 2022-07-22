#Make calculator
print('Select an Operation: ')
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')

operation = input('Enter your choice: ')

if operation == '1':
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    print('The sum of the two numbers is: ', num1 + num2)
elif operation == '2':
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    print('The difference of the two numbers is: ', num1 - num2)
elif operation == '3':
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    print('The product of the two numbers is: ', num1 * num2)
elif operation == '4':
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    print('The quotient of the two numbers is: ', num1 / num2)
else:
    print('Invalid Entry')


