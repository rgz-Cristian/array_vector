""" Vector en una Matriz """

rows = int(input("Introduzca el valor de las filas: "))
columns = int(input("Introduzca el valor de las columnas: "))


def vector(n, m):
    """ Calculo de la direccion de un vector que se mueve en forma de espiral """
    if m == n:
        if m % 2 != 0:
            print("right ⮕")
        else:
            print("left ⬅")
    else:
        if n > m:
            if m % 2 == 0:
                print("up ⬆")
            else:
                print("down ⬇")
        else:
            if n % 2 == 0:
                print("left ⬅")
            else:
                print("right ⮕")


vector(rows, columns)
