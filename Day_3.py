Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>  # Center
 
>>> # To return a centred string of length width
>>> # padding is done using the specified fill char (default is a space)
>>> s = 'amit'
>>> s
'amit'
>>> s.center(10)
'   amit   '
>>> s
'amit'
>>> len(s)
4
>>> a = s.center(10)
>>> a
'   amit   '
>>> len(a)
10
>>> s.center(9)
'   amit  '
>>> s.center(10,'$')
'$$$amit$$$'
>>> # expandtabs
>>> print('hello\thi')
hello	hi
>>> # return a copy where aal tab chars are expanded using spaces.
>>> # If tab size is not given, a tab size of 8 char
>>> s = 'rdtc\tscscoe\bhor'
>>> s
'rdtc\tscscoe\x08hor'
>>> s = 'rdtc\tscscoe\tbhor'
>>> s
'rdtc\tscscoe\tbhor'
>>> s.expandtabs()
'rdtc    scscoe  bhor'
>>> 'rdtc    scscoe  bhor'
'rdtc    scscoe  bhor'
>>> s
'rdtc\tscscoe\tbhor'
>>> s.expandtabs(0)
'rdtcscscoebhor'
>>> s.expandtabs(100)
'rdtc                                                                                                scscoe                                                                                              bhor'
>>> 
>>> # format
>>> help(s.format)
Help on built-in function format:

format(...) method of builtins.str instance
    S.format(*args, **kwargs) -> str
    
    Return a formatted version of S, using substitutions from args and kwargs.
    The substitutions are identified by braces ('{' and '}').

>>> # The main objective of format{} method to format string into meaningful output form
>>> name = 'suresh'
>>> age = 38
>>> salary = 75000
>>> # O/P
>>> # suresh's salary is 75000 and his age is 38
>>> print("{}'s salary is{} and his age is{}".format(name,salary,age))
suresh's salary is75000 and his age is38
>>> print("{0}'s salary is{1} and his age is{2}".format(name,salary,age))
suresh's salary is75000 and his age is38
>>> print("{z}'s salary is{y} and his age is{x}".format(y=salary,x=age,z=name))
suresh's salary is75000 and his age is38
>>> 
>>> # translate
>>> # return each character in the string using the given translation table
>>> s = 'Hello Sam'
>>> # => 'Hello Pam'
>>> # Ascii value of S = 83 and P = 80
>>> m = {83:80}
>>> m
{83: 80}
>>> s.translate(m)
'Hello Pam'
>>> s = 'Hello Sam Shyam Suresh'
>>> s
'Hello Sam Shyam Suresh'
>>> s.translate(m)
'Hello Pam Phyam Puresh'
>>> s = 'Hello Sam Shyam suresh'
>>> s.translate(m)
'Hello Pam Phyam suresh'
>>> 
>>> # maketrans
>>> # To create a mapping table
>>> # it return a translation table usable for str translate
>>> s = 'Hello sam'
>>> s
'Hello sam'
>>> s.maketrans('s','p')
{115: 112}
>>> s = 'Hello Sam'
>>> s
'Hello Sam'
>>> s.maketrans('S', 'P')
{83: 80}
>>> s
'Hello Sam'
>>> s.translate(s.maketrans('S','P'))
'Hello Pam'
>>> s.maketrans('Sam', 'Pam')
{83: 80, 97: 97, 109: 109}
>>> s = 'Hi Ameya'
>>> s.maketrans('Ameya', 'Amita')
{65: 65, 109: 109, 101: 105, 121: 116, 97: 97}
>>> s.translate(s.maketrans('Ameya', 'Amita'))
'Hi Amita'
>>> 
>>> # List
>>> 