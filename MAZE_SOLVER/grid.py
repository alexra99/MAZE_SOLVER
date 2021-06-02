from cell import Cell
from PIL import Image, ImageDraw
from json import dump
from frontier import Frontier
from node import Node
from json import load
import random

class Grid(object):
    '''
    Define el tablero del laberinto.
    '''
    def __init__(self, rows, columns, filename=None):
        '''
        Constructor del tablero: se inicializan las dimensiones del mismo tomándolas de un archivo .json.
        '''
        if filename is None:
            self.rows = rows
            self.columns = columns
            self.grid = self.prepare_grid()
            self.configure_cells()
        else:
            with open(filename) as fdata:
                jsondata = load(fdata)
            self.rows = jsondata['rows']
            self.columns = jsondata['cols']
            self.grid = self.prepare_grid()
            for cell in self.each_cell():
                key = f'{cell}'
                row, col = cell.row, cell.column
                cell.setValue(int(jsondata['cells'][key]['value']))
                cell.cellNorth = self[row - 1, col]
                cell.cellSouth = self[row + 1, col]
                cell.cellWest = self[row, col - 1]
                cell.cellEast = self[row, col + 1]

                if jsondata['cells'][key]['neighbors'][0]:
                    cell.link(self[row - 1, col])
                if jsondata['cells'][key]['neighbors'][1]:
                    cell.link(self[row, col + 1])
                if jsondata['cells'][key]['neighbors'][2]:
                    cell.link(self[row + 1, col])
                if jsondata['cells'][key]['neighbors'][3]:
                    cell.link(self[row, col - 1])

    def size(self):
        '''
        Obtener el tamaño del tablero: filas*columnas.
        '''
        return self.rows*self.columns

    def prepare_grid(self):
        """
        Genera tablero inicial en función de las filas y columnas de entrada.
        """
        grid = [[Cell(row, col) for col in range(self.columns)] for row in range(self.rows)]
        return grid

    def each_row(self):
        '''
        Itera sobre las filas 
        '''
        for row in self.grid:
            yield row

    def each_cell(self):
        '''
        Itera sobre las celdas siempre y cuando existan
        '''
        for row in self.each_row():
            for cell in row:
                if cell:
                    yield cell

    def configure_cells(self):
        '''
        Define los distintos tipos de celdas
        '''
        for cell in self.each_cell():
            row, col = cell.row, cell.column
            cell.cellNorth = self[row-1, col]
            cell.cellSouth = self[row+1, col]
            cell.cellWest = self[row, col-1]
            cell.cellEast = self[row, col+1]

    def __getitem__(self, pos):
        '''
        Sirve para seleccionar posiciones comprobando que dicha posición está en el tablero
        '''
        row, col = pos
        if self.rows-1 >= row >= 0 and self.columns-1 >= col >= 0:
            return self.grid[row][col]
        return None

    def grid_cells(self):
        '''
        Imprime el tablero mostrando las coordenadas de cada celda
        '''
        s = ""
        for row in range(self.rows):
            L = []
            for col in range(self.columns):
                L.append(str(self.grid[row][col]))
            s = s + ' '.join(L) + '\n'
        return s

    def contents_of(cell):
        '''
        Devuelve el contenido de un objeto celda
        '''
        return " "

    def dimensions(self):
        '''
        Dimensiones del laberinto
        '''
        return self.rows, self.columns

    def parse_tuple(self):
        '''
        Formatear los datos en formato String del json a int.
        '''
        l = self.replace("(", "").replace(")", "").split(",")
        return int(l[0]), int(l[1])
