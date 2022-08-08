"""
 Write a Python program to check whether a specified value is contained in a group of values. Go to the editor
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
"""

#
# data = [1, 3, 9, 20, -1, 89]
# def check_value(a):
#     for i in data:
#         if i == a:
#             print('found')
#         else:
#             print('not found')
# check_value(3)

def check_value2(a):
    for value in data:
        if value == a:
           return 'value found'
    return 'Given value is not in the list'

check_value2(3)
check_value2(90)