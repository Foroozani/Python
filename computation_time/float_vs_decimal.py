import sys
sys.getsizeof(0)
sys.getsizeof(1)
sys.getsizeof(2**1_000)
# decimal, Math operation
#import decimal
from decimal import Decimal
x = 10
y = 3
z = 2
print(x // y, x % y)
print(divmod(x,y))
help(Decimal)
# memory footprint
# decimal takes larger memory footprint and computational cost is expensive
a = 3.14           #float
b = Decimal('3.14') #decimal
sys.getsizeof(a)
sys.getsizeof(b)
print(b)

# how long will take simply creating float vs decimal
# check computational coast
import time
def run_float(n=1):
    for i in range(n):
        a = 3.1415

def run_decimal(n = 1):
    for i in range(n):
        a = Decimal('3.1415')

n = 10_000_000
start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('this operation for floats:',end-start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('this operation for decimal:',end-start)

# checking mathematical operation
def run_float(n=1):
    a = 3.1415
    for i in range(n):
        a + a

def run_decimal(n = 1):
    a = Decimal('3.1415')
    for i in range(n):
        a + a


n = 10_000_000
start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('this operation for floats:',end-start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('this operation for decimal:',end-start)

#----------------------------------
import math
n = 5_000_000

def run_float(n=1):
    a = 3.1415
    for i in range(n):
        math.sqrt(a)   #Return the square root of x

def run_decimal(n = 1):
    a = Decimal('3.1415')
    for i in range(n):
        a.sqrt()     #Return the square root of the argument to full precision.

start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('this operation for floats:',end-start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('this operation for decimal:',end-start)
# SO, stick to float, faster and more efficient