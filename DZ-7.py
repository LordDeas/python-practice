import numpy as np
import matplotlib.pyplot as plt

# Number of trajectories
num_trajectories = 10
# Number of steps
num_steps = 50
# Time step
dt = 0.1
# Poisson process intensity
lambda_ = 0.1

# Generation of Wiener process trajectories
wiener_trajectories = np.cumsum(np.sqrt(dt) * np.random.randn(num_steps, num_trajectories), axis=0)
wiener_trajectories = np.vstack([np.zeros((1, num_trajectories)), wiener_trajectories])

# Generation of Poisson process trajectories
poisson_trajectories = np.zeros((num_steps , num_trajectories))
for i in range(num_trajectories):
    n = np.random.poisson(lambda_ * dt, num_steps)
    poisson_trajectories[:, i] = np.cumsum(n)

# Creating individual graphs

# Graph for the Wiener process
plt.figure(figsize=(10, 6))
for i in range(num_trajectories):
    plt.plot(wiener_trajectories[:, i], label=f'Wiener Trajectory {i+1}', color='blue')
plt.title('Wiener Trajectories')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()

# Graph for Poisson process
plt.figure(figsize=(10, 6))
for i in range(num_trajectories):
    plt.plot(poisson_trajectories[:, i], label=f'Poisson Trajectory {i+1}', color='red', linestyle='--')
plt.title('Poisson Trajectories')
plt.xlabel('Time')
plt.ylabel('Number of Events')
plt.legend()
plt.grid(True)
plt.show()

# Graph for comparison
plt.figure(figsize=(10, 6))
for i in range(num_trajectories):
    plt.plot(wiener_trajectories[:, i], label=f'Wiener Trajectory {i+1}', color='blue')
    plt.plot(poisson_trajectories[:, i], label=f'Poisson Trajectory {i+1}', color='red', linestyle='--')
plt.title('Comparison of Wiener and Poisson Processes')
plt.xlabel('Time')
plt.ylabel('Value / Number of Events')
plt.legend()
plt.grid(True)
plt.show()

# Parameters
t = 252             # Number of time steps
X = 1               # Initial price
mu = 0.2            # Average expected growth
sigma = 0.4         # Volatility
simulations = 10    # Number of simulations

# Iterative scheme
def black_scholes_iteration(X, mu, sigma, t):
    dt = 1 / t
    prices = [X]
    for _ in range(t):
        e = np.random.normal(0, 1)
        new_price = prices[-1] + prices[-1] * mu * dt + e * prices[-1] * sigma * np.sqrt(dt)
        prices.append(new_price)
    return prices

# Running simulations
all_simulations = []
for i in range(simulations):
    prices = black_scholes_iteration(X, mu, sigma, t)
    all_simulations.append(prices)

# Graph construction
plt.figure(figsize=(10, 6))
for i, prices in enumerate(all_simulations):
    plt.plot(prices, label=f'Simulation {i+1}')
plt.title('Black-Scholes Price Trajectories')
plt.xlabel('Time Steps')
plt.ylabel('Price')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()