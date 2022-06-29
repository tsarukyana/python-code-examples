"""
You need to serialize a Python object into a byte stream so that you can do things such
as save it to a file, store it in a database, or transmit it over a network connection.
"""
import pickle

data = ...  # Some Python object
f = open('somefile', 'wb')
pickle.dump(data, f)

# To dump an object to a string, use pickle.dumps():

s = pickle.dumps(data)
# To re-create an object from a byte stream, use either the pickle.load() or pick
# le.loads() functions. For example:

# Restore from a file
f = open('somefile', 'rb')
data = pickle.load(f)
print(data)

# Restore from a string
data = pickle.loads(s)
print(data)
