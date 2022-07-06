"""
lm plots
The lm plot plots the scatter and fits the regression model on it. A scatter plot is the best
way to understand the relationship between two variables. Its output visualization is a joint
distribution of two variables. lmplot() takes two column names – x and y – as a string and
DataFrame variable. Let's see the following example:
"""
# Import the required libraries
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# Create DataFrame
df = pd.DataFrame({'x': [1, 3, 5, 7, 9, 11], 'y': [10, 25, 35, 33, 41, 59]})

# Create lmplot
sns.lmplot(x='x', y='y', data=df)

# Show figure
plt.show()
