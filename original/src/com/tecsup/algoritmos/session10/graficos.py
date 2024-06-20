import turtle


if __name__ == "__main__":

    # Define velocidad
    turtle.speed(15)

    turtle.home()

    turtle.color("red")        
    for i in range(100):
        turtle.circle(200)
        turtle.left(11)

    turtle.color("green")        
    for i in range(100):
        turtle.circle(100)
        turtle.left(11)

    turtle.color("blue")        
    for i in range(100):
        turtle.circle(50)
        turtle.left(11)

    turtle.color("yellow")        
    for i in range(100):
        turtle.circle(25)
        turtle.left(11)

    # Cierra la ventana cuando se hace clic en ella
    turtle.done()
