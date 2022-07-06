"""
Hide click policy
Hide click policy hides the desirable glyphs by clicking on the legend entry. Let's see an
example of a hide click policy:
"""
# Import the required modules
from bokeh.plotting import figure
from bokeh.plotting import output_notebook
from bokeh.plotting import show
from bokeh.models import CategoricalColorMapper

# Import iris flower dataset as pandas DataFrame
from bokeh.sampledata.iris import flowers as df

# Output to notebook
output_notebook()

# Instantiate a figure object
fig = figure(plot_width=500, plot_height=350, title="Petal length Vs. Petal Width",
             x_axis_label='petal_length', y_axis_label='petal_width')

# Create scatter marker plot by render the circles
for specie, color in zip(['setosa', 'virginica', 'versicolor'], ['blue', 'green', 'red']):
    data = df[df.species == specie]
    fig.circle('petal_length', 'petal_width', size=8, color=color, alpha=0.7, legend_label=specie, source=data)

# Set the legend location and click policy
fig.legend.location = 'top_left'
fig.legend.click_policy = "hide"

# Show the plot
show(fig)

"""
Here, we can set the click policy with the legend.click_policy parameter of the figure
object. Also, we need to run a for loop of each type of glyph or legend element on which
you click. In our example, we are running a for loop for types of species and colors. On the
click of any species in the legend, it will filter the data and hide that glyph.
"""
