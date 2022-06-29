"""
You want to implement new kinds of context managers for use with the with statement.
"""

import time
from contextlib import contextmanager


@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}: {}'.format(label, end - start))


# Example use
with timethis('counting'):
    n = 10000000
    while n > 0:
        n -= 1


# Here is a slightly more advanced context manager that implements a kind of transaction on a list object:
@contextmanager
def list_transaction(orig_list):
    working = list(orig_list)
    yield working
    orig_list[:] = working


# The idea here is that changes made to a list only take effect if an entire code block runs
# to completion with no exceptions. Here is an example that illustrates:
"""
>>> items = [1, 2, 3]
>>> with list_transaction(items) as working:
...    working.append(4)
...    working.append(5)
...
>>> items
[1, 2, 3, 4, 5]
>>> with list_transaction(items) as working:
...     working.append(6)
...     working.append(7)
...     raise RuntimeError('oops')
...
Traceback (most recent call last):
File "<stdin>", line 4, in <module>
RuntimeError: oops
>>> items
[1, 2, 3, 4, 5]
>>>
"""
