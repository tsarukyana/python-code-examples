"""
Plotting a simple graph
Let's plot a first and simple plot using Bokeh. First, we need to import the
basic bokeh.plotting module. The output_notebook() function defines that the plot
will render on the Jupyter Notebook. The figure object is used as one of the core objects to
draw charts and graphs. The figure object focuses on the plot title, size, label, grids, and
style. The figure object also deals with plot style, title, axes labels, axes, grids, and various
methods for adding data:
"""
# Import the required modules
from bokeh.plotting import figure
from bokeh.plotting import output_notebook
from bokeh.plotting import show

# Create the data
x = [1, 3, 5, 7, 9, 11]
y = [10, 25, 35, 33, 41, 59]

# Output to notebook
output_notebook()

# Instantiate a figure
fig = figure(plot_width=500, plot_height=350)

# Create scatter circle marker plot by rendering the circles
fig.circle(x, y, size=10, color="red", alpha=0.7)

# Show the plot
show(fig)

"""
After setting up the figure object, we will create a scatter circle markers plot using a circle
function. The circle() function will take x and y values. It also takes size, color, and
alpha parameters. The show() function will finally plot the output once all the features and
data are added to the plot.
"""
