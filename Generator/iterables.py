#-------------------------------------------------------
#    iterating collections
#-------------------------------------------------------
##
class CityIterator:
    def __init__(self, city_obj):
        # cities is an instance of Cities
        print('Calling CityIterator __init__')
        self._city_obj = city_obj
        self._index = 0

    def __iter__(self):
        print('Calling CitiyIterator instance __iter__')
        return self

    def __next__(self):
        print('Calling __next__')
        if self._index >= len(self._city_obj):
            raise StopIteration
        else:
            item = self._city_obj._cities[self._index]
            self._index += 1
            return item
##
class Cities:
    def __init__(self):
        self._cities = ['New York', 'Newark', 'New Delhi', 'Newcastle']

    def __len__(self):
        return len(self._cities)

    def __iter__(self):
        print('Calling Cities instance __iter__')
        return CityIterator(self)

##
cities = Cities()

for city in cities:
    print(city)
##
class Cities:
    def __init__(self):
        self._cities = ['New York', 'Newark', 'New Delhi', 'Newcastle']

    def __len__(self):
        return len(self._cities)

    def __getitem__(self, s):
        print('getting item...')
        return self._cities[s]

    def __iter__(self):
        print('Calling Cities instance __iter__')
        return self.CityIterator(self)

    class CityIterator:
        def __init__(self, city_obj):
            # cities is an instance of Cities
            print('Calling CityIterator __init__')
            self._city_obj = city_obj
            self._index = 0

        def __iter__(self):
            print('Calling CitiyIterator instance __iter__')
            return self

        def __next__(self):
            print('Calling __next__')
            if self._index >= len(self._city_obj):
                raise StopIteration
            else:
                item = self._city_obj._cities[self._index]
                self._index += 1
                return item

cities = Cities()
cities[0]
next(iter(cities))
cities = Cities()

for city in cities:
    print(city)
##
file_name = "/home/najmeh/PycharmProjects/pythonProject/deepdive2/cars.csv"
with open(file_name) as file:
    row_index = 0
    for line in file:
        if row_index == 0:
            # header file
            header = list(line.strip('\n').split(';'))
            print('File header is:', header)
        elif row_index == 1:
            # second line
            data_type = list(line.strip('\n').split(';'))
            print('data type is:', data_type)
        else:
            # third line
            data = line.strip('\n').split(';')
            print('data:', data)
        row_index += 1
##
from collections import namedtuple
cars = []
with open(file_name) as file:
    row_index = 0
    for line in file:
        if row_index == 0:
            # header file
            header = list(line.strip('\n').split(';'))
            print('File header is:', header)
            Car = namedtuple('Car', header)
        elif row_index == 1:
            # second line
            data_type = list(line.strip('\n').split(';'))
            print('data type is:', data_type)
        else:
            # third line
            data = line.strip('\n').split(';')
            #print('data:', data)
            car = Car(*data)
            cars.append(car)
        row_index += 1

from pprint import pprint
pprint(cars)
# Next we need to fix data type things
def cast(data_type, value):
    if data_type == 'DOUBLE':
        return float(value)
    elif data_type == 'INT':
        return int(value)
    else:
        return str(value)
##
def cast_row(data_type, data_row):
    return[
        cast(data_type, value)
        for data_type, value in zip(data_type, data_row)]

##
from collections import namedtuple
cars = []
with open(file_name) as file:
    row_index = 0
    for line in file:
        if row_index == 0:
            # header file
            header = list(line.strip('\n').split(';'))
            print('File header is:', header)
            Car = namedtuple('Car', header)
        elif row_index == 1:
            # second line
            data_type = list(line.strip('\n').split(';'))
            print('data type is:', data_type)
        else:
            # third line
            data = line.strip('\n').split(';')
            data = cast_row(data_type, data)
            car = Car(*data)
            cars.append(car)
        row_index += 1

pprint(cars)
##
# using iterators directly, more cleaner
from collections import namedtuple
cars = []

with open('cars.csv') as file:
    file_iter = iter(file)
    headers = next(file_iter).strip('\n').split(';')
    Car = namedtuple('Car', headers)
    data_types = next(file_iter).strip('\n').split(';')

    for line in file_iter:
        data = line.strip('\n').split(';')
        data = cast_row(data_types, data)
        car = Car(*data)
        cars.append(car)
##
# simply skip 2 lines, we read the file line by line, dont need to load it
# in memory all at once
origins = set()
with open(file_name) as f:
    next(f)
    next(f)
    for row in f:
        origin = row.strip('\n').split(';')[-1]
        origins.add(origin)
print(origins)
