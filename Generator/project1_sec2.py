"""
We need to create a Polygon class with the following properties:
    number of edges
    number of sides
    interior angle (in degrees)
    side length
    apothem
    surface area
    perimeter
    supports equality based on number of vertices and circumradius
    supports > based on number of vertices
"""
##
import math
class Polygon:
    """number of vertices n - passed to the initializer
    circumradius R - passed to the initializer"""
    def __init__(self, n, R):
        self._n = n
        self._R = R

    def __repr__(self):
        return f'Polygon(n={self._n}, R={self._R})'

    @property
    def count_vertices(self):
        return self._n

    @property
    def count_edges(self):
        return self._n

    @property
    def circumradius(self):
        return self._R

    @property
    def interior_angle(self):
        return (self._n - 2) * (180/ self._n)

    @property
    def side_length(self):
        return 2 * self._R * math.sin(math.pi/ self._n)

    @property
    def apothem(self):
        return self._R * math.cos(math.pi / self._n)

    @property
    def area(self):
        return self._n * self.side_length * self.apothem

    @property
    def perimeter(self):
        return self._n * self.side_length




##
assert 1 == 1
assert 1 > 10, 'This is not correct'
##

test_polygan()
##
def test_class_value():
    abs_tol = 0.001
    rel_tol = 0.001

    n = 3
    R = 1
    p = Polygon(n, R)
    assert str(p) == 'Polygon(n=3, R=1)', f'actual: {str(p)}'
    assert p.count_vertices == n, (f'actual: {p.count_vertices},'
                                   f' expected: {n}')
    assert p.count_edges == n, f'actual: {p.count_edges}, expected: {n}'
    assert p.circumradius == R, f'actual: {p.circumradius}, expected: {n}'
    assert p.interior_angle == 60, (f'actual: {p.interior_angle},'
                                    ' expected: 60')

    n = 4
    R = 1
    p = Polygon(n, R)
    assert p.interior_angle == 90, (f'actual: {p.interior_angle}, '
                                    ' expected: 90')
    assert math.isclose(p.area, 2,
                        rel_tol=abs_tol,
                        abs_tol=abs_tol), (f'actual: {p.area},'
                                           ' expected: 2.0')

test_class_value()

##
import math
class Polygon:
    """number of vertices n - passed to the initializer
    circumradius R - passed to the initializer"""
    def __init__(self, n, R):
        if n < 3:
            raise ValueError('Polygo must 3 edges')
        self._n = n
        self._R = R

    def __repr__(self):
        return f'Polygon(n={self._n}, R={self._R})'

    @property
    def count_vertices(self):
        return self._n

    @property
    def count_edges(self):
        return self._n

    @property
    def circumradius(self):
        return self._R

    @property
    def interior_angle(self):
        return (self._n - 2) * (180/ self._n)

    @property
    def side_length(self):
        return 2 * self._R * math.sin(math.pi/ self._n)

    @property
    def apothem(self):
        return self._R * math.cos(math.pi / self._n)

    @property
    def area(self):
        return self._n * self.side_length * self.apothem

    @property
    def perimeter(self):
        return self._n * self.side_length

    def __eq__(self, other):
        if isinstance(other, Polygon):
            return (self._n, self._R) == (other._n, other._R)
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Polygon):
            return self.count_vertices > other.count_vertices
            #return (self.area > other.area)
        else:
            return NotImplemented

p1 = Polygon(3, 10)
p2 = Polygon(10, 10)

p1 == p2
p1 > p2
p1 < p2
p1 != p2
p1.area
p2.area

