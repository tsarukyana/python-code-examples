import pandas as pd

bikes = ["bajaj", "tvs", "herohonda", "kawasaki", "bmw"]
cars = ["lamborghini", "masserati", "ferrari", "hyundai", "ford"]
d = {"cars": cars, "bikes": bikes}

df = pd.DataFrame(d)
a = [10, 20, 30, 40, 50]
df.index = a

print(df.loc[10])

