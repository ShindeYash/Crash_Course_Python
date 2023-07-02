'''
# WAP using lambda function to find out largest number amongst 2 number

# using normal function
def findlarg(x,y):
    if x>y:
        print('X is largest')
    else:
        print('Y is largest')

findlarg(10,20)

----------------------------------------------------
# using lambda function
largest = lambda x,y:'X is largest' if x>y else 'Y is largest'
print(largest(100,200))

'''

# WAP using lambda function to find even or odd number

s = lambda x: 'Given number is Even' if x%2==0 else 'Given number is Odd'
print(s(11))

# to implement this logic we need ternary operator

# return_of_if   if_condition  else  else_return