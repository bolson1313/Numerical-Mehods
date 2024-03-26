import math
def f(x):
    return math.sin(x) - 0.5*x
# Początkowe przybliżenia
x0 = math.pi / 2
x1 = math.pi
def newton_method(f, x0, x1, tol=1e-6, max_iter=1000):

    iter = 0
    while abs(f(x1)) > tol and iter < max_iter:
        x_next = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0, x1 = x1, x_next
        iter += 1

    return x1, iter
if f(x0) < 0 and 0 < f(x1):
    zero, iterations = newton_method(f, x0, x1, tol=0.01)
    print("Przybliżone rozwiązanie:", zero)
    print("Liczba iteracji:", iterations)
elif f(x0) > 0 and 0 > f(x1):
    zero, iterations = newton_method(f, x0, x1, tol=0.01)
    print("Przybliżone rozwiązanie:", zero)
    print("Liczba iteracji:", iterations)
else:
    print("Niepoprawnie")

# Wywołanie metody siecznych
