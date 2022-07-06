"""
Let's consider a 17th-century gambling house where you can bet on eight tossing pieces and
nine coins being flipped. If you get five or more heads then you win, otherwise you will
lose. Let's write code for this simulation for 1,000 coins using the binomial() function, as
follows:
"""
# Import required libraries
import numpy as np
import matplotlib.pyplot as plt

# Create an numpy vector of size 5000 with value 0
cash_balance = np.zeros(5000)
cash_balance[0] = 500

# Generate random numbers using Binomial
samples = np.random.binomial(9, 0.5, size=len(cash_balance))

# Update the cash balance
for i in range(1, len(cash_balance)):
    if samples[i] < 5:
        cash_balance[i] = cash_balance[i - 1] - 1
    else:
        cash_balance[i] = cash_balance[i - 1] + 1

# Plot the updated cash balance
plt.plot(np.arange(len(cash_balance)), cash_balance)
plt.show()

"""
In the preceding code block, we first created the cash_balance array of size 500 with zero
values and updated the first value with 500. Then, we generated values between 0 to 9
using the binomial() function. After this, we updated the cash_balance array based on
the results of coin tosses and plotted the cash balance using the Matplotlib library.
In each execution, the code will generate different results or random walks. If you want to
make walking constant, you need to use the seed value in the binomial() function. Let's
try another form of distribution for the random number generator: normal distribution.
"""