"""
A histogram shows the distribution of a numeric variable. We create a histogram using the
hist() method. It shows the probability distribution of a continuous variable. A histogram
only works on a single variable while a bar graph works on two variables:
"""
# Add the essential library
import matplotlib.pyplot as plt

# Create the data
employee_age = [21, 28, 32, 34, 35, 35, 37, 42, 47, 55]

# Create bins for histogram
bins = [20, 30, 40, 50, 60]

# Plot the histogram
plt.hist(employee_age, bins, rwidth=0.6)

# Add X Label on X-axis
plt.xlabel("Employee Age")

# Add X Label on X-axis
plt.ylabel("Frequency")

# Add title to graph
plt.title("Employee Age Distribution")

# Show the plot
plt.show()

"""
In the preceding histogram, the hist() function takes values, bins, and rwidth. In our
example, we are plotting the age of the employee and using a bin of 10 years. We are
starting our bin from 20 to 60 with a 10 years bin size. We are using a relative bar width of
0.6, but you can choose any size for thicker and thinner width.
"""
