class Persona:
    def __init__(self, nombre, apellidos, direccion):
        self.__nombre = nombre  # para poner atributos privados se pone .__apellido (dos guiones bajos)
        self.__apellidos = apellidos
        self.__direccion = direccion
        self.__telefonos = []


def agregar_telefono(self, numero, tipo):
    self.agregar_telefono(Telefono(numero, tipo))


def __agregar_telefono2(self, telefono):
    self.__telefonos.append(telefono)


@property  # Getter (hay que añadir getters y settesr a manos
def nombre(self):
    return self.__nombre.upper()


@nombre.setter  # setter
def nombre(self, nombre):
    self.__nombre = nombre


class Direccion:
    def __init__(self, direccion, cp, poblacion, provincia):
        self.direccion = direccion
        self.cp = cp
        self.poblacion = poblacion
        self.provincia = provincia


class Telefono:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo


p = Persona("Pepe", "Benítez", Direccion("Rue del Percebe, 13", 41010, "sevilla", "sevilla"))
p.__agregar_telefono("654654654", "iphone")


print(p.nombre)
