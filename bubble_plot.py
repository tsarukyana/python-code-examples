"""
A bubble plot is a type of scatter plot. It not only draws data points using Cartesian
coordinates but also creates bubbles on data points. Bubble shows the third dimension of a
plot. It shows three numerical values: two values are on the x and y axes and the third one
is the size of data points (or bubbles):
"""
# Import the required modules
import matplotlib.pyplot as plt
import numpy as np

# Set figure size
plt.figure(figsize=(8, 5))

# Create the data
countries = ['Qatar', 'Luxembourg', 'Singapore', 'Brunei', 'Ireland', 'Norway', 'UAE', 'Kuwait']
populations = [2781682, 604245, 5757499, 428963, 4818690, 5337962, 9630959, 4137312]
gdp_per_capita = [130475, 106705, 100345, 79530, 78785, 74356, 69382, 67000]

# scale GDP per capti income to shot the bubbles in the graph
scaled_gdp_per_capita = np.divide(gdp_per_capita, 80)

colors = np.random.rand(8)

# Draw the scatter diagram
plt.scatter(countries, populations, s=scaled_gdp_per_capita, c=colors, cmap="Blues", edgecolors="grey", alpha=0.5)

# Add X Label on X-axis
plt.xlabel("Countries")

# Add Y Label on X-axis
plt.ylabel("Population")

# Add title to graph
plt.title("Bubble Chart")

# rotate x label for clear visualization
plt.xticks(rotation=45)

# Show the plot
plt.show()

"""
In the preceding plot, a bubble chart is created using the scatter function. Here, the
important thing is the s (size) parameter of the scatter function. We assigned a third
variable, scaled_gdp_per_capita, to the size parameters. In the preceding bubble plot,
countries are on the x axis, the population is on the y axis, and GDP per capita is shown by
the size of the scatter point or bubble. We also assigned a random color to the bubbles to
make it attractive and more understandable. From the bubble size, you can easily see that
Qatar has the highest GDP per capita and Kuwait has the lowest GDP per capita. In all the
preceding sections, we have focused on most of the Matplotlib plots and charts.
"""
