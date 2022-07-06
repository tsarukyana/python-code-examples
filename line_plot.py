"""
A line plot is a chart that displays a line between two variables. It has a sequence of data
points joined by a segment:
"""
# Add the essential library matplotlib
import matplotlib.pyplot as plt

# create the data
x = [1, 3, 5, 7, 9, 11]
y = [10, 25, 35, 33, 41, 59]

# Draw the line chart
plt.plot(x, y)

# Append the label on X-axis
plt.xlabel("X-label")

# Append the label on X-axis
plt.ylabel("Y-label")

# Append the title to chart
plt.title("Line Chart Sample")

# Display the chart
plt.show()

"""
In the preceding line plot program, the plot() function takes x-axis and y-axis values.
"""
