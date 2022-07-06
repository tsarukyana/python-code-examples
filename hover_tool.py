"""
Hover tool
The hover tool shows the related information whenever the mouse pointer is placed over a
particular area. Let's see examples to understand the hovering plots:
"""
# Import the required modules
from bokeh.plotting import figure
from bokeh.plotting import output_notebook
from bokeh.plotting import show
from bokeh.models import CategoricalColorMapper
from bokeh.models import HoverTool

# Import iris flower dataset as pandas DataFrame
from bokeh.sampledata.iris import flowers as df

# Output to notebook
output_notebook()

# Create color mapper for categorical column
mapper = CategoricalColorMapper(factors=['setosa', 'virginica', 'versicolor'],
                                palette=['blue', 'green', 'red'])

color_dict = {'field': 'species', 'transform': mapper}

# Create hovertool and specify the hovering information
hover = HoverTool(tooltips=[('Species type', '@species'),
                            ('IRIS Petal Length', '@petal_length'),
                            ('IRIS Petal Width', '@petal_width')])

# Instantiate a figure object
p = figure(plot_width=500, plot_height=350, title="Petal length Vs. Petal Width",
           x_axis_label='petal_length', y_axis_label='petal_width',
           tools=[hover, 'pan', 'wheel_zoom'])

# Create scatter marker plot by render the circles
p.circle('petal_length', 'petal_width', size=8, color=color_dict, alpha=0.5, legend_group='species', source=df)

# Set the legend location
p.legend.location = 'top_left'

# Show the plot
show(p)

"""
In the preceding example, we have imported HoverTool from bokeh.models and created
its object by defining the information that will be shown on mouse hover. In our example,
we have defined information in the list of tuples. Each tuple has two arguments. The first is
for the string label and the second is for the actual value (preceded with @). This hover
object is passed into the figure object's tools parameter.
"""
