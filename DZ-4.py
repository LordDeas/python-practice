import numpy as np
from scipy.stats import chi2

# Функція для перевірки, чи точка знаходиться всередині області
def check_inside_region(x, y, z):
    return x/2 + y + z/3 <= 1 and x > 0 and y > 0 and z > 0

# Згенерувати випадкові значення
num_samples = 250
x = 3 * (1 - np.cbrt(1 - np.random.uniform(0, 1, num_samples)))
y = np.cbrt(1 - np.random.uniform(0, 1, num_samples)) * (1 - np.sqrt(1 - np.random.uniform(0, 1, num_samples)))
z = np.random.uniform(0, 1, num_samples) * 2 * np.cbrt(1 - np.random.uniform(0, 1, num_samples)) * np.sqrt(1 - np.random.uniform(0, 1, num_samples))

# Перевірити, скільки точок знаходиться всередині області
inside_region_count = np.sum([check_inside_region(x[i], y[i], z[i]) for i in range(num_samples)])

# Обчислити обсяг області
# Обсяг області описується як відсоток від загальної кількості спроб
total_volume = 3 * (1/2) * (1/3)  # Обсяг прямокутника * середнє значення області
expected_values = total_volume * num_samples

# Обчислити критерій хі-квадрат
degree_of_freedom = 1  # у вас є два можливі варіанти: точка може бути всередині або поза областю
chi_square_statistic = ((inside_region_count - expected_values)**2) / expected_values
p_value = 1 - chi2.cdf(chi_square_statistic, degree_of_freedom)

print("Кількість точок всередині області:", inside_region_count)
print("Хі-квадрат статистика:", chi_square_statistic)
print("p-значення:", p_value)
