"""
In the matplotlib module, we can add titles and axes labels to a graph. We can add a title
using plt.title() and labels using plt.xlabel() and plt.ylabel().
Multiple graphs mean multiple objects, such as line, bar, and scatter. Points of different
series can be shown on a single graph. Legends or graph series reflect the y axis. A legend is
a box that appears on either the right or left side of a graph and shows what each element
of the graph represents. Let's see an example where we see how to use these accessories in
our charts:
"""
# Add the required libraries
import matplotlib.pyplot as plt

# Create the data
x = [1, 3, 5, 7, 9, 11]
y = [10, 25, 35, 33, 41, 59]

# Let's plot the data
plt.plot(x, y, label='Series-1', color='blue')

# Create the data
x = [2, 4, 6, 8, 10, 12]
y = [15, 29, 32, 33, 38, 55]

# Plot the data
plt.plot(x, y, label='Series-2', color='red')

# Add X Label on X-axis
plt.xlabel("X-label")

# Add X Label on X-axis
plt.ylabel("Y-label")

# Append the title to graph
plt.title("Multiple Python Line Graph")

# Add legend to graph
plt.legend()

# Display the plot
plt.show()

"""
In the preceding graph, two lines are shown on a single graph. We have used two extra
parameters – label and color – in the plot() function. The label parameter defines the
name of the series and color defines the color of the line graph
"""
