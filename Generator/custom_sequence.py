##
"""We can call the __methods and create our own custom functions"""
class Myclass:
    def __init__(self, name):
        self.name = name # this object has a property called "name"

    def __repr__(self):
        """It return repr(self)"""
        return f'-----> {self.name}'

    def __add__(self, other):
        """This is custom add function, symbol (+) will call this method"""
        return self.name + other.name     # add two properties

    def __iadd__(self, other):
         self.name += other.name    # other is instance of the class
         return self

    def __mul__(self, n):   #symbol is *
        """This is custom multiplication function, one can use (*) symbol to call the method"""
        return (self * n)  #here "n" is not instance of the class ***

    def __rmul__(self, n):
        return self.__mul__(n)
        #OR return n * self.name

    def __imul__(self, n):   # symbol is *=
        """This is in-place multiplication, one can use *= to call this
        method """
        self.name *= n
        return self

    def __contains__(self, item):
        return item in self.name

##
c1 = Myclass(2) # create an object has Myclass properties
c2 = Myclass(3)
c3 = Myclass('object1') # here we
c4 = Myclass('object2')
c1.__add__(c2)
result= c1 + c2
c3 + c4
print(result)
c1 += c2
c1
c1 * c2
c1 *= c2
c1 * 7   # ***
del c1
c3 * 4

##
from collections import namedtuple
Point = namedtuple("Point", 'x y')

p1 = Point(3, 6)
p1
x, y = p1

import numbers
isinstance(10.8, numbers.Real)
##
# lets define our point class
class Point:
    def __init__(self, x, y):
        # lets make sure x, y are real numbers
        if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
            self._pt = (x,y)
        else:
            raise TypeError("Najmeh!!! point coordinate must be real values")

    # representation is how we mimic how we re-create the object
    def __repr__(self):
        return f'Point(x ={self._pt[0]}, y ={self._pt[1]}'

##
pt1 = Point(3, 7j)
pt1 = Point(3, 5)
# unpack point
x, y = pt1 # TypeError: 'Point' object is not iterable, this means we should
# make point a sequence type
##
class Point:
    def __init__(self, x, y):
        # lets make sure x, y are real numbers
        if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
            self._pt = (x,y)
        else:
            raise TypeError("Caveat!!! point coordinate must be real values")

    # representation is how we mimic how we re-create the object
    def __repr__(self):
        return f'Point(x ={self._pt[0]}, y ={self._pt[1]})'

    def __len__(self):
        return len(self._pt)

    def __getitem__(self, item):
        return self._pt[item]

pt1 = Point(3, 5)
pt1
x, y = pt1
x , y

##
class Polygon:
    def __init__(self, *pts):
        if pts:
            self._pts = [Point(*pt) for pt in pts]
        else:
            self._pts = []

    def __repr__(self):
        pts_str = ', '.join([str(pt) for pt in self._pts])
        return f'Polygon({pts_str})'

    def __len__(self):
        return len(self._pts)

    def __getitem__(self, s):
        return self._pts[s]

p = Polygon((0,0), (1,1))
p
# by using representation we can create another polygon
p1 = Polygon(Point(x =0, y =0), Point(x =1, y =1))
p1[1]
p[0:2], p[::-1]

##
# now let us concatinate to Polygon


class Polygon:
    def __init__(self, *pts):
        if pts:
            self._pts = [Point(*pt) for pt in pts]
        else:
            self._pts = []

    def __repr__(self):
        pts_str = ', '.join([str(pt) for pt in self._pts])
        return f'Polygon({pts_str})'

    def __len__(self):
        return len(self._pts)

    def __getitem__(self, s):
        return self._pts[s]

    def __add__(self, other):
        if isinstance(other, Polygon):
            new_pts = self._pts + other._pts
            return Polygon(*new_pts)
        else:
            raise TypeError('can only concatenate with another Polygon')

p1 = Polygon((0,0), (1,1))
p2 = Polygon((2,2), (3,3))
print(id(p1), p1)
print(id(p2), p2)
p1 + p2