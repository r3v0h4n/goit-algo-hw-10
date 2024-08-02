import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


def draw(f, a, b):
    # Створення діапазону значень для x
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)
    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
    plt.grid()
    plt.show()

def monte_carlo(f, a, b):
    # Кількість випадкових точок
    num_points = 100000

    # Генерація випадкових точок
    x_random = np.random.uniform(a, b, num_points)
    y_random = np.random.uniform(0, f(b), num_points)

    # Підрахунок точок під кривою
    under_curve = y_random < f(x_random)
    return (b - a) * f(b) * np.sum(under_curve) / num_points

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

draw(f, a, b)

integral, error = spi.quad(f, a, b)

print("quad: ", integral)
print(f"Монте-Карло: {monte_carlo(f, a, b):.5f}")