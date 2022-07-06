"""
Box plot, aka box-whisker plot, is one of the best plots to understand the distribution of
each variable with its quartiles. It can be horizontal or vertical. It shows quartile
distribution in a box, which is known as a whisker. It also shows the minimum and
maximum and outliers in the data. We can easily create a box plot using Seaborn:
"""
# Import the required libraries
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# Load the dataset
df = pd.read_csv("HR_comma_sep.csv")

# Create boxplot
sns.boxplot(data=df[['satisfaction_level', 'last_evaluation']])

# Show figure
plt.show()

"""
In the preceding example, we have used two variables for the box plot. Here, the box plot
indicates that the range of satisfaction_level is higher than last_evaluation
(performance).
"""