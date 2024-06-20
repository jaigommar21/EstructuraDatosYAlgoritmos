
# caso 1

""" nro = 1        # Es un tipo de dato entero, ocupa 4 bytes
print(nro)
print(type(nro))

nro = b'\x01'  # Es un tipo de dato byte, ocupa 1 byte
print(nro)
print(type(nro)) """


# caso 2

""" # index    0  1  2  3
numeros = [45,21,33,99]

numeros = [ i for i in range(1000)]

print(len(numeros))
print(numeros[0]) # index 0
print(numeros[2]) # index 2

#numeros[4] = 12 # IndexError: list assignment index out of range
#numeros[5] = 20 # IndexError: list assignment index out of range
numeros.append(12)
print(numeros[4]) # index 4 """



# Arreglos dinamicos : caso 1


numeros = [45,21,33,99]
print(numeros[0]) # index 0
print(numeros[2]) # index 2
numeros[4] = 12
#print(numeros[4]) # index 4



