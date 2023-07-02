Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> `# clear()
SyntaxError: invalid syntax
>>> # Clear()
>>> 
>>> # Remove all itemsfrom list
>>> s = [1,2,3,4]
>>> s
[1, 2, 3, 4]
>>> s.clear()
>>> s
[]
>>> l = [1,2,3,1,4,2,2,2]
>>> l
[1, 2, 3, 1, 4, 2, 2, 2]
>>> l[0]=10
>>> l
[10, 2, 3, 1, 4, 2, 2, 2]
>>> 
>>> 
>>> # copy()
>>> 
>>> # Return shallow copy of the list
>>> help(l.copy)
Help on built-in function copy:

copy() method of builtins.list instance
    Return a shallow copy of the list.

>>> # copy method is used to create a new copy of your object
>>> # new object will have same elements asthat of old one.
>>> # copy means cloning of list object
>>> l
[10, 2, 3, 1, 4, 2, 2, 2]
>>> l1 = l
>>> l1
[10, 2, 3, 1, 4, 2, 2, 2]
>>> l2 = l.copy()
>>> l2
[10, 2, 3, 1, 4, 2, 2, 2]
>>> # l1 = l  .... Deep Copy
>>> # l2 = l.copy() Shallow copy
>>> id(l)
60798472
>>> id(l2)
58221960
>>> id(l1)
60798472
>>> # Q. What is the difference between deep copy and shallow copy
>>> l1 = l
>>> l
[10, 2, 3, 1, 4, 2, 2, 2]
>>> l1
[10, 2, 3, 1, 4, 2, 2, 2]
>>> l[1]=20
>>> l
[10, 20, 3, 1, 4, 2, 2, 2]
>>> l1
[10, 20, 3, 1, 4, 2, 2, 2]
>>> l1[2]=30
>>> l1
[10, 20, 30, 1, 4, 2, 2, 2]
>>> l
[10, 20, 30, 1, 4, 2, 2, 2]
>>> l2
[10, 2, 3, 1, 4, 2, 2, 2]
>>> l2[0]=100
>>> l2
[100, 2, 3, 1, 4, 2, 2, 2]
>>> l
[10, 20, 30, 1, 4, 2, 2, 2]
>>> 
>>> # If changes perform in object l2 the old object list as it is .
>>> 
>>> # I want to create an object with same values and same id
>>> # It is known as deep copy
>>> # It is also known as Aliasing
>>> l1 = l    # Deep Copy
>>> l
[10, 20, 30, 1, 4, 2, 2, 2]
>>> l1
[10, 20, 30, 1, 4, 2, 2, 2]
>>> id(l)
60798472
>>> id(l1)
60798472
>>> 
>>> # Changes performed in any of the object persist in both object
>>> # changes persist in both object because of same id.
>>> 
>>> # Q. defference between = operator and copy() function
>>> # = operator means alising
>>> # copy() function means cloning
>>> 
>>> # count()
>>> 
>>> # return number of occurences of values
>>> l1
[10, 20, 30, 1, 4, 2, 2, 2]
>>> l1.count(2)
3
>>> # if value not found it return zero
>>> l1.count(50)
0
>>> # extend()
>>> 
>>> help(l.extend)
Help on built-in function extend:

extend(iterable, /) method of builtins.list instance
    Extend list by appending elements from the iterable.

>>> l
[10, 20, 30, 1, 4, 2, 2, 2]
>>> l.extend(5,6,7)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    l.extend(5,6,7)
TypeError: extend() takes exactly one argument (3 given)
>>> # iterables
>>> # list
>>> # tuple
>>> #range
>>> l.extend([5,6,7])
>>> l
[10, 20, 30, 1, 4, 2, 2, 2, 5, 6, 7]
>>> l.extend((100,200,300))
>>> l
[10, 20, 30, 1, 4, 2, 2, 2, 5, 6, 7, 100, 200, 300]
>>> l.extend(range(0,10))
>>> l
[10, 20, 30, 1, 4, 2, 2, 2, 5, 6, 7, 100, 200, 300, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> l.extend(l2)
>>> l
[10, 20, 30, 1, 4, 2, 2, 2, 5, 6, 7, 100, 200, 300, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 2, 3, 1, 4, 2, 2, 2]
>>> t = (1,2,3,4)
>>> t
(1, 2, 3, 4)
>>> type(t)
<class 'tuple'>
>>> l.extend(t)
>>> l
[10, 20, 30, 1, 4, 2, 2, 2, 5, 6, 7, 100, 200, 300, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 2, 3, 1, 4, 2, 2, 2, 1, 2, 3, 4]
>>> 
>>> # Q. What is the difference between append and extend
>>> l3 = [1,2]
>>> l3
[1, 2]
>>> l.append('hello')
>>> l3
[1, 2]
>>> l3.append('hello')
>>> l3
[1, 2, 'hello']
>>> l3.append([1,2,3])
>>> l3
[1, 2, 'hello', [1, 2, 3]]
>>> 
>>> l3.extend('Hello')  # String is also iterable
>>> l3
[1, 2, 'hello', [1, 2, 3], 'H', 'e', 'l', 'l', 'o']
>>> 
>>> # if we try to add same using extend then it will add each char/block seperatly
>>> # if we try to add iterable using append it will add complete as a single element
>>> 
>>> # extend does not accept int, float, complex, boolean
>>> # extend does not accept int, float, complex, boolean
>>> 
>>> 
>>> # index
>>> # It return index value of element
>>> 
>>> l3
[1, 2, 'hello', [1, 2, 3], 'H', 'e', 'l', 'l', 'o']
>>> l3.index('hello')
2
>>> # insert
>>> 
>>> # Insert object before index
>>> 
>>> help(l3.insert)
Help on built-in function insert:

insert(index, object, /) method of builtins.list instance
    Insert object before index.

>>> l3.insert(2,'Hi')
>>> l3
[1, 2, 'Hi', 'hello', [1, 2, 3], 'H', 'e', 'l', 'l', 'o']
>>> # Q. I want to add element 'B' between 'l' and 'o' using -ve indexing
>>> 
>>> l3.insert(-1,'B')
>>> l3
[1, 2, 'Hi', 'hello', [1, 2, 3], 'H', 'e', 'l', 'l', 'B', 'o']
>>> # add element 100 after 'o'
>>> l3.insert(13,100)
>>> l3
[1, 2, 'Hi', 'hello', [1, 2, 3], 'H', 'e', 'l', 'l', 'B', 'o', 100]
>>> len(l3)
12
>>> 