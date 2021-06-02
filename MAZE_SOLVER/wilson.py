from grid import Grid
from random import choice, seed

class Wilson:
    '''
    Se definen las funciones necesarias para crear laberintos con el 
    algoritmo de Wilson.
    '''
    
    @staticmethod
    def create(grid):
        '''
        Método estático para crear el laberinto con el algoritmo de Wilson.
        Funcionamiento:
            # Inicializa todas las celdas a no visitadas
            # Selecciona elemento a aleatorio de la lista.
            # Elige la primera celda de forma aletoria y la pone a visitada
            # Toma una celda de las no vistadas y la añade al camino.
            # Continúa seleccionando celdas vecinas de forma aleatoria hasta llegar a una celda visitada
            # Une todas las celdas que se han encotrado con el metodo link.

        '''
        def sample(lst):
            '''
            Selecciona elemento a aleatorio de la lista.
            ''' 
            if len(lst) == 0:
                return None
            return choice(lst)

        unvisited = []
        for cell in grid.each_cell():
            unvisited.append(cell)
        first = sample(unvisited)
        unvisited.remove(first)

        while len(unvisited) > 0:
            cell = sample(unvisited)
            path = [cell]

            
            while cell in unvisited:
                neighbor_cell = sample(cell.neighbors())
                if neighbor_cell in path:
                    path = path[0:path.index(neighbor_cell) + 1]
                else:
                    path.append(neighbor_cell)
                cell = neighbor_cell

            
            prev = None
            for cell in path:
                if prev:
                    prev.link(cell)
                    unvisited.remove(prev)
                prev = cell



