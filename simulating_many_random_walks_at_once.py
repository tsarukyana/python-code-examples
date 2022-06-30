"""
If your goal was to simulate many random walks, say 5,000 of them, you
can generate all the random walks with minor modifications to the
preceding code. If passed a 2-tuple, the numpy.random functions will
generate a two-dimensional array of draws, and we can compute the
cumulative sum for each row to compute all 5,000 random walks in one
shot:
"""
import numpy as np

n_walks = 5000

n_steps = 1000

draws = np.random.randint(0, 2, size=(n_walks, n_steps))  # 0 or 1

steps = np.where(draws > 0, 1, -1)

walks = steps.cumsum(1)
print(walks)

# Now, we can compute the maximum and minimum values obtained over of
# the walks:
max_walks = walks.max()
print(max_walks)

min_walks = walks.min()
print(min_walks)

# Out of these walks, let’s compute the minimum crossing time to 30 or –30.
# This is slightly tricky because not all 5,000 of them reach 30. We can check
# this using any method:
hits30 = (np.abs(walks) >= 30).any(1)
print(hits30)

sum_hints30 = hits30.sum()  # Number that hit 30 or -30
print(sum_hints30)

# We can use this boolean array to select out the rows of walks that actually
# cross the absolute 30 level and call argmax across axis 1 to get the
# crossing times:
crossing_times = (np.abs(walks[hits30]) >= 30).argmax(1)
print(crossing_times)

# Lastly, we compute the average minimum crossing time:
average_min_crossing_time = crossing_times.mean()
print(average_min_crossing_time)
