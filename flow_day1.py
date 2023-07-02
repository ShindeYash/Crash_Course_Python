'''
Flow Control Blocks:

1. Selective / Conditional statements: Purpose is to run the code
   on the basis of a Condition.

A. if (condition) # used to test only one condition

B. if else  # used to test 2 conditions

C. if elif else  # used to test 3 condition

D. if elif elif elif.......else [elif ladder]   # can test multiple conditions

E. nested if : can test dependent conditions

if hp:
    if 8gb:
    else: 6gb
else:
--------------------------------------------------------------------------

if is condition based

elif is condition based

else is optional and condition less
we use else to test default / last condition

-----------------------------------------------------------------

# Examples:

# if (condition)
# when condition is True, then only ur control will enter inside the block
# else it wont [ if condition is False]

# to Check given number is positive or negative
n = -1
if n > 0:
    print('Good Evening')

------------------------------------------------------

# Check number is even or odd
num = 27

if num % 2 == 0:
    print('number is even')
else:
    print('number is odd')
--------------------------------------------
# User Input

num = int(input('enter number'))

if num % 2 == 0:
    print('number is even')
else:
    print('number is odd')

-----------------------------------------------------
# Test student percentage and assign a class to the student

per = float(input('Enter Percentage:'))

if per >= 75 :
    print('You got Distinction')
elif per >= 65:
    print('First Class')
elif per >= 55:
    print('Second Class')
elif per >= 40:
    print('Pass Class')
else:
    print('Fail')
'''

# Q. Find out largest number among 3







