"""
You need to create an instance, but want to bypass the execution of the __init__()
method for some reason.
"""


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


d = Date.__new__(Date)
"""
>>> d
<__main__.Date object at 0x1006716d0>
>>> d.year
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'Date' object has no attribute 'year'
>>>
"""

data = {'year': 2012, 'month': 8, 'day': 29}

for key, value in data.items():
    setattr(d, key, value)

print(d.year)
print(d.month)
print(d.day)

"""
from time import localtime


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        
    @classmethod
    def today(cls):
        d = cls.__new__(cls)
        t = localtime()
        d.year = t.tm_year
        d.month = t.tm_mon
        d.day = t.tm_mday
        return d
"""