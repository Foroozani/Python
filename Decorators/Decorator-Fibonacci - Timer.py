#!/usr/bin/env python
# coding: utf-8

# ### Decorators Application (Timing)

# timing how long it takes to run a certain function.

def timed(fn):
    from time import perf_counter
    from functools import wraps
    
    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start
        
        args_ = [str(a) for a in args]
        kwargs_ = ['{0}={1}'.format(k, v) for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)
        print('{0}({1}) took {2:.6f}s to run.'.format(fn.__name__, 
                                                         args_str,
                                                         elapsed))
        return result
    
    return inner


#  calculates the n-th Fibonacci number:
# 
# `1, 1, 2, 3, 5, 8, ...`
# 
# implement this using three different methods:
# 1. recursion
# 2. a loop
# 3. functional programming (reduce)
# 
# We use a 1-based system, e.g. first Fibonnaci number has index 1, etc.

# #### Using Recursion

def calc_recursive_fib(n):
    if n <=2:
        return 1
    else:
        return calc_recursive_fib(n-1) + calc_recursive_fib(n-2)


calc_recursive_fib(3)

calc_recursive_fib(6)

@timed
def fib_recursed(n):
    return calc_recursive_fib(n)

fib_recursed(33)

fib_recursed(34)

fib_recursed(35)

@timed
def fib_recursed_2(n):
    if n <=2:
        return 1
    else:
        return fib_recursed_2(n-1) + fib_recursed_2(n-2)


fib_recursed_2(10)


# #### Using a Loop

@timed
def fib_loop(n):
    fib_1 = 1
    fib_2 = 1
    for i in range(3, n+1):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return fib_2               

fib_loop(3)

fib_loop(6)

fib_loop(34)

fib_loop(35)


# this method is much more efficient!

# #### Using  Reduce

# We first need to understand how we are going to calculate the Fibonnaci sequence using reduce: 
# 
# <pre>
# n=1:
# (1, 0) --> (1, 1)
# 
# n=2:
# (1, 0) --> (1, 1) --> (1 + 1, 1) = (2, 1)  : result = 2 
# 
# n=3
# (1, 0) --> (1, 1) --> (2, 1) --> (2+1, 2) = (3, 2)  : result = 3
# 
# n=4
# (1, 0) --> (1, 1) --> (2, 1) --> (3, 2) --> (5, 3)  : result = 5
# </pre>
# 
# In general each step in the reduction is as follows:
# 


from functools import reduce

@timed
def fib_reduce(n):
    initial = (1, 0)
    dummy = range(n-1)
    fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0]), 
                   dummy, 
                   initial)
    return fib_n[0]                  

fib_reduce(3)

fib_reduce(6)

fib_reduce(34)

fib_reduce(35)


# Now we can run a quick comparison between the various timed implementations:


fib_recursed(350)
fib_loop(350)
fib_reduce(350)


# Even though the recursive algorithm is by far the easiest to understand, it is also the slowest.

# local, non-local and global scopes
x = 'hello python monty'   # Global scope
def outer():
    x = 'hello'
    def inner1():
        nonlocal x
        x = 'python'
        def inner2():
            nonlocal x
            x = 'monty'
        inner2()
    inner1()
    print('The value of x in outer func', x)
outer()
print(x)

def outer():
    x = 'hello'
    def inner1():
        nonlocal x
        x = 'python'  # vaghti value az outer scope umade va assign shode,
        # bayad hatman scopesh nonlocal bashe
    inner1()
    print('value of x in outer is:', x)

outer()


#----------------------------
# Closuers
#----------------------------
def outer():
    x = 'python'
    def inner():
        print(x)
    return inner # return closure  from the function
# call the outer and assign the results back to fn
fn = outer()
fn.__code__.co_freevars
fn.__closure__

#
def outer():
    x = 1
    def inner():
        nonlocal x
        x += 3
        print (x)
    return inner # return closure  from the function
a = outer()
a()

def outer():
    count = 0
    def inc():
        nonlocal count
        count += 2
        return count
    return inc
fn = outer() # assign the closure
fn()  # call the closure

# define common free-variable, two different scope
def outer():
    count = 0

    def inner1():
        nonlocal count
        count += 1
        return count

    def inner2():
        nonlocal count
        count += 1
        return count

    return inner1, inner2
fn1, fn2 = outer()

def pow(n):
    def inner(x):
        return x**n
    return inner

square = pow(2)
cube = pow(3)
square(2), cube(2)

def average():
    num = []
    def adder(var):
        num.append(var)
        total = sum(num)
        count = len(num)
        return total / count
    return adder   # retun closure
a = average()
a(0)
a(3)
b = average()   # we can create another closure
b(10)
#
def counter():
    int_value = 4
    def adder(increment=1):
        nonlocal int_value
        int_value += increment
        return int_value
    return adder

a = counter()
a.__code__
a(5)
# calculata how many times a function has been run
def add_values(a, b):
    return a + b

def mult_values(a, b):
    return a * b

def counter(fn):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print('{0} function has been run {1} times'.format(fn.__name__, cnt))
        return fn(*args, **kwargs)

    return inner

coun_fn = counter(add_values)
coun_fn(2, 5)
count2 = counter(mult_values)
count2(2, 4)

#------------------------------------
# Decorators
#------------------------------------
def counter(fn):
    cnt = 0

    def inner(*args, **kwargs):
        """keep it generic means we can handle any function """
        nonlocal cnt
        cnt += 1
        print('"{0}" function has been run {1} times'.format(fn.__name__,cnt))
        return fn(*args, **kwargs)
    return inner  #return closure

