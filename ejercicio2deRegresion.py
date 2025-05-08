import numpy as np
import matplotlib.pyplot as plt

# Datos
x = np.array([0, 2, 4, 6, 8])  # Posición (cm)
y = np.array([100, 92, 85, 78, 71])  # Temperatura (°C)

# Cálculos
n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x**2)

b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
a = (sum_y - b * sum_x) / n
y_pred = a + b * x

# Estimación en x = 5
y_est_5 = a + b * 5

# Coeficiente R²
r2 = 1 - np.sum((y - y_pred)**2) / np.sum((y - np.mean(y))**2)

print("Ejercicio 2 - Transferencia de Calor")
print(f"a (intercepto): {a:.4f}")
print(f"b (pendiente): {b:.4f}")
print(f"Temperatura estimada en x = 5 cm: {y_est_5:.2f} °C")
print(f"R²: {r2:.4f}")

# Gráfica
plt.figure()
plt.plot(x, y, 'o', label='Datos')
plt.plot(x, y_pred, '-', color='red', label=f'y = {a:.2f} + {b:.2f}x')
plt.title('Ejercicio 2: Temperatura vs Posición')
plt.xlabel('Posición (cm)')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid()
plt.savefig('ej2_calor.png', dpi=300)
plt.show()
