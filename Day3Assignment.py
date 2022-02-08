# DAY3 ASSIGNMENT OF PYTHON
# FROM A DICT, PRINT THE  KEY WHOSE VALUE IS MAXIMUM
from collections import Counter
s = input("Enter the string value :")
a = s.islower()
d = dict(Counter(s))
print(d)
print(max(d, key=d.get))
