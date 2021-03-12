# # JSON is a natural fit for serializing and deserializing python dictionaries
# JSON keys must be string
# JSON value types are limited
from pprint import pprint
import json
d1 = {'a': 100, 'b': 200}
d1_json = json.dumps(d1, indent=2)
type(d1_json)
print(d1_json)
d2 = json.loads(d1_json)
##
#------------------------------------------------------------------------------
d_json = '''
{
    "name": "John Cleese",
    "age": 82,
    "height": 1.96,
    "walksFunny": true,
    "sketches": [
        {
        "title": "Dead Parrot",
        "costars": ["Michael Palin"]
        },
        {
        "title": "Ministry of Silly Walks",
        "costars": ["Michael Palin", "Terry Jones"]
        }
    ],
    "boring": null    
}
'''

#deserialize this JSON string:
d = json.loads(d_json)
pprint(d)  #null --> None
##
#------------------------------------------------------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

    def toJSON(self):
        return dict(name=self.name, age=self.age)

p = Person('John', 82)
p.toJSON()  #{'name': 'John', 'age': 82}
# Now we can serialize it as follows:
print(json.dumps({"john": p.toJSON()}, indent=2))
