#
#PROGRAMMING CLUB
#LESSON THREE
#
#User Input: retrieve input from the user using the function input()
#input(): function will give the user a prompt on the screen 
#assign information from input() as a variable and give it a name.
#i.e. var = input("type something: ")
#

print("Enter '1' for Addition")
print("Enter '2' for Subtraction")
print("Enter '3' for Multiplication")
print("Enter '4' for Division")

selectedOperator = input("Please make a selection:")

if selectedOperator == '1':
    print("Please enter two numbers to ADD")
    x = int(input("x: "))
    y = int(input("y: "))
    z = x + y
    print(str(x) + " + " + str(y) + " = " + str(z))
elif selectedOperator == '2':
    print("Please enter two numbers to SUBTRACT")
    x = int(input("x: "))
    y = int(input("y: "))
    z = x - y
    print(str(x) + " - " + str(y) + " = " + str(z))
elif selectedOperator == '3':
    print("Please enter two numbers to MULTIPLY")
    x = int(input("x: "))
    y = int(input("y: "))
    z = x * y
    print(str(x) + " * " + str(y) + " = " + str(z))
elif selectedOperator == '4':
    print("Please enter two numbers to DIVIDE")
    x = int(input("x: "))
    y = int(input("y: "))
    z = x / y
    print(str(x) + " / " + str(y) + " = " + str(z))
else:
    print("Invalid input!!")


##After your code compiles and runs successfully
#Your console should display the following results...
#
#Enter '1' for Addition
#Enter '2' for Subtraction
#Enter '3' for Multiplication
#Enter '4' for Division
#Please make a selection:
#
