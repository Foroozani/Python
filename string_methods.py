"""String note"""

import sys

a = 'This is a very long string'
b = 'This is a very long string'
print(a == b)  # comparison character by character
print(a is b)  # comparision of memory address
c = sys.intern('This is a very long string')
d = sys.intern('this is a very long string')
print(c is d)
