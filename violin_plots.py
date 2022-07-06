"""
Violin plots
Violin plots are a combined form of box plots and KDE, which offer easy-to-understand
analysis of the distribution:
"""
# Import the required libraries
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# Load the dataset
df = pd.read_csv("HR_comma_sep.csv")

# Create violin plot
sns.violinplot(data=df[['satisfaction_level', 'last_evaluation']])

# Show figure
plt.show()

"""
In the preceding example, we have used two variables for the violin plot. Here, we can
conclude that the range of satisfaction_level is higher than last_evaluation
(performance) and both the variables have two peaks in the distribution.
"""
