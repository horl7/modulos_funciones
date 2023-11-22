from enum import Enum

class Color(Enum):
    AZUL = 'azul'
    ROJO = 'rojo'
    VERDE = 'verde'
    AMARILLO = 'amarillo'

class Mesa:
    def __init__(self, color, precio):
        self.color = color
        self.precio = precio

    def obtener_descripcion(self):
        return f"Mesa - Color: {self.color.value}, Precio: ${self.precio:.2f}"

class Silla:
    def __init__(self, color, precio):
        self.color = color
        self._precio = precio

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio >= 0:
            self._precio = nuevo_precio
        else:
            raise ValueError("El precio no puede ser un valor negativo.")

    def obtener_descripcion(self):
        return f"Silla - Color: {self.color.value}, Precio: ${self._precio:.2f}"

class Lampara:
    def __init__(self, color, precio):
        self.color = color
        self.precio = precio

    def obtener_descripcion(self):
        return f"Lámpara - Color: {self.color.value}, Precio: ${self.precio:.2f}"
