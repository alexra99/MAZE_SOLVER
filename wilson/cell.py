class Cell:
    """
    Definition of a grid cell
    """
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.cellNorth = None
        self.cellSouth = None
        self.cellWest = None
        self.cellEast = None
        self.links = dict()

    def link(self, cell, bidir=True):
        """Crea unión"""
        self.links[cell] = True
        if bidir == True:
            cell.link(self, False)
        return self

    def unlink(self, cell, bidir=True):
        """Deshace unión"""
        del self.links[cell]
        if bidir == True:
            cell.unlink(self, False)
        return self

    def getLinks(self):
        """Devuelve una lista con todas las celdas unidas a otra"""
        return self.links.keys()

    def isLinked(self, cell):
        """ Comprueba si una celda esta unida a otra y devuelve True o False"""
        return cell in self.links

    def neighbors(self):
        """ Devuelve la lista de vecinos de una celda """
        n = []
        if self.cellNorth: n.append(self.cellNorth) 
        if self.cellSouth: n.append(self.cellSouth)
        if self.cellWest: n.append(self.cellWest)
        if self.cellEast: n.append(self.cellEast)
        return n

    def __str__(self):
        s = "("+str(self.row)+", "+str(self.column)+")"
        return s
