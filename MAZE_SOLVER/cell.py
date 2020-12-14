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
        self.value = 0
        self.links = dict()

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def link(self, cell, bidir=True):
        self.links[cell] = True
        if bidir == True:
            cell.link(self, False)
        return self

    def unlink(self, cell, bidir=True):
        del self.links[cell]
        if bidir == True:
            cell.unlink(self, False)
        return self

    def getLinks(self):
        """
        Return all cells linked to this cell
        Returns: List of keys
        """
        return self.links.keys()

    def isLinked(self, cell):
        """ Find out if <cell> is linked to this cell
        Returns: True, False
        """
        return cell in self.links

    def neighbors(self):
        """ Return a list of all cells neighboring this cell 
        """
        n = []
        if self.cellNorth: n.append(self.cellNorth) 
        if self.cellSouth: n.append(self.cellSouth)
        if self.cellWest: n.append(self.cellWest)
        if self.cellEast: n.append(self.cellEast)
        return n

    def neighbors_format(self):
        """ Return a list of all cells neighboring this cell
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
        return (self.row, self.column)

    

    def __str__(self):
        s = "("+str(self.row)+", "+str(self.column)+")"
        return s
