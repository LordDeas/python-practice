import numpy as np

I = 0.1

# determine the number of generated values
n1 = 100
n2 = 1000
n3 = 10000

t1 = np.random.exponential(scale = 0.5, size = n1)
t2 = np.random.exponential(scale = 0.5, size = n2)
t3 = np.random.exponential(scale = 0.5, size = n3)

# Define the function g(t)
def g(t):
    return 0.5*np.cos(t)*t**2

vec = np.vectorize(g)
eta1, eta2, eta3 = vec(t1), vec(t2), vec(t3)

theta1 = np.mean(eta1)
theta2 = np.mean(eta2)
theta3 = np.mean(eta3)

print("Approximate integral value for n = ", n1, " : " , theta1 )
print("Approximate integral value for n = ", n2, " : " , theta2 )
print("Approximate integral value for n = ", n3, " : " , theta3 )

# Find the modulus of the difference
print("Absolute deviation for n = ", n1, " : " , abs(theta1 - I))
print("Absolute deviation for n = ", n2, " : " , abs(theta2 - I))
print("Absolute deviation for n = ", n3, " : " , abs(theta3 - I))

Dni = 0.2243

D1, D2, D3 = np.sqrt(Dni/n1), np.sqrt(Dni/n2), np.sqrt(Dni/n3)

print("Standard deviation for ", n1, " values: ", D1)
print("Standard deviation for ", n2, " values: ", D2)
print("Standard deviation for ", n3, " values: ", D3)

#3
# 3.1 Heading Selection Method
I1 = 0.06875

def gn(t):
    return 0.5*np.cos(t)*t**2-t**4*1/24

gnfunc = np.vectorize(g)
eta_1, eta_2, eta_3 = gnfunc(t1), gnfunc(t2), gnfunc(t3)

theta_1 = np.mean(eta_1)
theta_2 = np.mean(eta_2)
theta_3 = np.mean(eta_3)

print("Approximate integral value for n = ", n1, " : " , theta_1 )
print("Approximate integral value for n = ", n2, " : " , theta_2 )
print("Approximate integral value for n = ", n3, " : " , theta_3 )

print("Absolute deviation for n = ", n1, " : " , abs(theta_1 - I1))
print("Absolute deviation for n = ", n2, " : " , abs(theta_2 - I1))
print("Absolute deviation for n = ", n3, " : " , abs(theta_3 - I1))

#
Dn_1=0.2143
D_1, D_2, D_3 = np.sqrt(Dn_1/n1), np.sqrt(Dn_1/n2), np.sqrt(Dn_1/n3)

print("Standard deviation for ", n1, " values: ", D_1)
print("Standard deviation for ", n2, " values: ", D_2)
print("Standard deviation for ", n3, " values: ", D_3)

# final values
print("Result for ", n1, " values: ", 0.5 + theta_1)
print("Result for ", n2, " values: ", 0.5 + theta_2)
print("Result for ", n3, " values: ", 0.5 + theta_3)

# Integration over part of the domain method
I2=0.0823764

def g2(t):
    return 0.5*np.cos(t)*t**2*np.exp(-3)

g2func = np.vectorize(g2)

et_1, et_2, et_3 = g2func(t1 + 1.5), g2func(t2 + 1.5), g2func(t3 + 1.5)

thet_1 = np.mean(et_1)
thet_2 = np.mean(et_2)
thet_3 = np.mean(et_3)

print("Approximate value of the modified integral at n = ", n1, " : " , thet_1 )
print("Approximate value of the modified integral at n = ", n2, " : " , thet_2 )
print("Approximate value of the modified integral at n = ", n3, " : " , thet_3 )

D = 0.00356

D_1, D_2, D_3 = np.sqrt(D/n1), np.sqrt(D/n2), np.sqrt(D/n3)

print("Standard deviation for ", n1, " values: ", D_1)
print("Standard deviation for ", n2, " values: ", D_2)
print("Standard deviation for ", n3, " values: ", D_3)

# final values
print("Result at ", n1, " values: ", I2 + theta_1)
print("Result at ", n2, " values: ", I2 + theta_2)
print("Result at ", n3, " values: ", I2 + theta_3)

