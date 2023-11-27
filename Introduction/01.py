# This function addition two numbers
def addition(x, y):
    return x + y

# This function subtracts two nubmers
def subtracts(x, y):
    return x - y

# This function multiplies two numbers
def multiplies(x, y):
    return x * y

# This function divide two numbers
def divide(x, y):
    return x / y


print("Select operation")
print("1.Add")
print("2.subtracts")
print("3.multiplies")
print("4.divide")

def cal():
    choise = input("Enter choise(1/2/3/4: )")
    tuple_num = ('1', '2', '3', '4')
    # Check if choise is one of the four options
    if choise in tuple_num:
        num1 = float(input("Enter first number "))
        num2 = float(input("Enter second number "))

        if choise == '1':
            print(num1, "+", num2, "=", addition(num1, num2))
        
        elif choise == '2':
            print(num1, "-", num2, "=", subtracts(num1, num2))

        elif choise == '3':
            print(num1, "*", num2, "=", multiplies(num1, num2))

        elif choise == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid Input")
cal()