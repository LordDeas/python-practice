import numpy as np
import matplotlib.pyplot as plt

# Given parameters
alpha = 2
# Find the value of the constant beta so that the function is a probability density
beta = alpha

class Pearson:
    def __init__(self,beta,alpha,x):
        pass

    # Probability density function
    def __chiln__(x,alpha,beta):
        if x <= 0:
            return 0
        else:
            return beta * np.exp(-alpha * x)
        
    # Generate 1200 values ​​of random variable X using the inverse function method
    def __generator__(alpha):
        random_values = np.random.exponential(scale=1/alpha, size=1200)
        sample_mean = np.mean(random_values)
        standard_error = np.std(random_values) / np.sqrt(len(random_values))

    # Building a histogram
    def __Gist__():
        plt.hist(random_values, bins=30, density=True, color='skyblue', edgecolor='black', alpha=0.7, label='Empirical distribution')
        # Constructing a theoretical distribution
        x = np.linspace(0, 10, 1000)
        y = beta * np.exp(-alpha * x)
        plt.plot(x, y, 'r-', label='Theoretical distribution')
        plt.xlabel('Random variable value')
        plt.ylabel('Probability density')
        plt.title('Comparison of theoretical and empirical distributions')
        plt.legend()
        plt.show()

    def rezalt():
        # Виведення результатів
        print(f"Sample mean: {sample_mean}")
        print(f"Standard error: {standard_error}")
        print(f"Expectation: {1/alpha}")
        print(f"Standard deviation: {1/alpha}")