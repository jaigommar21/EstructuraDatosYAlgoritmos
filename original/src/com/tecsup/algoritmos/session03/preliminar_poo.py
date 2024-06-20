'''
Tema : Introduccion a POO
Date : Mar 26, 2021
Author: jgomezm
'''


# Definicion de una clase
class Persona:

    # Constructor
    def __init__(self, cod, nom, ape):
        self.codigo = cod
        self.nombre = nom
        self.apellido = ape

    # Obtener datos
    def obtener_datos(self):
        data = self.nombre + " " +self.apellido
        return data


jose = Persona(100, "Jose", "Galvez")
print(jose.obtener_datos())
print(jose.nombre)        # everything are public 
print(jose)               # <__main__.Persona object at 0x105f4b8e0>
print(hex(id(jose)))

'''
# Definicion de una clase
class Persona:

     # Constructor
     def __init__(self, cod, nom, ape):
         self.codigo = cod
         self.nombre = nom
         self.apellido = ape

     # Obtener datos
     def obtener_datos(self):
         data = self.nombre + " " +self.apellido
         return data

     def getNombre(self):
         return self.nombre

jose = Persona(100, "Jose", "Galvez")
print(jose.codigo)
print(jose.nombre)
print(jose.apellido)
print(jose.obtener_datos())
print(jose.getNombre())
print(jose)
print(hex(id(jose)))
'''