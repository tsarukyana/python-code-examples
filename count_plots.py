"""
Count plots
countplot() is a special type of bar plot. It shows the frequency of each categorical
variable. It is also known as a histogram for categorical variables. It makes operations very
simple compared to Matplotlib. In Matplotlib, to create a count plot, first we need to group
by the category column and count the frequency of each class. After that, this count is
consumed by Matplotlib's bar plot. But the Seaborn count plot offers a single line of code to
plot the distribution:
"""
# Import the required libraries
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# Load the dataset
df = pd.read_csv("HR_comma_sep.csv")

# Create count plot (also known as Histogram)
sns.countplot(x='salary', data=df)
# sns.countplot(x='salary', data=df, hue='left')

# Show figure
plt.show()

"""
In the preceding example, we are counting the salary variable. The count() function
takes a single column and DataFrame. So, we can easily conclude from the graph that most
of the employees have low and medium salaries.
"""
