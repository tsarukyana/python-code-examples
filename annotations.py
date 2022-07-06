"""
Annotations
Bokeh offers several annotations for supplementary information for visualizations. It helps
the viewer by adding the following information:
    * Titles: This annotation provides a name to the plot.
    * Axis labels: This annotation provides labels to the axis. It helps us to understand
        what the x and y axes represent.
    * Legends: This annotation represents the third variable via color or shape and
        helps us to link features for easy interpretations.
    * Color bars: Color bars are created using ColorMapper with the color palette.
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

# Create color mapper for categorical column
color_mapper = CategoricalColorMapper(factors=['setosa', 'virginica', 'versicolor'], palette=['blue', 'green', 'red'])

color_dict = {'field': 'species', 'transform': color_mapper}

# Instantiate a figure object
p = figure(plot_width=500, plot_height=350, title="Petal length Vs. Petal Width",
           x_axis_label='petal_length', y_axis_label='petal_width')

# Create scatter marker plot by render the circles
p.circle('petal_length', 'petal_width', size=8, color=color_dict, alpha=0.5, legend_group='species', source=df)

# Set the legend location
p.legend.location = 'top_left'

# Show the plot
show(p)

"""
In the preceding example, CategoricalColorMapper is imported and objects are created
by defining factors or unique items in iris species and their respective colors. A color
dictionary is created by defining the field and transform parameters for the mapper. We
need to define the figure title; x_axis_label and y_axis_label were defined inside the
figure object. The legend is defined in the circle scatter marker function with the species
column and its location is defined using the location attribute of the figure object with
top_left.
"""
