import math

def secant_method(f, x0, x1, tol=1e-6, max_iter=100):
    iter = 0
    while abs(f(x1)) > tol and iter < max_iter:
        x_next = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0, x1 = x1, x_next
        iter += 1

    return x1, iter

def f(x):
    return x**3+x**2-x*3-3
x0 = 1
x1 = 2
if f(x0) < 0 and 0 < f(x1):
    zero, iterations = secant_method(f, x0, x1, tol=0.0001)
    print("Przybliżone rozwiązanie:", zero)
    print("Liczba iteracji:", iterations)
elif f(x0) > 0 and 0 > f(x1):
    zero, iterations = secant_method(f, x0, x1, tol=0.0001)
    print("Przybliżone rozwiązanie:", zero)
    print("Liczba iteracji:", iterations)
else:
    print("Niepoprawnie")
