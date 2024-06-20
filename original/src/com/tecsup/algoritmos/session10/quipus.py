import turtle

OFFSET_X = -300
OFFSET_Y = -200
RADIO_CIRCULO = 7

def dibujar_cuerda(color, numeros, i):

    # Configura el color 
    turtle.color(color)
    
    # Posición inicial de la cuerda
    x = OFFSET_X
    y = OFFSET_Y + 100 * i 
    
    turtle.penup()     # Levantar la pluma de la tortuga
    turtle.goto(x, y)  # Ir a la posicion x, y
    turtle.pendown()   # Bajar la pluma de la tortuga

    # Dibuja la cuerda
    turtle.forward(600) # Mueve la tortuja hacia adelante
    
    # Establece color de los circulos
    turtle.fillcolor(color)

    # desplazamiento del priemr circulo
    x = x + 20

    # Dibuja los nudos en la cuerda
    for numero in numeros:
        turtle.penup()
        turtle.goto(x , y)
        turtle.pendown()

        for i in range(numero):
            turtle.begin_fill()
            turtle.circle(RADIO_CIRCULO)  # Dibuja un círculo para cada "nudo"
            turtle.end_fill()
            turtle.penup()
            turtle.goto(x + 15 * (i + 1), y)  # Espacio entre nudos
            turtle.pendown()

        x = x + 150  # Espacio entre grupos de nudos

    
if __name__ == "__main__":

    turtle.speed(0)

    quipu = {
        'red'   : [3, 1, 4, 1],  # Cada lista representa los nudos en una cuerda
        'green' : [1, 5, 9, 2],
        'blue'  : [6, 1, 8, 7],
        'orange': [2, 4, 2, 7],
        'purple': [9, 9, 9, 9]
    }
    
    # Dibuja cada cuerda del quipu
    i = 0
    for color, nums in quipu.items():
        dibujar_cuerda(color, nums, i)
        i = i + 1

    turtle.done()