import math

# Tutaj definiujemy funkcję, której pierwiastek jest wyliczany
def f(x):
    return 3*x-math.cos(x)-1
# Tutaj definiujemy parametry początkowe
epsy = 0.00001  # Dokładność y
a = 0.25     # Początek przedziału poszukiwań pierwiastka
b = 0.75      # Koniec przedziału poszukiwań pierwiastka
n = 100        # Maksymalna liczba obiegów

# Obliczamy i zapamiętujemy wartości funkcji na krańcach przedziału [a,b]
fa = f(a)
fb = f(b)

# Sprawdzamy, czy na krańcach przedziału [a,b] wartości funkcji mają różne znaki
if fa * fb > 0:
    print("BŁĄD!!! Funkcja nie ma różnych znaków na krańcach przedziału")
else:
    result = True

    # W pętli wyznaczamy kolejne przybliżenia pierwiastka
    while True:
        # Wyznaczamy x0
        x0 = (fa * b - fb * a) / (fa - fb)

        # Sprawdzamy, wykonano maksymalną liczbę iteracji.
        if n == 0:
            break  # Jeśli tak, to kończymy
        else:
            n -= 1

        # Obliczamy i zapamiętujemy wartość funkcji w punkcie x0
        fx = f(x0)

        # Sprawdzamy, czy wartość funkcji jest dostatecznie bliska zeru
        if abs(fx) < epsy:
            break  # Jeśli tak, to kończymy

        # Za nowy przedział [a,b] przyjmujemy tą z części [a,x0], [x0,b],
        # w której funkcja ma różne znaki na krańcach
        if fa * fx < 0:
            b = x0
            fb = fx
        else:
            a = x0
            fa = fx

if result:
    print("Pierwiastek        x0 =", x0)
    print("Wartość funkcji f(x0) =", f(x0))
    print("Dokładność dla y epsy =", epsy)
    print("Liczba obiegów        =", 100 - n)
