def horner_scheme_division(coefficients, divisor):
    n = len(coefficients) - 1
    result = coefficients[0]
    for i in range(1, n):
        result = result * divisor + coefficients[i]
    remainder = result * divisor + coefficients[-1]
    return result, remainder

# Przykładowe współczynniki wielomianu (np. dla wielomianu 2x^3 + 3x^2 + 4x + 5)
coefficients = [2, 3, 4, 5]
divisor = 2  # Dzielnik (dwumian)

# Wywołanie funkcji do dzielenia wielomianu przez dwumian za pomocą schematu Hornera
quotient, remainder = horner_scheme_division(coefficients, divisor)

print("Wynik dzielenia wielomianu przez dwumian:", quotient)
print("Reszta z dzielenia:", remainder)
