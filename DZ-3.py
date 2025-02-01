import numpy as np
from scipy.stats import ks_2samp, shapiro

# Step 1: Generate a sample z_1 of 1000 values ​​from the standard normal distribution using the Central Limit Theorem (CLT)
z_1 = np.random.normal(0, 1, 1000)

# Step 2: Generate samples z_2 and z_3 of 1000 values ​​from the given distribution using the Box-Muller transform
u1 = np.random.uniform(0, 1, 1000)
u2 = np.random.uniform(0, 1, 1000)
z_2 = np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2)
z_3 = np.sqrt(-2 * np.log(u1)) * np.sin(2 * np.pi * u2)
z_4 = np.random.normal(0, 1, 1000)

# Create a vector consisting of 1000 vectors of 5 elements each
vector = np.vstack((z_1[:5], z_2[:5], z_3[:5], z_4[:5],))
rest = []
for i in range(1000):
    temp_vector = np.vstack((z_1[i], z_2[i], z_3[i], z_4[i],))
    rest.append(temp_vector)

# Step 3: Compare and check the consistency of the distributions using the Kolmogorov-Smirnov criterion for z_1, z_2, z_3, z_4, z_5 and with the theoretical distribution
ks_statistic, ks_pvalue_z1 = ks_2samp(z_1, np.random.normal(0, 1, 1000))
ks_statistic, ks_pvalue_z2 = ks_2samp(z_2, np.random.normal(0, 1, 1000))
ks_statistic, ks_pvalue_z3 = ks_2samp(z_3, np.random.normal(0, 1, 1000))
ks_statistic, ks_pvalue_z4 = ks_2samp(z_4, np.random.normal(0, 1, 1000))


# Step 4: Compare and check the consistency of the distribution using the Shapiro-Wilk test for rest
shapiro_values_rest = [shapiro(x.flatten()) for x in rest]

# Step 4: Generate a vector with a normal distribution using the known covariance matrix K and the mean vector M
K = np.array([[186, 111, 23, 97], [111, 143, 95, 78], [23, 95, 151, 132], [97, 78, 132, 230]])
M = np.array([1, -5, 3, 2])

# Find the mathematical expectation of each created vector using the vector M
means = []
for r in rest:
    mean = M + np.dot(np.linalg.inv(K), np.sum(r - M, axis=1))
    means.append(mean)

# Let's check the consistency of the obtained mathematical expectations with the vector M
ks_statistic_means, ks_pvalue_means = ks_2samp(means, M)

# Output results
print("Kolmogorov-Smirnov criterion for z_1:", ks_pvalue_z1)
print("Kolmogorov-Smirnov criterion for z_2:", ks_pvalue_z2)
print("Kolmogorov-Smirnov criterion for z_3:", ks_pvalue_z3)
print("Kolmogorov-Smirnov criterion for z_4:", ks_pvalue_z4)
print("Shapiro-Wilk criterion for rest:", shapiro_values_rest)
print("Kolmogorov-Smirnov criterion for expectation:", ks_pvalue_means)

# Kolmogorov-Smirnov criterion for z_1: 0.19957365535779528
# Kolmogorov-Smirnov criterion for z_2: 0.4659595288557257
# Kolmogorov-Smirnov criterion for z_3: 0.6101664688189142
# Kolmogorov-Smirnov criterion for z_4: 0.8595454206943325
# ShapiroResult (statistic=0.8602344438471801, pvalue=0.2610549678725763), ShapiroResult(statistic=0.8644017487868875, pvalue=0.27628227985901244)
# Kolmogorov-Smirnov criterion for mat. expectations: [0.99300699 0.995005 0.997003 0.995005 ]