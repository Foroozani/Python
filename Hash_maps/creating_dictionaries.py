# creatin dictionaries
from pprint import pprint
hash((1,2,3))
dict = {'a': 1, 'b':3, 'x':7}
dict.items()
dict.keys()
dict.values()
#----------------------------------------------

def fn_add(a, b):
    return a + b

def fn_div(a):
    return 1 / a

def fn_mult(a, b):
    return a * b

# create a dictionaries with functions
funcs = {fn_add: (2,4), fn_div: (3, ), fn_mult: (5, 6)}
for func in funcs:
    print(f'--->',func)

for func in funcs:
    results = func(*funcs[func])
    print(results)

for key, value in funcs.items():
    print('The key is:  ', key)
    print('The value is:', value)

for key, value in funcs.items():
    result = key(*value)
    print(result)

# creating dictionaries using literal
key = ['a', 'b', 'c']
value = [1, 2 ,3]
dic = {}
for k, v in zip(key,value):
    dic[k] = v


# dictionary comprehension
dict2 = {k:v for k,v in zip(key, value)}
dict2

d = dict(zip('abc', range(1, 4)))
d.get('b')
d.get('python','the key not exist')


"""dictionary.get(keyname, value) 
keyname: Required. The keyname of the item you want to return the value from
value: A value to return if the specified key does not exist.Default is None"""

text = 'Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, explicabo. Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam est, qui dolorem ipsum, quia dolor sit amet consectetur adipisci[ng] velit, sed quia non-numquam [do] eius modi tempora inci[di]dunt, ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit, qui in ea voluptate velit esse, quam nihil molestiae consequatur, vel illum, qui dolorem eum fugiat, quo voluptas nulla pariatur?'
# count the number of charachter in this string
counts = dict()
for c in text:
    counts[c] = counts.get(c, 0) + 1
pprint(counts)
# strip out the space and make all letters lower case
counts = dict()
for char in text:
    key = char.lower().strip()
    if key:
        counts[key] = counts.get(key,0) + 1
pprint(counts)

