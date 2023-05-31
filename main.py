# import math
#
#
# def newton_method(f, df, d2f, x0, eps=1e-6, max_iter=100):
#     """
#     Реализация метода Ньютона для поиска минимума функции
#
#     Args:
#         f (function): Целевая функция
#         df (function): Производная целевой функции
#         d2f (function): Вторая производная целевой функции
#         x0 (float): Начальное приближение
#         eps (float, optional): Точность вычисления. Defaults to 1e-6.
#         max_iter (int, optional): Максимальное число итераций. Defaults to 100.
#
#     Returns:
#         float: Результат минимизации
#     """
#
#     x = x0
#     for i in range(max_iter):
#         fx = f(x)
#         dfx = df(x)
#         d2fx = d2f(x)
#
#         if abs(d2fx) < eps:
#             break
#
#         x_new = x - dfx / d2fx
#
#         if abs(x_new - x) < eps:
#             break
#
#         x = x_new
#
#     return x
#
#
# def f(x1, x2,x3):
#     return 2* (x1**2) + 3*(x2**2) + 5*(x3**2) - 8*x1 - 6*x2 -30*x3 +56
#
# # Задаем производную целевой функции
# def df(x1):
#     return 4*x1 -8
#
# # Задаем вторую производную целевой функции
# def d2f(x):
#     return 2 * math.sin(x) + 4 * math.cos(x)
#
# # Задаем начальное приближение
# x0 = 1.5
#
# # Вызываем метод Ньютона
# result = newton_method(f, df, d2f, x0)
#
# print("Минимум функции:", result)








import numpy as np

def f(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    return 2*x1**2 + 3*x2**2 + 5*x3**2 - 8*x1 - 5*x2 - 30*x3 + 56

def df(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    return np.array([4*x1 - 8, 6*x2 - 5, 10*x3 - 30])

def ddf(x):
    return np.array([[4, 0, 0], [0, 6, 0], [0, 0, 10]])

def newton_method(f, df, ddf, x0, eps=0.001):
    while np.linalg.norm(df(x0)) > eps:
        x0 = x0 - np.linalg.inv(ddf(x0)) @ df(x0)

    return x0

x0 = np.array([5, 5, 5]) # начальное значение
result = newton_method(f, df, ddf, x0, eps=0.0001)
print("Минимальное значение функции равно:", f(result))
print("Найденное решение:", result)