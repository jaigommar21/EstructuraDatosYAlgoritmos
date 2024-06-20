# Llamada recursiva infinita
def imprimir(msg):
    print(msg)
    imprimir(msg)


if __name__ == "__main__":
    imprimir("Hello World ..!")