'''
# Q. Reverse the words: Rajgad Dnyanpeeth
s = 'Rajgad Dnyanpeeth'
for i in s.split()[::-1]:
    print(i,end=' ')

----------------------------------------------------------
# Q. Reverse the characters / blocks
s = 'Rajgad Dnyanpeeth'
#print(s[::-1])

# reversed:- inbuilt function
#print(reversed(s))
# Whenever u get output in the form object in order to get values from it

# we have 2 options
# 1. iterate over it
# 2. typecast
print(list(reversed(s)))
final = ''
for i in reversed(s):
    final+=i   # it will concatenate one block at a time
print(final)
----------------------------------------------------------------
# Q. Reverse the characters of individual word
s = 'Ameya Deshpande'
# o/p ayemA ednaphseD
for i in s.split():
    print(i[::-1],end=' ')

* Assignment *
 Q. Reverse the characters of individual word
s = 'Ameya Deshpande'
# o/p ayemA Deshpande
-----------------------------------------
# Q . I want to fetch vowels from the string: a e,i,o,u
s = 'Ameya Deshpande'
vowels = ['a','e', 'i', 'o','u', 'A', 'E', 'I', 'O', 'U' ]
for i in s:
    if i in vowels:
        print(i,end=' ')
-----------------------------------------
# Patterns : *, number, Alphabate

# Q.
*
* *
* * *
* * * *
for i in range(1,5):
    print(i*'*')
--------------------------------
for i in range(1,5):  # row
    for j in range(i):  # column
        print('*',end=' ')
    print()
-----------------------------------------

Assignment Question
1.
*****
****
***
**
*

2.
*****
 ***
  *
------------------------------------------
Alaphabates
A
BB
CCC
DDDD
EEEEE

for i in range(1,6):
    print(chr(i+64)*i)

'''





