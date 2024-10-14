
""" Vector on the Array """

rows = int(input("rows: "))
columns = int(input("columns: "))


def vector(n, m):
    """ Calculation of the direction of a vector moving in a spiral shape """

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
