'''
# Suntax of function

def func_name(parameters):
    print('Hi')


func_name(parameter_values)

# if in decleration we have parameters then we must need to supply values to it
------------------------------------------------------
# example

def add(a,b):
    print('Addition of two numbers:', a+b)

x = 10
y = 20
add(x,y)

-----------------------------------------------------
# a, b, are positional arguments

def add(a,b):
    print(a+b)

add(10,20)
add(100, 200)
add(1)   # this will raise exception bcz b value is not given
add()  # this will give error bcz a, b values not given
-------------------------------------------------------------

# types of arguments
# 1. Positional / required arguments
# 2. Keyword arguments
# 3. Default Arguments
# 4. Variable length arguments

# Positional Arguments
# Example

def info(name, age):
    print('Name is :', name)
    print('Age is :', age)

info('Amar', 38)
info(39, 'Ajay')

#  The arguments are passed to function in correct position order
# bcz its positional hence

# The number of arguments in the function call should exactly match with the
# number of parameters specified in the function def
-------------------------------------------------------------

# 2. Keyword arguments
# Keyword arguments in which the order (position) of the parameters/ arguments can be changed

# The values not assigned to arguments according to their position but based on their name(keywords)

# example

def info(name, age):
    print('Your name is :', name)
    print('Your age is ', age)

#info('Amar', 38)
info(age=40, name='Ajay')

# keyword map values to its exact parameters
# so , order doesnot matter in this case

-----------------------------------------------------
# 3. Default Arguments

# default are we can supply in declaration only

def info(name, age=30):
    print('Name is:', name)
    print('Age is :', age)

info('Ajay')
--------------------------------------------------
# 4. Variable length argument

# In some situation, it is not knows in advance how many arguments will be passed to a function

# in such case , python allows programmers to make function calls with arbitary number of arguments

# use * before the parameter name

def add(a,b):
    print(a+b)

add(10, 20)
add()
add(1,2,3)
add(10,20,30,40)

# we cant pass multiple values in above case as decleration only
# contains 2 parameters

# so above issue we can solve using variable length  arguments type.

def add(*args):   # instead of args we can use other valid identifier
    print(sum(args))

add(10,20)
add()
add(1,2,3)
add(10,20,30,40)
'''

# WAP to fetch only characters from function calling

def simple(*n):
    for i in n:
        if str(i).isalpha():
            print(i,end=' ')
    print()

simple('A', 10, 'X')
simple(1, 2, 'Z', 3, 'S')



