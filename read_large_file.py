"""
How to read an 8GB file in Python with a computer that has 2GB of RAM?
This solution works for any large (and even larger) files.

When you open the file, all you need to do is use the file object as an iterator: while looping over this file object,
you'll be fetching one line at a time and the previous lines will be cleared from memory (i.e. they are garbage collected).

This way, the file will never be entirely loaded in memory and your processing will be done on the go.

"""


def process_line(line):
    pass


with open("./large_dataset.txt") as input_file:
    for line in input_file:
        process_line(line)
