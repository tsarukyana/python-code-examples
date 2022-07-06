"""
KDE plots
The kde() function plots the probability density estimation of a given continuous variable.
It is a non-parametric kind of estimator. In our example, the kde() function takes one
parameter, satisfaction_level, and plots the KDE:
"""
# Import the required libraries
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# Load the dataset
df = pd.read_csv("HR_comma_sep.csv")

# Create density plot
sns.kdeplot(df.satisfaction_level)

# Show figure
plt.show()

"""
In the preceding code block, we have created a density plot using kdeplot().
"""
