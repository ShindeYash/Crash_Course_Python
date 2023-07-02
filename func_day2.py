'''
# Return Statment
# return is a keyword

# a function without return

def add():
    print(100+200)

result = add()
print(result)

# when ur function does not return anything then it return none means nothing
-----------------------------------------

# function using return statement

def add():
    a = 100+200
    s = 200-100
    m = 100*2
    d = 200/20
    return s
    return a
result = add()
print(result)

# how many values we can return
# n numbers

# return brings the value outside the def
# only single return is allowed

def test(fever):
    if fever > 96:
        return 'Positive'
    else:
        return 'Negative'
result = test(70)
if result == 'Positive':
    print('14 days isolation')
else:
    print('take medicine and rest')

--------------------------------------------------------------------------------

# Two types of variables
# 1. Global Variable
# 2. Local Variable

# GV
# The variable which is available anywhere throughout the program
# and we declare this variable outside the function

x = 100 # golbal variable
def test(): # access x variable inside the function
    print('Inside',x)

# access x outside a function
print('Outside', x)
test()
-------------------------------------
# Local Variable

def test():
    x=100 # local variable
    print('inside',x)

test()
print('outside',x)  # cant access local variable outside the function
----------------------------------------------
def test():
    global x
    x=100
    print('inside',x)
test()
print('outside',x)


'''

# lambda Function / Anonymous function / nameless function

# It is a function without name
# it is used for performing one time operation
# one time operation  means we can supply only one Expression
# multiple expressions are not allowed

# normal function
def add(x):
    return x+100

print('sum',add(50))

# Lambda Function
s = lambda x:x+100
print(s(50))

# WAP square of number


# normal Function

def sqr(n):
    return n*n
print(sqr(4))

print('-------lambda function----------')
s = lambda x:x*x
print(s(4))