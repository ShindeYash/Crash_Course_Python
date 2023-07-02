Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> a
10
>>> # PEP8 Standard (Python Enhancment proposal 8)
>>> a=10
>>> a
10
>>> a = 10
>>> a
10
>>> # Data Types in Python
>>>  a = 10
 
SyntaxError: unexpected indent
>>> # 1. Numeric Data Type
>>> # int => int data type represent whole number
>>> # base 10 (0-9)
>>> # in python we don't have a limit for int value
>>> a = 10
>>> a
10
>>> type(a)
<class 'int'>
>>> b = 'abc'
>>> type(b)
<class 'str'>
>>> # We can use represent int value in the following ways
>>> # 1. Decimal form (base 10)
>>> # 2. Binary form (base 2)
>>> # 3. octal form (base 8)
>>> # 4. Hexa decimal form (base 16)
>>> 
>>> # 2. Float
>>> # its represent float value
>>> c = 2.4
>>> type(c)
<class 'float'>
>>> 
>>> # 3. Complex
>>> # complex number is of the form
>>> # a + bj  a is real part and b is imaginary part
>>> # a and b contain integer and float point values
>>> d = 3 + 5j
>>> d
(3+5j)
>>> type(d)
<class 'complex'>
>>> 
>>> # Boolean
>>> # We can use this data type to represent boolean values
>>> b = True
>>> type(b)
<class 'bool'>
>>> # True and False
>>> # True as 1
>>> # False as 0
>>> 2 > 3
False
>>> 
>>> # 1. String
>>> # 2. List
>>> # 3. Tuple
>>> # 4. Dictionary
>>> # 5. Set
>>> # 6. Frozenset
>>> # 7. range
>>> 
>>> 
>>> 
>>> # String
>>> # A string is a sequence of characters enclosed within single or double quotes.
>>> # str represent string data type
>>> # Its a global data type bcz it accept everything
>>> 
>>> s = 'bhagwan'
>>> s
'bhagwan'
>>> type(s)
<class 'str'>
>>> s1 = 'ramesh 1234 suresh'
>>> s1
'ramesh 1234 suresh'
>>> s2 = 'abcd$@123.5'
>>> s2
'abcd$@123.5'
>>> type(s2)
<class 'str'>
>>> s = bhagwan
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    s = bhagwan
NameError: name 'bhagwan' is not defined
>>> s = "bhagwan"
>>> s
'bhagwan'
>>> s = bhagwan
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    s = bhagwan
NameError: name 'bhagwan' is not defined
>>> bhagwan = 123
>>> s = bhagwan
>>> s
123
>>> 123
123
>>> ''
''
>>> type('')
<class 'str'>
>>> "  "
'  '
>>> len("  ")
2
>>> ''''''
''
>>> type('''''')
<class 'str'>
>>> s = 'deep"
SyntaxError: EOL while scanning string literal
>>> s = 'deep'
>>> s
'deep'
>>> s = 'deep"amey"'
>>> s
'deep"amey"'
>>> s = "hi'ge'"
>>> s
"hi'ge'"
>>> 
>>> # Rule :- If we have single quote outside inside u must use double quote Viceversa
>>> 
>>> # By using single or double quotes we cannot represent multi line string literals.
>>> 
>>> s = ' Bhagwan
SyntaxError: EOL while scanning string literal
>>> 
>>> # For this requirement we should go for triple single quote(''' ''') or triple double quotes(""" """)
>>> s1 = ''' bhagwan
Thorat

Amey

Suyash

Deep '''
>>> s1
' bhagwan\nThorat\n\nAmey\n\nSuyash\n\nDeep '
>>> type(s1)
<class 'str'>
>>> 
>>> ''' ''' 123
SyntaxError: invalid syntax
>>> 123
123
>>> 2.5
2.5
>>> ''
''
>>> 1+2j
(1+2j)
>>> True
True
>>> 
>>> # Features of String
>>> # Background data structure is Array
>>> s = 'python data science ML'
>>> # if i want count total element in string
>>> # will use the len() function
>>> len(s)
22
>>> # Indexing
>>> # it gives an access to a single character
>>> s[8]
'a'
>>> s[7]
'd'
>>> # to access a subpart/ substring from main string
>>> 
>>> # we can use Slicing to access sub string
>>> # slice means a piece
>>> #[] operator is called slice operator  which can be used to retrive parts of string
>>> #[] operator is called slice operator  which can be used to retrive parts of string
>>> # string follows zero based index
>>> # The index can be either +ve or -ve
>>> # +ve indexing start with 0
>>> # -ve indexing start with -1
>>> s1 = 'scscoe'
>>> 
>>> # positive indexing means forword direction from left to right
>>> # -ve  indexing means backword direction from right to left
>>> # [:] => [start : stop ]
>>> s[8:11]
'ata'
>>> s[8:12]
'ata '
>>> s[7:10]
'dat'
>>> # stop is exclusive
>>> s[7:11]
'data'
>>> s[22]
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    s[22]
IndexError: string index out of range
>>> s[21]
'L'
>>> s[-1]
'L'
>>> s[:]
'python data science ML'
>>> s[:6]
'python'
>>> s[6:]
' data science ML'
>>> 