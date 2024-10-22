# Clase base Animal
class Animal:
    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser sobrescrito por la clase hija")

# Clase hija Perro
class Perro(Animal):
    def hacer_sonido(self):
        return "El perro dice: ¡Guau, guau!"

# Clase hija Gato
class Gato(Animal):
    def hacer_sonido(self):
        return "El gato dice: ¡Miau!"

# Clase hija Pájaro
class Pajaro(Animal):
    def hacer_sonido(self):
        return "El pájaro dice: ¡Pío, pío!"

# Clase hija Vaca
class Vaca(Animal):
    def hacer_sonido(self):
        return "La vaca dice: ¡Muuu!"

# Clase hija Serpiente
class Serpiente(Animal):
    def hacer_sonido(self):
        return "La serpiente dice: ¡Ssssss!"

# Ejemplo de uso de polimorfismo
def escuchar_animal(animal):
    print(animal.hacer_sonido())

# Instanciamos objetos de las clases hijas
perro = Perro()
gato = Gato()
pajaro = Pajaro()
vaca = Vaca()
serpiente = Serpiente()

# Probamos el polimorfismo
escuchar_animal(perro)       # El perro dice: ¡Guau, guau!
escuchar_animal(gato)        # El gato dice: ¡Miau!
escuchar_animal(pajaro)      # El pájaro dice: ¡Pío, pío!
escuchar_animal(vaca)        # La vaca dice: ¡Muuu!
escuchar_animal(serpiente)   # La serpiente dice: ¡Ssssss!
