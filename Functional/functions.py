# unpacking iterable
"""Note Dictionaries and set are unordered, there is no concept of position"""
a = 1, 2, 3
type(a)
a, b, c = [1, 'a', 3.14]
# iterate over string
for _ in 'hello':
    print(_)
# iterate over set
s = {1, 4 , 'r', 'n', 9}
for e in s:
    print(e)
# iterate over dictionaries
dic = {'a': 2, 'b': 4, 'key3': 8}
for e in dic:
    print(e)
for e in dic.values():
    print(e)
for e in dic.items():    # keys with values
    print(e)

# extended unpacking
l = [1, 2, 4, 6, 9, 5, 8]
a, *b = l
s1 = 'python'
join = [*l, *s1]

dic1 = {'a': 2, 'b': 4, 'key3': 8}
dic2 = {'c': 2, 'b': 8, 'key4': 8}
{*dic1, *dic2}    # unpack keys
{**dic1, **dic2} # unpacking key with values

# *args
def avg(*args):
    """To calculate the average value of some arguments"""
    count = len(args)
    total = sum(args)
    if count == 0:
        return 0
    else:
        return total/count
    print(args)
avg()

# an alternative and elegant way of writting is short curcuting
# *args
def avg(*args):
    """To calculate the average value of some arguments"""
    count = len(args)
    total = sum(args)
    return count and total/count
avg()

# we also can force the user to give atleast one parameter as input
def avg(a, *args):
    """To calculate the average value of some arguments"""
    count = len(args) + 1
    total = sum(args) + a
    return total/count
avg(1)

# keyword arguments

def my_func(a, b, *, d= True, **kwargs):
    print(a)
    print(b)
    print(d)
    #print(args)
    print(kwargs)
my_func(1, 2, f = 20, g = 'hello')

def func(a, b= 2, c= 3, *args):
    print(a, b, c, args)

func(1, 4, 5, 6, 7)
print()

# a simpler timer function
import time
def compute_power(n, *, start= 1, end):
       # using for loop
        results = []
        for i in range(start, end):
            results.append(n**i)
        return results
compute_power(2, end = 5)

# ---------------------------------------------
# first class function
# --------------------------------------------
def my_func(a: 'is string',
            b: 'integer > 0' = 1,
            *args: 'some extra argument',
            k1: 'keyword only arg1',
            k2: 'keyword only arg2' = 100,
            **kwargs: 'some extra keyword args') -> 'return something':
    print(a, b, args, k1, k2, kwargs)

print(my_func.__annotations__)

# lambda expression
f = lambda x: x**2
f(3)
g = lambda x, y = 10: x + y / 2
g(3, 7)
h = lambda x, *args, y, **kwargs: (x, *args, y, kwargs)
h(1, 3, 'a', 'b',y =7, w='hello')
def apply_func(x, fn):
    return fn(x)
apply_func(2, g)
apply_func(2, lambda x: x**2)

# sorted
#A custom key function can be supplied to customize the sort order, and the
#    reverse flag can be set to request the result in descending order.

l = ['H', 'a', 'B', 'c', 'E', 'b']
sorted(l)
sorted(l, key = lambda x: x.upper())
# sorting a value of dictionary
dic = {'abc': 100, 'def': 400, 'hip':300, 'jdhf':1}
sorted(dic, key = lambda e : dic[e])
print(dic[e])
def sqrt_dis(x):
    return (x.real)**2 + (x.imag)**2
sqrt_dis(1+2j)
# sort a string base on last character of each string
str = ['John', 'Joe', 'Sara', 'Katrin', 'Scott', 'Najmeh']
sorted(str, key = lambda str: str[-1], reverse = True)
import random
# shuffel a list
random.random()
lst =[1, 3, 4, 6, 7, 9, 10]
sorted(lst, key = lambda x: random.random())
#----------------------------------------
#  Map, Filter, Zip
# ---------------------------------------

def factorial(n):
    return n if n < 2 else n*factorial(n-1)

factorial(5)
results = map(factorial, range(10))
# either we can iterate through it or list it
print(results)
for _ in results:
    print(_)
list(map(factorial, range(10)))

l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9]
l3 = 10, 20, 30, 50, 90, 25, 33, 63, 0
l4 = 'python'
list(map(lambda x, y, z: x + y + z, l1, l2, l3))
list(filter(lambda x: x%3 == 0 ,l3))
list(filter(None, l3)) # filter out falsy values
list(zip(l1, l2, l3, l4))

#----------------------------------------
# CALLABLE
#----------------------------------------
import operator
my_string = 'python'
my_list = [1, 2, 3, 5, 6]
operator.setitem(my_list, 0, 100)
my_list    #[100, 2, 3, 5, 6]
operator.delitem(my_list, 3)
my_list    #[100, 2, 3, 6]
f = operator.itemgetter(2)
f(my_list), f(my_string)

# string class provide upper method
s = 'python'
s.upper()
# alternatively
f = ('upper')
