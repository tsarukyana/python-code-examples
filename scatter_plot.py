"""
Scatter plots draw data points using Cartesian coordinates to show the values of numerical
values. They also represent the relationship between two numerial values. We can create a
scatter plot in Matplotlib using the scatter() function, as follows:
"""
# Add the essential library matplotlib
import matplotlib.pyplot as plt

# create the data
x = [1, 3, 5, 7, 9, 11]
y = [10, 25, 35, 33, 41, 59]

# Draw the scatter chart
plt.scatter(x, y, c='blue', marker='*', alpha=0.5)

# Append the label on X-axis
plt.xlabel("X-label")

# Append the label on X-axis
plt.ylabel("Y-label")

# Add the title to graph
plt.title("Scatter Chart Sample")

# Display the chart
plt.show()

"""
In the preceding scatter plot, the scatter() function takes x-axis and y-axis values. In our
example, we are plotting two lists: x and y. We can also use optional parameters such as c
for color, alpha for the transparency of the markers, ranging between 0 and 1, and marker
for the shape of the points in the scatter plot, such as *, o, or any other symbol.
"""
