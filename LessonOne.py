#
#PROGRAMMING CLUB
#LESSON ONE
#
#Print: "Hello World", String Concatenation
#Variables: Integers, Strings
#Operators: (Arithmetic): add, subtract, multiply, divide
#Comments: how to comment code
#Concatenation: combining one string with another using the + operator
#Functions: print() Print to the Console, str() Converting Integrs to a String 
#


#This is a comment 
#This is another comment 
#Create comments using the '#' symbol

#Creating Integers Variables
#
x = 1 
#create an integer variable
#name it x and assign it a value of 1

y = 2 
#create an integer variable
#name it y and assign it a value of 2

z = 3 
#create an integer variable
#name it z and assign it a value of 3


print("Hello World!")

#concatenate strings using the + operator
print("string" + " " + "another string")
helloVar = "hello"
worldVar = "world"
#concatenate two predefined string variables
concatVar = helloVar + worldVar
print(concatVar)

#addition operand
result = str(x + y + z)
#add integer variables x, y, and z
print("x + y + z = " + result)
#print the result to the console


#subtraction operand
result = str(x - y - z)
#subtract integer variables x, y, and z 
print("x - y - z = " + result)
#print the result to the console

#multiplication operand
result = str(x * y * z)
#using the * operator
#multiply integer variables x, y, and z 
#store result as a string variable and name it "result"

print("x * y * z = " + result)
#print the result to the console

#division operand
result = str(z / y)
#using the / operator
#divide z by y by using the / operator
print("z / y = " + result)
#print the result to the console

#modulus operand
result = str(z % y)
#using the (modulus)% operator
#compute the remainder for z by y
print("z % y = " + result)
#print the result to the console


#After your code compiles and runs successfully
#If no other mistakes are found in your code
#Your console should display the following results...
#
#x + y + z = 6
#x - y - z = -4
#x * y * z = 6
#z / y = 1.5
#z % y = 1