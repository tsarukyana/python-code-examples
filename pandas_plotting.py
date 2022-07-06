"""
The pandas library offers the plot() method as a wrapper around the Matplotlib library.
The plot() method allows us to create plots directly on pandas DataFrames. The
following plot() method parameters are used to create the plots:
    kind: A string parameter for the type of graph, such as line, bar, barh, hist, box,
    KDE, pie, area, or scatter.
    figsize: This defines the size for a figure in a tuple of (width, height).
    title: This defines the title for the graph.
    grid: Boolean parameter for the axis grid line.
    legend: This defines the legend.
    xticks: This defines the sequence of x-axis ticks.
    yticks: This defines the sequence of y-axis ticks.
Let's create a scatter plot using the pandas plot() function:
"""
# Import the required modules
import pandas as pd
import matplotlib.pyplot as plt

# Let’s create a Dataframe
df = pd.DataFrame({
    'name': ['Ajay', 'Malala', 'Abhijeet', 'Yming', 'Desilva', 'Lisa'],
    'age': [22, 72, 25, 19, 42, 38],
    'gender': ['M', 'F', 'M', 'M', 'M', 'F'],
    'country': ['India', 'Pakistan', 'Bangladesh', 'China', 'Srilanka', 'UK'],
    'income': [2500, 3800, 3300, 2100, 4500, 5500]
})

# Create a scatter plot
df.plot(kind='scatter', x='age', y='income', color='red', title='Age Vs Income')

# Show figure
plt.show()

"""
In the preceding plot, the plot() function takes kind, x, y, color, and title values. In
our example, we are plotting the scatter plot between age and income using the kind
parameter as 'scatter'. The age and income columns are assigned to the x and y
parameters. The scatter point color and the title of the plot are assigned to the color and
title parameters:
"""
