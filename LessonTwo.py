#
#PROGRAMMING CLUB
#LESSON TWO
#
#If Statements: 
#if:   if 
#if - runs the code indented below it if the conditional returns TRUE
#elif: else if
#elif - else if will run if the if condition above it returns FALSE
# and the elif condition returns TRUE
#else: else
#else - else will run only if all the if condition above it return FALSE
#

x = 1 
y = 2
z = 3

print("x = " + str(x))
print("y = " + str(y))
print("z = " + str(z))


#IF STATEMENTS
#if - if the conditional returns true 
#(the code indented on the lines below 'if x > y:' will run)


#elif - else if will run if the if condition above it returns false 
#(the code indented on the lines below 'elif x == y:' will run)
#(you can create as many 'elif' conditions below your if statement as you want to)

#else - when all the above if or elif conditions return false. 
#(in other words no conditions were met)
#(the code indented on the lines below 'else:' will run)


#prints a different response to the console 
#based on the value of 'x' as it is compared to 'y'
if x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
else:
    print("x is less than y")
 
#prints a different response to the console 
#based on the value of 'x' as it is compared to 'z'
if x < z:
    print("x is less than z")
elif x == z:
    print("x is equal to z")
else:
    print("x is greater than z")

#will print to the screen if 'x' is equal to 1
#will print something different to screen if 'x' does not equal 1 
if x == 1:
    print("x is equal to 1")
else:
    print("x does not equal 1")
    
#will print to the screen if 'y' is equal to 2
#will not print anything to screen if 'y' does not equal 2
if y == 2:
    print("y is equal to 2")
    
##After your code compiles and runs successfully
#Your console should display the following results...
#
#x = 1
#y = 2
#z = 3
#x is less than y
#x is less than z
#x is equal to 1
#y is equal to 2