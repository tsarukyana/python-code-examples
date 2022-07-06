"""
Slider
A slider is a graphical track bar that controls the value by moving it on a horizontal scale.
We can change the values of the graph without affecting its formatting. Let's see an
example of a slider:
"""
# Import the required modules
from bokeh.plotting import Figure
from bokeh.plotting import output_notebook
from bokeh.plotting import show
from bokeh.models import CustomJS
from bokeh.models import ColumnDataSource
from bokeh.models import Slider
from bokeh.layouts import column

# Show output in notebook
output_notebook()

# Create list of data
x = [x for x in range(0, 100)]
y = x

# Create a DataFrame
df = ColumnDataSource(data={"x_values": x, "y_values": y})

# Instantiate the Figure object
fig = Figure(plot_width=350, plot_height=350)

# Create a line plot
fig.line('x_values', 'y_values', source=df, line_width=2.5, line_alpha=0.8)

# Create a callback using CustomJS
callback = CustomJS(args=dict(source=df), code="""
    var data = source.data;
    var f = cb_obj.value
    var x_values = data['x_values']
    var y_values = data['y_values']
    for (var i = 0; i < x_values.length; i++) {
        y_values[i] = Math.pow(x_values[i], f)
    }
    source.change.emit();
""")

slider_widget = Slider(start=0.0, end=10, value=1, step=.1, title="Display power of x")

slider_widget.js_on_change('value', callback)

# Create layout
slider_widget_layout = column(fig, slider_widget)

# Display the layout
show(slider_widget_layout)

"""
In the preceding code, the Bokeh slider() function takes start, end, value, step,
title, and CustomJS callback as input. In our example, we are creating a line graph and
changing its y variable by the power of the x variable using the slide bar. We can create the
slider by passing start, end, value, step, title, and a CustomJS callback to the Slider
object. We need to focus on the CustomJS callback. It takes the source DataFrame, gets the
value of the slider using cb_obj.value, and updates its values using the change.emit()
function. We are updating y_value in the for loop by finding its power using the slider
value.
"""
