class Cell:
    """
    Definición de una celda del tablero.
    """

    def __init__(self, row, column):
        """
             Constructor de una celda.
        """
        self.row = row
        self.column = column
        self.cellNorth = None
        self.cellSouth = None
        self.cellWest = None
        self.cellEast = None
        self.value = 0
        self.links = dict()

    def setValue(self, value):
        """
        Modificar value.
        """
        self.value = value

    def getValue(self):
        """
        Obtener value.
        """
        return self.value

    def link(self, cell, bidir=True):
        """
        Unir celda
        """
        self.links[cell] = True
        if bidir == True:
            cell.link(self, False)
        return self

    def unlink(self, cell, bidir=True):
        """
        Romper unión de una celda
        """
        del self.links[cell]
        if bidir == True:
            cell.unlink(self, False)
        return self

    def getLinks(self):
        """
        Obtener uniones de una celda
        """
        return self.links.keys()

    def isLinked(self, cell):
        """ 
        Determinar si una celda esta unida a otra
        """
        return cell in self.links

    def neighbors(self):
        """ 
        Obtener lista de celdas vecinas
        """
        n = []
        if self.cellNorth:
            n.append(self.cellNorth)
        if self.cellSouth:
            n.append(self.cellSouth)
        if self.cellWest:
            n.append(self.cellWest)
        if self.cellEast:
            n.append(self.cellEast)
        return n

    def neighbors_format(self):
        """ 
        Obtener lista de celdas vecinas en el siguiente formato: N, E, S, O.
        """
        n = []
        if self.isLinked(self.cellNorth):
            n.append(('N', self.cellNorth))
        if self.isLinked(self.cellEast):
            n.append(('E', self.cellEast))
        if self.isLinked(self.cellSouth):
            n.append(('S', self.cellSouth))
        if self.isLinked(self.cellWest):
            n.append(('O', self.cellWest))
        return n

    def get_tuple(self):
        """
        Obtener una tupla fila, columna.
        """
        return (self.row, self.column)

    def __str__(self):
        """
        Metodo de impresión de una celda.
        """
        s = "("+str(self.row)+", "+str(self.column)+")"
        return s
