import numpy as np
import matplotlib.pyplot as plt

# Кількість траєкторій
num_trajectories = 10
# Кількість кроків
num_steps = 50
# Крок часу
dt = 0.1
# Інтенсивність Пуассонівського процесу
lambda_ = 0.1

# Генерація траєкторій Вінерівського процесу
wiener_trajectories = np.cumsum(np.sqrt(dt) * np.random.randn(num_steps, num_trajectories), axis=0)
wiener_trajectories = np.vstack([np.zeros((1, num_trajectories)), wiener_trajectories])

# Генерація траєкторій Пуассонівського процесу
poisson_trajectories = np.zeros((num_steps , num_trajectories))
for i in range(num_trajectories):
    n = np.random.poisson(lambda_ * dt, num_steps)
    poisson_trajectories[:, i] = np.cumsum(n)

# Створення окремих графіків

# Графік для Вінерівського процесу
plt.figure(figsize=(10, 6))
for i in range(num_trajectories):
    plt.plot(wiener_trajectories[:, i], label=f'Wiener Trajectory {i+1}', color='blue')
plt.title('Вінерівські траєкторії')
plt.xlabel('Час')
plt.ylabel('Значення')
plt.legend()
plt.grid(True)
plt.show()

# Графік для Пуассонівського процесу
plt.figure(figsize=(10, 6))
for i in range(num_trajectories):
    plt.plot(poisson_trajectories[:, i], label=f'Poisson Trajectory {i+1}', color='red', linestyle='--')
plt.title('Пуассонівські траєкторії')
plt.xlabel('Час')
plt.ylabel('Кількість подій')
plt.legend()
plt.grid(True)
plt.show()

# Графік для порівняння
plt.figure(figsize=(10, 6))
for i in range(num_trajectories):
    plt.plot(wiener_trajectories[:, i], label=f'Wiener Trajectory {i+1}', color='blue')
    plt.plot(poisson_trajectories[:, i], label=f'Poisson Trajectory {i+1}', color='red', linestyle='--')
plt.title('Порівняння Вінерівського та Пуассонівського процесів')
plt.xlabel('Час')
plt.ylabel('Значення / Кількість подій')
plt.legend()
plt.grid(True)
plt.show()

# Параметри
t = 252         # Кількість часових кроків
X = 1           # Початкова ціна
mu = 0.2        # Середнє очікуване зростання
sigma = 0.4     # Волатильність
simulations = 10 # Кількість симуляцій

# Ітераційна схема
def black_scholes_iteration(X, mu, sigma, t):
    dt = 1 / t
    prices = [X]
    for _ in range(t):
        e = np.random.normal(0, 1)
        new_price = prices[-1] + prices[-1] * mu * dt + e * prices[-1] * sigma * np.sqrt(dt)
        prices.append(new_price)
    return prices

# Виконання симуляцій
all_simulations = []
for i in range(simulations):
    prices = black_scholes_iteration(X, mu, sigma, t)
    all_simulations.append(prices)

# Побудова графіка
plt.figure(figsize=(10, 6))
for i, prices in enumerate(all_simulations):
    plt.plot(prices, label=f'Симуляція {i+1}')
plt.title('Цінові траєкторії за моделлю Black-Scholes')
plt.xlabel('Часові кроки')
plt.ylabel('Ціна')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()