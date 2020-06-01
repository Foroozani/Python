Here is some basic examples. 



#---------------------------------------------------------------------------------
# Python_2Write a program that reads a positive integer, N
## from the user and then displays the sum of all of the integers from 1 to N.

##  sum = N* (N+1)/2
##---------------------------------------------------------------------------------
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

