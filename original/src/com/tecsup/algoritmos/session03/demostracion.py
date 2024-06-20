
# - Suponiendo que es un dato nativo
# - Es un entero
# - Asumamos que un entero ocupa 1 bytes
variable_a = 12 
variable_b = 15


# ------------------------

# Array Estaticos : caso 1
arr_nros = [8,23,1,5,6]
print(arr_nros[2])

# Array Dinamicos : caso 2
arr_nros2 = []
arr_nros2.append(8)  # [8]
arr_nros2.append(23) # [8,23]
arr_nros2.append(1)  # [8,23,1]
arr_nros2.append(5)  # [8,23,1,5]
arr_nros2.append(66)  # [8,23,1,5,66]
arr_nros2.append(11)  # [8,23,1,5,66,11]
arr_nros2.append(21)  # [8,23,1,5,66,11,21]
print(arr_nros2[2])

'''
# Array Dinamicos y Estaticos : caso 3

arr_nros3 = [1, 2, 3, .... ,1000]
arr_nros3.append(1001)
arr_nros3.append(1002)

# Listas enlazadas
var_c = ListaEnlazada(13)
var_c.agregar(18)
var_c.agregar(122)
var_c.agregar(66)
var_c.agregar(1)
'''

