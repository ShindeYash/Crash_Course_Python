Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # [] operator is clalled slice operator
>>> # indexing
>>> # +ve and -Ve indexing
>>> # +ve indexing L to R
>>> # -ve indexing R to L
>>> s = 'amit patil'
>>> s[:]
'amit patil'
>>> len(s)
10
>>> s[1]
'm'
>>> s[0]
'a'
>>> s[-10]
'a'
>>> s[start:stop]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s[start:stop]
NameError: name 'start' is not defined
>>> # s[start:stop]
>>> s[0:3]
'ami'
>>> # stop is ex
>>> s[0:4]
'amit'
>>> # slicing is always start from 0
>>> s[:]
'amit patil'
>>> # s[::]
>>> # s[start:stop:step]
>>> # slicing also step option
>>> s
'amit patil'
>>> s[::]
'amit patil'
>>> s[::1]
'amit patil'
>>> s[::2]
'ai ai'
>>> s[::3]
'atal'
>>> s[2::2]
'i ai'
>>> # when we have step 1 it progress from left to right always
>>> s[::1]
'amit patil'
>>> # But we have steping of -1 then it process from right to left
>>> s
'amit patil'
>>> s[::-1]
'litap tima'
>>> s = 'bhagwan'
>>> s[::-1]
'nawgahb'
>>> s = 'amit patil'
>>> s
'amit patil'
>>> a[-4::]
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a[-4::]
NameError: name 'a' is not defined
>>> s[-4::]
'atil'
>>> 
>>> # using -ve indexing i want to reverse the amit
>>> s[-7::-1]
'tima'
>>> s[-2:-5:-1]
'ita'
>>> s[-2:-6:-1]
'itap'
>>> s = '1234567890'
>>> S[1::2]
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    S[1::2]
NameError: name 'S' is not defined
>>> s[1::2]
'24680'
>>> s[::2]
'13579'
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> # Capitalize
>>> # make the first character have upper case and rest are lower case
>>> s = 'amit Patil'
>>> s.capitalize()
'Amit patil'
>>> s
'amit Patil'
>>> s.upper()
'AMIT PATIL'
>>> s
'amit Patil'
>>> a = s.upper()
>>> a
'AMIT PATIL'
>>> a
'AMIT PATIL'
>>> s
'amit Patil'
>>> s.title()
'Amit Patil'
>>> help(s.title)
Help on built-in function title:

title() method of builtins.str instance
    Return a version of the string where each word is titlecased.
    
    More specifically, words start with uppercased characters and all remaining
    cased characters have lower case.

>>> help(s.upper)
Help on built-in function upper:

upper() method of builtins.str instance
    Return a copy of the string converted to uppercase.

>>> s.lower()
'amit patil'
>>> a.lower()
'amit patil'
>>> s.index('a')
0
>>> help(s.index)
Help on built-in function index:

index(...) method of builtins.str instance
    S.index(sub[, start[, end]]) -> int
    
    Return the lowest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.
    
    Raises ValueError when the substring is not found.

>>> s.index('zz')
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    s.index('zz')
ValueError: substring not found
>>> s.find('a')
0
>>> help(s.find)
Help on built-in function find:

find(...) method of builtins.str instance
    S.find(sub[, start[, end]]) -> int
    
    Return the lowest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.
    
    Return -1 on failure.

>>> s.find('zz')
-1
>>> 