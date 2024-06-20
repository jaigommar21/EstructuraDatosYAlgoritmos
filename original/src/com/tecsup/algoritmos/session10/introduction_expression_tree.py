"""

- Programacion a bajo nivel 
  
  - Codigo maquina : 10020

  - Nemonicos : ( Acumuladores ) 
      * ADD 1
      * SUM 3 

  - Primer Lenguaje : FORTRAN
      * FOR : Formulas
      * TRAN : Traslation
 
  - Lenguaje de programacion : PYTHON
      
      ope1 = 12
      ope2 = 14
      suma = ope1 + ope2

  - Creamos un traductor que convierte

     CADENA CARACTERES ===>  ARBOL
     78-2*
     78--2* 

"""

ope1 = 12
ope2 = 14
suma = ope1 + ope2
print(suma)

## Compilador











"""
Realizar el arbol binario

 x ^ y : x elevado a y 

  (( 1 + 5 ) * (10 -5)) ^ 2

"""


"""
Año,Marca,Modelo,Descripción,Precio
1997,Ford,E350,"ac, abs, moon",3000.00
1999,Chevyr,Venture,Extended Edition,4900.00
1999,Chevy,Venture,"Extended Edition, Very Large",5000.00
1996,Jeep,Grand Cherokee,"MUST SELL! air, moon roof, loaded",4799.00
"""

"""

15+105-*2^

1,5,+,10,5,-,*,2,^,

"""

""" 15+95-*2^
15+95-*2^  ?
15+95-*2^

1,5,+,10,5,-,*,2,^ """

""""
INPUT : (( 1 + 5 ) * (10 -5)) ^ 2  # Indor
- Transformar de Indor a Postfix :
     algoritmo 1
- Transformar  la Postfix a un arbol
     algoritmo 2     
- Calcular la operacion
  en el arbol usando recursividad
     algoritmo 3



"""

""" s = "1,5,+,10,5,-,*,2,^"

print(s.split(",")) """