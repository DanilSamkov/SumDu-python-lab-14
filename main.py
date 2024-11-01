import numpy as np
import matplotlib.pyplot as plt

# Задання діапазону значень x
x = np.linspace(0, 5, 100)
y = np.sqrt(x) * np.sin(10 * x)

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(x, y, color='blue', linewidth=2, linestyle='-', label=r'$Y(x) = \sqrt{x} \cdot \sin(10x)$')

plt.xlabel('x')
plt.ylabel('Y(x)')

plt.title('Графік функції Y(x)')

plt.legend()

plt.grid()
plt.show()