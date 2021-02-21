#---------------------------------------------------
# List comprehensions
#---------------------------------------------------
##
import markdown

square = []
for i in range(1,101):
    square. append(i**2)

[i**2 for i in range(1,102) if i%2 and i%3]

[i**2 for i in range(1,102) if i%2 == 0]
##
# comprehensions are essentially functions
table = []
for i in range(1,11):
    row = []
    for j in range(1,11):
        row.append(i*j)
    table.append(row)
##
print(table)
table2 = [(i*j) for i in range(1,11) for j in range(1,11)]

#C(n,k) = n!/k! * (n-k)!
from math import factorial
def combo(n,k):
    return factorial(n) // (factorial(k)*factorial(n-k))

colomn = 10
pascal = [[combo(n,k) for k in range(n+1) ] for n in range(colomn+1)]
print(pascal)
# Nested loop
l1 = ['a', 'b', 'c', 'd', 'r', 'g']
l2 = ['x', 'y', 'z', 'w', 'g', 'a']

app = []
for i in l1:
    for j in l2:
        if i != j:
            app.append(i+j)

app2 = [i+j for i in l1 for j in l2 if i != j]
app2
app == app2

# equivalent to zip function
l1 = [1, 3, 4, 5, 7, 0, 9]
l2 = ['a', 'h', 'j', 'c']
list(zip(l1, l2))

#TODO : check the index
list(enumerate(l1))
result = []
for index_1, item_1 in enumerate(l1):
    for index_2, item_2 in enumerate(l2):
        if index_1 == index_2:
            result.append((item_1, item_2))

#
result2 = [(item_1, item_2)
            for index_1, item_1 in enumerate(l1)
            for index_2, item_2 in enumerate(l2)
            if index_1 == index_2]

print(result2)
##
if 'i' in globals():
    del i
##
