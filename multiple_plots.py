"""
Multiple plots
Multiple plots and objects can also be created using a grid layout. A grid layout arranges
the plots and widget objects in a row-column matrix fashion. It takes a list of figure objects
for each row. We can also use None as a placeholder:
"""
# Import the required modules
from bokeh.plotting import figure
from bokeh.plotting import output_notebook
from bokeh.plotting import show
from bokeh.layouts import gridplot

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

# Create a grid layout
grid_layout = gridplot([[fig1, fig2], [None, fig3]])

# Show the plot
show(grid_layout)

"""
The preceding layout is similar to the nested layout. Here, we have imported gridplot().
It arranges the components in rows and columns. The grid plot has taken a list of row
figures. The first items in the list are fig1 and fig2. The second items are None and fig3.
Each item is a row in the grid matrix. The None placeholder is used to leave the cell empty
or without components.
"""
