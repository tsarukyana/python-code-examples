"""
A pie plot is a circular graph that is split up into wedge-shaped pieces. Each piece is
proportionate to the value it represents. The total value of the pie is 100 percent:
"""
# Add the essential library matplotlib
import matplotlib.pyplot as plt

# create the data
subjects = ["Mathematics", "Science", "Communication Skills", "Computer Application"]
scores = [85, 62, 57, 92]

# Plot the pie plot
plt.pie(scores,
        labels=subjects,
        colors=['r', 'g', 'b', 'y'],
        startangle=90,
        shadow=True,
        explode=(0, 0.1, 0, 0),
        autopct='%1.1f%%')

# Add title to graph
plt.title("Student Performance")

# Draw the chart
plt.show()

"""
In the preceding code of the pie chart, we specified values, labels, colors, startangle,
shadow, explode, and autopct. In our example, values is the scores of the student in
four subjects and labels is the list of subject names. We can also specify the color list for
the individual subject scores. The startangle parameter specifies the first value angle,
which is 90 degrees; this means the first line is vertical.

Optionally, we can also use the shadow parameter to specify the shadow of the pie slice
and the explode parameter to pull out a pie slice list of the binary value. If we want to pull
out a second pie slice, then a tuple of values would be (0, 0.1, 0, 0).
"""
