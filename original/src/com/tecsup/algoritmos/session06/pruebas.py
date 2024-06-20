
def funcion3():

    ret = funcion2()

    if ret == -1:
        print("Todo super mal")
        return -1
    else:
        print("Todo super bien")
        return 0

def funcion2():

    ret = funcion1()

    if ret == -1:
        print("Todo mal")
        return -1
    else:
        print("Todo bien")
        return 0

def funcion1():

    raise IndexError
    return 0

funcion3()


