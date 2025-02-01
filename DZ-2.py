import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

#1 task

# Function for generating random values ​​using the inverse function method
def generate_random_values(p, size):
    U = np.random.rand(size)
    X = np.floor(np.log(1 - U) / np.log(1 - p)) + 1
    return X.astype(int)

# Generate 100 random values
random_v = generate_random_values(0.3, 100)

# Calculating the sample mean and standard error
sample_mean = np.mean(random_v)
standard_error = np.std(random_v)

# Building a histogram
plt.hist(random_v, bins=[1, 2, 3, 4, 5], align='left', rwidth=0.5, color='skyblue', edgecolor='black')
plt.xlabel('Keys')
plt.ylabel('Frequency')
plt.title('Histogram of random values')
plt.show()

D, _ = stats.kstest(random_v, 'expon', args=(0, 0.5))
print("Kolmogorov statistic (D):", D)
print(f"Sample mean: {sample_mean}")
print(f"Standard error: {standard_error}")


# 2 tasks

# Given parameters
alpha = 2
# Find the value of the constant beta so that the function is a probability density
beta = alpha

# Probability density function
def f(x, alpha, beta):
    if x <= 0:
        return 0
    else:
        return beta * np.exp(-alpha * x)

# Generate 1200 values ​​of random variable X using the inverse function method
random_values = np.random.rand(1200)
ober_values = -1/alpha * np.log(1-random_values)

# Find the sample mean and standard error
sample_mean = np.mean(ober_values)
standard_error = np.std(ober_values) / np.sqrt(len(ober_values))

# Calculation of Kolmogorov statistics
D, _ = stats.kstest(ober_values, 'expon', args=(0, 1/alpha))

# Building a histogram
plt.hist(ober_values, bins=30, density=True, color='skyblue', edgecolor='black', alpha=0.7, label='Empirical distribution')

# Construct the theoretical distribution
x = np.linspace(0, 10, 1000)
y = beta * np.exp(-alpha * x)
plt.plot(x, y, 'r-', label='Theoretical distribution')

plt.xlabel('Random variable value')
plt.ylabel('Probability density')
plt.title('Comparison of theoretical and empirical distributions')
plt.legend()
plt.show()

# Output the results
print(f"Sample mean: {sample_mean}")
print(f"Standard error: {standard_error}")
print(f"Expectation: {1/alpha}")
print(f"Random square deviation: {1/alpha}")
print("Kolmogorov statistic (D):", D)

