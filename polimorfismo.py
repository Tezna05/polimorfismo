def sumar(a, b):
    # Si ambos son números (int o float), realizamos una suma numérica
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    # Si ambos son listas, concatenamos las listas
    elif isinstance(a, list) and isinstance(b, list):
        return a + b
    # Si ambos son cadenas, concatenamos las cadenas
    elif isinstance(a, str) and isinstance(b, str):
        return a + b
    # Si los tipos no coinciden, devolvemos un mensaje de error
    else:
        return "Error: los tipos de los objetos no coinciden o no son compatibles."

# Ejemplos de uso
print(sumar(5, 10))         # Suma de números
print(sumar([1, 2], [3, 4])) # Concatenación de listas
print(sumar("Hola, ", "mundo")) # Concatenación de cadenas
print(sumar(5, "mundo"))     # Error, tipos incompatibles
