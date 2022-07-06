"""
Nested layout using row and column layouts
A nested layout is the combination of multiple row and column layouts. Let's see the
example given here for a better practical understanding:
"""
# Import the required modules
from bokeh.plotting import figure
from bokeh.plotting import output_notebook
from bokeh.plotting import show
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

# Create nested layout
nasted_layout = row(fig1, column(fig2, fig3))

# Show the plot
show(nasted_layout)

"""
Here, you can see the row layout has two rows. In the first, fig1 is assigned and the second
row has the column layout of fig2 and fig3. So, this layout becomes a 2*2 layout, in which
the first column has only one component and the second column has two components.
"""