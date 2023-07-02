Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #
>>> # Discard()
>>> 
>>> # Remove an element from a set if it is a member
>>> #
>>> # If the element is not member do nothing
>>> 
>>> s = {1,2,3,4,4,5,6,7}
>>> s
{1, 2, 3, 4, 5, 6, 7}
>>> s.discard(2)
>>> s
{1, 3, 4, 5, 6, 7}
>>> s.discard(10)
>>> s
{1, 3, 4, 5, 6, 7}
>>> s.discard()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s.discard()
TypeError: discard() takes exactly one argument (0 given)
>>> TypeError: discard() takes exactly one argument (0 given)
SyntaxError: invalid syntax
>>> 
>>> 
>>> # Intersection
>>> 
>>> # Fetch the common elements from 2 sets
>>> 
>>> # Return the intersection of two sets as a new set
>>> # all elements that are in both set
>>> 
>>> s1 = (1,2,3}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
>>> s1 = {1,2,3}
>>> s1
{1, 2, 3}
>>> 
>>> s2 = {2,3,4,5}
>>> s2
{2, 3, 4, 5}
>>> s1.intersection(s2)
{2, 3}
>>> 
>>> m1 = 'this is simple program'
>>> 
>>> m1
'this is simple program'
>>> 
>>> m2 = 'program is simple'
>>> 
>>> m1.intersection(m2)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    m1.intersection(m2)
AttributeError: 'str' object has no attribute 'intersection'
>>> 
>>> # find out common contents from m1 and m2
>>> 
>>> # convert string to set
>>> 
>>> ms1 = set(m1)
>>> ms1
{'h', 'o', 'e', 'i', ' ', 's', 'a', 'r', 'l', 'g', 'm', 't', 'p'}
>>> 
>>> # here it gives char
>>> 
>>> # but we want words
>>> 
>>> m1.split()
['this', 'is', 'simple', 'program']
>>> ms1 = set(m1.split())
>>> ms1
{'program', 'is', 'this', 'simple'}
>>> 
>>> ms2 = set(m2.split())
>>>  ms2
{'program', 'is', 'simple'}
>>> 
>>> ms1.intersection(ms2)
{'program', 'is', 'simple'}
>>> 
>>> 
>>> # union
>>> 
>>> # take all elements from both sets, without duplicates
>>> 
>>> s1 = {1,2,3,4}
>>> 
>>> s2 = (2,3,4,5,6}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
>>> s2 = {2,3,4,5,6}
>>> s1
{1, 2, 3, 4}
>>> s2
{2, 3, 4, 5, 6}
>>> 
>>> s1.union(s2)
{1, 2, 3, 4, 5, 6}
>>> 
>>> 
>>> # isdisjoint
>>> 
>>> # Return true if two sets have a null intersection
>>> # True and False
>>> 
>>> # going to check unique ness of 2 sets
>>> 
>>> s = {1,2,3,4,5}
>>> 
>>> m = {2,3,4,5,6}
>>> 
>>> x = {7,8,9,10,6}
>>> 
>>> s.isdisjoint(m) # {1,2,3,4} are common vlaues in both set s and m
False
>>> 
>>> s.isdisjoint(x)
True
>>> 
>>> # issubset()
>>> 
>>> # Return whether another set contains this set
>>> 
>>> 
>>> s
{1, 2, 3, 4, 5}
>>> s = {1,2,3,4,5,6}
>>> 
>>> s
{1, 2, 3, 4, 5, 6}
>>> 
>>> m = {2,4,6,7,8,9}
>>> m
{2, 4, 6, 7, 8, 9}
>>> 
>>> z = {6,7,8,9}
>>> 
>>> s.issubset(m)
False
>>> 
>>> m.issubset(z)
False
>>> 
>>> z.issubset(m)
True
>>> 
>>> # issuperset()
>>> 
>>> # report wether this set contains another set
>>> 
>>> s = {1,2,3,4,5,6}
>>> m = {2,4,6,7,8,9}
>>> z = {6,7,8,9}
>>> y = {1,2,3}
>>> 
>>> s.issuperset(m)
False
>>> 
>>> s.issuperset(y)
True
>>> 
>>> m.issuperset(z)
True
>>> 
>>> # pop
>>> 
>>> s.pop()
1
>>> s
{2, 3, 4, 5, 6}
>>> s.pop()
2
>>> 
>>> # It removes and return some random element from the set
>>> 
>>> 
>>> # remove()
>>> 
>>> # remove an element from set : it must be a memeber
>>> 
>>> # It remove specified element from the set
>>> 
>>> s
{3, 4, 5, 6}
>>> s.remove(6)
>>> s
{3, 4, 5}
>>> s.remove(6)
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    s.remove(6)
KeyError: 6
>>> 
>>> # symmetric_difference()
>>> 
>>> # return the symmetric diff. of two sets as a new set
>>> 
>>> # i.e. all elements tha are in exactly one of the sets.
>>> 
>>> # Fetch uncommon elements from both sets.
>>> 
>>> s = {1,23,4,6,7}
>>> s = {1,2,3,4,6,7}
>>> s
{1, 2, 3, 4, 6, 7}
>>> 
>>> m = {2,3,4,5,6,7,8,9}
>>> 
>>> m
{2, 3, 4, 5, 6, 7, 8, 9}
>>> s.symmetric_difference(m)
{1, 5, 8, 9}
>>> 
>>> # symmetric_difference_update()
>>> s
{1, 2, 3, 4, 6, 7}
>>> m
{2, 3, 4, 5, 6, 7, 8, 9}
>>> 
>>> # update a set with the symmetric diff. of itself and another
>>> 
>>> s.symmetric_difference_update(m)
>>> s
{1, 5, 8, 9}
>>> 
>>> 
>>> # update()
>>> 
>>> # update a set with the union of itself and others.
>>> 
>>> s
{1, 5, 8, 9}
>>> 
>>> s.update(7)
Traceback (most recent call last):
  File "<pyshell#181>", line 1, in <module>
    s.update(7)
TypeError: 'int' object is not iterable
>>> s.update([7])
>>> s
{1, 5, 7, 8, 9}
>>> s.update((1,2,3,4))
>>> s
{1, 3, 5, 2, 7, 8, 9, 4}
>>> 