def luhn_algorithm(card_number):
    """
    Función que implementa el algoritmo de Luhn para verificar la validez de un número de tarjeta de crédito.
    
    Parámetros:
    card_number (str): Número de tarjeta de crédito en formato string.
    
    Retorna:
    bool: True si el número de tarjeta es válido según el algoritmo de Luhn, False en caso contrario.
    """
    
    # Convertir el número de la tarjeta en una lista de números
    digits = [int(d) for d in str(card_number)]
    
    # Invertir la lista
    digits.reverse()
    
    # Multiplicar por 2 los números en las posiciones impares y restar 9 si el resultado es mayor que 9
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    
    # Sumar todos los números de la lista
    total = sum(digits)
    
    # Determinar si el número de la tarjeta es válido
    return total % 10 == 0

# Ejemplo de uso
numero_tarjeta = "4532015112830366"
if luhn_algorithm(numero_tarjeta):
    print("El número de tarjeta es válido.")
else:
    print("El número de tarjeta no es válido.")
