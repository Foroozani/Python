##
# sort the value of your dictonary
composers = {'Johann': 65, 'Ludwig': 56, 'Frederic': 39, 'Wolfgang': 35}
d=list(composers.values())


composers.items()
# will give an iterable
# sorted function take an iterable
sorted([1,3, 4, 8, 0 ,4, 1], reverse = True)
"""
Return a new list containing all items from the iterable in ascending order.

A custom key function can be supplied to customize the sort order, and the
reverse flag can be set to request the result in descending order.
"""

sorted(composers.items(), key= lambda arg: arg[1]) # take a value, which is
# the second element of tuple
# the output is a list, we want to have a dictionary so lets write a function
#------------------------------------------------------------------------------
def sort_dic_by_value(dic):
    new_dic = {k: v
         for k, v in sorted(dic.items(), key= lambda arg: arg[1])
    }
    return new_dic
sort_dic_by_value(composers)

# an alternative approach, because we are not oin trough a loop

def sorted_dic_by_value(dic):
    dict(sorted(dic.items(), key= lambda arg: arg[1]))

#
d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'b': 20, 'c': 30, 'y': 40, 'z': 50}
d = {'b': (2, 20), 'c': (3, 30)}

d1_keys = d1.keys()
d1_keys
d2_keys = d2.keys()
d1_keys & d2_keys
d1['b'], d2['b']
d1['c'], d2['c']

def intersect(d1, d2):
    d1_keys = d1.keys()
    d2_keys = d2.keys()
    keys = d1_keys & d2_keys
    d = {k: (d1[k], d2[k]) for k in keys}
    return d
intersect(d1, d2)

#------------------------------------------------------------------------------
##
#You have text data spread across multiple servers. Each server is able to
# analyze this data and return a dictionary that contains words and their frequency.
# combine this data to create a single dictionary that contains all the words
# and their combined frequencies from all these data sources.

d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
d2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}
d3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 1}
# result should be like this
d = {'python': 17,
     'javascript': 15,
     'java': 13,
     'c#': 12,
     'c++': 10,
     'go': 9,
     'erlang': 5,
     'haskell': 2,
     'pascal': 1}

def merge_dic(*dicts):
    unsorted = {}
    for d in dicts:
        for k, v in d.items():
            unsorted[k] = unsorted.get(k, 0) + v

    # create a dictionary sorted by value
    return dict(sorted(unsorted.items(), key=lambda e: e[1], reverse=True))
merge_dic(d1, d2, d3)

#--------------------------------------------------------------------------
n1 = {'employees': 100, 'employee': 5000, 'users': 10, 'user': 100}
n2 = {'employees': 250, 'users': 23, 'user': 230}
n3 = {'employees': 150, 'users': 4, 'login': 1000}

result = {'employee': (5000, 0, 0),
          'user': (100, 230, 0),
          'login': (0, 0, 1000)}

union = n1.keys() | n2.keys() | n3.keys()
intersection = n1.keys() & n2.keys() & n3.keys()

union, intersection, union - intersection

def identify(node1, node2, node3):
    union = node1.keys() | node2.keys() | node3.keys()
    intersection = node1.keys() & node2.keys() & node3.keys()
    relevant = union - intersection
    result = {key: (node1.get(key, 0),
                    node2.get(key, 0),
                    node3.get(key, 0))
              for key in relevant}
    return result