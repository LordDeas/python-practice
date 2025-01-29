import numpy as np
import matplotlib.pyplot as plt

# Задані параметри
alpha = 2
# Знаходимо значення сталої beta, щоб функція була щільністю ймовірності
beta = alpha

class Pearson:
    def __init__(self,beta,alpha,x):
        pass

    # Функція щільності ймовірності
    def __chiln__(x,alpha,beta):
        if x <= 0:
            return 0
        else:
            return beta * np.exp(-alpha * x)
        
    # Генеруємо 1200 значень випадкової величини X методом оберненої функції
    def __generator__(alpha):
        random_values = np.random.exponential(scale=1/alpha, size=1200)
        sample_mean = np.mean(random_values)
        standard_error = np.std(random_values) / np.sqrt(len(random_values))

    # Побудова гістограми
    def __Gist__():
        plt.hist(random_values, bins=30, density=True, color='skyblue', edgecolor='black', alpha=0.7, label='Емпіричний розподіл')
        # Побудова теоретичного розподілу
        x = np.linspace(0, 10, 1000)
        y = beta * np.exp(-alpha * x)
        plt.plot(x, y, 'r-', label='Теоретичний розподіл')
        plt.xlabel('Значення випадкової величини')
        plt.ylabel('Щільність ймовірності')
        plt.title('Порівняння теоретичного та емпіричного розподілів')
        plt.legend()
        plt.show()

    def rezalt():
        # Виведення результатів
        print(f"Вибіркове середнє: {sample_mean}")
        print(f"Стандартна похибка: {standard_error}")
        print(f"Математичне сподівання: {1/alpha}")
        print(f"Середнє квадратичне відхилення: {1/alpha}")