

var_x = 1       # int
var_x = 1.2     # float
var_x = "Jaime" # String









import struct
import sys

#  ---------------------------
#   System-defined data types
#  ---------------------------

# int
day = 24            # 4 bytes
print(type(day))
print(struct.calcsize("i"))  # prints the size of int in bytes


# float
price = 4.5        # 8 bytes
print(type(price))
print(struct.calcsize("d"))  # prints the size of int in bytes

price = price + 5  # --> precio = 9.5

# string
message = "Hola mundo"  # ? bytes
print(sys.getsizeof(message))  # prints the size of the string in bytes

# bool
is_student = True # ?
print(sys.getsizeof(is_student))  # prints the number of bytes used by the bool object



#  ---------------------------
#   User-defined data types
#  ---------------------------

class Alumno:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


alumno_01 = Alumno("Jose","Peréz")
print(type(alumno_01))

alumno_02 = Alumno("Jaime","Garcia")

#alumno_0X = alumno_01 + alumno_02



