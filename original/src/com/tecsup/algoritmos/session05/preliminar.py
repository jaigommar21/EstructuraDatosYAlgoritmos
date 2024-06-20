"""

"Jaime"

lista_atencion

"""

cola_de_personas = []

# Paso 1 : "Jaime" es el primero que esta en la cola
cola_de_personas.append("Jaime")
print(cola_de_personas)

# Paso 2 : llega "Rocio" a la cola
cola_de_personas.append("Rocio")
print(cola_de_personas)

# Paso 3 : llega "Eduardo" a la cola
cola_de_personas.append("Eduardo")
print(cola_de_personas)

# Paso 4 : Empieza la atencion
# Empieza a las 8:00 am

# Paso 5 : el banco atiende a "Jaime"

"""
['Jaime', 'Rocio', 'Eduardo']

A. ['Jaime', 'Rocio', 'Eduardo']
B. ['Rocio', 'Eduardo']
C. ['Rocio', 'Eduardo',"Jaime"]

['Rocio', 'Eduardo']
"""
#cola_de_personas.pop(0)
#del cola_de_personas[0]

#print(cola_de_personas.pop(0))

persona_atendida = cola_de_personas.pop(0)
print("Se ha atendido a", persona_atendida)
print(cola_de_personas)


# Paso 6 : Rocio se retira de la cola
persona_retirada = cola_de_personas.pop(0)
print("Se ha retirado de la cola", persona_retirada)
print(cola_de_personas)
"""
persona_no_atendida = cola_de_personas.pop(1)
print(persona_atendida)
print("No se atendido a", persona_no_atendida)
"""
#cola_de_personas.pop(0)
#del cola_de_personas[0]

# Paso 7 : el banco atiende a "Eduardo"
banco_atiende = cola_de_personas.pop(0)
print("Banco atiende a",banco_atiende)
print(cola_de_personas)

# HACER COLA
# COLAS

### CASO 2

"""
Inicio de atencion de la cola :

['Jaime', 'Rocio', 'Eduardo']

Abre 8:00 , atiende cada persona 10 minutos
- Atienden a Jaime
A las 8:10  
- COLA : ['Rocio', 'Eduardo']
- llega una señora embarazada : "Cristina"
    - OPCION 2 : ['Cristina','Rocio', 'Eduardo']

- Para el banco que personas con prioridad podrian existir:
   -

"""
