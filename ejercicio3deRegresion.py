import numpy as np
import matplotlib.pyplot as plt

# Datos
x = np.array([50, 70, 90, 110, 130])  # Presión (kPa)
y = np.array([15, 21, 27, 33, 39])    # Caudal (L/min)

# Cálculos
n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x**2)

b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
a = (sum_y - b * sum_x) / n
y_pred = a + b * x

# Predicción a 100 kPa
y_est_100 = a + b * 100

# Coeficiente R²
r2 = 1 - np.sum((y - y_pred)**2) / np.sum((y - np.mean(y))**2)

print("Ejercicio 3 - Caudal en Tuberías")
print(f"a (intercepto): {a:.4f}")
print(f"b (pendiente): {b:.4f}")
print(f"Caudal estimado a 100 kPa: {y_est_100:.2f} L/min")
print(f"R²: {r2:.4f}")

# Gráfica
plt.figure()
plt.plot(x, y, 'o', label='Datos')
plt.plot(x, y_pred, '-', color='red', label=f'y = {a:.2f} + {b:.2f}x')
plt.title('Ejercicio 3: Caudal vs Presión')
plt.xlabel('Presión (kPa)')
plt.ylabel('Caudal (L/min)')
plt.legend()
plt.grid()
plt.savefig('ej3_caudal.png', dpi=300)
plt.show()
