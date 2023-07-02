'''
import math
print(math.factorial(5))
print('Module Alinsing')

import math as m1
print(m1.sqrt(4))

If we want to access all the members of a module directly
then use

from module_name import function, variable, members

--------------------------------------------------
from math import *
print(factorial(5))
It will import everything inside math module

now i want to import specific thing from module
from math import factorial, sqrt, pi
print(pi)
---------------------------------
now i want to use member alising
from math import factorial as f, sqrt as s
print(f(4))

User Define modules
Module created by user as per business requirments
now i want to import module_day1.py in this file

---------------------------------------------------------
from module_day1 import a, b
c = a+b
print(c)
print(a)

__pycache__: when we import any module from a particular directory so
its .pyc file gets created and stored in this folder

why .pyc get created
to convert .py to bytecode/machine code



'''
