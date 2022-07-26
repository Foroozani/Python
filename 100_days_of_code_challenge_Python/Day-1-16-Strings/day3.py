"""
Write a Python Program that prints the reversed version of a string.
The program must preserve uppercase and lowercase letters.
"""

s = 'Hello'
print(s[::-1])
##
def reverse_a_string(x):
    reversed_word = x[::-1]
    return reversed_word

reverse_a_string('hello word')
##
"""
Write a Python Program that prints the reversed version of a string with charachter '-' in between.
The program must preserve uppercase and lowercase letters.
"""
# reversed(sequence)

def reverse_a_string_with_charachter(x):
    reversed_word = "-".join(reversed(x))
    return reversed_word

reverse_a_string_with_charachter('hello test')