def add(a: int, b: int = 2) -> 'return sum of two numbers':
    """This function add two values
    input: a, b
    output: a + b
    """
    return a + b

def mult(a: 'integer or float', b: int, c: int, *, d: 'keyword only '
                                                      'argument') -> 'return something':
    """This multiply four values"""
    return a * b * c * d

id(add)
add = counter(add)
id(add)
help(add)
add.__code__
add(10,60)
add(10)
mult(1, 2, 3, d = 4)
mult = counter(mult)
mult(1, 2, 4, d = 4)
# an easy way of doing this is "@", they are identical
# e.g we can decorate our function using decorator function "counter"
@counter
def func(a: 'integer or float', b: int) -> 'return something':
    """This multiply four values"""
    return a * b

func(2, 8)
mult.__name__
mult.__doc__

from functools import wraps
def counter(fn):
    cnt = 0
    @wraps(fn) #fn: the function being decorated
    def inner(*args, **kwargs):
        """keep it generic means we can handle any function """
        nonlocal cnt
        cnt += 1
        print('"{0}" function has been run {1} times'.format(fn.__name__,cnt))
        return fn(*args, **kwargs)
    return inner  #return closure

@counter
def func(a: 'integer or float', b: int) -> 'return something':
    """This multiply two values"""
    return a * b

func(1,4)
help(func)

# Decorator application (Timing)
def srt(a):
    pass


def timed(fn):
    from time import perf_counter
    from functools import wraps
    @wraps(fn)
    def inner(*args, **kwargs):
        """It will calculate how long will take to a function run"""
        start =  perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start
        # just print the args
        args_ = [str(a) for a in args]
        kwargs_ = ['{0}={1}'.format(k,v) for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        print('"{0}"{1} took {2:.6f} to run'.format(fn.__name__,all_args, elapsed))
        return result
    return inner

# write a function to calculate  Fibonacci number
# examine three different approaches 1. recursion 2. loop 3. reduce
@timed
def fib_loop(n):
    fib_1 = 1
    fib_2 = 1
    for i in range(3,n+1):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return fib_2

fib_loop(36)

# Another application of decorator, here i just log by printing by console
import logging
def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        #name = 'example3.log'
        logging.basicConfig(filename =
                            '/home/najmeh/PycharmProjects/pythonProject/deepdive2/example4.log' ,
                            level=logging.DEBUG)
        logging.debug('This message should go to the log file')
        logging.info('{0} time function called {1}'.format(run_dt,
                                                           fn.__name__))
        logging.info(result)
        print('{0} time function called {1}'.format(run_dt, fn.__name__))
        return result

    return inner

@logged
def func1():
    print('func1 is running ...')
    pass
@logged
def func2():
    print('func 2 is running ...')
    pass
@logged
@timed
def func3():
    pass

# calculating Fibonacci number
class Fib:
    def __init__(self):
        self.cach = {1: 1, 2: 1}

    def calc_fib(self, n):
        if n not in self.cach:
            print('calculating fib {0} ...'.format(n))
            self.cach[n] = self.fib(n-1) + self.fib(n-2)
        return self.cach[n]

f = Fib()  # create one instance from class
f.calc_fib(10)

#------------------------------
def fib():
    cache = {1: 1, 2: 1}

    def calc_fib(n):
        if n not in cache:
            cache[n] = calc_fib(n-1) + calc_fib(n - 2)
        return cache[n]

    return calc_fib

f1 = fib()  # we can create different closure
f2 = fib()  # create another closure

fib(10)

#--------------------------------------------------
# Parametrize decorator
#--------------------------------------------------
def dec_factory(a, b):
    def dec(fn):
        def inner(*args, **kwargs):
            print('running decorator inner')
            print('free vars: ', a, b)  # a and b are free variables!
            return fn(*args, **kwargs)
        return inner
    return dec

@dec_factory(10, 20)
def my_func():
    print('python rocks')

def calc_fib_recurse(n):
    return 1 if n < 3 else calc_fib_recurse(n-1) + calc_fib_recurse(n-2)

def fib(n):
    return calc_fib_recurse(n)

from functools import wraps

def timed(num_reps=1):
    def decorator(fn):
        from time import perf_counter

        @wraps(fn)
        def inner(*args, **kwargs):
            global result
            total_elapsed = 0
            for i in range(num_reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (perf_counter() - start)
            avg_elapsed = total_elapsed / num_reps
            print('Avg Run time: {0:.6f}s ({1} reps)'.format(avg_elapsed,
                                                            num_reps))
            return result
        return inner
    return decorator

@timed(5)
def fib(n):
    return calc_fib_recurse(n)

fib(30) # ==fib = timed(fib, 5)

#---------------------------------------
def my_dec(a, b):
    from time import perf_counter
    def dec(fn):
        def inner(*args, **kwargs):
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            elapsed = end - start
            print('elapsed time is: {0}'.format(elapsed))
            print('decorated function call {0}, {1}'.format(a, b))
            return result
        return inner
    return dec



def my_dec1(a, b):
    def dec(fn):
        def inner(*args, **kwargs):
            print('decorated function call {0}, {1}'.format(a, b))
            return fn(*args, **kwargs)
        return inner
    return dec

@my_dec1(10, 20)
def my_func(s):
    print ('Helle {0}'.format(s))

my_func("Najmeh")


