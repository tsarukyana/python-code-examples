from functools import reduce

sequences = [5, 8, 10, 20, 50, 100]
sum = reduce(lambda x, y: x + y, sequences)

print(sum)
