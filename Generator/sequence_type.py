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
# slicing, relies on indexing
#------------------------------------------
l = [11, 24, 36, 4, 85, 60, 73, 88, 93]
s = slice(0,3)
l[0:3]   #[11, 24, 36]
s.start, s.stop, s.step # (0, 3, None)
l[s]    #[11, 24, 36]
l[0:8:2]
start = None
l[start:4]
l[:5:2]
l[3:0:-1] # [4, 36, 24] attention: you wont get l[0]in this case
l[3::-1] # l[3::-1] #
t = slice(0,100, 2).indices(10)
t
range(*t)
list(range(*t))
start = 2
stop = 10
step = 2
length = 100
list(range(*slice(start, stop, step).indices(length))) # it will give you the indexes # [2, 4, 6, 8]
len(l), l.__len__()
l[2], l.__getitem__(s), l.__getitem__(slice(None, None, -1))

# Assignments in mutabale sequences
l = [1, 2, 3, 4, 5, 6, 7, 8]
l[1:3] = 'python' #[1, 'p', 'y', 't', 'h', 'o', 'n', 4, 5, 6, 7, 8]
# deletion is just special case of replacement with empty iterebale
l[2:4] = [] #[1, 2, 5, 6, 7, 8]
# or even
l[2:4] = ''  #[1, 2, 5, 6, 7, 8]
# we can also inseret iterabale to a mutabale sequence
l[2:2]  #[]
l[2:2] = 'hello'  #[1, 2, 'h', 'e', 'l', 'l', 'o', 3, 4, 5, 6, 7, 8]
# extended slices
l[0:5:2] = 'abc' #['a', 2, 'b', 4, 'c', 6, 7, 8]


#----------------------------------------------
# in place concatenation and repetition
#----------------------------------------------

l1 = [1, 2, 3, 4] # it is a mutabale sequence
l2 = [5, 6, 7, 8] # it is a mutabale sequence
id(l1), id(l2)
l1 = l1 + l2   # regular concatenation
id(l1)
l1 += l2
id(l1)


my_list = [1, 2, 3,4, 5, 6]
my_list.__getitem__(slice(None, None, -1))  # we can get a slice out of it
result = [e**2 for e in my_list]
print(result)
##
index = 0
while True:
    try:
        item = my_list.__getitem__(index)
    except IndexError:
        break
    print(item**2)
    index += 1

##
class Silly:
    def __init__(self, n):
        self.n = n

    def __len__(self):
       # print('Method __len__ is called')
        return self.n

    def __getitem__(self, value):
        print(f'you requested item at {value}')
        return 'This is a silly element'

silly = Silly(100)
len(silly)
silly.__getitem__(200)


##
from functools import lru_cache
@lru_cache(2**10)
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
fib(100000)

##
# create a fibonacci sequence of len n
class Fib:
    from functools import lru_cache
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, s):
        if isinstance(s, int):
            if s < 0:
                s = self.n + s
            if s < 0 or s >= self.n:
                raise IndexError
            else:
                return Fib._fib(s)
    @staticmethod
    @lru_cache(2 ** 10)
    def _fib(n):
        if n < 2:
            return 1
        else:
            return Fib._fib(n - 1) + Fib._fib(n - 2)
##
fib = Fib(10)
fib[3], fib[9], fib[-2], fib[0:4]  # get item from a list

##
class Fib:
    from functools import lru_cache
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, s):
        if isinstance(s, int):  # s: the element of given index
            if s < 0:
                s = self.n + s
            if s < 0 or s >= self.n:
                raise IndexError
            else:
                return Fib._fib(s)
        else:    # in case of list
            start, stop, step = s.indices(self.n)
            rng = range(start, stop, step)
            return [Fib._fib(i) for i in rng]

    @staticmethod
    @lru_cache(2 ** 10)
    def _fib(n):
        if n < 2:
            return 1
        else:
            return Fib._fib(n - 1) + Fib._fib(n - 2)
obj = Fib(20)
print(list(obj))
obj.__getitem__(-15)
obj[0:3]
obj.__getitem__(8)
##
class Myclass:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        """It return repr(self)"""
        return f'-----> {self.name}'

    def __add__(self, other):
        return Myclass(self.name + other.name)
        # MYCLASS will just call the __repr__

    def __mul__(self, n):
        return (self.name * n)

    def __rmul__(self, n):
        return Myclass(n * self.name)

    def __imul__(self, n):
        self.name *= n
        return self

    def __contains__(self, item):
        return item in self.name


##
c1 = Myclass('obj1')
c2 = Myclass('obj2')

c1.__add__(c2)
c1 + c2
c3 = Myclass(4)
c4 = Myclass(5)
c3 + c4
result = c1 * 2
print(result)
c1.__mul__(3)
c1 *= 10
7 * c1
'j' in c1
l = [1, 2, 3, 4, 5, 6]
5 in l
##
# ---------------------------------------------------------
# custom sequence (part 2)
#----------------------------------------------------------
import numbers
class Point:
    def __init__(self, x, y):
        if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
            self._pt=(x, y)
        else:
            raise TypeError('ATT: Point coordinates must be real number')

    def __repr__(self, *args, **kwargs):
        return f'Point(x={self._pt[0]}, y={self._pt[1]})'

    def __len__(self):
        return len(self._pt)

    def __getitem__(self, item):
        return self._pt[item]


pt =Point(3,8)
pt
x, y = pt
x
y


