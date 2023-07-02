'''
Iterative Statments

Used for performing iterations

Iteration means we use iterables(str, tuple, list, dict, range, set)
and form that iterables we fetch each element one by one.

It contains 2 types

1. for loop
2. while loop

1. for loop
syntax:
 for(keywords) var(identifier) in(operator) sequence/iterable:
     print(var)

----------------------------------------------------------------
# Example
# input as list
nm = ['Ramesh', 'Suresh', 'Mahesh', 'Amar', 'Amay', 'Ajay']
l = len(nm)
print(l)
# for loop default read from left to right
for i in range(l):
    print(nm[i])
----------------------------------------------------

# input as string

s = 'Good evening all of you'
for i in s:
    print(i, end=' ')
------------------------------------------

# string need to print only words
s = 'Good evening all of you'
l = s.split()
#print(l)
for i in l:
    print(i)
---------------------------------------------
# string need to print words ending with 'h'
s = 'good evening mahesh and Ajay '
for word in s.split():
    #print(i)
    if word.endswith('h'):
        print(word)
-------------------------------------------
# string need to print only numbers into another list
# o/p l1 = [9922151623, 9829126352]
s = 'good evening mahesh 9922151623 and Ajay 9829126352 '
l1 =[]
for word in s.split():
    if word.isdecimal():
        l1.append(word)
print(l1)
--------------------------------
# using dict
d = {'name':'python', 'age': 32, 'place': 'pune'}
for i in d:
    print(i)
    # default it fetches only keys
--------------------------------------------
# using dict
d = {'name':'python', 'age': 32, 'place': 'pune'}
for i in d.values():
    print(i)

----------------------------------------------------
# using dict
d = {'name':'python', 'age': 32, 'place': 'pune'}
for i in d:
    print(i, d.get(i))

'''





