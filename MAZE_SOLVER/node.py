class Node:
    '''
    Define la clase Noodo.
    '''
    def __init__(self,ID,cost,state,father_id,action,depth,h,value):
        self.ID = int(ID)
        self.cost = int(cost)
        self.state = state
        self.father_id = int(father_id)
        self.action = str(action)
        self.depth = int(depth)
        self.h = int(h)
        self.value = float(value)
    
    def __str__(self):
        '''
        Método para la impresión de un objeton Nodo.
        '''
        tex = f'[{self.ID}]({self.cost},{self.state},{self.father_id},{self.action},{self.depth},{self.h},{self.value})'
        return tex