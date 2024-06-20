"""
Concepto de Stack

"""

# Definimos 
personas = ["Jose","Maria","Pedro"]
print(personas)
# Push: Agregar un valor al final "Jesus"
personas.append("Jesus")
print(personas)
# Push: Agregar un valor al final "Rocio"
personas.append("Rocio")
print(personas)

# Pop : Obtener el último valor ingresado 
#       y lo elimina del arreglo
for i in range(6): # underflow
    print("-"*40)
    print(personas)
    persona_atendida = personas.pop()
    print("POP ->",persona_atendida)
    print(personas)

# Push: Agregar un valor al final "Eduardo"
#personas.append("Eduardo")


