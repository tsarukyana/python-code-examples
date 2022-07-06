"""
Pair plots
Seaborn offers quick exploratory data analysis with relationships and individual
distribution using a pair plot. A pair plot offers a single distribution using a histogram and
joint distribution using a scatter plot:
"""
# Import required library
import seaborn as sns
from matplotlib import pyplot as plt

# Load iris data using load_dataset() function
data = sns.load_dataset("iris")

# Create a pair plot
sns.pairplot(data)

# Show figure
plt.show()

"""
In the preceding example, the Iris dataset is loaded using load_dataset() and that
dataset is passed into the pairplot() function. In the plot, it creates an n by n matrix or a
grid of graphs. The diagonal shows the distribution of the columns, and the non-diagonal
elements of the grid show the scatter plot to understand the relationship among all the
variables.
"""
