import re

greeting = 'hello Hi there, how do you do ?'

re.findall('hello', greeting)
re.findall('h', greeting, re.IGNORECASE)
re.findall(r'.', greeting)
