'''
File
Is a medium to store the data / information in a suitable format
Each file will be stored on hard drive with specific extension.

Example
abc.txt
simple.py
.jpg
.mp3
.wav

python support default text files

python has 2 file formats:

1. .txt
2. .binary file (img, audio, video)

--------------------------------------------
File operation are as follows:

- create
- open
- read
- write
- close
------------------------------------------------
All above operations we can do using a single function of a python
i.e open()

open()
- default text file we can read
- default mode is 'r' read mode
------------------------------------------------------------------
f = open('file1.txt')
# f is a handle
print(f)

# lets read the properties of a file
print('Name of a file:', f.name) # name of file
print('Mode of a file:', f.mode)  # mode of file
print('Is read mode on??',f.readable()) # bool ans
print('Is write mode on??', f.writable()) # bool
print('Is my file colsed??', f.closed)  # bool
f.close()
print('After close is my file closed??',f.closed) # bool
---------------------------------------------------------------

If file is present in another directory in same project so we need to give complete path

how to read a file from another directory in the project
f = open('C://Users/Abhishek/PycharmProjects/File_Handling/dir_1/abc.txt')
print(f.readline())
-------------------------------------------------------------------------
Modes present in python

Character Meaning
-------------------------------
'r'     open for reading (default)
'w'     open for writing, truncating the file first
'x'     create a new file and open for writing
'a'     open for writing, appending to the end of the file if text exists
'b'     binary mode
't'     text mode(default)
'+'     open a disk file for updating (reading and writing)
---------------------------------------------------------------
# Read Operations

f = open('file1.txt')
# now read the contents from a file
# In read mode 3 operations present
# read()
# readline()
# readlines()

# print(f.read())

# read() will read all the contents start to end

# suppose if i want to read specific part
print(f.read(2))
-----------------------------------------------------
# readline(): It reads one line at a time

f = open('file1.txt')
print(f.readline())
print(f.readline())
------------------------------------------
f = open('file1.txt')
print(f.readline(8)) # will read 8 block from line one
print(f.readline())  # will read remaing from line one

--------------------------------------------------------------
# readlines

f = open('file1.txt')
print(f.readlines())

# used to read all the contents but format is : list of string
# means each line of text file will be a one element of a list
------------------------------------------------------------------------------------------------
# Iterations using the read operation

# read()

f = open('file1.txt')
data = f.read()
for i in data:
    print(i)

# read a single block/char line by line

'''



