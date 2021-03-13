# custom JSON Serialization
##
from datetime import datetime
import json

current = datetime.now()
current
json.dumps(current) #TypeError: Object of type datetime is not JSON serializable
str(current)   #'2021-03-13 08:44:20.619371', we need to change the # format
# the most common format is the ISO 8601, YYYY-MM-DDTHH:MM:SS
# strftime — Format a local time/date according to locale settings
# https://www.php.net/manual/en/function.strftime.php
def format_to_ISO(dt):
    """This function change time to custom format YYYY-MM-DDTHH:MM:SS
    we can also set the offset +/- """
    return dt.strftime('%Y-%m-%dT%H:%M:%S')

print(format_to_ISO(current))
log_record = {'time': datetime.utcnow().isoformat(), 'message': 'testing'}
log_record = {'time': format_to_ISO(datetime.now()), 'message': 'testing date time format'}
print(log_record)
# Now we can encode it
print(json.dumps(log_record, indent=2))
json.dumps(log_record, default=format_to_ISO)
##
def custom_json_formatter(arg):
    if isinstance(arg, datetime):
        return arg.isoformat()
    elif isinstance(arg, set):
        return list(arg)
log_record = {
    'time': datetime.utcnow(),
    'message': 'Testing...',
    'other': {'a', 'b', 'c'}
}
json.dumps(log_record, default=custom_json_formatter)
##
#-------------------------------------------------------------------------------
def custom_json_formatter(arg):
    if isinstance(arg, datetime):
        return arg.isoformat()
    elif isinstance(arg, set):
        return list(arg)
    else:
        try:
            return arg.toJSON()
        except AttributeError:
            try:
                return vars(arg)
            except TypeError:
                return str(arg)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.create_dt = datetime.utcnow()

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

    def toJSON(self):
        return vars(self)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'
##
#------------------------------------------------------------------------------
p = Person('Python', 27)
p.toJSON()
pt1 = Point(10, 10)
vars(pt1)

log_record = dict(time=datetime.utcnow(),
                  message='Created new point',
                  point=pt1,
                  created_by=p)
print(json.dumps(log_record, default=custom_json_formatter, indent=2))

#==============================================================================
# let's re-write our custom json formatter using the generic single dispatch decorator
#Our default approach is going to first try to use toJSON, if not it will try to
# use vars, and it that still fails we'll use the string representation,
# whatever that happens to be
##
from functools import singledispatch
@singledispatch
def json_format(arg):
    print(arg)
    try:
        print('\ttrying to use toJSON...')
        return arg.toJSON()
    except AttributeError:
        print('\tfailed - trying to use vars...')
        try:
            return vars(arg)
        except TypeError:
            print('\tfailed - using string representation...')
            return str(arg)
@json_format.register(datetime)
def _(arg):
    return arg.isoformat()
@json_format.register(set)
def _(arg):
    return list(arg)
# @json_format.register(Decimal)
# def _(arg):
#     return f'Decimal({str(arg)})'
print(json.dumps(log_record, default=json_format, indent=2))
##


print(json.dumps(dict(pt = Point(Person('Python', 27), 2+2j)),
          default=json_format, indent=2))

#==============================================================================
# JSON ENCODER class
#==============================================================================
##
import json

default_encoder = json.JSONEncoder()
default_encoder.encode([1, 2, 3])
import json
from datetime import datetime

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, arg):
        if isinstance(arg, datetime):
            return arg.isoformat()
        else:
            super().default(arg)

custom_encoder = CustomJSONEncoder()
custom_encoder.encode(True)
custom_encoder.encode(datetime.utcnow())


#=============================================================================
# Custom JSOn Decoding class
#==============================================================================

j = '''
    {
        "a": 100,
        "b": [1, 2, 3],
        "c": "python",
        "d": {
            "e": 4,
            "f": 5.5
        }
    }
'''

class CustomDecoder(json.JSONDecoder):
    def decode(self, arg):
        print("decode:", type(arg), arg)
        return "a simple string object"


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'

j_points = '''
{
    "points": [
        [10, 20],
        [-1, -2],
        [0.5, 0.5]
    ]
}
'''

j_other = '''
{
    "a": 1,
    "b": 2
}
'''

class CustomDecoder(json.JSONDecoder):
    def decode(self, arg):
        if 'points' in arg:
            obj = json.loads(arg)
            return "parsing object for points"
        else:
            return super().decode(arg)

json.loads(j_points, cls=CustomDecoder)
json.loads(j_other, cls=CustomDecoder)