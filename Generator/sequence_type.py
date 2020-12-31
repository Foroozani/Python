# Sequence type
# Strings, tuples are immutable - we can access but not modify the content of the sequence:
# here are three squence types, list, tuple and a string
l = [1, 2, 3, 4, 1, 3, 4, 5, 8, 6, 9, 0]
t = (1, 2, 3, 4)
s = 'python'

l[0], s[3], t[2]

for _ in l:
    print(_)

# a set
e = {10, 20, 50, 60, 20}
e[1]  # TypeError: 'set' object does not support indexing

for _ in e:
    print(_)   #10 20 50 60 you see the ordering is not supported

# in and not in operator
2 in l    # True
'a' in s  # False
100 not in range(0,20)  # True

[1,2,4] + [2, 3, 4]    #  [1, 2, 4, 2, 3, 4] the order is maintained

# I define an iterable of string type
s2 = "hello I am ok how are you"
list(enumerate(l))
list(enumerate(s2))

# return me the index
s2.index('o')    # 4
s2.index('o',5)  #looking after position 5
l.index(1)    # 0
l.index(1, 3) # 4
l.index(50)   # exeption, ValueError
l.index(1, 8)  # exeption, ValueError

# slicing is always return a new object
l2 = l[:]
l2 is l  # False, they have two different memory address
l[-1]   #0
l[5:0:-1], l[::-1] , l[::2], l[::-2]# az akhar be aval ba step -1

# Mutabale sequance type
id(l)
l[0] = 6
# replace
l[0:2] = [80, 50, 60, "a"]
l    # [80, 50, 60, 'a', 3, 4, 1, 3, 4, 5, 8, 6, 9, 0]
# you can add only one element to the object using 'append' function 
l.append(100)
l.extend(s)
result = l.pop(0)
del l[0:2] #it delet but does not retun any value

#-----------------------------------------
#   Sequence copies
#-----------------------------------------
# 1) shallow copy
# 1)
l1 = [1, 2, 3, 4, 5, 6, 7]

l1_copy = []
for item in l1:
    l1_copy.append(item)

print(l1_copy, l1)
print(id(l1_copy), id(l1)) # The memory address of these container are differ

#2) using list comprehension
l1_copy = [item for item in l1]
l1_copy

# 3) copy method, list is mutabale sequence
l1_copy = l1.copy()
l1_copy
# 4) list function
l1_copy = list(l1)
l1_copy
# 5) slicing
l1_copy = l1[:]
l1_copy

#------------------------------------------
# slicing
#------------------------------------------
















