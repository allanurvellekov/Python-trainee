#Calculator
def calculate():
    operation = input('''Please enter the operation !
                      like 
                      press '+'  for Add
                      press '-' for Substrack
                      press '*' for Multiply
                      press '/ ' for Divid
                      =   ''')
    a = float(input("Enter the first Number : "))
    b = float(input("Enter the second Number : "))
    if operation == '+':
        print('{} + {} = '.format(a, b))
        print( a + b)
    elif operation == '-':
        print('{} - {} = '.format(a, b))
        print(a - b)
    elif operation=='*':
        print('{} * {} = '.format(a, b))
        print(a * b)
    elif operation=='/':
        print('{} / {} = '.format(a, b))
        print(a / b)
    else:
        print(" You put invalid operation pls try it again!")
    run_again()

def run_again():
    calc_again = input(" Do you want Calc again ? Y/N    ")
    if calc_again().upper=='Y':
        calculate()
    elif calc_again.upper()=='N':
        print ("Thanks ! See you Later!")
    else:
        run_again()
calculate()

