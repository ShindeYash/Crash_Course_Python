Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Tuple
>>> 
>>> # tuple is same as list except that it is immutable
>>> 
>>> # once we create tuple we cannot perform any changes in that object.
>>> # tuple read only version of list
>>> # If our data is fixed and never changes then we should go far tuple.
>>> 
>>> # insersion order is preserved
>>> # Duplicates are allowed
>>> # Hetrogeneous objects are allowed
>>> # index is play important role in tuple
>>> # tuple support +ve and -ve indexing.
>>> 
>>> # We can represent tuple elements within parenthesis () and with comma sepretor
>>> # parenthesis is optional
>>> 
>>> # Create a empty tuple
>>> ()
()
>>> type(())
<class 'tuple'>
>>> t = ()
>>> t
()
>>> b = tuple()
>>> b
()
>>> # We can represent tuple elements within parenthesis () and with comma sepretor
>>> 
>>> t = (1,2,3,4,5)
>>> t
(1, 2, 3, 4, 5)
>>> type(t)
<class 'tuple'>
>>> t1 = (1,2,3,'A','B')
>>> t1
(1, 2, 3, 'A', 'B')
>>> # parenthesis is optional
>>> 
>>> t2 = 1,2,3,6,7,8
>>> t2
(1, 2, 3, 6, 7, 8)
>>> type(t2)
<class 'tuple'>
>>> 
>>> # compulsary the value should ends with comma, otherwise it is not treated as tuple
>>> t3 = 1,2
>>> t3
(1, 2)
>>> t4 = 1
>>> t4
1
>>> type(t4)
<class 'int'>
>>> t4 = 1,
>>> t4
(1,)
>>> type(t4)
<class 'tuple'>
>>> 
>>> t
(1, 2, 3, 4, 5)
>>> t[-1]
5
>>> t[-1]=50
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    t[-1]=50
TypeError: 'tuple' object does not support item assignment
>>> # so thats why tuple is immutable
>>> 
>>> 
>>> # Methods
>>> dir(tuple)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> 
>>> t
(1, 2, 3, 4, 5)
>>> t.count(2)
1
>>> t.count(10)
0
>>> 
>>> # index
>>> # returns index of first occurance of the given element
>>> 
>>> t.index(2)
1
>>> t.index(10)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    t.index(10)
ValueError: tuple.index(x): x not in tuple
>>> 
>>> # Accessing elements of tuple
>>> # We can access either by tuple elements by index or by slicing
>>> 
>>> t[3]
4
>>> t[:]
(1, 2, 3, 4, 5)
>>> t[3:]
(4, 5)
>>> 
>>> # Mathematical operators for tuple
>>> 
>>> # we can apply + and * operators for tuple
>>> 
>>> # concatenation operator(+)
>>> t
(1, 2, 3, 4, 5)
>>> t1
(1, 2, 3, 'A', 'B')
>>> t+t1
(1, 2, 3, 4, 5, 1, 2, 3, 'A', 'B')
>>> 
>>> # Multiplication operator or repition operator(*)
>>> 
>>> t
(1, 2, 3, 4, 5)
>>> t1
(1, 2, 3, 'A', 'B')
>>> t*t1
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    t*t1
TypeError: can't multiply sequence by non-int of type 'tuple'
>>> t*2
(1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
>>> t4
(1,)
>>> t4*5
(1, 1, 1, 1, 1)
>>> 
>>> len(t)
5
>>> t4
(1,)
>>> t4 = (1,5,2,4,3)
>>> t4
(1, 5, 2, 4, 3)
>>> sorted(t4)
[1, 2, 3, 4, 5]
>>> min(t4)
1
>>> max(t4)
5
>>> 
>>> # Tuple packing and unpacking
>>> 
>>> # Packing
>>> 
>>> # we can create a tuple by packing a group of variables
>>> 
>>> a = 10
>>> b = 20
>>> c = 30
>>> d = 40
>>> a
10
>>> b
20
>>> c
30
>>> d
40
>>> # (10, 20, 30, 40)
>>> t5 = a,b,c,d  # tuple packing
>>> t5
(10, 20, 30, 40)
>>> type(t5)
<class 'tuple'>
>>> 
>>> # here a,b,c,d are packed into a tuple t5. .... This nothing but tuple packing
>>> 
>>> # unpacking
>>> 
>>> # tuple unpacking is the reverse process of tuple packing
>>> # we can unpack a tuple and assign its values to different variables.
>>> 
>>> t6 = (100,200,300,400,500)
>>> t6
(100, 200, 300, 400, 500)
>>> p,q,r,s,u = t6
>>> p,q,r,s,u = t6 # tuple unpacking
>>> 
>>> p
100
>>> q
200
>>> r
300
>>> s
400
>>> u
500
>>> x,y,z = t6
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    x,y,z = t6
ValueError: too many values to unpack (expected 3)
>>> 
>>> # Note- At the time of tuple unpacking the number of variables and number of values should be same.
>>> # otherwise we will get valueError.
>>> 
>>> # Q. Which one is better tuple or list
>>> # Ans:- Its depends on the requirment of business.
>>> 
>>> # . Defference between tuple and list
>>> # Q. Which is faster
>>> # Q. why list required more memory compared to tuple?
>>> 
>>> # Difference tuple and list
>>> # 1. list is muttable
>>> #  tuple is immutable
>>> 
>>> # 2. List creation use square brackets and values seprated by cooma
>>> #    Tuple creation use parenthesis or its optional and values seprated by comma.
>>> 
>>> # 3. Tuple required less memory
>>> #    List required more memory
>>> 
>>> t = (1,2,3,4)
>>> t
(1, 2, 3, 4)
>>> l = [1,2,3,4]
>>> l
[1, 2, 3, 4]
>>> t.__sizeof__()
28
>>> l.__sizeof__()
36
>>> # Q. why list required more memory compared to tuple?
>>> # tuple are stored in a single block of memory
>>> # tuple is immutable so it doesn't required extra space to store new object.
>>> 
>>> # List are allocated in two blocks : the fixed one with all the python object information and a variable sized block for the data
>>> 
>>> # It is the reason creating a tuple is fater than list.
>>> 