def f(x):
    return x**3 + x - 1

def bisection_method(f, a, b, tolerance):
    if f(a) * f(b) > 0:
        print("Nie można zagwarantować istnienia pierwiastka w zadanym przedziale.")
        return None
    iterations = 0
    while (b - a) / 2.0 > tolerance:
        midpoint = (a + b) / 2.0
        if f(midpoint) == 0:
            return midpoint
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
        iterations += 1
    return (a + b) / 2.0, iterations

a = 0
b = 1
tolerance = 0.01

root, iterations = bisection_method(f, a, b, tolerance)

if root is not None:
    print("Pierwiastek rzeczywisty:", root)
    print("Liczba iteracji:", iterations)
