import numpy as np
import matplotlib.pyplot as plt

# Data from the problem
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Function for Lagrange interpolation
def lagrange_interpolation(x, y, xp):
    yp = 0
    for i in range(len(x)):
        p = 1
        for j in range(len(x)):
            if i != j:
                p *= (xp - x[j]) / (x[i] - x[j])
        yp += p * y[i]
    return yp

# Function for Newton interpolation
def newton_interpolation(x, y, xp):
    # Calculate divided differences
    def divided_diff(x, y):
        n = len(y)
        coef = np.zeros([n, n])
        coef[:,0] = y
        
        for j in range(1, n):
            for i in range(n - j):
                coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])
        
        return coef[0, :]  # Return the first row

    coef = divided_diff(x, y)

    # Evaluate the polynomial at xp
    n = len(coef)
    yp = coef[-1]
    for i in range(n - 2, -1, -1):
        yp = yp * (xp - x[i]) + coef[i]
    
    return yp

# Testing the functions
xp_values = np.linspace(5, 40, 100)
yp_lagrange = [lagrange_interpolation(x, y, xp) for xp in xp_values]
yp_newton = [newton_interpolation(x, y, xp) for xp in xp_values]

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'o', label='Data points')
plt.plot(xp_values, yp_lagrange, '-', label='Lagrange Interpolation')
plt.plot(xp_values, yp_newton, '--', label='Newton Interpolation')
plt.xlabel('Tegangan (kg/mm^2)')
plt.ylabel('Waktu patah (jam)')
plt.legend()
plt.title('Interpolation of the given data')
plt.grid(True)
plt.show()
