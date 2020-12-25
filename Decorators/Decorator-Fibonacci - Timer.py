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


