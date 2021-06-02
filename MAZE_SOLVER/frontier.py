from dataclasses import dataclass
from cell import Cell
from operator import attrgetter
import math


class Frontier:
    '''
    Define la estructura de datos Frontera en la que manejan los nodos.
    '''

    def __init__(self):
        '''
        Constructor de la clase Frontera.
        '''
        self.items = []

    def is_empty(self):
        '''
        Devolver frontera vacia.
        '''
        return self.items == []

    def push(self, data):
        '''
        Añadir elemento a la frontera.
        '''
        self.items.append(data)

    def insert(self, pos, data):
        '''
        Añadir elemento a la frontera en una posición determinada.
        '''
        self.items.insert(pos, data)

    def pop(self):
        '''
        Sacar elemento superior de la frontera.
        '''
        return self.items.pop()

    def remove(self):
        '''
        Eliminar elemento de la frontera,
        '''
        self.items.remove()

    def get_value(self, pos):
        '''
        Obtener value en posicion determinada.
        '''
        return self.items[pos].value

    def get_size(self):
        '''
        Obtener tamaño de la frontera.
        '''
        return len(self.items)

    def pop_order(self):
        '''
        Sacar elemento de la frontera en la posición 0.
        '''
        return self.items.pop(0)

    def remove_by_pos(self, pos):
        '''
        Eliminar elementos de la frontera por posición.
        '''
        for index in range(len(self.items)):
            if self.items[index].state.get_tuple() == pos:
                self.items.pop(index)
                break
