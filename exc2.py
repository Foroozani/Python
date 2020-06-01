""" EXERCISE 1
Write a program that reads a positive integer, N
, from the user and then displays the sum of all of the integers from 1 to N.

sum = N* (N+1)/2
"""
n = int(input("Enter a number: \n"))

if n > 0:
# compute the sum
    total = 0.
    total = n *(n + 1) /2
    #Display the results
    print("The sum of the first ", n, " positive integer is:", total)
elif n < 0:
    print('The number is negative')
else:
    print('The entered number is N = 0 ')

#%%
##-----------------------------------------------------------------------------
##                    volume_cyl.py
##  The volume of a cylinder can be computed by multiplying the area
## of its circular base by its height. Write a program that reads the
## radius of the cylinder, along with its height, from the user and
## computes its volume
##-----------------------------------------------------------------------------
import math

radius = float(input("enter the radius of cylinder \n"))
height = float(input('enter the height of cylinder \n'))

def area(r):
    ar = math.pi * r ** 2
    return ar

volume = area(radius) * height
print('Volume of cylinder with radius', radius, ' and height', height, 'is = ', volume)

#%%

##-----------------------------------------------------------------------------
##                  EvenOrOdd.py
## Write a program that reads an integer from the user. Then your program should
## display a message indicating whether the integer is even or odd.
##-----------------------------------------------------------------------------
# read the integer from the user
number = int(input("Enter a number \n"))

if number % 2 == 0:
    print(number,' is even ')
else:
    print(number, ' is odd')


#%%
##-----------------------------------------------------------------------------
## This program gets 10 numbers from the user and counts how many of those
## numbers are greater than 10.
##-----------------------------------------------------------------------------

count = 0

for i in range(10):
     num = eval(input('Enter a number: '))
     if num>10:
         count=count+1
print('There are', count, 'numbers greater than 10.')


#-----------------------------------------------------------------------------
#
#This modification of the previous example counts how many of the numbers the
# user enters are greater than 10 and also how many are equal to 0.
#-----------------------------------------------------------------------------

count1 = 0
count2 = 0
for i in range(10):
    num = eval(input('Enter a number: '))
    if num>10:
        count1=count1+1
    if num==0:
        count2=count2+1
print('There are', count1, 'numbers greater than 10.')
print('There are', count2, 'zeroes.')

#%%
from random import randint
count = 0
for i in range(100):
    num = randint(1, 100)
    if num%12==0:
         count=count+1
         print('Number of multiples of 12:', count)

#%%
##  -----------------------------------------------------------------------
## Factorial, recursion
#---------------------------------------------------------------------------
memo = [0] * 200

n = 100
def fac(n):
    if n == 0: return 1
    result = n * fac(n-1)
    return result


print('Factorial of', n, 'is ', fac(n))

#%%

""" I use the lambda syntax only once
    which have some input arguments and give the output into f"""

f = lambda a, b, c: a**2 +b**2 + c**2

print(f(1,2,3))

#%%

""" A trik to use lambda function""
"""
# def is_even(n):
#     return n%2==0


num = [1, 2, 5, 8, 9, 10, 6, 22, 33, 44]  # this is my input list of data

evens = list(filter(lambda n : n%2==0, num))  # i m filtering my data
double = list(map(lambda a: a*2, num))   # i am mapping the data by lambda function


print('Filtered data   ', evens)
print("Map data        ",double)

#%%

import some_modules

def func1():
    print("This comes from function 1")

def func2():
    print("This comes from function 2")

def func3():
    print("This comes from function 3")

c = some_modules.add(1, 2, 3)

def main():
    func1()   # we can call the functions in main
    print("Hello")
    print("Welcome User")
    print(c)

if __name__ == "__main__":
    main()

print("Program name is here" + __name__)

#%%
class Computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram


    def config(self):
        print("Configuration is", self.cpu, self.ram)

comp1 = Computer("i5",32)
comp2 = Computer("i9", 64)

Computer.config(comp1)
Computer.config(comp2)
# #print(comp1)
# comp1.config(comp1)
# As an example
x = 8
x.bit_length()
print(type(x))

#%%
import math

def distance(x1, x2, y1, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

print(distance(1,3,4,6))
