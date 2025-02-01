import numpy as np
from scipy.stats import kstest

def inverse_cdf(u):
    if u <= 0.5:
        return -1 + np.sqrt(2 * u)
    else:
        return 1 - np.sqrt(2 - 2 * u)

# Generate 10 random values
random_values = [inverse_cdf(np.random.rand()) for _ in range(10)]

# Perform Kolmogorov-Smirnov test
D, p_value = kstest(random_values, 'uniform')

# Output the test result
print("D =", D)
print("p-value =", p_value)
