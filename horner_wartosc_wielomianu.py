def horner_scheme(coefficients, x):
    n = len(coefficients)
    result = coefficients[0]

    for i in range(1, n):
        result = result * x + coefficients[i]

    return result

# Przykładowe współczynniki wielomianu (np. dla wielomianu 2x^3 + 3x^2 + 4x + 5)
coefficients = [2, 3, 4, 5]
point = 2  # Punkt, w którym chcemy obliczyć wartość wielomianu

# Obliczanie wartości wielomianu w punkcie za pomocą schematu Hornera
result = horner_scheme(coefficients, point)
print("Wartość wielomianu w punkcie", point, "to:", result)
