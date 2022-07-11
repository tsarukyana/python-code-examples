"""
With the scipy and math libraries to calculate the confidence interval for an estimated proportion.
Here, the sample size is 30 and the occurrences is 6.
"""
import scipy.stats as stats
import math

# Specify sample occurrences (x), sample size (n) and confidence level
x = 6
n = 30
confidence_level = 0.95

# Calculate the point estimate, alpha, the critical z-value, the standard error, and the margin of error
point_estimate = x / n
alpha = (1 - confidence_level)
critical_z = stats.norm.ppf(1 - alpha / 2)
standard_error = math.sqrt((point_estimate * (1 - point_estimate) / n))
margin_of_error = critical_z * standard_error

# Calculate the lower and upper bound of the confidence interval
lower_bound = point_estimate - margin_of_error
upper_bound = point_estimate + margin_of_error

# Print the results
print("Point Estimate: {:.3f}".format(point_estimate))
print("Critical Z-value: {:.3f}".format(critical_z))
print("Margin of Error: {:.3f}".format(margin_of_error))
print("Confidence Interval: [{:.3f},{:.3f}]".format(lower_bound, upper_bound))
print("The {:.1%} confidence interval for the population proportion is:".format(confidence_level))
print("between {:.3f} and {:.3f}".format(lower_bound, upper_bound))
