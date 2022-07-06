"""
Joint plots
The joint plot is a multi-panel visualization; it shows the bivariate relationship and
distribution of individual variables in a single graph. We can also plot a KDE using the
kind parameter of jointplot(). By setting the kind parameter as "kde", we can draw
the KDE plot. Let's see the following example:
"""
# Import the required libraries
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# Load the dataset
df = pd.read_csv("HR_comma_sep.csv")

# Create joint plot using kernel density estimation(kde)
sns.jointplot(x='satisfaction_level', y='last_evaluation', data=df, kind="kde")

# Show figure
plt.show()

"""
In the preceding plot, we have created the joint plot using jointplot() and also added
the kde plot using a kind parameter as "kde".
"""
