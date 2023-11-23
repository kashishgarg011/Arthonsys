#7. Perform basic arithmetic operations (addition, subtraction, multiplication, division) using user input
num1=int(input('first no is:'))
num2=int(input('second no is:'))
choice=input('''Enter your choice:
                1. + for Addition
                2. - for Subtraction
                3. * for Multiplication
                4. / for Division:- ''')
if choice=='+':
    result=num1+num2
    print('Addition of two numbers is',result)
elif choice=='-':
    result=num1-num2
    print('Subtraction of two numbers is',result)
elif choice=='*':
    result=num1*num2
    print('Multiplication of two numbers is',result)
elif choice=='/':
    result=num1/num2
    print('Division of two numbers is',result)
