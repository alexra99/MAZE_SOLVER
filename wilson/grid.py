from cell import Cell
from PIL import Image, ImageDraw
from json import dump
from json import load
import random

class Grid(object):
    def __init__(self, rows, columns, filename=None):
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
            for row in self.each_row():
                for cell in row:
                    key = f'{cell}'
                    row, col = cell.row, cell.column
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
        return self.rows*self.columns

    def prepare_grid(self):
        """Genera tablero inicial"""
        grid = [[Cell(row, col) for col in range(self.columns)] for row in range(self.rows)]
        return grid

    def each_row(self):
        """Itera sobre las filas"""
        for row in self.grid:
            yield row

    def each_cell(self):
        """Itera sobre las celdas siempre y cuando existan"""
        for row in self.each_row():
            for cell in row:
                if cell:
                    yield cell

    def configure_cells(self):
        """Define los distintos tipos de celdas"""
        for cell in self.each_cell():
            row, col = cell.row, cell.column
            cell.cellNorth = self[row-1, col]
            cell.cellSouth = self[row+1, col]
            cell.cellWest = self[row, col-1]
            cell.cellEast = self[row, col+1]

    def random_cell(self):
        """ Asigna fila y columna aleatoria para obtener una celda aleatoria"""
        row = random.randint(0, self.rows-1)
        col = random.randint(0, self.columns-1)
        return self[row, col]

    def __getitem__(self, pos):
        """ Sirve para seleccionar posiciones comprobando que dicha posición está en el tablero """
        row, col = pos
        if self.rows-1 >= row >= 0 and self.columns-1 >= col >= 0:
            return self.grid[row][col]
        return None

    @property
    def grid_cells(self):
        """ Imprime el tablero mostrando las coordenadas de cada celda """
        s = ""
        for row in range(self.rows):
            L = []
            for col in range(self.columns):
                L.append(str(self.grid[row][col]))
            s = s + ' '.join(L) + '\n'
        return s

    @staticmethod
    def contents_of(cell):
        """ Devuelve el contenido de un objeto celda"""
        return " "

    def dimensions(self):
        return self.rows, self.columns

    def save_image(self):
        """Dibuja el laberinto"""
        SIZE_LINE = 20
        im = Image.new('RGBA', ((self.columns + 4) * SIZE_LINE, (self.rows + 4) * SIZE_LINE), (255, 255, 255, 255))
        draw = ImageDraw.Draw(im)

        for r in range(self.rows):
            for column in range(self.columns):
                """Va comprobando donde tiene que empezar a dibujar y si tiene pared en alguna coordenada(N,S,E,O)"""
                startx, starty = (column + 2) * SIZE_LINE, (r + 2) * SIZE_LINE
                if not self.grid[r][column].isLinked(self.grid[r][column].cellNorth):
                    draw.line((startx, starty, startx + SIZE_LINE, starty), fill=128)
                if not self.grid[r][column].isLinked(self.grid[r][column].cellEast):
                    draw.line((startx + SIZE_LINE, starty, startx + SIZE_LINE, starty + SIZE_LINE), fill=128)
                if not self.grid[r][column].isLinked(self.grid[r][column].cellSouth):
                    draw.line((startx, starty + SIZE_LINE, startx + SIZE_LINE, starty + SIZE_LINE), fill=128)
                if not self.grid[r][column].isLinked(self.grid[r][column].cellWest):
                    draw.line((startx, starty, startx, starty + SIZE_LINE), fill=128)

        im.save(f'Lab_{self.rows}_{self.columns}.png')

    def save_json(self):
        """Generar el json con el formato dado"""
        output = {
            "rows": 4,
            "cols": 4,
            "max_n": 4,
            "mov": [[-1, 0], [0, 1], [1, 0], [0, -1]],
            "id_mov": ["N", "E", "S", "O"],
            "cells": {}
        }
        for r in range(self.rows):
            for column in range(self.columns):
                key_cell = f'({r}, {column})'
                output["cells"][key_cell] = {
                    "value": 0,
                    "neighbors": [self.grid[r][column].isLinked(self.grid[r][column].cellNorth),
                                  self.grid[r][column].isLinked(self.grid[r][column].cellEast),
                                  self.grid[r][column].isLinked(self.grid[r][column].cellSouth),
                                  self.grid[r][column].isLinked(self.grid[r][column].cellWest)]
                }

        with open(f'Lab_{self.rows}_{self.columns}.json', 'w') as outfile:
            dump(output, outfile)

    

