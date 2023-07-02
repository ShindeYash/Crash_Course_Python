Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d = {}
>>> d
{}
>>> d.fromkeys([1,2,3]) # fromkeys(iterable, value=none)
{1: None, 2: None, 3: None}
>>> d1.fromkeys([10,20,30],1000) # fromkeys(iterable, value=none)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    d1.fromkeys([10,20,30],1000) # fromkeys(iterable, value=none)
NameError: name 'd1' is not defined
>>> d1 = {}
>>> d
{}
>>> 
>>> d1
{}
>>> d1.fromkeys([10,20,30],1000) # fromkeys(iterable, value=none)
{10: 1000, 20: 1000, 30: 1000}
>>> 
>>> # Q.
>>> a = [10,20,30]
>>> b = ['A','B','C']
>>> # o/P {10:'A', 20:'B', 30:'C'}
>>> 
>>> t = [(10,'A'),(20,'B'),(30,'C')]
>>> t
[(10, 'A'), (20, 'B'), (30, 'C')]
>>> 
>>> # o/P {10:'A', 20:'B', 30:'C'}
>>> dict(t)
{10: 'A', 20: 'B', 30: 'C'}
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    dict(a)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> 
>>> a = [10,20,30]
>>> b = ['A','B','C']
>>> dict(a,b)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    dict(a,b)
TypeError: dict expected at most 1 argument, got 2
>>> dict(a:b)
SyntaxError: invalid syntax
>>> 
>>> # There is one function "zip"
>>> # we can use zip function
>>> 
>>> # zip
>>> # It returns z zip object whose, __next__() method
>>> # retrun a tuple. where the ith element comes from the ith iterable arguments
>>> 
>>> # create and return new object
>>> 
>>> # zip(*, iterables)----> zip object
>>> 
>>> zip(a,b)
<zip object at 0x036E67E8>
>>> 
>>> 
>>> list(zip(a,b))
[(10, 'A'), (20, 'B'), (30, 'C')]
>>> dict(list(zip(a,b)))
{10: 'A', 20: 'B', 30: 'C'}
>>> 
>>> a1 = ['a','b','c']
>>> b1 = [1,2,3,4]
>>> dict(zip(a1,b1))
{'a': 1, 'b': 2, 'c': 3}
>>> 
>>> 
>>> # Any questions
>>> 
>>> #get()
>>> # return the value for key if key is in the dict.
>>> a
[10, 20, 30]
>>> d
{}
>>> d1
{}
>>> d1 = dict(t)
>>> d1
{10: 'A', 20: 'B', 30: 'C'}
>>> d.get(10)
>>> d1.get(10)
'A'
>>> 
>>> # item()
>>> 
>>> # rettun list of tuples representing key value pair.
>>> 
>>> d1
{10: 'A', 20: 'B', 30: 'C'}
>>> d1.items()
dict_items([(10, 'A'), (20, 'B'), (30, 'C')])
>>> l1 = d1.items()
>>> l1
dict_items([(10, 'A'), (20, 'B'), (30, 'C')])
>>> # [(k,v),(k,v)]
>>> 
>>> 
>>> # keys()
>>> 
>>> # returns all keys associated with dict.
>>> 
>>> d1
{10: 'A', 20: 'B', 30: 'C'}
>>> d1.keys()
dict_keys([10, 20, 30])
>>> 
>>> 
>>> # values
>>> 
>>> # It retruns all values associated with dict.
>>> 
>>> d1.values()
dict_values(['A', 'B', 'C'])
>>> 
>>> # pop()
>>> 
>>> # remove specified key and return the corresponding values.
>>> 
>>> d1
{10: 'A', 20: 'B', 30: 'C'}
>>> d1.pop(10)
'A'
>>> d1
{20: 'B', 30: 'C'}
>>> d1.pop(40)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    d1.pop(40)
KeyError: 40
>>> 
>>> 
>>> # popitem()
>>> 
>>> d1.pop()
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    d1.pop()
TypeError: pop expected at least 1 argument, got 0
>>> 
>>> d1.popitem()
(30, 'C')
>>> 
>>> # If the dict is empty then it will get error
>>> d1
{20: 'B'}
>>> d1.popitem()
(20, 'B')
>>> d1
{}
>>> d1.popitem()
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    d1.popitem()
KeyError: 'popitem(): dictionary is empty'
>>> 