# Función que realiza el algoritmo de Luhn
def luhn_algorithm(card_number):
    # Convertir el número de la tarjeta en una lista de números
    digits = [int(d) for d in str(card_number)]
    # Invertir la lista
    digits = digits[::-1]
    # Multiplicar por 2 los números en las posiciones pares
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    # Sumar los números de la lista
    total = sum(digits)
    # Determinar si el número de la tarjeta es válido
    return total % 10 == 0