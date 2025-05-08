import numpy as np
import matplotlib.pyplot as plt

# Datos
x = np.array([5, 10, 15, 20, 25])  # Carga (kN)
y = np.array([0.6, 1.2, 1.9, 2.5, 3.1])  # Elongación (mm)

# Cálculos
n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x**2)

b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
a = (sum_y - b * sum_x) / n
y_pred = a + b * x

# Coeficiente de determinación R²
r2 = 1 - np.sum((y - y_pred)**2) / np.sum((y - np.mean(y))**2)

print("Ejercicio 1 - Resistencia de Materiales")
print(f"a (intercepto): {a:.4f}")
print(f"b (pendiente): {b:.4f}")
print(f"R²: {r2:.4f}")

# Gráfica
plt.figure()
plt.plot(x, y, 'o', label='Datos')
plt.plot(x, y_pred, '-', color='red', label=f'y = {a:.2f} + {b:.2f}x')
plt.title('Ejercicio 1: Elongación vs Carga')
plt.xlabel('Carga (kN)')
plt.ylabel('Elongación (mm)')
plt.legend()
plt.grid()
plt.savefig('ej1_resistencia.png', dpi=300)
plt.show()
