from grid import Grid
from json import dump
from json import load
import random

class Save:
    """
    Define los métodos necesarios para manejar y guardar los ficheros .json
    """
    
    def save_json(self):
        """
        Generar el archivo json con el formato dado"
        """
        output = {
            "rows": self.rows,
            "cols": self.columns,
            "max_n": 4,
            "mov": [[-1, 0], [0, 1], [1, 0], [0, -1]],
            "id_mov": ["N", "E", "S", "O"],
            "cells": {}
        }
        for r in range(self.rows):
            for column in range(self.columns):
                key_cell = f'({r}, {column})'
                output["cells"][key_cell] = {
                    "value": random.randint(0,3),
                    "neighbors": [self.grid[r][column].isLinked(self.grid[r][column].cellNorth),
                                  self.grid[r][column].isLinked(self.grid[r][column].cellEast),
                                  self.grid[r][column].isLinked(self.grid[r][column].cellSouth),
                                  self.grid[r][column].isLinked(self.grid[r][column].cellWest)]
                }

        with open(f'puzzle_{self.rows}_{self.columns}.json', 'w') as outfile:
            dump(output, outfile)


    def save_json_problem(self):
        """
        Generar un problema y guardarlo en un archivo .json
        """
        objetive_r = self.rows-1
        objetive_c = self.columns-1 
        output = {
            "INITIAL": f'({0}, {0})',
            "OBJETIVE": f'({objetive_r}, {objetive_c})',
            "MAZE": 'problema_' + str(self.rows) + 'x' + str(self.columns) + '_maze.json'
        }
        with open(f'problema_{self.rows}x{self.columns}.json', 'w') as outfile:
            dump(output, outfile)
