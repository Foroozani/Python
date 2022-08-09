
"""
Write a Python program to valid an IP address.
"""

import re
ip_regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
def check_ip_address(user_ip):
   if(re.search(ip_regex, user_ip)):
       return "Valid Ip address"
   else:
       return "Invalid Ip address"
user_ip = "10.0.0.0"

print("\n",user_ip,"->",check_ip_address(user_ip))