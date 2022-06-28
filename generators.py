def repeat(n, message):
    for _ in range(n):
        yield message


repeat_hello_five_times = repeat(5, "hello")

"""

>>> for message in repeat_hello_five_times:
        print(message)

"hello"
"hello"
"hello"
"hello"
"hello"

>>> repeat_hello_five_time = ("hello" for _ in range(5))
>>> repeat_hello_five_times
<generator object <genexpr> at 0x7fb64f2362d0>

>>> for message in repeat_hello_five_times:
        print(message)

"hello"
"hello"
"hello"
"hello"
"hello"

"""
