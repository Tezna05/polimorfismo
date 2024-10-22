class Punto3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Sobrecargamos el operador de resta (-) mediante el método __sub__
    def __sub__(self, otro):
        return Punto3D(self.x - otro.x, self.y - otro.y, self.z - otro.z)

    # Método para representar el objeto como una cadena (para impresión)
    def __repr__(self):
        return f"Punto3D({self.x}, {self.y}, {self.z})"

# Ejemplo de uso
punto1 = Punto3D(4, 50, 7)
punto2 = Punto3D(1, 30, 3)

# Restando los dos puntos
resultado = punto1 - punto2

# Mostrando el resultado
print(f"Resultado de restar {punto1} y {punto2}: {resultado}")
