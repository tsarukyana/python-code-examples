"""
Layouts
Bokeh offers layouts for organizing plots and widgets. Layouts organize more than one plot
in a single panel for interactive visualizations. They also allow setting the sizing modes for
resizing the plots and widgets based on panel size. The layout can be of the following types:
    * Row layout: This organizes all the plots in a row or in a horizontal fashion.
    * Column layout: This organizes all the plots in a column or in a vertical fashion.
    * Nested layout: This is a combination of row and column layouts.
    * Grid layout: This offers you a grid of matrices for arranging the plots in.
"""
# Import the required modules
from bokeh.plotting import figure
from bokeh.plotting import output_notebook, show
from bokeh.layouts import row, column

# Import iris flower dataset as pandas DataFrame
from bokeh.sampledata.iris import flowers as df

# Output to notebook
output_notebook()

# Instantiate a figure
fig1 = figure(plot_width=300, plot_height=300)
fig2 = figure(plot_width=300, plot_height=300)
fig3 = figure(plot_width=300, plot_height=300)

# Create scatter marker plot by render the circles
fig1.circle(df['petal_length'], df['sepal_length'], size=8, color="green", alpha=0.5)
fig2.circle(df['petal_length'], df['sepal_width'], size=8, color="blue", alpha=0.5)
fig3.circle(df['petal_length'], df['petal_width'], size=8, color="red", alpha=0.5)

# Create row layout
row_layout = row(fig1, fig2, fig3)

# Show the plot
show(row_layout)

"""
In this layout plot, we have imported the row and column layouts, loaded the Iris data from
Bokeh sample data, instantiated the three figure objects with plot width and height,
created the three scatter circle markers on each figure object, and created the row layout.
This row layout will take the figure objects as input and is drawn using the show()
function.
"""
