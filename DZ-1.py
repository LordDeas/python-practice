`import numpy as np
import scipy.stats as st
import pandas as pd
import matplotlib.pyplot as plt


a = 134775813
c = 1
m = 2**32
x0 = 1
n = 1000

def gen(n:int, a:int, c:int, m:int, start:int, scale = True):
    assert m>=2, "Argument m is less than 2 - change parameter m"
    assert n>0, "Size of sample is not a positive number"
    
    result = []
    current = start
    result.append(current)
    
    for i in range(1, n):
        following = (current*a+c)%m
        result.append(following)
        current = following
    
    if scale:
        result = [elem/m for elem in result]
    
    assert len(result) == n, "Size of output is not matching with expected"
    
    return result






sample = gen(n, a, c,  m, x0)



class Pearson:
    def __init__(self, sample, pass_value = False, critical_value = 0.05):
        self.n = len(sample)
        self.sample = np.array(sample)
        self.interval_start = 0
        self.interval_end = 1
        self.is_value = pass_value
        self.critical_value = critical_value

    # знаходження критичного значення
    def __get_critical_value():
        df = int(N - 2)
        
        if not is_value:
            critical_value = st.chi2.ppf(1-critical_value, df = df)

    # метод знаходження оптимального N - кількісті інтервалів
    def __get_optimal_N():
        for N in range(1, n):
            output = N
            if int(n/N) < 10:
                break
        
        self.N = output - 1
        self.interval_lenght = 1/self.N

    # розрахунок статистики
    def __calculate_chi_squared():
        pearson_sum = 0

        for i in range(N):
            
            condition_1  = sample <= interval_start + interval_lenght*(i+1)
            condition_2 = sample >= interval_start + interval_lenght*i
            mask = condition_1&condition_2
            
            sample_in_count = np.count_nonzero(mask)
            pearson_sum += (sample_in_count - n*1/N)**2/(n/N)
            
        pearson_sum = pearson_sum


    def __compare_chi_squared():
        if pearson_sum < critical_value:
            return "Приймаємо гіпотезу H_0 - згенеровані величини не суперечать рівномірному розподілу на (0,1)"
        else: 
            return "Відхиляємо гіпотезу H_0 на користь альтернативної, суперечить рівномірному розподілу на (0,1)"


    def test():
        __get_optimal_N()
        print("Оптимальне значення N = ", str(N))
        
        __get_critical_value()  
        print("Критичне значення = ", str(round(critical_value, 2)) + ", кількість степенів свободи = ", str(df))   
        
        __calculate_chi_squared()
        print("Значення статистики Пірсона: ", str(round(pearson_sum, 3)))
        
        message = __compare_chi_squared()
        print(message)


test_1 = Pearson(sample, pass_value = False, critical_value = 0.05)

test_1.test()

class Kolmogorov:
    def __init__(self, sample, pass_value = False, critical_value = 0.05):
        self.n = len(sample)
        self.sample = np.sort(np.array(sample))
        self.interval_start = 0
        self.interval_end = 1
        self.is_value = pass_value
        self.critical_value = critical_value
    
    # знаходження критичного значення за p
    def __get_critical_value(self):        
        if not self.is_value:
            self.critical_value = st.ksone.ppf(1- self.critical_value/2, self.n)


    # розрахунок статистики
    def __calculate_kolmogorov(self):
        kolmogorov_stat = 0
        result = []
        
        for i in range(self.n):
            first_value = np.abs(self.sample[i] - (i-1)/self.n) 
            second_value = np.abs(i/self.n - self.sample[i]) 
            current_value = max(first_value, second_value)
            if kolmogorov_stat < current_value:
                kolmogorov_stat = current_value
            
            result.append(current_value)
            
        self.kolmogorov_stat = kolmogorov_stat * np.sqrt(n)
        self.residuals = pd.Series(result)
    
    # висновок
    def __compare_kolmogorov(self):
        if self.kolmogorov_stat < self.critical_value:
            return "Приймаємо гіпотезу H_0 - згенеровані величини не суперечать рівномірному розподілу на (0,1)"
        else: 
            return "Відхиляємо гіпотезу H_0 на користь альтернативної, суперечить рівномірному розподілу на (0,1)"
    
    # весь тест
    def test(self):        
        self.__get_critical_value()  
        print("Критичне значення = ", str(round(self.critical_value, 4)))   
        
        self.__calculate_kolmogorov()
        print("Значення статистики Колмогорова: ", str(round(self.kolmogorov_stat, 3)))
        
        message = self.__compare_kolmogorov()
        print(message)
        
    def show_residuals_stats(self):
        print("Основні статистики абсолютних відхилень:")
        print(self.residuals.describe())
        print("Гістограма абсолютних відхилень функцій розподілу:")
        self.residuals.hist(bins=int(self.n/10)).plot()

test_2 = Kolmogorov(sample,  pass_value = False, critical_value = 0.05)

class SKM:
    def __init__(self, sample, critical_value = 0.215):
        self.n = len(sample)
        self.sample = np.sort(np.array(sample))
        self.interval_start = 0
        self.interval_end = 1
        self.critical_value = critical_value

    # розрахунок статистики
    def __calculate_skm(self):
        skm_stat = 1/(12*self.n)
        #\frac{1}{12n} + \sum_{k=1}^{n}{(x_k - \frac{2k-1}{2n})} 
        
        for i in range(self.n):
            skm_stat += (self.sample[i] - (2*i-1)/(2*self.n))

        self.skm_stat = skm_stat
    
    # висновок
    def __compare_skm(self):
        if self.skm_stat < self.critical_value:
            return "Приймаємо гіпотезу H_0 - згенеровані величини не суперечать рівномірному розподілу на (0,1)"
        else: 
            return "Відхиляємо гіпотезу H_0 на користь альтернативної, суперечить рівномірному розподілу на (0,1)"
    
    # весь тест
    def test(self):        
        print("Критичне значення = ", str(round(self.critical_value, 4)))   
        
        self.__calculate_skm()
        print("Значення статистики: ", str(round(self.skm_stat, 3)))
        
        message = self.__compare_skm()
        print(message)

test_3 =  SKM(sample, critical_value =  0.5)
