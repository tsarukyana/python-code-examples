# Add the essential library matplotlib
import matplotlib.pyplot as plt
import numpy as np

# create the data
a = np.linspace(0, 20)

# Draw the plot
plt.plot(a, a + 0.5, label='linear')

# Display the chart
plt.show()
