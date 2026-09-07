# calculator functions
def add(number1,number2):
    return number1 + number2
def subtract(number1,number2):
    return(number1 - number2)
def multiply(number1,number2):
    return(number1 * number2)
def divide (number1,number2):
    if number2==0:
        return "cannot divide by zero"
    else:
        return number1/number2
while True:
    # Get numbers from user
    number1=float(input("enter first number:"))
    number2=float(input("enter second number"))
    # Get operation from user
    operation=input("enter operation(+,-,*,/):")
    if operation=="+":
        result=add(number1,number2)
        print(result)
    elif operation=="-":
        result=subtract(number1,number2)
        print(result)
    elif operation=="*":
        result=multiply(number1,number2)
        print(result)
    elif operation=="/":
        result=divide(number1,number2)
        print(result)
    else:
        print("invalid operation")
    answer=input("do you want to calculate again(yes/no):").lower()
    if answer=="no":
        break


