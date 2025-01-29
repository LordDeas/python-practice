import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

#1 завдання

# Функція для генерації випадкових значень методом оберненої функції
def generate_random_values(p, size):
    U = np.random.rand(size)
    X = np.floor(np.log(1 - U) / np.log(1 - p)) + 1
    return X.astype(int)

# Генерація 100 випадкових значень
random_v = generate_random_values(0.3, 100)

# Обчислення вибіркового середнього та стандартної похибки
sample_mean = np.mean(random_v)
standard_error = np.std(random_v)

# Побудова гістограми
plt.hist(random_v, bins=[1, 2, 3, 4, 5], align='left', rwidth=0.5, color='skyblue', edgecolor='black')
plt.xlabel('Ключі')
plt.ylabel('Частота')
plt.title('Гістограма випадкових значень')
plt.show()

D, _ = stats.kstest(random_v, 'expon', args=(0, 0.5))
print("Статистика Колмогорова (D):", D)
print(f"Вибіркове середнє: {sample_mean}")
print(f"Стандартна похибка: {standard_error}")


# 2 завдання

# Задані параметри
alpha = 2
# Знаходимо значення сталої beta, щоб функція була щільністю ймовірності
beta = alpha

# Функція щільності ймовірності
def f(x, alpha, beta):
    if x <= 0:
        return 0
    else:
        return beta * np.exp(-alpha * x)

 # Генеруємо 1200 значень випадкової величини X методом оберненої функції
random_values = np.random.rand(1200)
ober_values = -1/alpha * np.log(1-random_values)

# Знаходимо вибіркове середнє та стандартну похибку
sample_mean = np.mean(ober_values)
standard_error = np.std(ober_values) / np.sqrt(len(ober_values))

# Обчислення статистики Колмогорова
D, _ = stats.kstest(ober_values, 'expon', args=(0, 1/alpha))

# Побудова гістограми
plt.hist(ober_values, bins=30, density=True, color='skyblue', edgecolor='black', alpha=0.7, label='Емпіричний розподіл')

# Побудова теоретичного розподілу
x = np.linspace(0, 10, 1000)
y = beta * np.exp(-alpha * x)
plt.plot(x, y, 'r-', label='Теоретичний розподіл')

plt.xlabel('Значення випадкової величини')
plt.ylabel('Щільність ймовірності')
plt.title('Порівняння теоретичного та емпіричного розподілів')
plt.legend()
plt.show()

# Виведення результатів
print(f"Вибіркове середнє: {sample_mean}")
print(f"Стандартна похибка: {standard_error}")
print(f"Математичне сподівання: {1/alpha}")
print(f"Середнє квадратичне відхилення: {1/alpha}")
print("Статистика Колмогорова (D):", D)

