"""
Tab panel
Tab panes allow us to create multiple plots and layouts in a single window. Let's see an
example of a tab panel:
"""
# Import the required modules
from bokeh.plotting import figure
from bokeh.plotting import output_notebook
from bokeh.plotting import show
from bokeh.models.widgets import Tabs
from bokeh.models.widgets import Panel

# Import iris flower dataset as pandas DataFrame
from bokeh.sampledata.iris import flowers as df

# Output to notebook
output_notebook()

# Instantiate a figure
fig1 = figure(plot_width=300, plot_height=300)
fig2 = figure(plot_width=300, plot_height=300)

# Create scatter marker plot by render the circles
fig1.circle(df['petal_length'], df['sepal_length'], size=8, color="green", alpha=0.5)
fig2.circle(df['petal_length'], df['sepal_width'], size=8, color="blue", alpha=0.5)

# Create panels
tab1 = Panel(child=fig1, title='tab1')
tab2 = Panel(child=fig2, title='tab2')

# Create tab by putting panels into it
tab_layout = Tabs(tabs=[tab1, tab2])

# Show the plot
show(tab_layout)

"""
In the preceding code, we have created the two panels by passing figure objects to a child
parameter and title to a title parameter to Panel. Both panels are combined into a list
and passed to the Tabs layout object. This Tabs object is shown by the show() function.
You can change the tab by just clicking on it.
"""