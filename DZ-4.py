import numpy as np
from scipy.stats import chi2

# Function to check if a point is inside the region
def check_inside_region(x, y, z):
    return x/2 + y + z/3 <= 1 and x > 0 and y > 0 and z > 0

# Generate random values
num_samples = 250
x = 3 * (1 - np.cbrt(1 - np.random.uniform(0, 1, num_samples)))
y = np.cbrt(1 - np.random.uniform(0, 1, num_samples)) * (1 - np.sqrt(1 - np.random.uniform(0, 1, num_samples)))
z = np.random.uniform(0, 1, num_samples) * 2 * np.cbrt(1 - np.random.uniform(0, 1, num_samples)) * np.sqrt(1 - np.random.uniform(0, 1, num_samples))

# Check how many points are inside the region
inside_region_count = np.sum([check_inside_region(x[i], y[i], z[i]) for i in range(num_samples)])

# Calculate the volume of the region
# The volume of the region is described as a percentage of the total number of attempts
total_volume = 3 * (1/2) * (1/3) # Volume of the rectangle * average value of the region
expected_values = total_volume * num_samples

# Calculate the chi-square test
degree_of_freedom = 1 # you have two possible options: the point can be inside or outside the region
chi_square_statistic = ((inside_region_count - expected_values)**2) / expected_values
p_value = 1 - chi2.cdf(chi_square_statistic, degree_of_freedom)

print("Number of points inside the region:", inside_region_count)
print("Chi-square statistic:", chi_square_statistic)
print("p-value:", p_value)
