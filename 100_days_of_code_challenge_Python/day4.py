"""
Write a Python program that prints the first and last three characters of the string s as a single string.
If the string has less than six characters, print an empty string (blank output)
"""

s = 'erful'

print(s[0:3])
print(s[-3:])
##
def get_string_slice(x):
    if len(x) >= 6:
        print('The first three charachter of "{0}" is -'.format(x),x[0:3],'- and the last three charachter is', '-',x[-3:],'-')
    else:
        print("")

get_string_slice('amazing')