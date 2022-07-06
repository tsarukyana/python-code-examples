"""
Normal distribution
Normal distributions occur frequently in real-life scenarios. A normal distribution is also
known as a bell curve because of its characteristic shape. The probability density function
models continuous distribution. The numpy.random subpackage offers lots of continuous
distributions such as beta, gamma, logistic, exponential, multivariate normal, and normal
distribution. The normal() functions find samples from Gaussian or normal distribution.
Let's write code for visualizing the normal distribution using the normal() function, as
follows:
"""
# Import required library
import numpy as np
import matplotlib.pyplot as plt

sample_size = 225000

# Generate random values sample using normal distribution
sample = np.random.normal(size=sample_size)

# Create Histogram
n, bins, patch_list = plt.hist(sample, int(np.sqrt(sample_size)), density=True)

# Set parameters
mu, sigma = 0, 1
x = bins
y = 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2))

# Plot line plot(or bell curve)
plt.plot(x, y, color='red', lw=2)
plt.show()

"""
Here, we have generated random values using the normal() function of the numpy.
random subpackage and displayed the values using a histogram and line plot or bell curve
or theoretical probability density function (PDF) with mean 0 and standard deviation of 1.
"""
