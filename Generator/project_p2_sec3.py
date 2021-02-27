##
file_name = "/home/najmeh/PycharmProjects/pythonProject/deepdive2/part2" \
            "/project3/nyc_parking_tickets_extract.csv"
# if you have a big file, do not to overload the file content in memory
# instead with python we open the file to see first few lines

with open(file_name) as f:
    for _ in range(10):
        print(next(f))

with open(file_name) as f:
    column_header = next(f).strip('\n').split(',')
    sample_data = next(f).strip('\n').split(',')

from pprint import pprint
pprint(column_header)
pprint(sample_data)

# note data read back as a string
# NOTE, valid field name for namedtouple should not have any space in them
# they also can not start with number
column_header = [item.replace(' ', '_').lower() for item in column_header]
list(zip(column_header, sample_data))

from collections import namedtuple
Ticket = namedtuple('Ticket', column_header)

with open(file_name) as f:
    next(f)
    raw_data_file = (next(f))
print(raw_data_file)

##
def read_data():
    with open(file_name) as f:
        next(f)
        yield from f

# call generation function
raw_data = read_data()
for _ in range(5):
    print(next(raw_data))

# to clean the data lets start with writing some parsing functions
# in order to parse string to int, date/time/, correct_string

def parse_int(value, *, default = None):
    try:
        return int(value)
    except ValueError:
        return default

parse_int(10, default='N/A')
parse_int('hello', default='N/A')
from datetime import datetime
def parse_date(value, *, default = None):
    date_format = '%m/%d/%Y'
    try:
        return datetime.strptime(value, date_format).date()
    except ValueError:
        return default

parse_date("hello", default = 'Error, I/O')
parse_date('2/8/2000', default = 'Error I/O')

# For string, we need also take care of empty string
def parse_string(value, *, default = None):
    cleaned = value.strip().lower()  # strip put spaces
    if cleaned:
        return cleaned
    else:
        return default
parse_string('     Hello', default= 'N/A')
parse_string('      ', default = 'N/A')
column_header
#
from functools import partial
# an example from partial function
def func(u,v,w,x):
    return u*4 + v*3 + w*2 + x
p = partial(func,5,6,7)
print(p(5))
#
column_parsers = (parse_int, parse_string,
                  lambda x: parse_string(x, default= ''),
                  partial(parse_string, default = ''),
                  parse_date, parse_int,
                  partial(parse_string, default = ''), parse_string,
                  lambda x: parse_string(x, default = ' '))

# write a function to handle a single row
def row_parser(row):
    fields = row.strip('\n').split(',')
    parsed_data = (func(item) for func, item in zip(column_parsers, fields))
    return parsed_data

all_row = read_data() # read file, skip first line and return rest of the
# file
for _ in range(5):
    row = next(all_row)
    parsed_data = row_parser(row)
    pprint(list(parsed_data))

##
def parse_row(row, *, default=None):
    fields = row.strip('\n').split(',')
    # note that I'm using a list comprehension here,
    # since we'll need to iterate through the entire parsed fields
    # twice - one time to check if nothing is None
    # and another time to create the named tuple
    parsed_data = [func(field)
                   for func, field in zip(column_parsers, fields)]
    if all(item is not None for item in parsed_data):
        print(*parsed_data)
        return Ticket(*parsed_data)
    else:
        return default

rows = read_data()
for _ in range(5):
    row = next(rows)
    parsed_data = parse_row(row)
    print(parsed_data)

for row in read_data():
    parsed_row = parse_row(row)
    if parsed_row is None:
        pprint(list(zip(column_header, row.strip('\n').split(','))))
        # print(list(zip(column_header, row.strip('\n').split(','))),
        #        end='\n\n')

def parsed_data():
    for row in read_data():
        parsed = parse_row(row)
        if parsed:
            yield parsed
parsed_rows = parsed_data()
for _ in range(5):
    print(next(parsed_rows))

###############################################################################

from collections import namedtuple
from datetime import datetime
from functools import partial

file_name = 'nyc_parking_tickets_extract.csv'

with open(file_name) as f:
    column_headers = next(f).strip('\n').split(',')

column_names = [header.replace(' ', '_').lower()
                for header in column_headers]

Ticket = namedtuple('Ticket', column_names)


def read_data():
    with open(file_name) as f:
        next(f)
        yield from f


def parse_int(value, *, default=None):
    try:
        return int(value)
    except ValueError:
        return default


def parse_date(value, *, default=None):
    date_format = '%m/%d/%Y'
    try:
        return datetime.strptime(value, date_format).date()
    except ValueError:
        return default


def parse_string(value, *, default=None):
    try:
        cleaned = str(value).strip()
        if not cleaned:
            # empty string
            return default
        else:
            return cleaned
    except:
        return default


column_parsers = (parse_int,  # summons_number, default is None
                  parse_string,  # plate_id, default is None
                  partial(parse_string, default=''),  # state
                  partial(parse_string, default=''),  # plate_type
                  parse_date,  # issue_date, default is None
                  parse_int,  # violation_code
                  partial(parse_string, default=''),  # body type
                  parse_string,  # make, default is None
                  lambda x: parse_string(x, default='')  # description
                  )


def parse_row(row, *, default=None):
    fields = row.strip('\n').split(',')
    # note that I'm using a list comprehension here,
    # since we'll need to iterate through the entire parsed fields
    # twice - one time to check if nothing is None
    # and another time to create the named tuple
    parsed_data = [func(field)
                   for func, field in zip(column_parsers, fields)]
    if all(item is not None for item in parsed_data):
        return Ticket(*parsed_data)
    else:
        return default


def parsed_data():
    for row in read_data():
        parsed = parse_row(row)
        if parsed:
            yield parsed

###############################################################################
# part 2 Calculating Number of Violations by Car Make
makes_counts = {}

for data in parsed_data():
    if data.vehicle_make in makes_counts:
        makes_counts[data.vehicle_make] += 1
    else:
        makes_counts[data.vehicle_make] = 1

for make, cnt in sorted(makes_counts.items(),
                        key=lambda t: t[1],
                        reverse=True):
    print(make, cnt)

from collections import defaultdict

makes_counts = defaultdict(int)

for data in parsed_data():
    makes_counts[data.vehicle_make] += 1

for make, cnt in sorted(makes_counts.items(),
                        key=lambda t: t[1],
                        reverse=True):
    print(make, cnt)


def violation_counts_by_make():
    makes_counts = defaultdict(int)
    for data in parsed_data():
        makes_counts[data.vehicle_make] += 1

    return {make: cnt
            for make, cnt in sorted(makes_counts.items(),
                                    key=lambda t: t[1],
                                    reverse=True)
            }
