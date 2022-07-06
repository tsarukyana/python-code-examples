"""
Mute click policy
Mute click policy mutes the glyph by clicking on a legend entry. Here, the following code
shows the desirable glyph with high intensity and uninteresting glyphs using lower
intensity instead of hiding the whole glyph. Let's see an example of a mute click policy:
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
    fig.circle('petal_length', 'petal_width', size=8, color=color, alpha=0.7, legend_label=specie, source=data,
               muted_color=color, muted_alpha=0.2)

# Set the legend location and click policy
fig.legend.location = 'top_left'
fig.legend.click_policy = "mute"

# Show the plot
show(fig)

"""
Here, we can set the mute click policy with the legend.click_policy parameter to mute
figure objects. Also, we need to run the for loop of each type of glyph or legend element on
which you click. In our example, we are running a for loop for types of species and colors.
On the click of any species in the legend, it will filter the data and hide that glyph. In
addition to that, we need to add a muted_color and muted_alpha parameter to the
scatter circle marker.
"""
