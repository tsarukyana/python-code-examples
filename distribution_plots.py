"""
Distribution plots
This plots a univariate distribution of variables. It is a combination of a histogram with the
default bin size and a Kernel Density Estimation (KDE) plot. In our example, distplot()
will take the satisfaction_level input column and plot the distribution of it. Here, the
distribution of satisfaction_level has two peaks:
"""
# Import the required libraries
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# Load the dataset
df = pd.read_csv("HR_comma_sep.csv")

# Create a distribution plot (also known as Histogram)
sns.distplot(df.satisfaction_level)

# Show figure
plt.show()

"""
In the preceding code block, we have created the distribution plot using distplot()
"""
