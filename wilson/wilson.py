from grid import Grid
from random import choice, seed
import json

class Wilson:
    def __init__(self):
        pass

    @staticmethod
    def create(grid):
        def sample(lst):
            # Selecciona elemento a aleatorio de la lista
            if len(lst) == 0:
                return None
            return choice(lst)

        # Inicializa todas las celdas a no visitadas
        unvisited = []
        for cell in grid.each_cell():
            unvisited.append(cell)

        # Elige la primera celda de forma aletoria y la pone a visitada
        first = sample(unvisited)
        unvisited.remove(first)

        while len(unvisited) > 0:
            # Toma una celda de las no vistadas y la añade al camino.
            cell = sample(unvisited)
            path = [cell]

            # Continúa seleccionando celdas vecinas de forma aleatoria hasta llegar a una celda visitada
            while cell in unvisited:
                neighbor_cell = sample(cell.neighbors())
                if neighbor_cell in path:
                    path = path[0:path.index(neighbor_cell) + 1]
                else:
                    path.append(neighbor_cell)
                cell = neighbor_cell

            # Une todas las celdas que se han encotrado con el metodo link.
            prev = None
            for cell in path:
                if prev:
                    prev.link(cell)
                    unvisited.remove(prev)
                prev = cell

        # Elige una casilla de inicio y de salida del laberinto
        inicio = grid.random_cell()
        fin = grid.random_cell()
def chooseOption():
    correct = False
    num = 0
    while (not correct):
        try:
            num = int(input("Introduce un numero entero: "))
            correct = True
        except ValueError:
            print('Error, introduce un numero entero')

    return num

def menu():
    print("1. Generar Laberinto")
    print("2. Leer fichero .json")
    print("3. Salir")
    print("Elige una opcion")


if __name__ == "__main__":

    exit = False
    option = 0

    while not exit:
        menu()
        option = chooseOption()

        if option == 1:
            try:
                nRows = int(input('Introduzca el número de filas: '))
                nColumns = int(input('Introduzca el número de columnas: '))
            except ValueError as error:
                print('Intentelo de nuevo, insertando numeros enteros')
            else:
                # Generar laberinto
                g = Grid(nRows, nColumns)
                Wilson.create(g)
                g.save_image()
                g.save_json()
                print('Laberinto de ' + str(nRows) + ' filas y ' + str(nColumns) + ' columnas generado correctamente.')
                print('Imagen y fichero .json guardados en el directorio actual.')
                g.problem_json()
                g.sucesors_function()

        elif option == 2:
            file = str(input('Introduzca ruta del fichero:'))
            g = Grid(0, 0, file)
            g.problem_json()
            g.save_image()
            print('Pintando laberinto...')
            print('Laberinto creado, Imagen guardada en el directorio actual.')

        elif option == 3:
            exit = True
        else:
            print("Introduce un número entre 1 y 3")

    print("Has salido del programa con éxito")
