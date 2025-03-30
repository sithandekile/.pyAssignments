print(' Simple Calculator')

num1=float(input('Enter your first number: '))
num2=float(input('Enter your second number: '))
print(f'Enter your chosen operator \n 1. + \n 2. - \n3. x \n4. /')

choice=input('chosen option: ')
if int(choice)==1 or choice.lower()=='+':
    addition = num1 + num2
    print(f'The Sum of {num1} and {num2} is: {addition}')
elif int(choice)==2 or choice.lower()=='-':
    subtraction=num1 - num2
    print(f'The subtraction of {num1} and {num2} is:{subtraction}')
elif int(choice)==3 or choice.lower()=='x':
    multiplication = num1 * num2
    print(f'The multiple of {num1} and {num2} is: {multiplication}')
elif int(choice)==4 or choice.lower()=='/':
    devision = num1 / num2
    print(f'The devision of {num1} and {num2} is: {devision}')
else:
    print('Invalid Choice')
        
