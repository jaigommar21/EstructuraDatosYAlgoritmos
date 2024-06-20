class ColeccionLibros:

    def __init__(self, libros):
        self.libros = libros

    def __iter__(self):
        return iter(self.libros.values())

libros = {"001":"Matematicas Básica","002":"Historia del Perú" }

cl = ColeccionLibros(libros)

for item in cl:
    print(item)




#print(cl.libros)

"""
libros = {"001":"Matematicas Básica","002":"Historia del Perú" }

print(libros)
print(libros.values())
print(libros.keys())
"""
