import numpy as np
from scipy.stats import kstest

def inverse_cdf(u):
    if u <= 0.5:
        return -1 + np.sqrt(2 * u)
    else:
        return 1 - np.sqrt(2 - 2 * u)

# Генеруємо 10 випадкових значень
random_values = [inverse_cdf(np.random.rand()) for _ in range(10)]

# Проводимо тест Колмогорова-Смірнова
D, p_value = kstest(random_values, 'uniform')

# Виводимо результат тесту
print("D =", D)
print("p-value =", p_value)
