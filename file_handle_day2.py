'''

Read operation
- read()
- readline()
- readlines()

read()   # used to read all the contents
f = open('abc.txt')
print(f.read())
-------------------------------------

- readline() # it is used to read one line at time
f = open('abc.txt')
print(f.readline())
print(f.readline())
---------------------------------------------
- readlines # read all the contents but in list of string
f = open('abc.txt')
print(f.readlines())
---------------------------------------------
# read()

f = open('abc.txt')
data = f.read()
#print(data)
for i in data:
    print(i)
------------------------------------------------
# readline()

f = open('abc.txt')
data = f.readline()
#print(data)
for i in data:
    print(i,end='')
----------------------------------------------------
# Iteration using the read operation

# readline()

f = open('abc.txt')
data = f.read(18)
#print(data)
for i in data:
    print(i,end='')
========================================================

# write Operation

# Modes used in write operation
# 'w' write
# 'a' append
# 'x' exclusive

# All above modes are used to create a file perform write operation

--------------------------------------------------------
# w mode
f=open('ABC.txt') # default its read mode
print(f.read())

# case sensitivity abt file name it not an issue
# but extension(.txt) + proper name u should give reading

----------------------------------------------------
# lets create new file using write mode
f = open('a1.txt','w')

# w mode perform Truncate operation
# remove old contents

# Lets add new contents in a file
print(f.writable())
#f.write(('This is a1.txt data\n'))
#f.write('I am adding new contents in this file')

# above new contents is overwritten in a1.txt file
f.write(1234) # accept only string data not allowed int data

------------------------------------------------------------
f = open('a1.txt','w')
#f.writelines('This is string we are\n supplying ')
f.writelines(['Name is Amar','Age is 30','Place is Pune'])
-------------------------------------------------------------
# a append mode

# Append mode is create + add lines at the end

f = open('abc.txt', 'a')
print(f.writable())
# add some contents in file abc.txt
f.write('\nwe can add contents at the end')
-------------------------------------------------------


# Write operation
# X exclusive mode

# If file is not present then create a new file
# but if file is already present then throw an exception
# FileExistError
# This is used to create a file only ones

f= open('pqr.txt','x')
print(f.writable())
f.write('Hi Hello every one')
-----------------------------------------
# seek() and tell() functions in a file Handling

# tell() : It will tell current position of ur cursor in the file
# used for cheking operation
f = open('pqr.txt')
print(f.tell())
# lets read some blocks
print(f.read(4))
print(f.tell())
print(f.read(10))
print(f.tell())
----------------------------------------
# seek(): bring the cursor to given position
f= open('pqr.txt')
print(f.tell())
print(f.read())
f.seek(5)
print(f.read())

=================================================

# Find out mobile number present in the pqr.txt file

f = open('pqr.txt')
# print(f.read())

for i in f.read():
    if i.isdigit():
        print(i,end='')
----------------------------------------------------------
f = open('pqr.txt')
print(f.read().find('9'))
f.seek(39)
print(f.read(10))

'''
