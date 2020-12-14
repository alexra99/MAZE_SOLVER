from dataclasses import dataclass
from cell import Cell
from operator import attrgetter
import math

class Frontier:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
        
    def push(self, data):
        self.items.append(data)
    
    def insert(self, pos, data):
        self.items.insert(pos, data)

    def pop(self):
        return self.items.pop()
    
    def remove(self):
        self.items.remove()

    def get_value(self, pos):
        return self.items[pos].value
    
    def get_size(self):
        return len(self.items);

    def pop_order(self):
        return self.items.pop(0)

    def remove_by_pos(self, pos):
        for index in range(len(self.items)):
           if self.items[index].state.get_tuple() ==  pos:
               self.items.pop(index)
               break
