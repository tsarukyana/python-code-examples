d = {"foo": 1}

# bad practice

f = open("./data.csv", "wb")
f.write("some data")

v = d["bar"]  # KeyError
# f.close() never executes which leads to memory issues

f.close()

# good practice

with open("./data.csv", "wb") as f:
    f.write("some data")
    v = d["bar"]
# python still executes f.close() even if the KeyError exception occurs
