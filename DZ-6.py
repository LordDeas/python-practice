import numpy as np

def generate_random_points(n):
    x = np.random.uniform(0, 1, size=n)
    y = np.random.uniform(0, 1 - x, size=n)
    return x, y

def u(x, y):
    return x**2 + y**2

def Monte_Carlo(n):
    x, y = generate_random_points(n)
    u_values = u(x, y)
    return np.mean(u_values)

def Chebyshev_inequality(n, epsilon, true_value):
    u_estimate = Monte_Carlo(n)
    variance = np.var([u(np.random.uniform(0, 1), np.random.uniform(0, 1 - x)) for x in np.random.uniform(0, 1, size=n)])
    probability = variance / (n * epsilon**2)
    print(f"The probability of deviation from the true value is greater than {epsilon}: {probability:.4f}")
    return probability

true_value = 0.4**2 + 0.2**2
epsilon = 0.01
n = 1000

Chebyshev_inequality(n, epsilon, true_value)

n = 1000
u_estimate = Monte_Carlo(n)
print(f"Estimated value of u(0.4, 0.2) using the Monte Carlo method: {u_estimate:.4f}")


