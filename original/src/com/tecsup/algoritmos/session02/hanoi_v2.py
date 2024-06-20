def hanoi(n):
    if n == 1:
        count = 1
    else:
        count = (2 * hanoi(n-1) + 1)
    
    return count 

def ToH(n , A, B, C):
    if n==1:
        print("Mover Disco 1 desde",A, "a", B)
        return
    ToH(n-1, A, C, B)
    print("Mover Disco",n, "desde",A,"a",B)
    ToH(n-1, C, B, A)

def main():
    n = eval(input("Introduzca el número total de discos de la torre Hanói:"))
    print("{} los discos deben moverse: {} veces".format(n, hanoi(n)))
    ToH(n, 'A', 'B', 'C')

if __name__ == "__main__":       
    main()