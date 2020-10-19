from grid import Grid
from random import choice, seed

class Wilson:
    def __init__(self):
        pass

    @staticmethod
    def create(grid):
        def sample(lst):
            #Selecciona elmento a aleatorio de la lista
            if len(lst) == 0:
                return None
            return choice(lst)

        #Inicializa todas las celdas a no visitadas
        unvisited = []
        for cell in grid.each_cell():
            unvisited.append(cell)

        #Elige la primera celda de forma aletoria y la pone a visitada
        first = sample(unvisited)
        unvisited.remove(first)

        while len(unvisited) > 0:
            #Toma una celda de las no vistadas y la añade al camino.
            cell = sample(unvisited)
            path = [cell]

            #Continúa seleccionando celedas vecinas de forma aleatoria hasta llegar a una celda visitada
            while cell in unvisited:
                neighbor_cell = sample(cell.neighbors())
                if neighbor_cell in path:
                    path = path[0:path.index(neighbor_cell) + 1]
                else:
                    path.append(neighbor_cell)
                cell = neighbor_cell

            #Une todas las celdas que se han encotrado con el metodo link.
            prev = None
            for cell in path:
                if prev:
                    prev.link(cell)
                    unvisited.remove(prev)
                prev = cell


if __name__ == "__main__":
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
